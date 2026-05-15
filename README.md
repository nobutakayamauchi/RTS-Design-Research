# RTS-Design-Research

## What this repository is
RTS-Design-Research is the design-intelligence extension layer for the RTS ecosystem. It converts external UI references, screenshots, product patterns, and design research findings into reconstructable UI decisions.

## Why it exists
Design research is often persuasive but not reconstructable. RTS requires decisions to be auditable over time. This repository defines the contracts, templates, and skill interfaces that transform visual/design research into RTS-compatible decision records.

## What it is not
This repository is not:
- the RTS trust core
- a runtime or orchestration bridge
- a raw MCP connector dump
- a generic design gallery
- a product implementation repository

## Core outputs
- Design research reports (`report.md`)
- UI specifications (`ui-spec.md`)
- Implementation briefs (`implementation-brief.md`)
- RTS-compatible design decision blocks (`rts-design-decision-block.yaml`)
- Skill definitions for repeatable design research jobs
- Pack placeholders for reference-source integrations

## First supported source: Lazyweb MCP
Initial integrations are designed around Lazyweb MCP as a **read-only external UI reference source**. This repository does not store tokens, credentials, or raw `.lazyweb` outputs.

## Relationship to other RTS repositories
- **RTS core**: structural ledger for decision reconstructability.
- **RTS-Skills**: reusable job-shaped execution skills.
- **RTS-MCP-Packs**: connector bundle definitions.
- **RTS-Hermes-Drive**: runtime/orchestration bridge.
- **RTS-Design-Research (this repo)**: bridge from design research artifacts to RTS-recordable design decisions.

## Initial workflow
1. Run design research.
2. Produce `report.md`.
3. Produce `ui-spec.md`.
4. Produce `implementation-brief.md`.
5. Produce `rts-design-decision-block.yaml`.
6. Commit the decision block back into RTS core or a downstream implementation repository.

## Repository layout
- `docs/` — position, architecture, contracts, and examples
- `skills/` — draft skill definitions for design-oriented jobs
- `packs/` — draft MCP pack placeholders (starting with Lazyweb)
- `templates/` — reusable authoring templates
- `registry/` — compatibility and index metadata
- `schemas/` — validation schemas for RTS design decision artifacts
- `scripts/` — lightweight repository validation utilities

## Governance and traceability
- [Reference asset policy](docs/policy/REFERENCE_ASSET_POLICY.md) defines how external design references may be used.
- [Provenance model](docs/contracts/provenance_model.md) defines source metadata required for reconstructable decisions.
- [Traceability model](docs/architecture/TRACEABILITY_MODEL.md) explains how research inputs connect to RTS-compatible decision records.
- Examples are placeholders unless explicitly marked as sourced.
- This repository records design decisions, not raw inspiration dumps.
