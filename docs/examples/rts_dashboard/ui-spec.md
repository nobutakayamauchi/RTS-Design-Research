# ui-spec.md (Example)

## Scope
RTS audit console dashboard main workspace.

## Layout regions
- Left nav: Projects / Decisions / Transitions / Boundaries / Reports.
- Center panel: decision ledger timeline with filter controls.
- Right inspector: selected decision details and provenance.

## Key data fields
- Context
- Assumptions
- Constraints
- Action
- Outcome
- Commit-linked evidence
- State transition history

## Interaction model
- Selecting timeline entry updates inspector.
- Filters apply to timeline and keep selection if valid.
- Evidence links open commit/revision context.

## States
- Empty: no decisions yet for selected project.
- Loading: fetch ledger and transitions.
- Error: data retrieval failure with retry.
