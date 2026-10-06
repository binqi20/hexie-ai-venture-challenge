# Adapting the stakeholder panel

Keep the five canonical roles and capability clusters. Change the discipline-specific decision, evidence expectations and tensions. The panel should expose a consequential choice that students can defend within the activity's scope. A consultation with a STEM academic covered personas, conflicting feedback, technical-feasibility questions and oral-defence prompts. The worked example below is an authored implementation of that input; it is not a record of a consultation exercise or completed technical trial.

## Configuration workflow

1. Identify the venture decision and the discipline-specific uncertainty. Define what evidence could support a proceed, pivot, pause or stop judgement. Separate a fictional premise from a claim about real technology.
2. Copy a scenario entry in `scenarios.yaml`. Give it a unique ID, title, the canonical synthetic notice, brief, explicit assumptions and evidence placeholders. Define two or three questions with contrasting positions under the exact canonical role names. Across the tensions, include all five roles. Remove sector-specific claims unless the frozen evidence pack supports them.
3. Edit the relevant persona fields in `personas.yaml`. Preserve the required field names and base IDs. A specialist Customer can ask about laboratory workflow; the Operations Partner can ask about calibration and maintenance. Retain their decision interests and prohibited moves. Do not add demographic detail or pretend a role represents interviewed users.
4. Use `load_personas(investor_variant=True)` for the lender / green-finance substitution, `customer_variant=True` for the enterprise-buyer substitution, or both. Each replaces one role. Consultations with green-finance practitioners at a commercial bank and a planning manager at a large trading enterprise inform these variants; they do not imply that a real institution has approved the venture.
5. Freeze the scenario and cards before comparing runs. Use source IDs, status and locations for genuinely supplied evidence. Mark missing material `placeholder`. External documents supplied later require human source checking. Generation remains a template demonstration even when evidence is supplied; it will not read attachments or synthesise research.
6. Run the tests and inspect the output role by role. Check that the tension remains real when facts are shared, support is conditional, concerns can be acted on and no role invents technical or regulatory authority. Revise the authored cards if necessary. Record the changed configuration through the explicit export.

The engine accepts a scenario ID through `load_scenario('your_id')`. Existing IDs can be edited without changing code. The minimal app and `prototype/run_demo.py` intentionally expose the three shipped scenarios and the first demonstration respectively. To expose an additional ID in the app, add it to the scenario list in `prototype/app.py`; this small selector edit does not require an engine rebuild. The app is a facilitator demonstration, not a content-management system.

## Worked mini-example: sensor-supported crop monitoring
> SYNTHETIC CASE. Generated for internal validation of the HeXie-AI Venture Challenge resources. Not student work.

**Decision:** whether a proposed crop-monitoring concept is ready for a bounded field trial. The technical concept and potential demand are team assumptions. No measured sensor accuracy, crop-yield gain or environmental saving is supplied. Start from `demo_02`.

**Persona swap:** retain the Investor, Regulator and Community roles. Use the enterprise-buyer variant as the Customer, with a hypothetical agricultural operator's need for usable measurements and dependable service. In the Operations Partner card, focus evidence expectations on calibration, field maintenance and failure recovery. These are role criteria, not empirical descriptions of actual buyers.

| Shared uncertainty | Competing priorities | Evidence request |
|---|---|---|
| Whether bench performance would transfer to field conditions | Investor wants staged spending tied to viability; Operations Partner wants repeatable delivery under variable conditions | A proposed test protocol identifying operating conditions, failure criteria and responsibility for maintenance |
| Whether the measurement informs a useful action | Enterprise buyer wants operational relevance and responsiveness; Community role asks whether access and support costs exclude some users | A task walkthrough and benefit/burden map, labelled as planned until carried out |
| Whether deployment creates unresolved safety questions | Regulator asks for qualified review; Investor asks how review affects the next decision | A review question describing the proposed activity and safeguards, without claiming legal approval |

**Sample synthesis:** DEFER a commitment to a broad field trial because performance and maintenance demands are untested. Evidence that would change this decision is a reviewed trial protocol and preliminary results addressing the defined operating conditions. PARTIALLY ADOPT the buyer's request for customisation by testing one defined use context first, while leaving wider integration for later. Reconsider that boundary if evidence shows the measurement is unusable without integration. These are illustrative decisions, not preferred answers or a scoring key.

**Oral-defence follow-up:** “Which operating condition is most likely to invalidate your technical-feasibility judgement, and what result would make you pause?” Link this to Feasibility Judgement. Ask who may bear unresolved maintenance costs for Ethical Positioning. Do not assess scientific sophistication merely from specialist vocabulary.

## Preserve the assessment and oversight contract

Keep ADOPT, PARTIALLY ADOPT, REJECT and DEFER with reasons and change-of-mind evidence. Use the canonical submission headings in the assessment kit, including the two AI-use declarations. Carry Regulator and Community challenges into the Venture Value Map's anticipated harms, then explain the proposed mechanisms and remaining exposure. The Venture Value Lens remains part of the existing capability evidence, with no additional cluster or venture letter rating.

Before a live use, the facilitator checks domain-specific safety issues with appropriate expertise, prepares accessible materials and a printed alternative, and confirms the applicable ethics and data arrangements. Confirm these operational arrangements locally before use, through your approved documents and named institutional owners. Do not infer a new module's assessment rules or ethics coverage from this worked example. December participation remains voluntary and separate from module assessment.
