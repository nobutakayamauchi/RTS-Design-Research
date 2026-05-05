# Contract: Design Research Report

## Purpose
Capture research findings that can be transformed into UI requirements and RTS decision records.

## Inputs vs outputs
- `reference_queries` are input instructions used by skills to retrieve external references.
- `research.sources` entries are output provenance records created after retrieval.
- Findings must cite one or more `source_id` values from provenance records.

## Required sections
- Objective
- Scope
- Reference retrieval log (`reference_queries` used)
- Provenance table (`research.sources` with `source_id`)
- Findings (each with source citations)
- Implications for UI spec and implementation brief
