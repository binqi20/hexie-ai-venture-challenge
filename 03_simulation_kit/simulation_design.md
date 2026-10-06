# Stakeholder-Agent Swarm Simulation: design

Version 1.0, October 2026. This is a design package and working deterministic prototype. No students, judges or observers have taken part. The first live run is scheduled for early December 2026.

## Educational purpose and operationalisation

The simulation is designed to elicit independent judgement about a venture when stakeholder priorities conflict. Students identify the assumption behind a challenge, examine its evidence, choose a response and defend the consequences. The resulting evidence contributes to Opportunity Recognition, Feasibility Judgement, Stakeholder Reasoning, Ethical Positioning and Venture Communication. Accepting more comments does not itself demonstrate stronger capability.

The approved label is **Stakeholder-Agent Swarm Simulation**. Its operationalisation is a moderated multi-voice panel: five roles examine a shared brief independently, followed by facilitator review and student synthesis. A free-running swarm could change the task through uncontrolled conversation, unequal turns or invented context. Fixed roles and structured responses make the challenge inspectable and repeatable. This choice follows the project's redesign towards bounded interaction.

The prototype demonstrates this interaction structure offline. It assembles authored text deterministically from persona fields and scenario tensions. It does not reason about a new business, simulate negotiation or establish whether advice is correct. The prompt library specifies a possible future LLM workflow; that mode is explicitly unavailable in this release.

## Five roles and two substitutions

The Investor examines viability, scalability, execution risk and return. The Customer asks whether the venture fits a problem and deserves trust, adoption and payment. The Supplier / Operations Partner examines deliverability, dependence, terms and capacity. The Regulator identifies compliance, procedural-legitimacy and public-safety questions requiring review. The Community / Ethics Stakeholder examines access, distributional effects, sustainability and local impact.

Each card specifies its stake, objectives, decision criteria, red lines, evidence expectations, conflict levers, communication style and prohibited moves. Roles contain no demographic profiles, invented interviews or real business identities. Conditional support accompanies challenge so that disagreement offers a possible next step.

Two variants replace existing roles while retaining the five-role structure. The lender / green-finance variant replaces the Investor and examines commercial viability, environmental impact, risk and evidence credibility. The enterprise-buyer variant replaces the Customer and examines fit, delivery capability, reliability, quality assurance and responsiveness. The lender variant draws on a consultation with a senior green-finance manager at a commercial bank. The enterprise-buyer variant draws on a consultation with a planning manager at a large trading enterprise and a green-finance analyst. The cards are authored operationalisations of consultation inputs, not quotations or claims of consultee endorsement.

## Shared evidence and bounded conflict

The governing rule is **shared facts, different stakeholder utilities**. Every role receives the same brief, assumptions and evidence bundle. A supplied source must have an identifier, a checkable location and a clear relationship to the claim. A placeholder is a request for evidence; it cannot support a factual assertion. Unsupported propositions must be expressed as questions or explicitly labelled assumptions. A role cannot invent a law, customer response, market statistic or environmental saving to strengthen its position.

Scenario authors define two or three tensions through a shared question and distinct stakeholder positions. Synthetic simulation QA on 5 October 2026 found that different requests could be satisfied in sequence, leaving no demonstrated conflict. The revised prompt therefore requires the moderator, before the panel responds, to identify a binding constraint from the brief's stated assumptions and specify the common decision. At least two roles must seek incompatible uses of that same price, budget, capacity, scope, data or other supported constraint, so satisfying one demand requires giving up part of the other. The moderator checks this again after generation. Estimated limits and conditional shortfalls remain labelled assumptions; scarcity and empirical facts cannot be invented to create disagreement. A panel with no defensible constraint or competing demands is held for revision. This rule comes from internal synthetic QA, with no students involved; it is a prompt and facilitator check, not a new capability of the deterministic prototype.

The three demonstration briefs concern an AI-enabled service, science commercialisation and a mission-led sustainability venture. They are fictional, labelled SYNTHETIC and separate from the worked cases in `05_evaluation/exemplar_cases/`. Their evidence bundles contain placeholders only. They do not report completed interviews, experiments or environmental measurements.

## Hidden moderator and human oversight

The hidden moderator is a quality-control function, not an additional stakeholder. “Hidden” means outside the student-facing panel; its existence and purpose are disclosed. It checks response completeness, unsupported claims, tone and role boundaries, and preserves unresolved disagreement for student judgement. It cannot award marks, determine the best venture or resolve trade-offs on a team's behalf.

In the prototype, this function checks the response schema and screens sentences for unlabelled digits, absolute words and selected legal-advice phrases. It flags source markers that refer to missing evidence or placeholders. A sentence-level assumption prefix can identify a numerical estimate, but does not validate it. The screen has false positives and false negatives, particularly for qualitative claims or paraphrased authority claims. Zero flags means only that these checks found nothing.

The facilitator reviews all responses before presenting them to students. A flagged response is held for correction or discussed as an error, with a clear explanation. Staff check that concerns differ substantively and that any proposed test is appropriate. They can stop the exercise and use printed role cards. Human-led pedagogy, AI-assisted simulation, no AI-only decisions about students is the operating model.

## Structured output and student synthesis

Each response contains `stakeholder`, `top_concern`, `support`, `challenge`, `evidence_needed`, `assumption_or_fact`, `confidence` and `suggested_next_test`. Confidence is low, medium or high. It describes the stated judgement within the supplied evidence and must be explained in `assumption_or_fact`; it is neither a probability nor a grade. Demonstration responses use low confidence because their empirical assumptions are untested.

Phase A provides the Venture Brief, AI-Use Declaration: Stage 1 and first Venture Value Map. In Phase B, the approved challenges enter the Stakeholder Response Log in canonical role order. Teams record **ADOPT**, **PARTIALLY ADOPT**, **REJECT** or **DEFER** for each key point, with a reason and the evidence that would change the decision. Partial adoption specifies what is retained and bounded. Deferral identifies missing evidence and the decision awaiting it.

Phase C requires revision, the Decision Memo, revised Venture Value Map, final AI-use declaration and oral defence. The defence lasts 8 to 12 minutes and examines independent command of the reasoning. The prototype supplies one question per capability cluster for facilitator selection. It produces no answers or scores. Markdown and CSV exports preserve inputs, challenges, flags, designed conflicts and decisions; they do not establish learning effects.

## Anticipated harms and the Venture Value Lens

Regulator and Community challenges feed “Anticipated harms and response” in the Venture Value Map. Teams identify the affected role, the mechanism through which harm could arise, relevant uncertainty and the proposed response. They connect that response to a material topic and a specific readiness mechanism, including ownership and resource implications where possible.

An unresolved harm remains visible even if the team rejects a proposed mitigation. The alignment thesis explains who benefits, who pays and which risk remains. Anticipated harms replace controversy deductions because a pre-launch venture lacks an operating track record. The Venture Value Lens informs the existing capability clusters; it adds no sixth cluster and produces no venture letter rating. The full ESG-derived method belongs in `04_venture_value_lens/`.

## Boundaries and source status

Adaptation changes role priorities and scenario evidence while preserving canonical roles, shared facts, decision labels and human review. A consultation with a STEM academic supplies the documented basis for STEM adaptation, including technical-feasibility questions and oral-defence prompts. Neither consultation input nor deterministic reproducibility demonstrates educational effectiveness.

No personal or confidential data are needed for these demonstrations. The app has no login or persistent session store; explicit exports remain files under facilitator control. Confirm locally before use: institutional storage, retention arrangements and any future provider approval, through your approved ethics documents and institutional decisions.
