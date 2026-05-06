# Contract: RTS Design Decision Block

## Purpose
Encode UI design decisions into RTS-compatible reconstructable records.

## Required structure
- `id`
- `type`
- `project`
- `screen`
- `created_at`
- `context`
- `research`
- `findings`
- `decision`
- `constraints`
- `assumptions`
- `action`
- `outcome`

## Canonical type
`type` must be `design_decision`.

## Canonical nested shape
- `research.sources[]` contains provenance records.
- `findings.observed_patterns[]` captures source-backed patterns.
- `findings.anti_patterns[]` captures patterns to avoid.
- `decision.selected_pattern` names the chosen pattern.
- `decision.rationale` explains why the selected pattern fits the context.
- `action.outputs[]` lists generated artifacts.
- `outcome.status` is one of `proposed`, `in_progress`, `validated`, or `rejected`.

## Source provenance
Every `research.sources[]` entry must include the standard provenance fields defined in `schemas/rts_design_decision_block.schema.json`:

- `source_id`
- `source_type`
- `provider`
- `query`
- `retrieved_at`
- `reference_url`
- `screenshot_path`
- `license_or_usage_note`
- `confidence`
- `notes`

Use `na` for unavailable URL or screenshot path values.

## Reconstructability alignment
The block must preserve:
- Context
- Decision
- Constraints
- Assumptions
- Action
- Outcome

## Validation rules
- `id` is stable and unique.
- `type` is `design_decision`.
- `created_at` uses ISO-8601.
- `research` and `findings` preserve evidence-backed reasoning.
- `outcome` can be updated as real results arrive.
