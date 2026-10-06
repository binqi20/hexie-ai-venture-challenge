# HeXie-AI Venture Challenge: modular adoption kit

Version 1.0, October 2026 | Project EASE-R1-2526-85

## Purpose and present status

This kit helps colleagues organise a venture challenge in which students use AI transparently, respond to conflicting stakeholder feedback, and defend their own decisions. It combines a competition playbook, five-cluster capability rubric, moderated stakeholder simulation, and Venture Value Lens. The Lens examines commercial and social value through exposure, readiness, and explicit trade-offs. It supplies evidence for existing rubric clusters; it adds no sixth cluster or venture letter rating.

The package is a design and prototype resource. No students, judges, or observers have taken part in the Challenge. The first live run is scheduled for early December 2026 at IBSS. Consultations inform the design; SYNTHETIC checks provide internal QA. Human judge calibration and participant evaluation remain prospective. Publication on Learning Mall is not claimed.

## Choose an adoption route

| Route | Suitable starting point | Action and boundary |
|---|---|---|
| Run as-is | A colleague wants the venture challenge with the default capabilities, roles and sequence | Use the playbook, default rubric weights, declaration templates, five stakeholder roles and Value Lens. Confirm local staffing, consent, access and timing before delivery. “As-is” describes educational design, not automatic ethics or platform approval. |
| Adapt lightly | The capabilities fit, but the venture context or delivery arrangements differ | Replace the scenario, select role variants, choose a relevant SASB industry and adjust timing or weights with reasons. Preserve decision records, human defence and oversight. Use the adaptation guide to record changes. |
| Reuse the design pattern in another discipline | A colleague wants an authentic challenge with conflicting perspectives and visible student judgement | Reframe the problem and disciplinary evidence. Map local outcomes explicitly to the five capabilities; retain transparent AI use, reasoned decisions, defence and the Value Lens sequence. Treat substantial changes as a new local design requiring review. |

Read [the quick start](quick_start_guide.md) first. It is designed for 10 to 15 minutes of orientation, not complete preparation for teaching.

## Intended users and responsibilities

Module leaders choose outcomes, local adaptations and delivery conditions. Facilitators manage the shared facts and review stakeholder feedback before release. Human assessors apply the rubric and calibrate interpretations. Educational developers and Learning Mall colleagues support adaptation, accessibility and distribution. The project leader confirms evaluation scope and evidence claims.

The initial December activity is voluntary and separate from module assessment. Reuse within formal assessment would require the adopting module's own review and approval arrangements; the December plan does not change any module assessment.

## Components and exact package paths

All paths below are relative to the repository root.

| Component | Files to use |
|---|---|
| Overview and design | `README.md`; `REFERENCES.md`; `00_design/project_architecture.md`; `00_design/hexie_design_logic.md` |
| Delivery | `01_playbook/competition_playbook.md`; `01_playbook/facilitator_run_sheet.md` |
| Judging and defence | `02_assessment_kit/capability_rubric.md`; `02_assessment_kit/scoring_sheet_template.csv`; `02_assessment_kit/oral_defence_guide.md`; `02_assessment_kit/judge_calibration_guide.md` |
| Student records | `02_assessment_kit/submission_pack_overview.md`; `02_assessment_kit/ai_use_declaration.md`; `02_assessment_kit/decision_memo_template.md`; `02_assessment_kit/stakeholder_response_log_template.md` |
| Stakeholder simulation | `03_simulation_kit/simulation_design.md`; `03_simulation_kit/personas.yaml`; `03_simulation_kit/scenarios.yaml`; `03_simulation_kit/prompts.md`; `03_simulation_kit/adaptation_guide.md` |
| Offline demonstration | `03_simulation_kit/prototype/README.md`; `03_simulation_kit/prototype/engine.py`; `03_simulation_kit/prototype/app.py`; `03_simulation_kit/prototype/run_demo.py`; `03_simulation_kit/prototype/requirements.txt`; `03_simulation_kit/prototype/tests/`; `03_simulation_kit/prototype/sample_runs/` |
| Venture Value Lens | `04_venture_value_lens/value_lens_method.md`; `04_venture_value_lens/materiality_worksheet.md`; `04_venture_value_lens/value_alignment_map_template.md`; `04_venture_value_lens/industry_topics.md`; `04_venture_value_lens/worked_example.md`; `04_venture_value_lens/facilitator_note.md` |
| SYNTHETIC exemplar cases | `05_evaluation/exemplar_cases/` |
| Live evaluation forms | `05_evaluation/instruments/judge_feedback_form.md`; `05_evaluation/instruments/participant_feedback_form.md`; `05_evaluation/instruments/observer_notes_form.md` |
| Responsible operation | `06_responsible_ai/responsible_ai_plan.md` |
| Adoption and publication | `07_adoption_kit/quick_start_guide.md`; `07_adoption_kit/adaptation_guide.md`; `07_adoption_kit/good_practice_note.md`; `07_adoption_kit/learning_mall_readiness_checklist.md` |
| Planned next steps | `08_next_phase/dissemination_plan.md` |

Use only clearly labelled SYNTHETIC examples for pre-run demonstrations. The prototype is deterministic and offline; its LLM interface is a stub. Its demonstration exports are not a system for storing real participant records. A facilitator can use reviewed text and role cards without running the interface.

## Ownership and release conditions

Content owner: Dr Binqi Tang, College of Industry-Entrepreneurs and HeXie Management Research Centre, XJTLU. Learning Mall liaison: Ms Wei Cui. Confirm operational publication responsibilities before release.

Use [the readiness checklist](learning_mall_readiness_checklist.md) before uploading. Record an actual version and date, verify linked components, retain editable sources, and test the downloaded pack.
