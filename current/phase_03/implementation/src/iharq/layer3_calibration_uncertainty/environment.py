"""Exact offline dependency-cache verification and restart-aware installation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable, Mapping

from .errors import GateBlocked
from .identity import sha256_file


def locate_cache_manifest(search_roots: Iterable[str | Path], filename: str = "P03_WHEEL_CACHE_MANIFEST.json") -> Path:
    matches = []
    for root in map(Path, search_roots):
        if root.exists():
            matches.extend(root.rglob(filename))
    matches = sorted(set(path.resolve() for path in matches))
    if len(matches) != 1:
        raise GateBlocked("G03-02-ENVIRONMENT", "OFFLINE_CACHE_MANIFEST_RESOLUTION_FAILED", f"expected=1, observed={len(matches)}")
    return matches[0]


def verify_cache_manifest(path: str | Path, expected: Mapping[str, Any]) -> dict[str, Any]:
    path = Path(path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("python") != expected["python_exact"]:
        raise GateBlocked("G03-02-ENVIRONMENT", "OFFLINE_CACHE_PYTHON_MISMATCH", str(payload.get("python")))
    rows = payload.get("distributions", [])
    by_name = {str(row.get("name")): row for row in rows}
    failures = []
    wheel_root = path.parent
    for name, version in expected["exact_direct_pins"].items():
        row = by_name.get(name)
        if not row:
            failures.append({"name": name, "reason": "MISSING_MANIFEST_ROW"})
            continue
        if str(row.get("version")) != str(version):
            failures.append({"name": name, "reason": "VERSION_MISMATCH", "expected": str(version), "observed": row.get("version")})
            continue
        wheel = wheel_root / str(row.get("filename"))
        expected_hash = str(row.get("sha256", ""))
        if not wheel.is_file():
            failures.append({"name": name, "reason": "WHEEL_MISSING", "path": wheel.as_posix()})
        elif len(expected_hash) != 64 or sha256_file(wheel) != expected_hash:
            failures.append({"name": name, "reason": "WHEEL_HASH_MISMATCH", "path": wheel.as_posix()})
        if not row.get("license"):
            failures.append({"name": name, "reason": "LICENSE_MISSING"})
    if failures:
        raise GateBlocked("G03-02-ENVIRONMENT", "OFFLINE_CACHE_VALIDATION_FAILED", json.dumps(failures, sort_keys=True))
    return {"status": "PASS", "manifest_path": path.as_posix(), "wheel_root": wheel_root.as_posix(), "distribution_count": len(rows), "manifest_sha256": sha256_file(path), "rows": rows}


def install_verified_cache(verification: Mapping[str, Any], requirements_path: str | Path) -> dict[str, Any]:
    requirements_path = Path(requirements_path)
    lines = [f"{row['name']}=={row['version']} --hash=sha256:{row['sha256']}" for row in verification["rows"]]
    requirements_path.parent.mkdir(parents=True, exist_ok=True)
    requirements_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    command = [sys.executable, "-m", "pip", "install", "--no-index", "--require-hashes", "--find-links", str(verification["wheel_root"]), "-r", str(requirements_path)]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        raise GateBlocked("G03-02-ENVIRONMENT", "OFFLINE_INSTALL_FAILED", result.stderr[-4000:])
    return {"status": "INSTALLED_RESTART_REQUIRED", "command": [part if "token" not in part.lower() else "[REDACTED]" for part in command], "stdout_tail": result.stdout[-4000:], "stderr_tail": result.stderr[-4000:]}

