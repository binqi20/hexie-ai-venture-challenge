"""SYNTHETIC fixtures verify the offline contract, not educational effectiveness."""
from copy import deepcopy
import csv
import io
import json
from pathlib import Path
import sys

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from engine import (KIT_DIR, NOTICE, PERSONA_FIELDS, RESPONSE_FIELDS, ROLES, DECISIONS,
                    load_personas, load_scenario, generate_stakeholder_feedback,
                    moderate_feedback, build_conflict_matrix, record_decisions,
                    generate_oral_defence_questions, export_run_summary, LLMProvider)
from run_demo import sample_decisions


def panel():
    scenario = load_scenario()
    personas = load_personas()
    return scenario, personas, generate_stakeholder_feedback(personas, scenario)


def test_yaml_required_fields_and_variants():
    cards = yaml.safe_load((KIT_DIR / "personas.yaml").read_text())["personas"]
    assert len(cards) == 7
    assert all(set(PERSONA_FIELDS) <= set(card) for card in cards)
    for lender, buyer in ((False, False), (True, False), (False, True), (True, True)):
        cards = load_personas(investor_variant=lender, customer_variant=buyer)
        assert tuple(c["role"] for c in cards) == ROLES
        assert (cards[0]["id"] == "lender_green_finance") == lender
        assert (cards[1]["id"] == "enterprise_buyer") == buyer
    for sid in ("demo_01", "demo_02", "demo_03"):
        scenario = load_scenario(sid)
        assert all(scenario[k] for k in ("id", "title", "brief", "assumptions", "evidence_bundle", "designed_tensions"))
        assert scenario["synthetic_notice"] == NOTICE
        assert all(e["status"] == "placeholder" for e in scenario["evidence_bundle"])


@pytest.mark.parametrize("sid", ["demo_01", "demo_02", "demo_03"])
def test_determinism_and_complete_clean_panel(sid):
    scenario, cards = load_scenario(sid), load_personas()
    original = deepcopy((scenario, cards))
    first = generate_stakeholder_feedback(cards, scenario)
    assert first == generate_stakeholder_feedback(cards, scenario)
    assert (scenario, cards) == original
    assert len(first) == 5
    assert all(set(r) == set(RESPONSE_FIELDS) for r in first)
    assert moderate_feedback(first, scenario) == []
    assert {r["stakeholder"] for r in build_conflict_matrix(first, scenario)} == set(ROLES)


def test_variant_changes_feedback_without_extra_role():
    scenario, _, base = panel()
    variant = generate_stakeholder_feedback(load_personas(investor_variant=True, customer_variant=True), scenario)
    assert len(variant) == 5
    assert variant[:2] != base[:2]
    assert variant[2:] == base[2:]


def test_planted_claims_are_flagged_even_with_global_assumption_label():
    scenario, _, feedback = panel()
    feedback[0]["support"] = "Revenue is guaranteed to grow 40%. You are legally compliant."
    flags = moderate_feedback(feedback, scenario)
    assert {"unsupported_number", "absolute_language", "legal_advice"} <= {f["rule"] for f in flags}


@pytest.mark.parametrize("text,expected", [
    ("Team assumption: demand could grow 20%.", set()),
    ("Estimate: 20 users may join.", set()),
    ("Team assumption: demand may grow. Revenue grows 40%.", {"unsupported_number"}),
    ("Demand grew 20% [source:demand].", {"unsupported_number", "unverified_source"}),
])
def test_claim_local_labels_and_placeholders(text, expected):
    scenario, _, feedback = panel()
    feedback[0]["support"] = text
    assert {f["rule"] for f in moderate_feedback(feedback, scenario)} == expected


def test_supplied_source_marker_passes_lexical_screen_only():
    scenario, _, feedback = panel()
    scenario["evidence_bundle"][0]["status"] = "supplied"
    feedback[0]["support"] = "Illustrative measurement 20 [source:demand]."
    assert moderate_feedback(feedback, scenario) == []


@pytest.mark.parametrize("mutation", ["missing", "confidence", "duplicate", "type"])
def test_schema_errors(mutation):
    scenario, _, feedback = panel()
    if mutation == "missing":
        del feedback[0]["support"]
    elif mutation == "confidence":
        feedback[0]["confidence"] = "certain"
    elif mutation == "duplicate":
        feedback[0]["stakeholder"] = feedback[1]["stakeholder"]
    else:
        feedback[0]["support"] = 12
    assert "schema" in {f["rule"] for f in moderate_feedback(feedback, scenario)}


@pytest.mark.parametrize("field,value", [("reason", ""), ("evidence_that_would_change_decision", " "), ("decision", "ACCEPT"), ("stakeholder", "Unknown")])
def test_invalid_decisions_rejected(field, value):
    _, _, feedback = panel()
    decisions = sample_decisions(feedback)
    decisions[0][field] = value
    with pytest.raises(ValueError):
        record_decisions(decisions, feedback)


def test_exports_preserve_feedback_decisions_and_input(tmp_path):
    scenario, cards, feedback = panel()
    decisions = sample_decisions(feedback)
    assert set(d["decision"] for d in decisions) == set(DECISIONS)
    questions = generate_oral_defence_questions(decisions)
    assert len(questions) == 5
    result = export_run_summary(scenario, cards, feedback, [], build_conflict_matrix(feedback, scenario), decisions, questions, tmp_path / "run")
    assert (tmp_path / "run.md").read_text() == result["markdown"]
    assert (tmp_path / "run.csv").read_bytes().decode() == result["csv"]
    assert result["markdown"].splitlines()[1] == NOTICE
    rows = list(csv.DictReader(io.StringIO(result["csv"])))
    assert rows[0]["details"] == NOTICE
    assert json.loads(rows[1]["details"])["scenario"] == scenario
    exported = [r for r in rows if r["record_type"] == "feedback"]
    assert [{k: r[k] for k in RESPONSE_FIELDS} for r in exported] == feedback
    assert len([r for r in rows if r["record_type"] == "decision"]) == 5


def test_llm_mode_is_explicitly_unavailable():
    scenario, cards, _ = panel()
    with pytest.raises(NotImplementedError, match="not wired"):
        generate_stakeholder_feedback(cards, scenario, mode="llm")
    with pytest.raises(NotImplementedError):
        LLMProvider.generate(None, cards[0], scenario)
