"""Exact-key matching for A1/A2/A3 comparisons."""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Iterable, Mapping, Sequence


def build_matched_operating_points(rows: Iterable[Mapping[str, Any]], profile: Mapping[str, Any]) -> dict[str, Any]:
    key_fields = list(profile["matching_key_fields"])
    expected = set(profile["required_ablations"])
    grouped: dict[tuple[Any, ...], dict[str, Mapping[str, Any]]] = defaultdict(dict)
    duplicates: list[dict[str, Any]] = []
    for row in rows:
        key = tuple(row.get(field) for field in key_fields)
        ablation = str(row["ablation_id"])
        if ablation in grouped[key]:
            duplicates.append({"key": list(key), "ablation_id": ablation})
        grouped[key][ablation] = row
    if duplicates:
        raise ValueError(f"Duplicate matched rows: {duplicates[:5]}")
    matched = []
    unmatched = []
    for key, members in sorted(grouped.items(), key=lambda item: repr(item[0])):
        missing = sorted(expected - set(members))
        payload = {field: value for field, value in zip(key_fields, key)}
        payload["member_ids"] = {ablation: members[ablation].get("record_id") for ablation in sorted(members)}
        if missing:
            payload.update({"status": "INCOMPLETE_MATCH", "missing_ablations": missing})
            unmatched.append(payload)
        else:
            payload.update({"status": "MATCHED", "missing_ablations": []})
            matched.append(payload)
    return {"matched": matched, "unmatched": unmatched, "matching_key_fields": key_fields, "required_ablations": sorted(expected)}

