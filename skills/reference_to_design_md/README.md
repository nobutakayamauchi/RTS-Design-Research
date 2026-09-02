# reference_to_design_md

Turns a design need plus sourced reference evidence into an evidence-backed `DESIGN.md` for ChatGPT, Codex, or another design-capable agent.

## Inputs
Required:
- `project`
- `artifact_type`
- `audience`
- `primary_goal`
- `traits`

Optional:
- `sector`
- `reference_queries`
- `constraints`

## Required behavior
1. Decompose the requested design into reusable visual traits.
2. Retrieve 3-5 references using provenance-aware research.
3. Prefer references with explicit preference evidence.
4. Search across industries when trait similarity is stronger than sector similarity.
5. Separate source facts, visual observations, and AI interpretation.
6. Extract reusable principles rather than copying layouts or assets.
7. Generate `DESIGN.md` using `templates/DESIGN.md`.
8. Emit `REFERENCE_GAP` when credible references are insufficient.
9. Keep final aesthetic approval behind a Human Gate.

## Outputs
- `reference_set`
- `preference_evidence`
- `transferable_principles`
- `design_md`
- `reference_audit_checklist`
- `rts_design_decision_block_yaml`

## Anti-goals
- Do not clone a reference.
- Do not equate popularity with quality without context.
- Do not invent awards, usage metrics, or expert approval.
- Do not silently drop provenance.
