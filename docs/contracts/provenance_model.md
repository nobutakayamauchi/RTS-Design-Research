# Provenance Model

`reference_queries` are skill inputs used to retrieve evidence.
`research.sources` are structured provenance outputs recorded after retrieval.
Findings must cite `source_id` values from `research.sources`.

## Required fields
- `source_id`: Stable identifier used in findings citations.
- `source_type`: e.g., screenshot, article, product-page, design-system.
- `provider`: e.g., lazyweb.
- `query`: Retrieval query that produced this source.
- `retrieved_at`: ISO-8601 timestamp.
- `reference_url`: Public source URL when available.
- `screenshot_path`: Local placeholder/example path when used.
- `license_or_usage_note`: Usage constraints or rights note.
- `confidence`: low | medium | high.
- `notes`: Analyst interpretation notes.
