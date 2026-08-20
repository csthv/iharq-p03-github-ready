"""Schema discovery and validation with an exact jsonschema path and a fallback check."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping


def load_schema(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        schema = json.load(handle)
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise ValueError(f"Unsupported/missing schema dialect: {path}")
    return schema


def validate_instance(instance: Mapping[str, Any], schema: Mapping[str, Any]) -> None:
    try:
        import jsonschema
    except ImportError:
        missing = [key for key in schema.get("required", []) if key not in instance]
        if missing:
            raise ValueError("Missing required schema fields: " + ", ".join(missing))
        if schema.get("type") == "object" and not isinstance(instance, Mapping):
            raise ValueError("Instance is not an object")
        return
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.validate(dict(instance), dict(schema), cls=jsonschema.Draft202012Validator)


def validate_all_schemas(schema_root: str | Path) -> dict[str, Any]:
    root = Path(schema_root)
    checked = []
    for path in sorted(root.rglob("*.schema.json")):
        schema = load_schema(path)
        try:
            import jsonschema
        except ImportError:
            pass
        else:
            jsonschema.Draft202012Validator.check_schema(schema)
        checked.append(path.relative_to(root).as_posix())
    if not checked:
        raise ValueError(f"No schemas found under {root}")
    return {"status": "PASS", "schema_count": len(checked), "schemas": checked}
