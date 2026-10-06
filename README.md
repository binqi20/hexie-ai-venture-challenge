# HeXie-AI Venture Challenge

**Assessment resources for entrepreneurship education when students can use generative AI.**

Version 1.0, October 2026. Developed at Xi'an Jiaotong-Liverpool University (XJTLU) with support from the XJTLU EASE Fund (project EASE-R1-2526-85).

## Why these resources exist

Generative AI allows student teams to produce persuasive business plans, market analyses and pitch decks with little of the reasoning those documents once signalled. A polished plan may show what an AI system can assemble while revealing little about whether the team can recognise an opportunity, judge feasibility, weigh competing stakeholders or defend a choice under questioning.

The HeXie-AI Venture Challenge moves the object of assessment from the venture document to the judgement behind it. Teams develop a venture with AI tools, face a moderated panel of five simulated stakeholders whose demands conflict, decide which feedback to adopt, reject or defer, and defend those decisions in a short oral examination. Three linked traces make the reasoning visible: a one-page decision memo, a stakeholder response log and the oral defence. A Venture Value Lens, adapted from the logic of ESG rating methods, helps students show where a venture's commercial and social value reinforce or conflict. HeXie Management Theory supplies the design logic: structure where processes can be specified, and room for initiative where they cannot.

## What is in this repository

| Folder | Contents | Start with |
|---|---|---|
| [`00_design`](00_design) | Project architecture; HeXie design logic | [project_architecture.md](00_design/project_architecture.md) |
| [`01_playbook`](01_playbook) | Competition playbook; facilitator run sheet | [competition_playbook.md](01_playbook/competition_playbook.md) |
| [`02_assessment_kit`](02_assessment_kit) | Five-cluster, four-level capability rubric and scoring sheet; Stage 1 and Final AI-use declarations; decision memo; stakeholder response log; oral-defence guide; judge-calibration guide | [capability_rubric.md](02_assessment_kit/capability_rubric.md) |
| [`03_simulation_kit`](03_simulation_kit) | Simulation design; persona library; demonstration scenarios; stakeholder and moderator prompts; adaptation guide; a lightweight Python prototype | [simulation_design.md](03_simulation_kit/simulation_design.md) |
| [`04_venture_value_lens`](04_venture_value_lens) | Method; materiality worksheet; value-alignment map; industry-topic guide; worked example; facilitator note | [value_lens_method.md](04_venture_value_lens/value_lens_method.md) |
| [`05_evaluation`](05_evaluation) | Judge, participant and observer feedback forms; four SYNTHETIC exemplar cases for assessor calibration | [exemplar_cases](05_evaluation/exemplar_cases) |
| [`06_responsible_ai`](06_responsible_ai) | Responsible-AI plan with risk register and safeguards | [responsible_ai_plan.md](06_responsible_ai/responsible_ai_plan.md) |
| [`07_adoption_kit`](07_adoption_kit) | Quick-start guide; adoption routes; adaptation guide; good-practice note; Learning Mall readiness checklist | [quick_start_guide.md](07_adoption_kit/quick_start_guide.md) |
| [`08_next_phase`](08_next_phase) | Dissemination plan with a 12-slide storyline and a 60-minute staff workshop | [dissemination_plan.md](08_next_phase/dissemination_plan.md) |

## Quick start

1. Read the [quick-start guide](07_adoption_kit/quick_start_guide.md). It takes 10 to 15 minutes.
2. Review the [capability rubric](02_assessment_kit/capability_rubric.md) and the [submission pack overview](02_assessment_kit/submission_pack_overview.md).
3. Choose an adoption route in the [adoption kit](07_adoption_kit/adoption_kit_readme.md): run the Challenge as designed, adapt it lightly, or reuse the design pattern in another discipline.
4. Try the prototype:

   ```bash
   cd 03_simulation_kit/prototype
   pip install -r requirements.txt
   python3 run_demo.py
   python3 -m pytest tests -q
   ```

## Status and evidence

This is a first release. The resources have been reviewed through consultations with academics, students and practitioners, and validated internally:

- **Rubric:** on 24 SYNTHETIC venture cases written to designed levels, an AI-assisted blind check matched the designed level in 20 cases and fell within one level in all 24. All four "polish trap" cases (fluent but weakly reasoned) were flagged and kept at their designed level.
- **Simulation:** two rounds of quality assurance on eight venture briefs led to a binding-constraint rule that makes stakeholder demands compete for the same scarce resource. All six panels run under the revised prompts produced real trade-offs.

No student or judge data has been collected yet. The first live run is planned for December 2026 at XJTLU. All synthetic material is labelled SYNTHETIC.

## How to cite

Tang, B. (2026). *HeXie-AI Venture Challenge: Assessment resources for entrepreneurship education* (Version 1.0) [Teaching resources]. Xi'an Jiaotong-Liverpool University. https://github.com/binqi20/hexie-ai-venture-challenge

Citation metadata is also available in [CITATION.cff](CITATION.cff). Works cited across the materials are listed in [REFERENCES.md](REFERENCES.md).

## Licence

The teaching materials are licensed under the [Creative Commons Attribution-NonCommercial 4.0 International licence](LICENSE) (CC BY-NC 4.0). The prototype code in [`03_simulation_kit/prototype`](03_simulation_kit/prototype) is licensed under the [MIT licence](03_simulation_kit/prototype/LICENSE).

The Venture Value Lens describes, in the project's own words, concepts drawn from published ESG methodologies by MSCI, FTSE Russell and the Sustainability Accounting Standards Board (SASB). Those methodologies remain the property of their owners and are not covered by this licence. SASB disclosure-topic names appear as short labels with attribution.

## Acknowledgements

Supported by the XJTLU EASE Fund (Education + AI Sprint Enablement Fund), project EASE-R1-2526-85. Project leader: Dr Binqi Tang, College of Industry-Entrepreneurs and HeXie Management Research Centre, XJTLU. Project team: Dr Wim Coreynen, Dr Yan Pan and Ms Wei Cui. We thank the academics, practitioners, student and alumnus who reviewed the design.

## Use of AI in preparing these materials

In keeping with the transparency the Challenge asks of students: the materials were prepared with the assistance of AI tools (Claude by Anthropic; Codex and ChatGPT by OpenAI) and reviewed by the project leader, who takes responsibility for their content. The synthetic cases and the blind scoring were AI-generated and are labelled as such.
