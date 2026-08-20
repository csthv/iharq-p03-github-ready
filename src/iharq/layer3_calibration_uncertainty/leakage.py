"""Field visibility, role authorization, and split-overlap firewall."""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Iterable, Mapping

from .errors import LeakageBlocked


def authorize_view(
    *,
    operation: str,
    source_role: str,
    requested_fields: Iterable[str],
    role_map: Mapping[str, Any],
    field_visibility: Mapping[str, Iterable[str]],
) -> dict[str, Any]:
    allowed_roles = set(role_map.get(operation, []))
    if source_role not in allowed_roles:
        raise LeakageBlocked(f"Operation {operation!r} cannot use role {source_role!r}; allowed={sorted(allowed_roles)}")
    visible = set(field_visibility.get(source_role, []))
    denied = sorted(set(requested_fields) - visible)
    if denied:
        raise LeakageBlocked(f"Role {source_role!r} cannot expose fields {denied} for {operation!r}")
    return {"operation": operation, "source_role": source_role, "fields": sorted(set(requested_fields)), "authorized": True}


def split_overlap_report(rows: Iterable[Mapping[str, Any]], *, role_field: str, identity_fields: Iterable[str]) -> dict[str, Any]:
    rows = list(rows)
    overlaps: dict[str, int] = {}
    details: dict[str, list[dict[str, Any]]] = {}
    for field in identity_fields:
        by_value: dict[str, set[str]] = defaultdict(set)
        for row in rows:
            value = row.get(field)
            role = row.get(role_field)
            if value is not None and role is not None:
                by_value[str(value)].add(str(role))
        violations = [{"value": value, "roles": sorted(roles)} for value, roles in by_value.items() if len(roles) > 1]
        overlaps[field] = len(violations)
        details[field] = sorted(violations, key=lambda item: item["value"])
    return {"overlap_counts": overlaps, "overlap_details": details, "validation_status": "PASS" if not any(overlaps.values()) else "FAIL"}


def evaluate_leakage(rows: Iterable[Mapping[str, Any]], profile: Mapping[str, Any]) -> dict[str, Any]:
    report = split_overlap_report(
        rows,
        role_field=str(profile["role_field"]),
        identity_fields=list(profile["identity_fields"]),
    )
    if report["validation_status"] != "PASS":
        raise LeakageBlocked("Cross-role identity overlap detected: " + str(report["overlap_counts"]))
    return report

