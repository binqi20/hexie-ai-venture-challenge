"""Run the first SYNTHETIC demonstration offline and export its full record."""
from pathlib import Path

from engine import (load_personas, load_scenario, generate_stakeholder_feedback,
                    moderate_feedback, build_conflict_matrix, record_decisions,
                    generate_oral_defence_questions, export_run_summary)


def sample_decisions(feedback: list[dict]) -> list[dict]:
    """Return illustrative authored decisions, never purported student work."""
    choices = [
        ("PARTIALLY ADOPT", "Test demand promptly", "Run a bounded demand test while limiting enquiry types until review capacity is understood.", "Evidence that review capacity can safely support a wider enquiry scope."),
        ("ADOPT", "Preserve access to human support", "A disputed answer needs a usable route to review; include the support cost in the test plan.", "Task-test evidence that an alternative route provides equally usable redress."),
        ("REJECT", "Narrow the supported enquiry types to fit current review capacity", "Reject narrowing the enquiry scope as the preferred response; propose a staffed review trial first, keeping deployment paused until capacity is established.", "A delivery rehearsal showing that expansion creates unresolved failure-handling gaps."),
        ("DEFER", "Resolve applicable rules and safety review", "Applicable rules cannot be established from placeholders; defer the launch judgement pending qualified review.", "A documented review of the proposed data flow, operating context and safeguards."),
        ("ADOPT", "Examine exclusion from automated support", "Include an alternative human route and identify who bears its cost before proposing scale.", "Evidence that the alternative still excludes intended users or shifts burdens unfairly."),
    ]
    return record_decisions([
        {"stakeholder": response["stakeholder"], "key_point": key_point, "decision": decision,
         "reason": reason, "evidence_that_would_change_decision": evidence}
        for response, (decision, key_point, reason, evidence) in zip(feedback, choices)
    ], feedback)


def main() -> None:
    """Write explicit demonstration exports next to this script."""
    personas = load_personas()
    scenario = load_scenario()
    feedback = generate_stakeholder_feedback(personas, scenario)
    flags = moderate_feedback(feedback, scenario)
    conflicts = build_conflict_matrix(feedback, scenario)
    decisions = sample_decisions(feedback)
    questions = generate_oral_defence_questions(decisions)
    output = Path(__file__).resolve().parent / "sample_runs" / "demo_run"
    export_run_summary(scenario, personas, feedback, flags, conflicts, decisions, questions, output)
    print(f"SYNTHETIC demo: {len(feedback)} responses, {len(flags)} moderator flags, {len(decisions)} decisions.")
    print(output.with_suffix(".md"))
    print(output.with_suffix(".csv"))


if __name__ == "__main__":
    main()
