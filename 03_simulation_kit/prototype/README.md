# Offline stakeholder-panel prototype

A small implementation of the Stakeholder-Agent Swarm Simulation. It generates five structured responses from authored personas and scenario tensions, screens them for selected problems, maps designed conflicts and exports reasoned decisions. The supplied run is SYNTHETIC. No students, judges or observers took part.

## Setup and run

Use Python 3.10 or newer. From this directory, create an isolated environment if dependencies are missing:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest tests -q
.venv/bin/python run_demo.py
.venv/bin/python -m streamlit run app.py
```

If using an existing environment with PyYAML and pytest installed:

```sh
python -m pytest tests -q
python run_demo.py
```

Run the demo from any working directory by passing its absolute script path. Outputs always go to `sample_runs/demo_run.md` and `sample_runs/demo_run.csv` beside the script. Rerunning replaces only these two demonstration exports. It makes no network requests and needs no credentials. Do not install Streamlit system-wide for this demonstration.

The facilitator view selects a scenario and optional variants, displays five responses and moderation flags, and shows the authored conflict matrix. Complete the practice decision table and confirm human review before downloading Markdown or CSV. The view is for synthetic demonstrations only. Decisions remain in temporary browser-session state; switching scenario or variants uses a separate editor state. No data service or durable session storage is included.

## Deterministic and LLM modes

`engine.py` uses stable string composition. Identical persona and scenario inputs produce identical feedback without clocks, randomness, external lookups or hidden memory. The role-specific concerns come from authored fields and tension positions. This demonstrates a workflow; it does not demonstrate LLM intelligence or factual validation.

`LLMProvider` declares a future provider interface whose method raises `NotImplementedError`. Calling `generate_stakeholder_feedback(..., mode='llm')` also raises that error, even when a provider is supplied. LLM mode is not wired in this release. `../prompts.md` documents a possible later implementation and its human review requirements.

## Data and function contract

- `load_personas()` reads `../personas.yaml` and selects five canonical roles. `investor_variant=True` and `customer_variant=True` replace the relevant base cards.
- `load_scenario('demo_01')` reads one brief from `../scenarios.yaml`. Optional `path` arguments permit another authored YAML file with the same structure.
- `generate_stakeholder_feedback(personas, scenario)` returns the eight required string fields per role. Demo confidence is low because evidence placeholders establish no empirical result.
- `moderate_feedback(feedback, scenario)` returns flags without changing responses. `build_conflict_matrix(feedback, scenario)` lists the authored question and each role's competing position. It does not infer disagreement from natural language.
- `record_decisions(decisions, feedback)` requires one decision per role, a key point, an exact decision label, a reason and evidence that would change it. This minimal table captures one key point per role; the fuller assessment template can record several points.
- `generate_oral_defence_questions(decisions)` returns one question per canonical capability cluster, without grades or answers.
- `export_run_summary(...)` returns `markdown` and `csv` strings. An optional `output_base` explicitly writes both files. Inputs, responses, flags, conflicts, decisions and questions are included. CSV uses a `record_type` column; complex records are JSON in `details`, and responses/decisions have separate columns. Filter `record_type=decision` for the decision table.

All exports from this release are labelled SYNTHETIC. Do not use them to record real participants. Markdown contains the full frozen input for inspection. CSV preserves the equivalent input and response/decision records. Neither format captures a live interaction, timestamped human approval or an incident-resolution audit trail.

## Moderation limitations

The moderator checks required fields, confidence values and one response per role. It scans sentences for digits lacking an `Assumption:`, `Team assumption:`, `Estimate:` or `Hypothesis:` prefix or a `[source:ID]` marker resolving to evidence marked `supplied`. A placeholder never counts as evidence. The marker check only checks status and identity: the facilitator must check that the source actually supports the claim.

Absolute words and selected legal-advice phrases are flagged even in labelled assumptions. The lexical screen can flag benign wording and miss paraphrases, spelled-out quantities, qualitative fabrications, discriminatory implications or prompt attacks. A general assumption statement in another field cannot excuse an unlabelled numerical claim. Flags are review requests, not automated safety judgements. No flags does not mean factual accuracy, legal compliance or an acceptable student-facing response.

Generation does not parse evidence attachments, evaluate empirical claims or automatically enforce every `communication_style` and `prohibited_moves` instruction. Those fields guide authoring, human review and any future prompt-based mode. It generates template text from the other role fields, never applies a source as an answer key and does not update confidence when evidence is added.

## Explicitly outside this release

No autonomous agent negotiation, persistent world, persistence service, login, grading, student profiling, live web retrieval, provider integration, automatic correction or regulatory certification. Explicit exports are ordinary files, so facilitators control storage and deletion. No personal or confidential data are needed. A printed role-card workflow is available if the interface is unsuitable.

The first live run is scheduled for early December 2026. This prototype supplies no evidence of participant learning or judge usability. Confirm locally before use: institutional retention, future provider approval and live deployment arrangements, through approved ethics documents and institutional decisions.

## Tests

Run `python3 -m pytest tests -q` from this folder. The 21 tests check the YAML structure of the personas and scenarios, the reproducibility of deterministic output, the moderator's handling of a planted unsupported claim, and the exports. `python3 run_demo.py` writes a sample session record to `sample_runs/`. The Streamlit facilitator view (`app.py`) requires `pip install streamlit` and has not yet been tested with users.
