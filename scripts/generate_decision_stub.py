#!/usr/bin/env python3
"""Generate a minimal RTS design decision block from JSON input.

The script intentionally uses only Python's standard library. It accepts a
small JSON payload from stdin or a file path and writes YAML to stdout or an
optional output path.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_TIMESTAMP = "1970-01-01T00:00:00Z"
SOURCE_FIELDS = [
    "source_id",
    "source_type",
    "provider",
    "query",
    "retrieved_at",
    "reference_url",
    "screenshot_path",
    "license_or_usage_note",
    "confidence",
    "notes",
]


def slug(value: Any, fallback: str) -> str:
    text = str(value or fallback).strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or fallback


def stable_decision_id(data: dict[str, Any]) -> str:
    project = slug(data.get("project"), "project")
    screen = slug(data.get("screen"), "screen")
    return str(data.get("id") or f"decision-{project}-{screen}-001")


def source_id(source: dict[str, Any], index: int) -> str:
    if source.get("source_id"):
        return str(source["source_id"])
    seed = source.get("query") or source.get("provider") or f"source-{index}"
    return f"src-{slug(seed, 'source')}-{index:03d}"


def input_sources(data: dict[str, Any]) -> list[dict[str, Any]]:
    provenance_model = data.get("provenance_model") or {}
    candidates = (
        data.get("sources")
        or data.get("research", {}).get("sources")
        or provenance_model.get("sources")
        or []
    )
    if not isinstance(candidates, list):
        raise ValueError("sources must be a list when provided")
    return [item for item in candidates if isinstance(item, dict)]


def normalize_sources(data: dict[str, Any]) -> list[dict[str, str]]:
    queries = data.get("reference_queries") or []
    if isinstance(queries, str):
        queries = [queries]
    sources = input_sources(data)
    if not sources:
        query = str(queries[0]) if queries else "placeholder reference query"
        sources = [{"query": query}]

    normalized = []
    for index, source in enumerate(sources, start=1):
        normalized_source = {field: str(source.get(field, "")) for field in SOURCE_FIELDS}
        normalized_source["source_id"] = source_id(source, index)
        normalized_source["source_type"] = normalized_source["source_type"] or "article"
        normalized_source["provider"] = normalized_source["provider"] or "placeholder"
        normalized_source["query"] = normalized_source["query"] or str(queries[0] if queries else "")
        normalized_source["retrieved_at"] = normalized_source["retrieved_at"] or DEFAULT_TIMESTAMP
        normalized_source["reference_url"] = normalized_source["reference_url"] or "na"
        normalized_source["screenshot_path"] = normalized_source["screenshot_path"] or "na"
        normalized_source["license_or_usage_note"] = (
            normalized_source["license_or_usage_note"]
            or "Placeholder provenance; replace before final publication."
        )
        normalized_source["confidence"] = normalized_source["confidence"] or "low"
        normalized_source["notes"] = normalized_source["notes"] or "Generated decision stub source."
        normalized.append(normalized_source)
    return normalized


def as_list(value: Any, fallback: list[str]) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value]
    if isinstance(value, str) and value:
        return [value]
    return fallback


def decision_block(data: dict[str, Any]) -> dict[str, Any]:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return {
        "id": stable_decision_id(data),
        "type": "design_decision",
        "project": str(data.get("project") or "Project"),
        "screen": str(data.get("screen") or "screen"),
        "created_at": str(data.get("created_at") or now),
        "context": str(data.get("context") or data.get("research_goal") or "Generated decision stub."),
        "research": {"sources": normalize_sources(data)},
        "findings": {
            "observed_patterns": as_list(
                data.get("observed_patterns"), ["Placeholder observed pattern from reference_queries."]
            ),
            "anti_patterns": as_list(data.get("anti_patterns"), ["Placeholder anti-pattern to validate."]),
        },
        "decision": {
            "selected_pattern": str(data.get("selected_pattern") or "Placeholder selected pattern"),
            "rationale": str(data.get("rationale") or "Generated stub; replace with decision rationale."),
        },
        "constraints": as_list(data.get("constraints"), ["Preserve source provenance fields."]),
        "assumptions": as_list(data.get("assumptions"), ["Generated values require human review."]),
        "action": {
            "outputs": as_list(
                data.get("outputs"),
                ["report.md", "ui-spec.md", "implementation-brief.md", "rts-design-decision-block.yaml"],
            )
        },
        "outcome": {
            "status": str(data.get("status") or "proposed"),
            "expected": as_list(data.get("expected"), ["Decision can be reviewed and refined."]),
            "observed": as_list(data.get("observed"), []),
        },
    }


def quote(value: Any) -> str:
    text = str(value)
    escaped = text.replace('"', '\\"')
    return f'"{escaped}"'


def emit_yaml(value: Any, indent: int = 0) -> list[str]:
    prefix = " " * indent
    lines: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if child == []:
                lines.append(f"{prefix}{key}: []")
            elif isinstance(child, (dict, list)):
                lines.append(f"{prefix}{key}:")
                lines.extend(emit_yaml(child, indent + 2))
            else:
                lines.append(f"{prefix}{key}: {quote(child)}")
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, dict):
                lines.append(f"{prefix}- {next(iter(item))}: {quote(next(iter(item.values())))}")
                remaining = dict(list(item.items())[1:])
                lines.extend(emit_yaml(remaining, indent + 2))
            elif isinstance(item, list):
                lines.append(f"{prefix}-")
                lines.extend(emit_yaml(item, indent + 2))
            else:
                lines.append(f"{prefix}- {quote(item)}")
    return lines


def load_input(path: str | None) -> dict[str, Any]:
    raw = Path(path).read_text(encoding="utf-8") if path else sys.stdin.read()
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("input JSON must be an object")
    return data


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate rts-design-decision-block.yaml from JSON.")
    parser.add_argument("input", nargs="?", help="JSON input path. Reads stdin when omitted.")
    parser.add_argument("-o", "--output", help="YAML output path. Writes stdout when omitted.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data = load_input(args.input)
    yaml_text = "\n".join(emit_yaml(decision_block(data))) + "\n"
    if not yaml_text.strip():
        raise ValueError("generated YAML is empty")
    if args.output:
        Path(args.output).write_text(yaml_text, encoding="utf-8")
    else:
        sys.stdout.write(yaml_text)


if __name__ == "__main__":
    main()
