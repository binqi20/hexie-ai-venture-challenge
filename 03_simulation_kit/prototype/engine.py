"""Offline stakeholder-panel prototype. No network, grading or stored sessions."""
from __future__ import annotations

import csv
import io
import json
import re
from pathlib import Path
from typing import Protocol

import yaml

KIT_DIR = Path(__file__).resolve().parent.parent
NOTICE = "> SYNTHETIC CASE. Generated for internal validation of the HeXie-AI Venture Challenge resources. Not student work."
BASE_IDS = ("investor", "customer", "operations", "regulator", "community")
ROLES = ("Investor", "Customer", "Supplier / Operations Partner", "Regulator", "Community / Ethics Stakeholder")
PERSONA_FIELDS = ("id", "name", "role", "stake", "objectives", "decision_criteria", "red_lines", "evidence_expectations", "conflict_levers", "communication_style", "prohibited_moves")
RESPONSE_FIELDS = ("stakeholder", "top_concern", "support", "challenge", "evidence_needed", "assumption_or_fact", "confidence", "suggested_next_test")
DECISION_FIELDS = ("stakeholder", "key_point", "decision", "reason", "evidence_that_would_change_decision")
DECISIONS = ("ADOPT", "PARTIALLY ADOPT", "REJECT", "DEFER")


class LLMProvider(Protocol):
    """Future provider interface. LLM mode is not wired in this release."""

    def generate(self, persona: dict, scenario: dict) -> dict:
        """An eventual adapter must implement this; no provider is included."""
        raise NotImplementedError("LLM mode is not wired in this release.")


def _load(path: Path, key: str) -> list[dict]:
    with Path(path).open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict) or not isinstance(data.get(key), list):
        raise ValueError(f"Expected a YAML list named {key}.")
    return data[key]


def load_personas(path: Path | None = None, *, investor_variant: bool = False,
                  customer_variant: bool = False) -> list[dict]:
    """Load five ordered roles; requested variants replace their base cards."""
    cards = _load(path or KIT_DIR / "personas.yaml", "personas")
    for card in cards:
        if not isinstance(card, dict) or any(not card.get(k) for k in PERSONA_FIELDS):
            raise ValueError("Each persona must have all required, non-empty fields.")
        for key in ("objectives", "decision_criteria", "red_lines", "evidence_expectations", "conflict_levers", "prohibited_moves"):
            if not isinstance(card[key], list) or any(not isinstance(v, str) or not v.strip() for v in card[key]):
                raise ValueError(f"Persona {key} must contain non-empty strings.")
    by_id = {card["id"]: card for card in cards}
    if len(by_id) != len(cards):
        raise ValueError("Persona IDs must be unique.")
    selected = list(BASE_IDS)
    if investor_variant:
        selected[0] = "lender_green_finance"
    if customer_variant:
        selected[1] = "enterprise_buyer"
    if any(key not in by_id for key in selected):
        raise ValueError("A requested persona is missing.")
    result = [by_id[key] for key in selected]
    if tuple(card["role"] for card in result) != ROLES:
        raise ValueError("The panel must retain the five canonical roles in order.")
    return result


def load_scenario(scenario_id: str = "demo_01", path: Path | None = None) -> dict:
    """Load a frozen demonstration brief with labelled assumptions/placeholders."""
    scenarios = _load(path or KIT_DIR / "scenarios.yaml", "scenarios")
    if len({s["id"] for s in scenarios}) != len(scenarios):
        raise ValueError("Scenario IDs must be unique.")
    for scenario in scenarios:
        if any(not scenario.get(k) for k in ("id", "title", "brief", "assumptions", "evidence_bundle", "designed_tensions", "synthetic_notice")):
            raise ValueError("Scenario fields must be present and non-empty.")
        if not 2 <= len(scenario["designed_tensions"]) <= 3:
            raise ValueError("A scenario needs two to three designed tensions.")
        covered = set()
        for tension in scenario["designed_tensions"]:
            if not tension.get("question") or len(tension.get("positions", {})) < 2:
                raise ValueError("A tension needs a question and at least two positions.")
            covered.update(tension["positions"])
        if covered != set(ROLES):
            raise ValueError("Tensions must cover exactly the five canonical roles.")
        if scenario["synthetic_notice"] != NOTICE:
            raise ValueError("The canonical synthetic notice is required.")
    for scenario in scenarios:
        if scenario["id"] == scenario_id:
            return scenario
    raise ValueError(f"Unknown scenario: {scenario_id}")


def generate_stakeholder_feedback(personas: list[dict], scenario: dict,
                                  mode: str = "deterministic",
                                  provider: LLMProvider | None = None) -> list[dict]:
    """Compose role-conditioned templates from fields and tensions, without randomness.

    No inference, retrieval or claim verification occurs. Provider is reserved;
    requesting LLM mode always fails explicitly, including with a provider.
    """
    if mode == "llm":
        raise NotImplementedError("LLM mode is not wired in this release.")
    if mode != "deterministic":
        raise ValueError("Mode must be deterministic or llm.")
    responses = []
    for card in personas:
        tensions = [t for t in scenario["designed_tensions"] if card["role"] in t["positions"]]
        if not tensions:
            raise ValueError(f"No designed tension for {card['role']}.")
        challenges = " ".join(f"{t['question']} Position: {t['positions'][card['role']]}" for t in tensions)
        if card["role"] == "Regulator":
            challenges += " I cannot verify applicable rules from these materials. This may require qualified review; this is not legal advice."
        responses.append({
            "stakeholder": card["role"],
            "top_concern": f"{card['name']}: {card['stake']} Priorities: {'; '.join(card['decision_criteria'])}.",
            "support": f"Conditional support for a bounded test addressing: {'; '.join(card['objectives'])}.",
            "challenge": challenges + f" Red lines: {'; '.join(card['red_lines'])}. Tension lens: {'; '.join(card['conflict_levers'])}.",
            "evidence_needed": "; ".join(card["evidence_expectations"]) + ". Inspect the status and supporting content of each evidence entry; placeholders are requests for evidence, not completed tests.",
            "assumption_or_fact": "SYNTHETIC stakeholder judgement on team assumptions; no empirical facts verified. " + " ".join(scenario["assumptions"]),
            "confidence": "low",
            "suggested_next_test": f"Design and review: {card['evidence_expectations'][0]}. Record what result would change the decision before collecting evidence.",
        })
    return responses


def moderate_feedback(feedback: list[dict], scenario: dict | None = None) -> list[dict]:
    """Return review flags without modifying feedback or certifying its safety.

    Check schema, enum and panel coverage. Scan each sentence for digits lacking
    an explicit assumption/estimate prefix or a [source:ID] marker referring to
    supplied evidence. Placeholders never qualify. This lexical screen cannot
    verify a source's meaning, detect every false claim, or replace human review.
    """
    flags = []
    supplied = {e["id"] for e in (scenario or {}).get("evidence_bundle", []) if e.get("status") == "supplied"}
    def flag(who, field, rule, text):
        flags.append({"stakeholder": who, "field": field, "rule": rule, "text": text})
    seen = []
    for response in feedback:
        if not isinstance(response, dict):
            flag("Unknown", "response", "schema", "Response must be an object.")
            continue
        who = response.get("stakeholder", "Unknown")
        seen.append(who)
        if set(response) != set(RESPONSE_FIELDS):
            flag(who, "response", "schema", "Required response fields must match exactly.")
        for field in RESPONSE_FIELDS:
            value = response.get(field)
            if not isinstance(value, str) or not value.strip():
                flag(who, field, "schema", "Expected a non-empty string.")
                continue
            if field == "confidence" and value not in ("low", "medium", "high"):
                flag(who, field, "schema", "Confidence must be low, medium or high.")
            for sentence in re.split(r"(?<=[.!?])\s+|\n+", value):
                refs = re.findall(r"\[source:([^\]]+)\]", sentence, re.I)
                if any(ref not in supplied for ref in refs):
                    flag(who, field, "unverified_source", sentence)
                plain = re.sub(r"\[source:[^\]]+\]", "", sentence, flags=re.I)
                labelled = bool(re.match(r"\s*(?:team\s+)?(?:assumption|estimate|hypothesis)\s*:", plain, re.I))
                if re.search(r"\d", plain) and not labelled and not any(ref in supplied for ref in refs):
                    flag(who, field, "unsupported_number", sentence)
                if re.search(r"\b(guaranteed|guarantee|always|never|certainly|infallible|risk-free)\b", plain, re.I):
                    flag(who, field, "absolute_language", sentence)
                if re.search(r"\b(legally compliant|fully compliant|legally required|the law requires|you must legally|legal advice is|no permit is required|no licence is required|no license is required|you are legally|legally approved)\b", plain, re.I):
                    flag(who, field, "legal_advice", sentence)
    if len(seen) != len(ROLES) or any(seen.count(role) != 1 for role in ROLES):
        flag("Panel", "stakeholder", "schema", "Expected one response per canonical role.")
    return flags


def build_conflict_matrix(feedback: list[dict], scenario: dict) -> list[dict]:
    """Map authored competing positions to feedback; this is not inferred conflict."""
    available = {r["stakeholder"] for r in feedback}
    return [{"tension": t["id"], "question": t["question"], "stakeholder": role, "position": position}
            for t in scenario["designed_tensions"]
            for role, position in t["positions"].items() if role in available]


def record_decisions(decisions: list[dict], feedback: list[dict]) -> list[dict]:
    """Validate a complete role-level log with reasons and change-of-mind evidence.

    The small prototype records one key point per role. Detailed logs may be
    maintained in the assessment template. Labels never indicate grade quality.
    """
    expected = [r["stakeholder"] for r in feedback]
    if len(decisions) != len(expected):
        raise ValueError("Record one decision for each stakeholder.")
    recorded = []
    for decision in decisions:
        if any(not isinstance(decision.get(k), str) or not decision[k].strip() for k in DECISION_FIELDS):
            raise ValueError("Every decision needs a key point, reason and evidence that would change it.")
        if decision["decision"] not in DECISIONS:
            raise ValueError("Use ADOPT, PARTIALLY ADOPT, REJECT or DEFER.")
        recorded.append({k: decision[k].strip() for k in DECISION_FIELDS})
    if sorted(d["stakeholder"] for d in recorded) != sorted(expected):
        raise ValueError("Record each stakeholder exactly once.")
    return recorded


def generate_oral_defence_questions(decisions: list[dict]) -> list[dict]:
    """Return one human-facilitated question per canonical capability cluster."""
    conflict = next((d for d in decisions if d["decision"] != "ADOPT"), decisions[0] if decisions else None)
    focus = f"Your {conflict['decision']} decision for {conflict['stakeholder']}" if conflict else "Your main stakeholder decision"
    return [
        {"cluster": "Opportunity Recognition", "question": "Which credible observation would change your framing of the opportunity, and why?"},
        {"cluster": "Feasibility Judgement", "question": "Defend a proceed, pivot, pause or stop judgement. Which untested assumption matters most?"},
        {"cluster": "Stakeholder Reasoning", "question": f"{focus}: who bears the cost, and what evidence would change your position?"},
        {"cluster": "Ethical Positioning", "question": "Which anticipated harm raised by the Regulator or Community role needs an owned, costed mechanism, and who may remain exposed?"},
        {"cluster": "Venture Communication", "question": "State your recommendation clearly, then explain its strongest counterargument and remaining uncertainty."},
    ]


def export_run_summary(scenario: dict, personas: list[dict], feedback: list[dict],
                       flags: list[dict], conflict_matrix: list[dict], decisions: list[dict],
                       questions: list[dict], output_base: Path | None = None) -> dict[str, str]:
    """Render Markdown and record-typed CSV; optionally write the explicit export.

    No persistent session store exists. CSV details retain complete input,
    moderation, conflict and question records as JSON; feedback/decisions have
    separate columns. Both exports carry the synthetic provenance notice.
    """
    decisions = record_decisions(decisions, feedback)
    lines = [f"# {scenario['title']}: deterministic demonstration", NOTICE, "",
             "SYNTHETIC sample decisions, not student responses. No LLM calls or grading.", "",
             "## Frozen input", "```json", json.dumps({"scenario": scenario, "personas": personas}, ensure_ascii=False, indent=2), "```", "",
             "## Stakeholder challenges received"]
    for response in feedback:
        lines += [f"### {response['stakeholder']}"]
        lines += [f"- **{key}:** {response[key]}" for key in RESPONSE_FIELDS if key != "stakeholder"]
    lines += ["", "## Moderator flags", "```json", json.dumps(flags, ensure_ascii=False, indent=2), "```",
              "No flags is not evidence of factual accuracy. Human review remains necessary.", "", "## Conflict matrix"]
    def cell(value):
        return str(value).replace("|", "\\|").replace("\n", " ")
    def table(headers, rows):
        return ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"] + ["| " + " | ".join(cell(v) for v in row) + " |" for row in rows]
    lines += table(["Tension", "Question", "Stakeholder", "Position"], [[r[k] for k in ("tension", "question", "stakeholder", "position")] for r in conflict_matrix])
    lines += ["", "## Team decisions"]
    lines += table(["Stakeholder", "Key point", "Decision", "Reason", "Evidence that would change our decision"], [[r[k] for k in DECISION_FIELDS] for r in decisions])
    lines += ["", "## Oral defence questions"] + [f"- **{q['cluster']}:** {q['question']}" for q in questions]
    markdown = "\n".join(lines) + "\n"
    columns = ["record_type", *RESPONSE_FIELDS, *[k for k in DECISION_FIELDS if k != "stakeholder"], "details"]
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=columns)
    writer.writeheader()
    writer.writerow({"record_type": "provenance", "details": NOTICE})
    writer.writerow({"record_type": "input", "details": json.dumps({"scenario": scenario, "personas": personas, "mode": "deterministic", "decisions": "SYNTHETIC"}, ensure_ascii=False)})
    for record_type, records in (("feedback", feedback), ("decision", decisions)):
        for record in records:
            writer.writerow({"record_type": record_type, **record})
    for record_type, records in (("moderator_flag", flags), ("conflict", conflict_matrix), ("oral_defence", questions)):
        for record in records:
            writer.writerow({"record_type": record_type, "details": json.dumps(record, ensure_ascii=False)})
    result = {"markdown": markdown, "csv": buffer.getvalue()}
    if output_base is not None:
        base = Path(output_base)
        base.parent.mkdir(parents=True, exist_ok=True)
        base.with_suffix(".md").write_text(result["markdown"], encoding="utf-8")
        base.with_suffix(".csv").write_text(result["csv"], encoding="utf-8")
    return result
