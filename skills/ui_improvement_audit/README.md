# ui_improvement_audit

Audits an existing UI snapshot against target outcomes and optional source queries.

## Inputs
Required:
- `project`
- `screen`
- `current_ui_snapshot`
- `target_outcomes`

Optional:
- `reference_queries`

## Outputs
- `audit_report_md`
- `prioritized_recommendations_md`
- `rts_design_decision_block_yaml`
