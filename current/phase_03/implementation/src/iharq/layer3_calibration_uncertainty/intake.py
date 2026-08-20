"""Immutable P02 artifact discovery, manifest validation, and streaming intake."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping, Sequence

from .errors import ContractViolation, GateBlocked
from .identity import sha256_file, sha256_json


def discover_by_capability(search_roots: Sequence[str | Path], required_relatives: Sequence[str]) -> list[Path]:
    """Find roots by required file capabilities, never by mutable dataset display name."""
    found: list[Path] = []
    seen: set[Path] = set()
    for search_root in map(Path, search_roots):
        if not search_root.exists():
            continue
        candidates = [search_root]
        candidates.extend(p.parent for rel in required_relatives for p in search_root.rglob(Path(rel).name))
        for candidate in candidates:
            candidate = candidate.resolve()
            if candidate in seen:
                continue
            seen.add(candidate)
            if all((candidate / rel).exists() for rel in required_relatives):
                found.append(candidate)
    return sorted(set(found))


def validate_p02_readiness(record: Mapping[str, Any]) -> dict[str, Any]:
    terminal = record.get("terminal_status")
    compatibility = record.get("compatibility_status")
    blockers = record.get("blocking_reasons", [])
    missing_fields = list(record.get("missing_fields", []))
    if terminal != "SUCCESS" or compatibility != "PASS" or blockers or missing_fields:
        raise GateBlocked("G03-04-HANDOFF", "P02_NOT_READY", f"terminal={terminal}, compatibility={compatibility}, blockers={blockers}")
    return {"terminal_status": terminal, "compatibility_status": compatibility, "blocking_reasons": list(blockers), "missing_fields": missing_fields}


def validate_partition_manifest(manifest: Mapping[str, Any], *, expected_class_order: Sequence[str]) -> None:
    required = {"record_family", "run_cell_id", "row_count", "record_ids_sha256", "fields", "config_sha256", "partition_path"}
    missing = sorted(required - set(manifest))
    if missing:
        raise ContractViolation("Prediction partition manifest missing: " + ", ".join(missing))
    if manifest["record_family"] != "PredictionRecord":
        raise ContractViolation("Manifest is not for PredictionRecord")
    if int(manifest["row_count"]) < 1:
        raise ContractViolation("Prediction manifest row_count must be positive")
    if not isinstance(manifest["fields"], list) or "record_id" not in manifest["fields"]:
        raise ContractViolation("Prediction manifest fields must include record_id")
    if not isinstance(manifest["partition_path"], str) or Path(manifest["partition_path"]).is_absolute() or ".." in Path(manifest["partition_path"]).parts:
        raise ContractViolation("Prediction manifest partition_path is unsafe")
    if len(str(manifest["record_ids_sha256"])) != 64:
        raise ContractViolation("Prediction manifest record_ids_sha256 is invalid")
    class_order = manifest.get("class_order")
    if class_order is not None and list(class_order) != list(expected_class_order):
        raise ContractViolation("Prediction manifest class order mismatch")


def iter_jsonl_partitions(
    manifests: Iterable[Mapping[str, Any]],
    root: str | Path,
    *,
    projected_fields: Sequence[str] | None = None,
) -> Iterator[list[dict[str, Any]]]:
    root = Path(root).resolve()
    for manifest in manifests:
        path = (root / str(manifest["partition_path"])).resolve()
        if root not in path.parents:
            raise ContractViolation("Partition path escapes immutable P02 root")
        if not path.is_file():
            raise GateBlocked("G03-03-RETRIEVAL", "PREDICTION_PARTITION_MISSING", path.as_posix())
        expected = manifest.get("sha256") or manifest.get("partition_sha256")
        if expected and sha256_file(path) != expected:
            raise ContractViolation(f"Partition SHA-256 mismatch: {path}")
        rows: list[dict[str, Any]] = []
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                row = json.loads(line)
                if projected_fields is not None:
                    row = {field: row.get(field) for field in projected_fields}
                rows.append(row)
        if len(rows) != int(manifest["row_count"]):
            raise ContractViolation(f"Partition row-count mismatch: {path}")
        record_ids = [str(row.get("record_id", "")) for row in rows]
        if any(not record_id for record_id in record_ids) or len(record_ids) != len(set(record_ids)):
            raise ContractViolation(f"Prediction partition record IDs are empty or duplicated: {path}")
        import hashlib
        observed_record_ids_sha256 = hashlib.sha256("\n".join(record_ids).encode("utf-8")).hexdigest()
        if observed_record_ids_sha256 != str(manifest["record_ids_sha256"]):
            raise ContractViolation(f"Prediction partition record_ids_sha256 mismatch: {path}")
        yield rows


def immutable_object_index(root: str | Path, relative_paths: Iterable[str]) -> dict[str, Any]:
    root = Path(root).resolve()
    objects = []
    for relative in sorted(set(relative_paths)):
        path = (root / relative).resolve()
        if root not in path.parents or not path.is_file():
            raise ContractViolation(f"Unsafe or missing immutable object: {relative}")
        objects.append({"path": relative, "bytes": path.stat().st_size, "sha256": sha256_file(path)})
    return {"object_count": len(objects), "objects": objects, "object_index_sha256": sha256_json(objects)}
