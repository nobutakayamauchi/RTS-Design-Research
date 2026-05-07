#!/usr/bin/env python3
"""Validate structural requirements for RTS design decision blocks.

This validator intentionally supports the small YAML subset used by repository
fixtures and generated stubs. It avoids third-party YAML dependencies while
checking the canonical fields that must be present before a decision block is
considered structurally valid.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_TOP_LEVEL_FIELDS = [
    "id",
    "type",
    "project",
    "screen",
    "created_at",
    "context",
    "research",
    "findings",
    "decision",
    "constraints",
    "assumptions",
    "action",
    "outcome",
]

REQUIRED_SOURCE_FIELDS = [
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

VALID_OUTCOME_STATUSES = {"proposed", "in_progress", "validated", "rejected"}
KEY_PATTERN = re.compile(r"^(?P<indent> *)(?:- )?(?P<key>[A-Za-z0-9_]+):(?: *(?P<value>.*))?$")


class DecisionBlockValidationError(ValueError):
    """Raised when a decision block fails structural validation."""


def fail(message: str) -> None:
    raise DecisionBlockValidationError(message)


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def key_value(line: str) -> tuple[int, str, str] | None:
    match = KEY_PATTERN.match(line)
    if not match:
        return None
    value = match.group("value") or ""
    return len(match.group("indent")), match.group("key"), strip_quotes(value)


def top_level_values(lines: list[str]) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in lines:
        parsed = key_value(line)
        if parsed is None:
            continue
        indent, key, value = parsed
        if indent == 0:
            values[key] = value
    return values


def section_lines(lines: list[str], section: str) -> list[str]:
    start = None
    for index, line in enumerate(lines):
        if line == f"{section}:":
            start = index + 1
            break
    if start is None:
        return []

    end = len(lines)
    for index in range(start, len(lines)):
        if lines[index] and not lines[index].startswith(" "):
            end = index
            break
    return lines[start:end]


def nested_value(lines: list[str], section: str, key: str) -> str | None:
    for line in section_lines(lines, section):
        parsed = key_value(line)
        if parsed is None:
            continue
        _, parsed_key, value = parsed
        if parsed_key == key:
            return value
    return None


def has_nested_key(lines: list[str], section: str, key: str) -> bool:
    return nested_value(lines, section, key) is not None


def source_blocks(lines: list[str]) -> list[dict[str, str]]:
    research = section_lines(lines, "research")
    sources_start = None
    for index, line in enumerate(research):
        if line.strip() == "sources:":
            sources_start = index + 1
            break
    if sources_start is None:
        return []

    blocks: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for line in research[sources_start:]:
        if not line.strip():
            continue
        if line.startswith("  ") and not line.startswith("    "):
            break
        parsed = key_value(line)
        if parsed is None:
            continue
        _, key, value = parsed
        if line.lstrip().startswith("- "):
            if current is not None:
                blocks.append(current)
            current = {key: value}
        elif current is not None:
            current[key] = value
    if current is not None:
        blocks.append(current)
    return blocks


def validate_decision_block(path: Path) -> None:
    if not path.is_file():
        fail(f"missing decision block: {path}")
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        fail(f"decision block is empty: {path}")

    lines = text.splitlines()
    top_level = top_level_values(lines)
    for field in REQUIRED_TOP_LEVEL_FIELDS:
        if field not in top_level:
            fail(f"missing required top-level field {field!r}: {path}")
    if top_level.get("type") != "design_decision":
        fail(f"type must be design_decision: {path}")

    sources = source_blocks(lines)
    if not sources:
        fail(f"research.sources must be non-empty: {path}")
    for index, source in enumerate(sources, start=1):
        for field in REQUIRED_SOURCE_FIELDS:
            if not source.get(field):
                fail(f"source {index} missing required provenance field {field!r}: {path}")

    if not has_nested_key(lines, "findings", "observed_patterns"):
        fail(f"findings.observed_patterns is required: {path}")
    if not has_nested_key(lines, "findings", "anti_patterns"):
        fail(f"findings.anti_patterns is required: {path}")
    if not nested_value(lines, "decision", "selected_pattern"):
        fail(f"decision.selected_pattern is required: {path}")
    if not nested_value(lines, "decision", "rationale"):
        fail(f"decision.rationale is required: {path}")

    status = nested_value(lines, "outcome", "status")
    if status not in VALID_OUTCOME_STATUSES:
        allowed = ", ".join(sorted(VALID_OUTCOME_STATUSES))
        fail(f"outcome.status must be one of {allowed}: {path}")


def main(argv: list[str] | None = None) -> None:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print("usage: validate_decision_block.py <rts-design-decision-block.yaml> [...]", file=sys.stderr)
        raise SystemExit(2)

    try:
        for item in args:
            validate_decision_block(Path(item))
    except DecisionBlockValidationError as exc:
        print(f"decision_block_validation=failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    print(f"decision_blocks_checked={len(args)}")
    print("decision_block_validation=ok")


if __name__ == "__main__":
    main()
