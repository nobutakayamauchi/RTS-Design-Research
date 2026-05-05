# Contract: UI Spec

## Purpose
Translate research findings into explicit, implementable UI requirements.

## Traceability requirement
Each material UI requirement should map to:
- `requirement_id`
- `finding_id`
- `source_id`
- related RTS decision block field (where relevant)

## Required sections
- `scope`: screen/view covered.
- `layout_regions`: major panes/sections and responsibilities.
- `information_hierarchy`: primary vs secondary data.
- `interaction_model`: key user actions and responses.
- `states`: empty/loading/error/success and transition notes.
- `data_bindings`: what data each region requires.
- `requirements_traceability`: mapping between requirement IDs, findings, and sources.

## Output quality rules
- Requirements are testable.
- Avoid stylistic ambiguity.
- Document tradeoffs explicitly.
