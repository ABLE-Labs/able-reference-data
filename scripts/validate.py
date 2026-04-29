"""Validate records.json files against their schema.json counterparts.

Run manually or via pre-commit hook:
    python scripts/validate.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
COLLECTIONS = ["labware", "modules", "liquid"]


def validate_collection(name: str) -> list[str]:
    try:
        import jsonschema
    except ImportError:
        print("Install jsonschema: pip install jsonschema")
        sys.exit(1)

    errors: list[str] = []
    schema_path = ROOT / name / "schema.json"
    records_path = ROOT / name / "records.json"

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    records = json.loads(records_path.read_text(encoding="utf-8"))

    keys_seen: set[str] = set()
    for i, record in enumerate(records):
        try:
            jsonschema.validate(record, schema)
        except jsonschema.ValidationError as e:
            errors.append(f"[{name}][{i}] {e.message}")

        key = record.get("key", "")
        if key in keys_seen:
            errors.append(f"[{name}][{i}] Duplicate key: {key!r}")
        keys_seen.add(key)

    return errors


def main() -> None:
    all_errors: list[str] = []
    for collection in COLLECTIONS:
        all_errors.extend(validate_collection(collection))

    if all_errors:
        print("Validation FAILED:")
        for err in all_errors:
            print(f"  ✗ {err}")
        sys.exit(1)
    else:
        total = sum(
            len(json.loads((ROOT / c / "records.json").read_text()))
            for c in COLLECTIONS
        )
        print(f"Validation PASSED — {total} records across {len(COLLECTIONS)} collections")


if __name__ == "__main__":
    main()
