# Contract: Design Research Report

## Purpose
Capture evidence-backed findings that can be transformed into UI requirements and RTS decision records.

## Inputs vs outputs
- `reference_queries` are input instructions used by research skills.
- `research.sources` are structured provenance outputs recorded after retrieval.
- Findings must cite one or more `source_id` values from `research.sources`.

## Required sections
- Objective
- Scope
- Reference retrieval log (`reference_queries`)
- Provenance table (`research.sources` with `source_id`)
- Findings (each citing `source_id` values)
- Implications for UI spec
- Implications for implementation brief
- Open questions
