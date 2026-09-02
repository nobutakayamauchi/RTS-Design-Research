# RTS-Design-Research

## What this repository is
RTS-Design-Research is the design-intelligence extension layer for the RTS ecosystem. It converts external UI references, screenshots, product patterns, preference evidence, and design research findings into reconstructable UI decisions and reusable design guidance.

## Why it exists
Design research is often persuasive but not reconstructable. RTS requires decisions to be auditable over time. This repository defines the contracts, templates, and skill interfaces that transform visual/design research into RTS-compatible decision records.

It also exists to solve a practical AI-design failure mode: when ChatGPT, Codex, or another agent has no credible visual reference, it tends to invent a generic average design. This repository provides a provenance-aware path from **design need -> reference evidence -> reusable principles -> DESIGN.md -> generation -> audit**.

## What it is not
This repository is not:
- the RTS trust core
- a runtime or orchestration bridge
- a raw MCP connector dump
- a generic design gallery
- a product implementation repository
- a reference-cloning system

## Core outputs
- Design research reports (`report.md`)
- UI specifications (`ui-spec.md`)
- Implementation briefs (`implementation-brief.md`)
- RTS-compatible design decision blocks (`rts-design-decision-block.yaml`)
- Evidence-backed project `DESIGN.md` files
- Reference evidence records with preference signals and provenance
- Skill definitions for repeatable design research jobs
- Pack placeholders for reference-source integrations

## Reference Intelligence
When a design is underspecified, generic, visually weak, or explicitly described as dull/ugly, agents should not immediately regenerate from a blank prompt.

Use this flow:

`DESIGN_NEED -> SEMANTIC_DECOMPOSITION -> REFERENCE_RETRIEVAL -> PREFERENCE_EVIDENCE -> PRINCIPLE_EXTRACTION -> DESIGN.md -> GENERATION -> REFERENCE_AUDIT -> HUMAN_GATE`

The key rule is:

> Do not ask the model to invent taste when taste can be grounded in evidence.

References may come from the same industry or from adjacent industries that better express the desired traits. For example, an inheritance or funeral design may borrow reusable principles from premium hospitality, healthcare, financial services, or editorial minimalism when those sources provide stronger evidence for calm, trust, dignity, and legibility.

See [Reference Intelligence Layer](docs/architecture/REFERENCE_INTELLIGENCE.md).

## First supported source: Lazyweb MCP
Initial integrations are designed around Lazyweb MCP as a **read-only external UI reference source**. This repository does not store tokens, credentials, or raw `.lazyweb` outputs.

## Relationship to other RTS repositories
- **RTS core**: structural ledger for decision reconstructability.
- **RTS-Skills**: reusable job-shaped execution skills.
- **RTS-MCP-Packs**: connector bundle definitions.
- **RTS-Hermes-Drive**: runtime/orchestration bridge.
- **RTS-Design-Research (this repo)**: bridge from design research artifacts and reference evidence to RTS-recordable design decisions and reusable design guidance.

## Initial workflow
1. Capture the design need.
2. Decompose the need into audience, goals, and visual traits.
3. Retrieve 3-5 provenance-backed references.
4. Record preference evidence separately from visual observations.
5. Extract transferable design principles and `do_not_copy` constraints.
6. Produce a project `DESIGN.md`.
7. Generate or revise the design using those constraints.
8. Run a reference audit.
9. Produce `report.md`, `ui-spec.md`, `implementation-brief.md`, and `rts-design-decision-block.yaml` as needed.
10. Keep final aesthetic approval behind the Human Gate.

## Repository layout
- `docs/` — position, architecture, contracts, and examples
- `skills/` — draft skill definitions for design-oriented jobs
- `packs/` — draft MCP pack placeholders (starting with Lazyweb)
- `templates/` — reusable authoring templates, including `DESIGN.md`
- `registry/` — compatibility and index metadata
- `schemas/` — validation schemas for RTS design decision and reference evidence artifacts
- `scripts/` — lightweight repository validation utilities

## Agent entry point
For a design task that needs stronger visual direction, use `skills/reference_to_design_md/` and `templates/DESIGN.md`.

The agent should search by:
- `artifact_type`
- `audience`
- `primary_goal`
- `traits`
- `sector` when useful

If credible references cannot be found, output `REFERENCE_GAP` rather than inventing design authority.

## Governance and traceability
- [Reference asset policy](docs/policy/REFERENCE_ASSET_POLICY.md) defines how external design references may be used.
- [Provenance model](docs/contracts/provenance_model.md) defines source metadata required for reconstructable decisions.
- [Traceability model](docs/architecture/TRACEABILITY_MODEL.md) explains how research inputs connect to RTS-compatible decision records.
- [Reference Intelligence Layer](docs/architecture/REFERENCE_INTELLIGENCE.md) defines how preference evidence becomes reusable design guidance.
- Examples are placeholders unless explicitly marked as sourced.
- This repository records design decisions and evidence-backed reference intelligence, not raw inspiration dumps.
