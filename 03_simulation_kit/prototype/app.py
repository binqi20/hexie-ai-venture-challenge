"""Minimal local facilitator view for SYNTHETIC deterministic demonstrations."""
from engine import (NOTICE, DECISIONS, load_personas, load_scenario,
                    generate_stakeholder_feedback, moderate_feedback,
                    build_conflict_matrix, record_decisions,
                    generate_oral_defence_questions, export_run_summary)


def main() -> None:
    """Import Streamlit only when launched; no provider, login or session store."""
    import streamlit as st

    st.set_page_config(page_title="Stakeholder panel", layout="wide")
    st.title("Stakeholder-Agent Swarm Simulation")
    st.markdown(NOTICE)
    st.caption("Deterministic demonstration. Simulated feedback may be incomplete. Human review is required. No grading.")
    scenarios = [load_scenario(f"demo_0{i}") for i in (1, 2, 3)]
    by_id = {s["id"]: s for s in scenarios}
    selected = st.selectbox("Scenario", list(by_id), format_func=lambda key: by_id[key]["title"])
    lender = st.checkbox("Use lender / green-finance variant")
    buyer = st.checkbox("Use enterprise-buyer variant")
    scenario = by_id[selected]
    personas = load_personas(investor_variant=lender, customer_variant=buyer)
    st.write(scenario["brief"])
    with st.expander("Shared assumptions and evidence placeholders"):
        st.json({k: scenario[k] for k in ("assumptions", "evidence_bundle")})
    responses = generate_stakeholder_feedback(personas, scenario)
    flags = moderate_feedback(responses, scenario)
    conflicts = build_conflict_matrix(responses, scenario)
    for response in responses:
        with st.expander(response["stakeholder"], expanded=True):
            st.json(response)
    st.subheader("Facilitator moderation")
    st.write(flags or "No lexical flags detected. This does not establish accuracy or safety.")
    st.subheader("Designed conflict matrix")
    st.dataframe(conflicts, hide_index=True, use_container_width=True)
    st.subheader("SYNTHETIC practice decision table")
    st.caption("Complete each key point, reason and evidence that would change the decision. Do not enter personal or confidential data.")
    rows = [{"stakeholder": r["stakeholder"], "key_point": "", "decision": "DEFER", "reason": "", "evidence_that_would_change_decision": ""} for r in responses]
    run_key = f"{selected}_{lender}_{buyer}"
    edited = st.data_editor(rows, key=f"decisions_{run_key}", disabled=["stakeholder"],
                            column_config={"decision": st.column_config.SelectboxColumn("Decision", options=list(DECISIONS), required=True)},
                            hide_index=True, use_container_width=True)
    reviewed = st.checkbox("I have reviewed the responses and resolved any flagged concerns for this demonstration.", key=f"review_{run_key}")
    if not reviewed:
        st.info("Facilitator review and a complete decision table are needed before export.")
        return
    try:
        decisions = record_decisions(edited, responses)
    except ValueError as error:
        st.info(str(error))
        return
    questions = generate_oral_defence_questions(decisions)
    st.subheader("Oral defence prompts")
    st.write(questions)
    exports = export_run_summary(scenario, personas, responses, flags, conflicts, decisions, questions)
    st.download_button("Download Markdown", exports["markdown"], file_name=f"{selected}.md", mime="text/markdown")
    st.download_button("Download CSV", exports["csv"], file_name=f"{selected}.csv", mime="text/csv")


if __name__ == "__main__":
    main()
