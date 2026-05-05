# implementation-brief.md (Example)

## Objective
Implement an audit-focused dashboard that prioritizes reconstructability over promotional visuals.

## Deliverables
- Three-pane layout (left nav / center timeline / right inspector).
- Timeline item and inspector components.
- Provenance links and transition-history view.

## Constraints
- Preserve traceability fields: context, assumptions, constraints, action, outcome.
- Support responsive behavior without collapsing traceability data.

## Non-goals
- Marketing landing-page style hero treatments.
- Animation-first interaction patterns.

## Acceptance checks
- Decision selection updates inspector deterministically.
- Commit-linked evidence is visible for each decision where available.
