# design_research_to_ui_spec

## Purpose
Convert design research into reconstructable RTS design artifacts.

## When to use
Use when a team needs a report, UI spec, implementation brief, and decision block from reference-driven research.

## Inputs
- `project`
- `screen`
- `research_goal`
- `reference_queries`
- `constraints` (optional)

## Outputs
- `report_md`
- `ui_spec_md`
- `implementation_brief_md`
- `rts_design_decision_block_yaml`

## Required pack
- `lazyweb`

## RTS recording behavior
Produces an RTS-compatible `type: design_decision` block with provenance-linked findings.

## Example invocation
```yaml
project: rts
screen: audit_console
research_goal: Improve decision timeline readability
reference_queries:
  - "audit timeline ux patterns"
  - "developer console split view inspector"
constraints:
  - "preserve keyboard navigation"
```

## Failure handling notes
If reference quality is low, stop and return query refinement needs before final outputs.
