# Decision Flow

RTS-Design-Research bridges skill outputs into canonical RTS design decision artifacts. The flow is intentionally structural: each artifact narrows research context into implementation-ready decisions while preserving provenance for audit and replay.

## Canonical artifact sequence

```text
report.md
-> ui-spec.md
-> implementation-brief.md
-> rts-design-decision-block.yaml
```

## Layer responsibilities

### 1. `report.md`

The research report captures the design research frame, `reference_queries`, findings, and source-level evidence. It is the broadest artifact in the flow and should retain enough context for reviewers to understand why a UI direction was considered.

Required provenance anchors:

- `reference_queries` used to find or compare external patterns.
- `source_id` for each cited source or captured reference.
- Notes compatible with the repository `provenance_model` contract.

### 2. `ui-spec.md`

The UI specification translates research findings into screen structure, interaction states, information architecture, and content priorities. It should cite the relevant `source_id` values from the report instead of copying raw reference assets.

### 3. `implementation-brief.md`

The implementation brief converts the UI specification into build-facing constraints, component boundaries, instrumentation notes, and handoff criteria. It should preserve the same decision thread and explicitly name the downstream `design_decision` artifact that must be generated.

### 4. `rts-design-decision-block.yaml`

The decision block is the canonical RTS-compatible record. It stores the selected `design_decision`, the source provenance fields needed to reconstruct the decision, and the expected outcome of the implementation work.

At minimum, generated decision stubs must preserve:

- `type: design_decision`
- `research.sources[].source_id`
- `reference_queries` in upstream artifacts or generator input
- fields defined by the `provenance_model` contract for each source

## Generator bridge

`scripts/generate_decision_stub.py` accepts a small JSON object from a skill or handoff process and emits a minimal `rts-design-decision-block.yaml`. The generated YAML is intentionally a stub: it creates stable placeholder IDs and carries source provenance forward, but authors are expected to refine findings, rationale, constraints, assumptions, and outcomes before treating the block as final.
