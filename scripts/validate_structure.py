#!/usr/bin/env python3
"""Validate the RTS Design Research repository structure."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "docs/policy/REFERENCE_ASSET_POLICY.md",
    "docs/contracts/provenance_model.md",
    "docs/contracts/design_research_report.md",
    "docs/contracts/ui_spec.md",
    "docs/contracts/implementation_brief.md",
    "docs/contracts/rts_design_decision_block.md",
    "docs/architecture/TRACEABILITY_MODEL.md",
    "schemas/rts_design_decision_block.schema.json",
    "scripts/validate_structure.py",
    "docs/examples/rts_landing_page/report.md",
    "docs/examples/rts_landing_page/ui-spec.md",
    "docs/examples/rts_landing_page/implementation-brief.md",
    "docs/examples/rts_landing_page/rts-design-decision-block.yaml",
]

REQUIRED_DIRECTORIES = [
    "docs",
    "docs/architecture",
    "docs/contracts",
    "docs/examples",
    "docs/overview",
    "docs/policy",
    "packs",
    "registry",
    "schemas",
    "scripts",
    "skills",
    "templates",
]

EXPECTED_SKILL_DIRS = [
    "design_research_to_ui_spec",
    "ui_improvement_audit",
    "landing_page_reference_brief",
    "screenshot_to_redesign_plan",
]

SKILL_FILES = [
    "README.md",
    "failure_modes.md",
    "inputs.schema.json",
    "outputs.schema.json",
    "skill.yaml",
]

LANDING_PAGE_OUTPUTS = [
    "report_md",
    "landing_page_brief_md",
    "rts_design_decision_block_yaml",
]

DEPRECATED_DECISION_BLOCK_TYPES = [
    "type: ui_design_decision",
    "type: rts_design_decision",
    '"type": "ui_design_decision"',
    '"type": "rts_design_decision"',
]

DEPRECATED_SKILL_TERMS = [
    "references",
    "reference_domains",
    "current_state",
    "change_list_md",
    "reference_report_md",
]

SKILL_DEPRECATED_PATHS = [
    "README.md",
    "skill.yaml",
    "inputs.schema.json",
    "outputs.schema.json",
]

CANONICAL_SKILL_INPUT_REQUIRED = {
    "design_research_to_ui_spec": ["project", "screen", "research_goal", "reference_queries"],
    "ui_improvement_audit": ["project", "screen", "current_ui_snapshot", "target_outcomes"],
    "landing_page_reference_brief": ["project", "audience", "positioning", "reference_queries"],
    "screenshot_to_redesign_plan": ["project", "screen", "screenshot", "target_direction"],
}

CANONICAL_SKILL_OUTPUT_REQUIRED = {
    "design_research_to_ui_spec": [
        "report_md",
        "ui_spec_md",
        "implementation_brief_md",
        "rts_design_decision_block_yaml",
    ],
    "ui_improvement_audit": [
        "audit_report_md",
        "prioritized_recommendations_md",
        "rts_design_decision_block_yaml",
    ],
    "landing_page_reference_brief": [
        "report_md",
        "landing_page_brief_md",
        "rts_design_decision_block_yaml",
    ],
    "screenshot_to_redesign_plan": [
        "redesign_plan_md",
        "ui_spec_md",
        "rts_design_decision_block_yaml",
    ],
}


def fail(message: str) -> None:
    print(f"validation=failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_required_files() -> int:
    for item in REQUIRED_FILES:
        if not (ROOT / item).is_file():
            fail(f"missing required file: {item}")
    duplicate_provenance_contract = ROOT / "docs" / "contracts" / "provenance.md"
    if duplicate_provenance_contract.exists():
        fail("duplicate provenance contract found: docs/contracts/provenance.md")
    for base in (ROOT / "docs", ROOT / "templates"):
        for path in sorted(base.rglob("*")):
            if path.is_file() and "provenance.md" in read_text(path):
                fail(f"provenance contract reference must use provenance_model.md in {relative(path)}")
    return len(REQUIRED_FILES)


def check_required_directories() -> int:
    for item in REQUIRED_DIRECTORIES:
        if not (ROOT / item).is_dir():
            fail(f"missing required directory: {item}")
    return len(REQUIRED_DIRECTORIES)


def check_skill_dirs() -> int:
    for skill in EXPECTED_SKILL_DIRS:
        skill_dir = ROOT / "skills" / skill
        if not skill_dir.is_dir():
            fail(f"missing skill directory: skills/{skill}")
        for filename in SKILL_FILES:
            if not (skill_dir / filename).is_file():
                fail(f"missing skill file: skills/{skill}/{filename}")
    return len(EXPECTED_SKILL_DIRS)


def check_json_files() -> int:
    checked = 0
    for path in sorted(ROOT.rglob("*.json")):
        if ".git" in path.parts:
            continue
        try:
            json.loads(read_text(path))
        except json.JSONDecodeError as exc:
            fail(f"invalid JSON in {relative(path)}: {exc}")
        checked += 1
    return checked


def check_yaml_files() -> int:
    checked = 0
    for pattern in ("*.yaml", "*.yml"):
        for path in sorted(ROOT.rglob(pattern)):
            if ".git" in path.parts:
                continue
            if not read_text(path).strip():
                fail(f"empty YAML file: {relative(path)}")
            checked += 1
    return checked


def yaml_list_values(path: Path, top_key: str, child_key: str) -> list[str]:
    values: list[str] = []
    lines = read_text(path).splitlines()
    in_section = False
    for line in lines:
        if line.strip() == f"{top_key}:":
            in_section = True
            continue
        if in_section and line and not line.startswith(" "):
            in_section = False
        if in_section:
            stripped = line.strip()
            prefix = f"- {child_key}:"
            if stripped.startswith(prefix):
                values.append(stripped.split(":", 1)[1].strip())
    return values


def check_registry_paths() -> int:
    checked = 0
    registry_skills = yaml_list_values(ROOT / "registry" / "skills.yaml", "skills", "id")
    for skill in registry_skills:
        if not (ROOT / "skills" / skill).is_dir():
            fail(f"registry skill path missing: skills/{skill}")
        checked += 1

    registry_packs = yaml_list_values(ROOT / "registry" / "packs.yaml", "packs", "id")
    for pack in registry_packs:
        if not (ROOT / "packs" / pack).is_dir():
            fail(f"registry pack path missing: packs/{pack}")
        checked += 1

    compatibility = read_text(ROOT / "registry" / "compatibility.yaml")
    for skill in registry_skills:
        if f"skill: {skill}" not in compatibility and f"skill_id: {skill}" not in compatibility:
            fail(f"compatibility missing skill: {skill}")
        checked += 1
    return checked


def check_landing_page_outputs() -> int:
    path = ROOT / "skills" / "landing_page_reference_brief" / "outputs.schema.json"
    data = json.loads(read_text(path))
    required = set(data.get("required", []))
    properties = set(data.get("properties", {}).keys())
    for output in LANDING_PAGE_OUTPUTS:
        if output not in required or output not in properties:
            fail(f"landing page output missing from schema: {output}")
    return len(LANDING_PAGE_OUTPUTS)


def check_example_reports() -> int:
    checked = 0
    for path in sorted((ROOT / "docs" / "examples").rglob("report.md")):
        text = read_text(path)
        for token in ("reference_queries", "source_id", "Findings"):
            if token not in text:
                fail(f"example report {relative(path)} missing {token}")
        checked += 1
    if checked == 0:
        fail("no example reports found")
    return checked


def check_canonical_skill_schemas() -> int:
    checked = 0
    for skill, required_inputs in CANONICAL_SKILL_INPUT_REQUIRED.items():
        inputs_path = ROOT / "skills" / skill / "inputs.schema.json"
        input_schema = json.loads(read_text(inputs_path))
        if input_schema.get("required") != required_inputs:
            fail(f"canonical required inputs mismatch in {relative(inputs_path)}")
        for name in required_inputs:
            prop = input_schema.get("properties", {}).get(name, {})
            if prop.get("type") == "array" and prop.get("minItems") != 1:
                fail(f"required array input {name} missing minItems=1 in {relative(inputs_path)}")
        for name, prop in input_schema.get("properties", {}).items():
            if name not in required_inputs and prop.get("type") == "array" and prop.get("minItems") != 1:
                fail(f"optional array input {name} missing minItems=1 in {relative(inputs_path)}")
        checked += 1

    for skill, required_outputs in CANONICAL_SKILL_OUTPUT_REQUIRED.items():
        outputs_path = ROOT / "skills" / skill / "outputs.schema.json"
        output_schema = json.loads(read_text(outputs_path))
        if output_schema.get("required") != required_outputs:
            fail(f"canonical required outputs mismatch in {relative(outputs_path)}")
        checked += 1
    return checked


def check_canonical_decision_schema() -> int:
    path = ROOT / "schemas" / "rts_design_decision_block.schema.json"
    schema = json.loads(read_text(path))
    properties = schema.get("properties", {})
    if properties.get("type", {}).get("const") != "design_decision":
        fail("decision block schema type const must be design_decision")
    sources = properties.get("research", {}).get("properties", {}).get("sources", {})
    if sources.get("minItems") != 1:
        fail("decision block schema research.sources must have minItems=1")
    confidence = schema.get("$defs", {}).get("source", {}).get("properties", {}).get("confidence", {})
    if confidence.get("enum") != ["low", "medium", "high"]:
        fail("decision block source confidence enum mismatch")
    status = properties.get("outcome", {}).get("properties", {}).get("status", {})
    if status.get("enum") != ["proposed", "in_progress", "validated", "rejected"]:
        fail("decision block outcome.status enum mismatch")
    return 1


def check_deprecated_terms() -> int:
    checked = 0
    for skill_dir in sorted((ROOT / "skills").iterdir()):
        if not skill_dir.is_dir():
            continue
        for filename in SKILL_DEPRECATED_PATHS:
            path = skill_dir / filename
            text = read_text(path)
            for term in DEPRECATED_SKILL_TERMS:
                if re.search(rf"(?<![A-Za-z0-9_]){re.escape(term)}(?![A-Za-z0-9_])", text):
                    fail(f"deprecated skill term {term!r} found in {relative(path)}")
            checked += 1

    for base in (ROOT / "templates", ROOT / "docs" / "examples", ROOT / "schemas"):
        for path in sorted(base.rglob("*")):
            if not path.is_file():
                continue
            text = read_text(path)
            for term in DEPRECATED_DECISION_BLOCK_TYPES:
                if term in text:
                    fail(f"deprecated decision block type {term!r} found in {relative(path)}")
            checked += 1
    return checked


def main() -> None:
    counts = {
        "required_files_checked": check_required_files(),
        "required_directories_checked": check_required_directories(),
        "skill_dirs_checked": check_skill_dirs(),
        "json_files_checked": check_json_files(),
        "yaml_files_checked": check_yaml_files(),
        "registry_paths_checked": check_registry_paths(),
        "landing_page_outputs_checked": check_landing_page_outputs(),
        "example_reports_checked": check_example_reports(),
        "canonical_skill_schemas_checked": check_canonical_skill_schemas(),
        "canonical_decision_schema_checked": check_canonical_decision_schema(),
        "deprecated_terms_checked": check_deprecated_terms(),
    }
    for key, value in counts.items():
        print(f"{key}={value}")
    print("validation=ok")


if __name__ == "__main__":
    main()
