#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

REQUIRED_FILES = [
    "README.md",
    "docs/policy/REFERENCE_ASSET_POLICY.md",
    "docs/contracts/provenance_model.md",
    "docs/architecture/TRACEABILITY_MODEL.md",
    "schemas/rts_design_decision_block.schema.json",
    "scripts/validate_structure.py",
]

REQUIRED_DIRS = ["docs", "skills", "packs", "templates", "registry", "schemas", "scripts"]
SKILL_REQUIRED = ["skill.yaml", "README.md", "inputs.schema.json", "outputs.schema.json", "failure_modes.md"]


def main() -> int:
    root = Path(".")
    missing = []

    for d in REQUIRED_DIRS:
        if not (root / d).is_dir():
            missing.append(d)

    for f in REQUIRED_FILES:
        if not (root / f).exists():
            missing.append(f)

    skill_dirs = [p for p in (root / "skills").iterdir() if p.is_dir()] if (root / "skills").exists() else []
    for sd in skill_dirs:
        for req in SKILL_REQUIRED:
            if not (sd / req).exists():
                missing.append(str(sd / req))

    json_files = list(root.rglob("*.json"))
    invalid_json = []
    for jf in json_files:
        try:
            json.loads(jf.read_text(encoding="utf-8"))
        except Exception as e:
            invalid_json.append((str(jf), str(e)))

    yaml_files = list(root.rglob("*.yaml")) + list(root.rglob("*.yml"))
    empty_yaml = [str(yf) for yf in yaml_files if yf.stat().st_size == 0]

    registry_paths = []
    bad_registry_paths = []
    path_re = re.compile(r"^\s*path:\s*(\S+)\s*$")
    for reg in (root / "registry").glob("*.yaml"):
        for line in reg.read_text(encoding="utf-8").splitlines():
            m = path_re.match(line)
            if m:
                ref = m.group(1)
                registry_paths.append(ref)
                if not (root / ref).exists():
                    bad_registry_paths.append(ref)

    print(f"required_files_checked={len(REQUIRED_FILES) + len(REQUIRED_DIRS)}")
    print(f"json_files_checked={len(json_files)}")
    print(f"yaml_files_checked={len(yaml_files)}")
    print(f"registry_paths_checked={len(registry_paths)}")

    if missing:
        print("missing_paths:")
        for m in missing:
            print(f"- {m}")
    if invalid_json:
        print("invalid_json:")
        for path, err in invalid_json:
            print(f"- {path}: {err}")
    if empty_yaml:
        print("empty_yaml:")
        for y in empty_yaml:
            print(f"- {y}")
    if bad_registry_paths:
        print("missing_registry_paths:")
        for p in bad_registry_paths:
            print(f"- {p}")

    if missing or invalid_json or empty_yaml or bad_registry_paths:
        return 1
    print("validation=ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
