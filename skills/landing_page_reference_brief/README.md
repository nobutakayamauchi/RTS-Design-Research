# landing_page_reference_brief

## Purpose
Create a structured landing page brief from reference-driven research.

## When to use
Use when messaging structure and section hierarchy need to be defined before implementation.

## Inputs
- `project`
- `audience`
- `positioning`
- `reference_queries`

## Outputs
- `report_md`
- `landing_page_brief_md`
- `rts_design_decision_block_yaml`

## Required pack
- `lazyweb`

## RTS recording behavior
Captures section and CTA decisions with provenance-linked rationale.

## Example invocation
```yaml
project: rts
audience: engineering_leads
positioning: decision reconstructability infrastructure
reference_queries:
  - "developer infrastructure landing page sections"
  - "auditability product messaging structure"
```

## Failure handling notes
If references are audience-mismatched, narrow and rerun queries before drafting sections.
