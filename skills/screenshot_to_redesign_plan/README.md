# screenshot_to_redesign_plan

## Purpose
Turn a screenshot plus direction into an implementable redesign plan and UI spec.

## When to use
Use when a concrete current-state screen is available and a redesign direction is known.

## Inputs
- `project`
- `screen`
- `screenshot`
- `target_direction`
- `constraints` (optional)

## Outputs
- `redesign_plan_md`
- `ui_spec_md`
- `rts_design_decision_block_yaml`

## Required pack
- `lazyweb`

## RTS recording behavior
Records redesign rationale, constraints, and expected outcomes in `type: design_decision` form.

## Example invocation
```yaml
project: rts
screen: audit_console
screenshot: "docs/examples/current/audit-console-placeholder.png"
target_direction: "improve event-to-inspector traceability"
constraints:
  - "no framework migration"
```

## Failure handling notes
If screenshot clarity or direction is insufficient, return blocked with required clarifications.
