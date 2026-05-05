# ui_improvement_audit

## Purpose
Audit an existing UI against references and produce prioritized operational improvements.

## When to use
Use when a current screen exists and outcomes are defined.

## Inputs
- `project`
- `screen`
- `current_ui_snapshot`
- `target_outcomes`
- `reference_queries` (optional)

## Outputs
- `audit_report_md`
- `prioritized_recommendations_md`
- `rts_design_decision_block_yaml`

## Required pack
- `lazyweb`

## RTS recording behavior
Records recommendation rationale and selected actions as a reconstructable decision entry.

## Example invocation
```yaml
project: rts
screen: decisions_list
current_ui_snapshot: "docs/examples/current/decisions-list-placeholder.png"
target_outcomes:
  - "faster triage"
  - "reduced misclassification"
reference_queries:
  - "incident dashboard prioritization patterns"
```

## Failure handling notes
If prioritization cannot be tied to target outcomes, mark recommendations as provisional.
