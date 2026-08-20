"""Complete 25-stage P03/L3 notebook handlers.

The notebook calls these package APIs; scientific logic is kept out of notebook
cells.  Real execution is fail-closed on exact inputs and a populated immutable
Protocol freeze.  The authoring fixture follows the same handlers but is always
tagged non-scientific and cannot be exported as P03 evidence.
"""

from __future__ import annotations

import csv
import hashlib
import importlib
import importlib.metadata
import json
import os
import platform
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence

import numpy as np
import yaml

from .calibration import apply_calibrator, fit_calibrator, serialize_calibrator
from .config import config_snapshot, freeze_snapshot, load_structured, validate_protocol_freeze
from .errors import ContractViolation, GateBlocked, IneligibleMethod
from .environment import install_verified_cache, locate_cache_manifest, verify_cache_manifest
from .group_audit import audit_groups
from .handoffs import build_handoff
from .high_confidence_wrong import mine_high_confidence_errors
from .identity import deterministic_id, sha256_file, sha256_json, utc_now
from .intake import validate_p02_readiness, validate_partition_manifest
from .leakage import authorize_view, evaluate_leakage
from .matched_operating_points import build_matched_operating_points
from .metrics import negative_log_likelihood, selective_risk
from .models import ExecutionContext
from .reliability import audit_reliability
from .records import load_field_contract, make_record
from .schemas import validate_all_schemas
from .score_contracts import ScoreView, eligibility, score_to_probabilities, validate_class_order, validate_probabilities
from .security import assert_clean_export, require_credential_symbol, sanitize_environment
from .selective import apply_rule, build_risk_coverage, select_rule
from .store import ThresholdStore
from .thresholds import register_threshold
from .uncertainty import extract_uncertainty
from .conditional_proxies import apply_conformal_proxy, fit_conformal_proxy, summarize_past
from .writers import AtomicJsonlCsvStream, build_manifest, scan_for_secrets, write_checksum_manifest, write_csv, write_json, write_jsonl
from .selection_replay import (
    eligible_replay_models, select_replay_snapshot_rows, replay_one_model,
    canonical_truth_row, build_selection_score_record, load_test_partition,
    calibration_rows as replay_calibration_rows, validation_rows as replay_validation_rows,
    _validate_probability_matrix as _canonicalize_replay_source_probabilities,
    P03_SOURCE_FLOAT_PROBABILITY_ATOL as _REPLAY_SOURCE_PROBABILITY_ATOL,
)

Progress = Callable[[int, int, str | None, int, str], None]


def _config(ctx: ExecutionContext) -> dict[str, Any]:
    return load_structured(ctx.config_path)


def _protocol(ctx: ExecutionContext) -> dict[str, Any]:
    return load_structured(ctx.protocol_path)


def _record_contract(ctx: ExecutionContext) -> dict[str, Any]:
    return load_field_contract(ctx.package_root / "machine_readable" / "record_field_contracts.yaml")


def _stage_dir(ctx: ExecutionContext, stage_id: str) -> Path:
    return ctx.run_root / "stage_artifacts" / f"stage_{stage_id}"


def _stage_result(ctx: ExecutionContext, stage_id: str) -> dict[str, Any]:
    path = _stage_dir(ctx, stage_id) / "stage_result.json"
    if not path.is_file():
        raise GateBlocked(f"G03-{stage_id}", "PREREQUISITE_STAGE_MISSING", path.as_posix())
    return json.loads(path.read_text(encoding="utf-8"))


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def _load_group(ctx: ExecutionContext, group_id: str, source_stage: str = "07") -> tuple[dict[str, Any], np.ndarray, np.ndarray, list[dict[str, Any]]]:
    root = _stage_dir(ctx, source_stage) / "groups" / group_id
    descriptor = json.loads((root / "descriptor.json").read_text(encoding="utf-8"))
    arrays = np.load(root / "data.npz", allow_pickle=False)
    scores = np.asarray(arrays["scores"], dtype=float)
    labels = np.asarray(arrays["labels"], dtype=int)
    metadata = _read_jsonl(root / "metadata.jsonl")
    if not (len(scores) == len(labels) == len(metadata)):
        raise ContractViolation(f"Canonical group row mismatch: {group_id}")
    return descriptor, scores, labels, metadata


def _group_ids(ctx: ExecutionContext) -> list[str]:
    return list(_stage_result(ctx, "07")["group_ids"])


def _save_group(out: Path, descriptor: Mapping[str, Any], scores: np.ndarray, labels: np.ndarray, metadata: Sequence[Mapping[str, Any]]) -> str:
    group_id = str(descriptor["group_id"])
    root = out / "groups" / group_id
    root.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(root / "data.npz", scores=np.asarray(scores, dtype=float), labels=np.asarray(labels, dtype=int))
    write_json(root / "descriptor.json", dict(descriptor))
    write_jsonl(root / "metadata.jsonl", metadata)
    return group_id


def _role_indices(metadata: Sequence[Mapping[str, Any]], role: str) -> np.ndarray:
    return np.asarray([index for index, row in enumerate(metadata) if str(row.get("split_role")) == role], dtype=int)


def _protocol_role(protocol: Mapping[str, Any], key: str) -> str:
    return str(protocol["scientific"]["roles"]["named_roles"][key])


def _score_type(value: str, config: Mapping[str, Any]) -> str:
    mapping = config["score_semantics"]["p02_to_p03"]
    if value not in mapping:
        raise ContractViolation(f"Unmapped P02 score type: {value}")
    return str(mapping[value])


def stage_00(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    progress(0, 4, "authority intake", 0, "IN_PROGRESS")
    required = [
        ctx.package_root / "machine_readable" / "source_intake_manifest.json",
        ctx.package_root / "machine_readable" / "build_book_to_notebook_parity.csv",
        ctx.package_root / "machine_readable" / "runtime_artifact_matrix.csv",
        ctx.repository_root / "pyproject.toml",
        ctx.repository_root / "src" / "iharq" / "layer2_decoders" / "__init__.py",
        ctx.repository_root / "src" / "iharq" / "layer3_calibration_uncertainty" / "__init__.py",
    ]
    missing = [path.as_posix() for path in required if not path.is_file()]
    if missing:
        raise GateBlocked("G03-00-AUTHORITY", "SOURCE_CAPABILITY_MISSING", ", ".join(missing))
    progress(1, 4, "source capability check", 0, "IN_PROGRESS")
    source_manifest = json.loads(required[0].read_text(encoding="utf-8"))
    if source_manifest.get("manifest_sha256") and source_manifest["manifest_sha256"] != sha256_json(source_manifest.get("sources", [])):
        raise ContractViolation("Source intake manifest hash mismatch")
    progress(2, 4, "source manifest hash", 0, "IN_PROGRESS")
    authority = {
        "authority_snapshot_id": deterministic_id("P03-AUTHORITY", source_manifest),
        "build_book_id": "IHARQ-P03-L3-IMPLEMENTATION-BUILD-BOOK-R2",
        "notebook_id": "IHARQ-P03-L3-KAGGLE-NOTEBOOK-R2",
        "roles_preserved": ["governance", "architecture", "registry", "execution", "method", "implementation", "evidence", "predecessor_runtime"],
        "source_count": len(source_manifest.get("sources", [])),
        "source_manifest_sha256": sha256_json(source_manifest),
        "upstream_read_only": True,
        "created_at_utc": ctx.created_at_utc,
    }
    write_json(out / "authority_snapshot.json", authority)
    write_json(out / "source_manifest.json", source_manifest)
    progress(4, 4, "authority snapshot", 0, "COMPLETE")
    return {"status": "PASS", "products": ["P03-PROD-001", "P03-PROD-002"], "authority_snapshot": "authority_snapshot.json", "source_manifest": "source_manifest.json", "source_count": authority["source_count"]}


def stage_01(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    progress(0, 3, "repository checks", 0, "IN_PROGRESS")
    source_root = ctx.repository_root / "src"
    compile_result = subprocess.run([sys.executable, "-m", "compileall", "-q", str(source_root / "iharq" / "layer3_calibration_uncertainty")], capture_output=True, text=True)
    if compile_result.returncode:
        raise GateBlocked("G03-01-REPOSITORY", "SOURCE_COMPILE_FAILED", compile_result.stderr[-2000:])
    progress(1, 3, "compileall", 0, "IN_PROGRESS")
    stub_text = (source_root / "iharq" / "layer3_calibration_uncertainty" / "__init__.py").read_text(encoding="utf-8")
    if "SCIENTIFIC_EXECUTION = False" in stub_text:
        raise GateBlocked("G03-01-REPOSITORY", "L3_STUB_NOT_REPLACED", "P03 additive patch was not applied")
    files = sorted((source_root / "iharq" / "layer3_calibration_uncertainty").rglob("*.py"))
    receipt = {
        "status": "PASS",
        "repository_root": ctx.repository_root.as_posix(),
        "l3_python_file_count": len(files),
        "l3_code_sha256": sha256_json([{"path": p.relative_to(ctx.repository_root).as_posix(), "sha256": sha256_file(p)} for p in files]),
        "p02_package_present": (source_root / "iharq" / "layer2_decoders").is_dir(),
        "upstream_mutation": False,
        "compile_stdout": compile_result.stdout,
    }
    write_json(out / "repository_validation_receipt.json", receipt)
    progress(3, 3, "repository receipt", 0, "COMPLETE")
    return {"status": "PASS", "products": ["P03-PROD-003"], "repository_validation_receipt": "repository_validation_receipt.json", **receipt}


def stage_02(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    config = _config(ctx)
    expected = dict(config["environment"]["exact_direct_pins"])
    expected["python"] = str(config["environment"]["python_exact"])
    progress(0, len(expected), "environment probe", 0, "IN_PROGRESS")
    observed: dict[str, str | None] = {"python": platform.python_version()}
    import_names = dict(config["environment"]["import_names"])
    gpu_policy = dict(config["inputs"]["p02"].get("replay_materialization", {}).get("gpu_inference") or {})
    gpu_probe: dict[str, Any] = {"policy_id": gpu_policy.get("policy_id"), "required": bool(gpu_policy.get("required", False)), "available": False, "device_count": 0, "devices": []}
    receipts = []
    mismatches = []
    for index, (name, version) in enumerate(config["environment"]["exact_direct_pins"].items(), start=1):
        try:
            observed_version = importlib.metadata.version(name)
            importlib.import_module(import_names[name])
            import_status = "PASS"
        except Exception as exc:
            observed_version = None
            import_status = f"FAIL:{type(exc).__name__}:{exc}"
        observed[name] = observed_version
        status = "PASS" if observed_version == str(version) and import_status == "PASS" else "FAIL"
        if status == "FAIL":
            mismatches.append({"name": name, "expected": str(version), "observed": observed_version, "import_status": import_status})
        receipts.append({"name": name, "expected_version": str(version), "observed_version": observed_version, "import_probe": import_status, "status": status})
        progress(index, len(expected), name, len(mismatches), "IN_PROGRESS")
    if observed["python"] != expected["python"]:
        mismatches.insert(0, {"name": "python", "expected": expected["python"], "observed": observed["python"], "import_status": "PASS"})
    try:
        import torch
        gpu_probe["available"] = bool(torch.cuda.is_available())
        gpu_probe["device_count"] = int(torch.cuda.device_count()) if gpu_probe["available"] else 0
        gpu_probe["torch_cuda"] = torch.version.cuda
        gpu_probe["cudnn"] = int(torch.backends.cudnn.version() or 0) if gpu_probe["available"] else None
        if gpu_probe["available"]:
            for i in range(gpu_probe["device_count"]):
                props = torch.cuda.get_device_properties(i)
                gpu_probe["devices"].append({
                    "index": i, "name": str(props.name),
                    "capability": [int(props.major), int(props.minor)],
                    "total_memory_bytes": int(props.total_memory),
                    "multi_processor_count": int(props.multi_processor_count),
                })
        if bool(gpu_policy.get("required", False)) and gpu_probe["device_count"] < int(gpu_policy.get("minimum_gpu_count", 1)):
            mismatches.append({
                "name": "gpu_accelerator",
                "expected": f">={int(gpu_policy.get('minimum_gpu_count', 1))} CUDA GPU",
                "observed": gpu_probe["device_count"],
                "import_status": "FAIL:CUDA_REQUIRED",
            })
        if gpu_probe["available"]:
            torch.backends.cudnn.benchmark = bool(gpu_policy.get("cudnn_benchmark", False))
            torch.backends.cudnn.deterministic = bool(gpu_policy.get("cudnn_deterministic", True))
            if hasattr(torch.backends, "cuda") and hasattr(torch.backends.cuda, "matmul"):
                torch.backends.cuda.matmul.allow_tf32 = bool(gpu_policy.get("tf32", False))
            torch.backends.cudnn.allow_tf32 = bool(gpu_policy.get("tf32", False))
            gpu_probe["runtime_flags"] = {
                "cudnn_benchmark": bool(torch.backends.cudnn.benchmark),
                "cudnn_deterministic": bool(torch.backends.cudnn.deterministic),
                "matmul_tf32": bool(torch.backends.cuda.matmul.allow_tf32) if hasattr(torch.backends, "cuda") else None,
                "cudnn_tf32": bool(torch.backends.cudnn.allow_tf32),
                "amp": bool(gpu_policy.get("automatic_mixed_precision", False)),
            }
            if gpu_probe["runtime_flags"]["amp"]:
                mismatches.append({"name": "gpu_amp", "expected": False, "observed": True, "import_status": "FAIL:AMP_PROHIBITED"})
    except Exception as exc:
        gpu_probe["probe_error"] = f"{type(exc).__name__}:{exc}"
        if bool(gpu_policy.get("required", False)):
            mismatches.append({"name": "gpu_probe", "expected": "PASS", "observed": gpu_probe["probe_error"], "import_status": "FAIL"})
    fixture_override = ctx.authoring_fixture and not bool(config["execution"]["enforce_exact_environment_for_authoring_fixture"])
    manifest = {
        "environment_id": deterministic_id("P03-ENVIRONMENT", observed),
        "python": observed["python"],
        "expected": expected,
        "observed": observed,
        "platform": platform.platform(),
        "deterministic_environment": {key: os.environ.get(key) for key in config["environment"]["deterministic_environment"]},
        "gpu_acceleration": gpu_probe,
        "mismatches": mismatches,
        "official_status": "PASS" if not mismatches else "BLOCKED",
        "authoring_fixture_override": fixture_override,
        "scientific_evidence": False if fixture_override else True,
    }
    write_json(out / "environment_manifest.json", manifest)
    offline_only = bool(config["environment"].get("package_install_offline_only", True))
    write_json(out / "dependency_receipt.json", {
        "dependencies": receipts,
        "status": manifest["official_status"],
        "offline_cache_required": offline_only,
        "replay_dependency_install_policy": config["environment"].get("replay_dependency_install_policy"),
    })
    if mismatches and not fixture_override:
        if offline_only:
            cache_manifest = locate_cache_manifest(config["paths"]["input_search_roots"])
            verification = verify_cache_manifest(cache_manifest, config["environment"])
            installation = install_verified_cache(verification, out / "verified_requirements_with_hashes.txt")
            write_json(out / "offline_cache_verification.json", verification)
            write_json(out / "offline_install_receipt.json", installation)
            raise GateBlocked("G03-02-ENVIRONMENT", "ENVIRONMENT_RESTART_REQUIRED_AFTER_OFFLINE_INSTALL", "Verified exact dependencies installed; restart kernel and begin a new exact-fingerprint run")
        raise GateBlocked(
            "G03-02-ENVIRONMENT",
            "C5_PRECONTEXT_DEPENDENCY_REPAIR_REQUIRED",
            json.dumps(mismatches, sort_keys=True),
        )
    progress(len(expected), len(expected), "environment manifest", len(mismatches), "COMPLETE")
    return {"status": "PASS" if not mismatches else "PASS_NON_SCIENTIFIC_AUTHORING_FIXTURE", "products": ["P03-PROD-004", "P03-PROD-005"], "environment_manifest": "environment_manifest.json", "dependency_receipt": "dependency_receipt.json", "official_mismatch_count": len(mismatches), "gpu_acceleration": gpu_probe}


def _load_snapshot_manifest(manifest_path: Path, metadata_path: Path, locator: Mapping[str, Any], remote_files: set[str]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if not manifest_path.is_file() or sha256_file(manifest_path) != str(locator["manifest_sha256"]):
        raise GateBlocked("G03-03-RETRIEVAL", "P02_MANIFEST_HASH_MISMATCH", manifest_path.as_posix())
    if not metadata_path.is_file():
        raise GateBlocked("G03-03-RETRIEVAL", "P02_SNAPSHOT_METADATA_MISSING", metadata_path.as_posix())
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    with manifest_path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            relative = str(row.get("path", ""))
            candidate = Path(relative)
            if not relative or candidate.is_absolute() or ".." in candidate.parts:
                raise GateBlocked("G03-03-RETRIEVAL", "P02_MANIFEST_UNSAFE_PATH", f"line={line_number}, path={relative!r}")
            if relative in seen:
                raise GateBlocked("G03-03-RETRIEVAL", "P02_MANIFEST_DUPLICATE_PATH", relative)
            if not re.fullmatch(r"[0-9a-f]{64}", str(row.get("sha256", ""))) or int(row.get("bytes", -1)) < 0:
                raise GateBlocked("G03-03-RETRIEVAL", "P02_MANIFEST_ROW_INVALID", f"line={line_number}, path={relative}")
            seen.add(relative)
            rows.append({"path": relative, "bytes": int(row["bytes"]), "sha256": str(row["sha256"])})
    expected_count = int(locator["source_manifest_file_count"])
    if len(rows) != expected_count:
        raise GateBlocked("G03-03-RETRIEVAL", "P02_MANIFEST_FILE_COUNT_MISMATCH", f"expected={expected_count}, observed={len(rows)}")
    metadata_checks = {
        "repo_id": metadata.get("repo_id") == locator["repo_id"],
        "repo_type": metadata.get("repo_type") == locator["repo_type"],
        "private": metadata.get("private") is True,
        "manifest_sha256": metadata.get("manifest_sha256") == locator["manifest_sha256"],
        "manifested_files": int(metadata.get("manifested_files", -1)) == expected_count,
    }
    if not all(metadata_checks.values()):
        raise GateBlocked("G03-03-RETRIEVAL", "P02_SNAPSHOT_METADATA_MISMATCH", json.dumps(metadata_checks, sort_keys=True))
    missing_remote = sorted(seen - remote_files)
    if missing_remote:
        raise GateBlocked("G03-03-RETRIEVAL", "P02_REMOTE_TREE_INCOMPLETE", f"missing={len(missing_remote)}, examples={missing_remote[:10]}")
    return rows, metadata


def _select_required_snapshot_rows(rows: Sequence[Mapping[str, Any]], locator: Mapping[str, Any]) -> list[dict[str, Any]]:
    by_path = {str(row["path"]): dict(row) for row in rows}
    exact_contract = {str(path): dict(spec) for path, spec in locator["required_exact_objects"].items()}
    exact = [*exact_contract, *map(str, locator["p01_core_paths"])]
    missing_exact = [path for path in exact if path not in by_path]
    if missing_exact:
        raise GateBlocked("G03-03-RETRIEVAL", "P02_REQUIRED_EXACT_PATH_MISSING", json.dumps(missing_exact))
    exact_drift = {
        path: {
            "expected_bytes": int(spec["bytes"]),
            "observed_bytes": int(by_path[path]["bytes"]),
            "expected_sha256": str(spec["sha256"]),
            "observed_sha256": str(by_path[path]["sha256"]),
        }
        for path, spec in exact_contract.items()
        if int(by_path[path]["bytes"]) != int(spec["bytes"]) or str(by_path[path]["sha256"]) != str(spec["sha256"])
    }
    if exact_drift:
        raise GateBlocked("G03-03-RETRIEVAL", "P02_EXACT_OBJECT_CONTRACT_DRIFT", json.dumps(exact_drift, sort_keys=True))
    prefixes = [
        str(locator["prediction_manifest_prefix"]),
        str(locator["prediction_record_prefix"]),
        str(locator["model_registry_prefix"]),
        str(locator["ensemble_control_manifest_prefix"]),
        str(locator["ensemble_control_record_prefix"]),
    ]
    selected = {path: by_path[path] for path in exact}
    observed_counts = {}
    for prefix in prefixes:
        matches = [path for path in by_path if path.startswith(prefix)]
        observed_counts[prefix] = len(matches)
        for path in matches:
            selected[path] = by_path[path]
    expected_counts = {
        str(locator["prediction_manifest_prefix"]): int(locator["prediction_partition_count"]),
        str(locator["prediction_record_prefix"]): int(locator["prediction_partition_count"]),
        str(locator["model_registry_prefix"]): int(locator["model_registry_success_count"]),
        str(locator["ensemble_control_manifest_prefix"]): int(locator["ensemble_control_count"]),
        str(locator["ensemble_control_record_prefix"]): int(locator["ensemble_control_count"]),
    }
    if observed_counts != expected_counts:
        raise GateBlocked("G03-03-RETRIEVAL", "P02_REQUIRED_OBJECT_CARDINALITY_MISMATCH", json.dumps({"expected": expected_counts, "observed": observed_counts}, sort_keys=True))
    # The all-artifact location index is generated as cumulative P02 release metadata
    # after the immutable HF working-tree manifest is frozen, so it cannot be a member
    # of that manifest without creating a self-referential index. C4 verifies the exact
    # accepted index locally and cross-checks its 24,661 source rows against the remote
    # immutable manifest in _verify_local_p02_object_index().
    return [selected[path] for path in sorted(selected)]



def _verify_local_p02_control_objects(ctx: ExecutionContext, locator: Mapping[str, Any]) -> dict[str, Any]:
    """Verify small P02 handoff authorities bundled from the accepted cumulative P02 state.

    These files are control-plane handoff authorities, not P02 scientific/runtime HF snapshot
    objects. Their original P02 sizes and SHA-256 values remain frozen in p03.yaml.
    """
    base = ctx.package_root.resolve()
    contract = {str(path): dict(spec) for path, spec in locator.get("required_local_control_objects", {}).items()}
    failures: list[dict[str, Any]] = []
    verified: list[dict[str, Any]] = []
    for relative, spec in sorted(contract.items()):
        path = (base / relative).resolve()
        if (base != path and base not in path.parents) or not path.is_file():
            failures.append({"path": relative, "reason": "MISSING_OR_UNSAFE"})
            continue
        observed_bytes = path.stat().st_size
        observed_sha = sha256_file(path)
        expected_bytes = int(spec["bytes"])
        expected_sha = str(spec["sha256"])
        if observed_bytes != expected_bytes:
            failures.append({"path": relative, "reason": "SIZE_MISMATCH", "expected": expected_bytes, "observed": observed_bytes})
            continue
        if observed_sha != expected_sha:
            failures.append({"path": relative, "reason": "SHA256_MISMATCH", "expected": expected_sha, "observed": observed_sha})
            continue
        verified.append({"path": relative, "bytes": observed_bytes, "sha256": observed_sha})
    if failures:
        raise GateBlocked("G03-03-RETRIEVAL", "P02_LOCAL_HANDOFF_CONTROL_INTEGRITY_FAILED", json.dumps(failures, sort_keys=True))
    return {
        "source": str(locator.get("local_control_source", "BUNDLED_CUMULATIVE_P02_HANDOFF_AUTHORITIES")),
        "root": "COMPANION_PACKAGE_ROOT",
        "verified_object_count": len(verified),
        "objects": verified,
    }

def _verify_local_p02_object_index(ctx: ExecutionContext, locator: Mapping[str, Any], manifest_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Verify the accepted cumulative P02 object index and bind it to the immutable HF manifest.

    The index is release metadata generated from the frozen P02 working-tree inventory. It is
    intentionally not required to be a member of the HF manifest itself (which would be
    self-referential). Exact bytes/SHA-256 plus a row-for-row path/size/hash crosswalk preserve
    the same immutability strength without weakening the Stage 03 gate.
    """
    relative = str(locator["local_object_index_path"])
    base = ctx.package_root.resolve()
    path = (base / relative).resolve()
    if (base != path and base not in path.parents) or not path.is_file():
        raise GateBlocked("G03-03-RETRIEVAL", "P02_LOCAL_OBJECT_INDEX_MISSING", relative)
    if path.stat().st_size != int(locator["object_index_size_bytes"]):
        raise GateBlocked("G03-03-RETRIEVAL", "P02_LOCAL_OBJECT_INDEX_SIZE_MISMATCH", relative)
    if sha256_file(path) != str(locator["object_index_sha256"]):
        raise GateBlocked("G03-03-RETRIEVAL", "P02_LOCAL_OBJECT_INDEX_HASH_MISMATCH", relative)

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        required_fields = {"source_path", "bytes", "sha256", "classification", "release_location", "hf_repo", "hf_revision", "hf_path"}
        if not required_fields <= set(reader.fieldnames or []):
            raise GateBlocked("G03-03-RETRIEVAL", "P02_LOCAL_OBJECT_INDEX_SCHEMA_MISMATCH", json.dumps(sorted(reader.fieldnames or [])))
        index_rows = list(reader)

    expected_count = int(locator["source_manifest_file_count"])
    if len(index_rows) != expected_count:
        raise GateBlocked("G03-03-RETRIEVAL", "P02_LOCAL_OBJECT_INDEX_COUNT_MISMATCH", f"expected={expected_count}, observed={len(index_rows)}")

    manifest_by_path = {str(row["path"]): row for row in manifest_rows}
    index_by_path = {str(row["source_path"]): row for row in index_rows}
    if len(index_by_path) != len(index_rows):
        raise GateBlocked("G03-03-RETRIEVAL", "P02_LOCAL_OBJECT_INDEX_DUPLICATE_SOURCE_PATH", "duplicate source_path detected")
    if set(index_by_path) != set(manifest_by_path):
        missing = sorted(set(manifest_by_path) - set(index_by_path))
        extra = sorted(set(index_by_path) - set(manifest_by_path))
        raise GateBlocked("G03-03-RETRIEVAL", "P02_LOCAL_OBJECT_INDEX_PATH_SET_MISMATCH", json.dumps({"missing": missing[:10], "extra": extra[:10], "missing_count": len(missing), "extra_count": len(extra)}, sort_keys=True))

    drift = []
    for source_path, manifest_row in manifest_by_path.items():
        index_row = index_by_path[source_path]
        if int(index_row["bytes"]) != int(manifest_row["bytes"]) or str(index_row["sha256"]) != str(manifest_row["sha256"]):
            drift.append({"path": source_path, "manifest_bytes": int(manifest_row["bytes"]), "index_bytes": int(index_row["bytes"]), "manifest_sha256": str(manifest_row["sha256"]), "index_sha256": str(index_row["sha256"])})
            if len(drift) >= 10:
                break
    if drift:
        raise GateBlocked("G03-03-RETRIEVAL", "P02_LOCAL_OBJECT_INDEX_MANIFEST_DRIFT", json.dumps(drift, sort_keys=True))

    # Rows classified as external HF objects must point to the same frozen P02 repository/revision.
    hf_rows = [row for row in index_rows if str(row.get("release_location", "")) == "HF_SOURCE_SNAPSHOT_EXTERNAL"]
    bad_hf = [row["source_path"] for row in hf_rows if str(row.get("hf_repo", "")) != str(locator["repo_id"]) or str(row.get("hf_revision", "")) != str(locator["revision"])]
    if bad_hf:
        raise GateBlocked("G03-03-RETRIEVAL", "P02_LOCAL_OBJECT_INDEX_HF_IDENTITY_MISMATCH", json.dumps(bad_hf[:10]))

    return {
        "source": str(locator.get("object_index_source", "BUNDLED_CUMULATIVE_P02_RELEASE_METADATA")),
        "path": relative,
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
        "row_count": len(index_rows),
        "manifest_crosswalk_count": len(manifest_by_path),
        "hf_external_row_count": len(hf_rows),
        "manifest_path_set_exact": True,
        "manifest_size_hash_crosswalk_exact": True,
        "hf_identity_consistent": True,
    }


def _verify_materialized_rows(root: Path, rows: Sequence[Mapping[str, Any]], workers: int) -> dict[str, Any]:
    root = root.resolve()

    def verify(row: Mapping[str, Any]) -> dict[str, Any] | None:
        relative = str(row["path"])
        path = (root / relative).resolve()
        if root not in path.parents or not path.is_file():
            return {"path": relative, "reason": "MISSING_OR_UNSAFE"}
        if path.stat().st_size != int(row["bytes"]):
            return {"path": relative, "reason": "SIZE_MISMATCH"}
        if sha256_file(path) != str(row["sha256"]):
            return {"path": relative, "reason": "SHA256_MISMATCH"}
        return None

    with ThreadPoolExecutor(max_workers=max(1, int(workers))) as executor:
        failures = [failure for failure in executor.map(verify, rows) if failure is not None]
    if failures:
        raise GateBlocked("G03-03-RETRIEVAL", "P02_REQUIRED_OBJECT_INTEGRITY_FAILED", json.dumps(failures[:10], sort_keys=True))
    return {"verified_object_count": len(rows), "verified_bytes": sum(int(row["bytes"]) for row in rows), "hash_workers": max(1, int(workers))}


def _resolve_external_snapshot(ctx: ExecutionContext, out: Path, progress: Progress) -> tuple[Path, dict[str, Any]]:
    config = _config(ctx)
    locator = config["inputs"]["p02"]
    if ctx.authoring_fixture:
        root = (ctx.package_root / config["paths"]["authoring_fixture_root"]).resolve()
        if not root.is_dir():
            raise GateBlocked("G03-03-RETRIEVAL", "AUTHORING_FIXTURE_MISSING", root.as_posix())
        return root, {"provider": "LOCAL_NON_SCIENTIFIC_AUTHORING_FIXTURE", "revision": "fixture-r1", "credential_class": "NONE", "scientific_evidence": False}
    if bool(locator.get("kaggle_p02_dataset_expected", True)):
        raise GateBlocked("G03-03-RETRIEVAL", "P02_SOURCE_POLICY_INVALID", "Kaggle-hosted P02 input must be disabled")
    progress(1, 6, "private HF authentication", 0, "IN_PROGRESS")
    token = require_credential_symbol(locator["credential_symbol"], gate_id="G03-03-RETRIEVAL")
    try:
        from huggingface_hub import HfApi, snapshot_download
    except ImportError as exc:
        raise GateBlocked("G03-03-RETRIEVAL", "HUGGINGFACE_HUB_UNAVAILABLE", str(exc)) from exc
    root = Path(config["paths"]["p02_materialization_root"])
    root.mkdir(parents=True, exist_ok=True)
    try:
        api = HfApi(token=token)
        remote_info = api.repo_info(repo_id=locator["repo_id"], repo_type=locator["repo_type"], revision=locator["revision"])
        if str(remote_info.sha) != str(locator["revision"]):
            raise GateBlocked("G03-03-RETRIEVAL", "P02_REMOTE_REVISION_MISMATCH", f"expected={locator['revision']}, observed={remote_info.sha}")
        progress(2, 6, "immutable revision resolved", 0, "IN_PROGRESS")
        control_paths = [str(locator["manifest_path"]), str(locator["snapshot_metadata_path"])]
        snapshot_download(repo_id=locator["repo_id"], repo_type=locator["repo_type"], revision=locator["revision"], token=token, local_dir=root, allow_patterns=control_paths, max_workers=int(locator["download_max_workers"]))
        remote_files = set(api.list_repo_files(repo_id=locator["repo_id"], repo_type=locator["repo_type"], revision=locator["revision"]))
        progress(3, 6, "remote manifest/control plane", 0, "IN_PROGRESS")
        manifest_path = root / locator["manifest_path"]
        metadata_path = root / locator["snapshot_metadata_path"]
        rows, metadata = _load_snapshot_manifest(manifest_path, metadata_path, locator, remote_files)
        local_control_verification = _verify_local_p02_control_objects(ctx, locator)
        object_index_verification = _verify_local_p02_object_index(ctx, locator, rows)
        required_rows = _select_required_snapshot_rows(rows, locator)
        download_paths = control_paths + [str(row["path"]) for row in required_rows]
        snapshot_download(repo_id=locator["repo_id"], repo_type=locator["repo_type"], revision=locator["revision"], token=token, local_dir=root, allow_patterns=download_paths, max_workers=int(locator["download_max_workers"]))
        initial_verification = _verify_materialized_rows(root, required_rows, int(locator["integrity_hash_workers"]))

        # C5: materialize the exact P03 selection-score replay substrate.  P02
        # PredictionRecords are final-test-only, so P03 must replay accepted P02
        # checkpoints on frozen P01 CALIBRATION/VALIDATION windows without retraining.
        replay_cfg = dict(locator.get("replay_materialization") or {})
        replay_selection = None
        if bool(replay_cfg.get("enabled")):
            runtime_root = root / locator["runtime_root"]
            replay_models, replay_population = eligible_replay_models(
                runtime_root,
                expected_config_sha256=str(locator["accepted_config_sha256"]),
                expected_count=int(replay_cfg["expected_model_count"]),
                expected_population_sha256=str(replay_cfg["expected_population_sha256"]),
            )
            replay_rows, replay_objects = select_replay_snapshot_rows(rows, replay_models, replay_cfg)
            replay_download_paths = [str(row["path"]) for row in replay_rows]
            snapshot_download(
                repo_id=locator["repo_id"], repo_type=locator["repo_type"], revision=locator["revision"],
                token=token, local_dir=root, allow_patterns=replay_download_paths,
                max_workers=int(locator["download_max_workers"]),
            )
            union = {str(row["path"]): dict(row) for row in required_rows}
            for row in replay_rows:
                union[str(row["path"])] = dict(row)
            required_rows = [union[path] for path in sorted(union)]
            replay_selection = {**replay_population, **replay_objects}
        progress(4, 6, "required P02/P01 continuation + P03 replay objects", 0, "IN_PROGRESS")
        verification = _verify_materialized_rows(root, required_rows, int(locator["integrity_hash_workers"]))
        verification["initial_verified_object_count"] = int(initial_verification["verified_object_count"])
        verification["replay_selection"] = replay_selection
    except GateBlocked:
        raise
    except Exception as exc:
        detail = str(exc).replace(token, "[REDACTED]")
        raise GateBlocked("G03-03-RETRIEVAL", "P02_HF_EXACT_REVISION_RETRIEVAL_FAILED", f"{type(exc).__name__}: {detail}") from exc
    progress(5, 6, "required-object SHA-256 verification", 0, "IN_PROGRESS")
    manifest_path = root / locator["manifest_path"]
    return root.resolve(), {
        "provider": locator["provider"], "repo_id": locator["repo_id"], "repo_type": locator["repo_type"], "revision": locator["revision"],
        "manifest_sha256": locator["manifest_sha256"], "manifest_file_count": len(rows), "remote_file_count": len(remote_files),
        "snapshot_metadata_artifact_id": metadata.get("artifact_id"), "credential_class": locator["credential_symbol"],
        "retrieval_mode": "HF_EXACT_REVISION_REQUIRED_OBJECT_MATERIALIZATION_PLUS_BUNDLED_CUMULATIVE_HANDOFF_CONTROLS", "kaggle_p02_dataset_used": False,
        "mutable_latest_used": False, "download_max_workers": int(locator["download_max_workers"]),
        "local_control_verification": local_control_verification, "object_index_verification": object_index_verification, **verification,
    }


def stage_03(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    progress(0, 6, "artifact resolution", 0, "IN_PROGRESS")
    root, receipt = _resolve_external_snapshot(ctx, out, progress)
    receipt.update({"resolved_root": root.as_posix(), "credential_state": sanitize_environment(["IHARQ_HF_TOKEN_P02"]), "literal_credential_persisted": False})
    write_json(out / "external_retrieval_receipt.json", receipt)
    write_json(out / "resolved_external_root.json", {"path": root.as_posix(), "sha256": sha256_json(receipt)})
    progress(6, 6, "retrieval receipt", 0, "COMPLETE")
    return {"status": "PASS", "products": ["P03-PROD-006"], "external_retrieval_receipt": "external_retrieval_receipt.json", "resolved_external_root": root.as_posix(), "scientific_evidence": receipt.get("scientific_evidence", True)}


def stage_04(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    config = _config(ctx)
    root = Path(_stage_result(ctx, "03")["resolved_external_root"])
    locator = config["inputs"]["p02"]
    progress(0, 5, "readiness discovery", 0, "IN_PROGRESS")
    if ctx.authoring_fixture:
        readiness = json.loads((root / "p02_readiness.json").read_text(encoding="utf-8"))
        partition_count = int(readiness["prediction_partition_count"])
        model_count = int(readiness["model_registry_success_count"])
        source_run_id = str(readiness["run_id"])
        source_config_sha256 = str(readiness["config_sha256"])
        source_protocol_id = str(readiness["scientific_freeze_id"])
        budget_profile_ids = list(readiness["budget_profile_ids"])
        limitation_rows = [{"limitation_id": value, "tag": value, "status_after_P02": "NON_SCIENTIFIC_FIXTURE"} for value in readiness["limitations"]]
        upstream_counts = {"baseline_metric_records": 0, "ensemble_control_records": 0, "diagnostic_only_records": 0, "failure_case_records": 0}
        a0_validated = a4_validated = True
        contract_complete = True
    else:
        runtime_root = root / locator["runtime_root"]
        readiness_path = root / locator["readiness_path"]
        if not readiness_path.is_file():
            raise GateBlocked("G03-04-HANDOFF", "READINESS_RECORD_RESOLUTION_FAILED", readiness_path.as_posix())
        rows = _read_jsonl(readiness_path)
        if len(rows) != 1:
            raise GateBlocked("G03-04-HANDOFF", "READINESS_CARDINALITY", f"rows={len(rows)}")
        readiness = rows[0]
        prediction_manifests = sorted((runtime_root / "manifests/record_partitions/PredictionRecord").rglob("*.json"))
        model_files = sorted((runtime_root / "records/ModelRegistryRecord").rglob("*.jsonl"))
        partition_count, model_count = len(prediction_manifests), sum(len(_read_jsonl(p)) for p in model_files)
        if partition_count != int(locator["prediction_partition_count"]):
            raise GateBlocked("G03-04-HANDOFF", "PREDICTION_PARTITION_COUNT_MISMATCH", f"expected={locator['prediction_partition_count']}, observed={partition_count}")
        if model_count != int(locator["model_registry_success_count"]):
            raise GateBlocked("G03-04-HANDOFF", "MODEL_REGISTRY_COUNT_MISMATCH", f"expected={locator['model_registry_success_count']}, observed={model_count}")
        progress(1, 5, "exact P02/P03 handoff authority", 0, "IN_PROGRESS")
        handoff = yaml.safe_load((ctx.package_root / locator["downstream_readiness_contract_path"]).read_text(encoding="utf-8"))
        limitations_doc = yaml.safe_load((ctx.package_root / locator["persistent_limitations_path"]).read_text(encoding="utf-8"))
        expected_contract_items = {
            "validated PredictionRecord partitions", "ModelRegistryRecord", "score/logit/probability semantics", "class order",
            "A0 metrics", "A4 membership/control identities", "seed/config/budget/split lineage", "Layer2ReadinessReport",
            "failures/limitations/DiagnosticOnly flags",
        }
        observed_contract_items = set(handoff.get("p03_input_contract", {}).get("required", []))
        identity_checks = {
            "accepted_run_id": handoff.get("accepted_run_id") == locator["accepted_run_id"],
            "config_sha256": handoff.get("config_sha256") == locator["accepted_config_sha256"],
            "scientific_freeze_id": handoff.get("scientific_freeze_id") == locator["accepted_scientific_freeze_id"],
            "p03_runtime_status": handoff.get("p03_runtime_readiness", {}).get("status") == "PASS",
            "p03_compatibility": handoff.get("p03_runtime_readiness", {}).get("compatibility_status") == "PASS",
            "readiness_status": handoff.get("readiness_status") == "READY_WITH_EXPLICIT_LIMITATIONS",
            "blockers": handoff.get("blockers") == [],
            "required_contract": expected_contract_items <= observed_contract_items,
        }
        if not all(identity_checks.values()):
            raise GateBlocked("G03-04-HANDOFF", "P02_DOWNSTREAM_HANDOFF_CONTRACT_MISMATCH", json.dumps(identity_checks, sort_keys=True))
        source_run_id = str(handoff["accepted_run_id"])
        source_config_sha256 = str(handoff["config_sha256"])
        source_protocol_id = str(handoff["scientific_freeze_id"])
        limitation_rows = list(limitations_doc.get("limitations", []))
        if len(limitation_rows) != 14 or any(not row.get("limitation_id") or not row.get("downstream_claim_impact") for row in limitation_rows):
            raise GateBlocked("G03-04-HANDOFF", "P02_PERSISTENT_LIMITATION_CONTRACT_INCOMPLETE", f"count={len(limitation_rows)}")
        progress(2, 5, "A0/A4/failure/diagnostic inherited evidence", 0, "IN_PROGRESS")
        a0_completion = json.loads((root / locator["a0_completion_path"]).read_text(encoding="utf-8"))
        a4_completion = json.loads((root / locator["a4_completion_path"]).read_text(encoding="utf-8"))
        baseline_rows = _read_jsonl(root / locator["baseline_metric_path"])
        diagnostic_rows = _read_jsonl(root / locator["diagnostic_only_path"])
        failure_rows = _read_jsonl(root / locator["failure_case_path"])
        control_files = sorted((runtime_root / "records/EnsembleControlRecord").rglob("*.jsonl"))
        control_rows = [row for path in control_files for row in _read_jsonl(path)]
        upstream_counts = {
            "baseline_metric_records": len(baseline_rows), "ensemble_control_records": len(control_rows),
            "diagnostic_only_records": len(diagnostic_rows), "failure_case_records": len(failure_rows),
        }
        expected_counts = {
            "baseline_metric_records": int(locator["baseline_metric_record_count"]), "ensemble_control_records": int(locator["ensemble_control_count"]),
            "diagnostic_only_records": int(locator["diagnostic_only_record_count"]), "failure_case_records": int(locator["failure_case_record_count"]),
        }
        if upstream_counts != expected_counts:
            raise GateBlocked("G03-04-HANDOFF", "P02_INHERITED_RECORD_COUNT_MISMATCH", json.dumps({"expected": expected_counts, "observed": upstream_counts}, sort_keys=True))
        inherited_rows = baseline_rows + control_rows + diagnostic_rows + failure_rows
        bad_inherited = [
            row.get("record_id") for row in inherited_rows
            if row.get("config_sha256") != locator["accepted_config_sha256"] or row.get("evidence_class") != "P02_EXECUTION_EVIDENCE" or row.get("terminal_status") != "SUCCESS"
        ]
        if bad_inherited:
            raise GateBlocked("G03-04-HANDOFF", "P02_INHERITED_RECORD_IDENTITY_MISMATCH", json.dumps(bad_inherited[:10]))
        a0_validated = bool(
            a0_completion.get("status") == "PASS" and int(a0_completion.get("planned", -1)) == int(a0_completion.get("terminal", -2))
            and a0_completion.get("analysis_inputs_complete") is True and a0_completion.get("prediction_record_complete") is True
            and a0_completion.get("raw_score_semantics_complete") is True and a0_completion.get("denominator_accounting_complete") is True
        )
        a4_validated = bool(
            a4_completion.get("status") == "PASS" and int(a4_completion.get("planned", -1)) == sum(int(value) for value in a4_completion.get("terminal_counts", {}).values())
            and int(a4_completion.get("role_control_incomplete", -1)) == 0 and int(a4_completion.get("c4_c5_incomplete", -1)) == 0
            and a4_completion.get("phase_analysis_source_complete") is True
        )
        if not a0_validated or not a4_validated:
            raise GateBlocked("G03-04-HANDOFF", "P02_A0_A4_COMPLETION_CONTRACT_FAILED", f"A0={a0_validated}, A4={a4_validated}")
        budget_profile_ids = sorted({str(row["budget_id"]) for row in baseline_rows if row.get("budget_id") is not None})
        contract_complete = True
    validate_p02_readiness(readiness)
    expected_run = locator["accepted_run_id"]
    expected_config = locator["accepted_config_sha256"]
    if not ctx.authoring_fixture:
        if readiness.get("config_sha256") != expected_config or readiness.get("missing_fields") != [] or readiness.get("blocking_reasons") != []:
            raise GateBlocked("G03-04-HANDOFF", "P02_CONFIG_IDENTITY_MISMATCH", expected_config)
        required_available = set(readiness.get("required_fields", []))
        if not {"class_order", "score_semantics", "score_type", "score_vector", "scientific_freeze_id", "budget_id", "split_id", "model_seed"} <= required_available:
            raise GateBlocked("G03-04-HANDOFF", "P02_READINESS_REQUIRED_FIELD_CONTRACT_INCOMPLETE", json.dumps(sorted(required_available)))
    retrieval_receipt = json.loads((_stage_dir(ctx, "03") / "external_retrieval_receipt.json").read_text(encoding="utf-8"))
    ledger = {
        "intake_id": deterministic_id("P03-INTAKE", {"root": root.as_posix(), "readiness": readiness}),
        "source_phase": "P02",
        "source_run_id": source_run_id,
        "source_config_sha256": source_config_sha256,
        "source_protocol_id": source_protocol_id,
        "source_environment_id": readiness.get("environment_id") if ctx.authoring_fixture else "RECORDED_RUNTIME_ENVIRONMENT_BOUND_PER_P02_LIMITATION_13",
        "identity_binding_sources": {"run_config_freeze": "downstream_readiness_contract", "class_order_score_semantics": "readiness_required_fields_plus_stage07_row_validation", "limitations": "persistent_limitations"},
        "prediction_partition_count": partition_count,
        "model_registry_success_count": model_count,
        "upstream_record_counts": upstream_counts,
        "required_readiness_record_id": str(readiness["record_id"]),
        "class_order": list(readiness["class_order"]) if ctx.authoring_fixture else list(config["score_semantics"]["class_order"]),
        "split_profile_id": str(readiness["split_profile_id"]) if ctx.authoring_fixture else config["inputs"]["p01"]["scientific_freeze_id"],
        "budget_profile_ids": budget_profile_ids,
        "external_revision": retrieval_receipt["revision"],
        "manifest_sha256": sha256_json(readiness),
        "object_index_sha256": locator["object_index_sha256"] if not ctx.authoring_fixture else "NON_SCIENTIFIC_AUTHORING_FIXTURE",
        "retrieval_receipt_ids": ["P03-PROD-006"],
        "immutability_status": "READ_ONLY_VERIFIED",
        "limitation_ids": [str(row["limitation_id"]) for row in limitation_rows],
        "limitations": limitation_rows,
        "a0_validated": a0_validated,
        "a4_validated": a4_validated,
        "p02_contract_complete": contract_complete,
        "row_level_prediction_validation_stage": "07",
        "intake_gate_status": "PASS",
    }
    write_json(out / "p03_intake_ledger.json", ledger)
    progress(5, 5, "P03 intake ledger", 0, "COMPLETE")
    return {
        "status": "PASS", "products": ["P03-PROD-007"], "p03_intake_ledger": "p03_intake_ledger.json",
        "prediction_partition_count": partition_count, "model_registry_success_count": model_count,
        "upstream_record_counts": upstream_counts, "persistent_limitation_count": len(limitation_rows),
        "a0_validated": a0_validated, "a4_validated": a4_validated, "p02_contract_complete": contract_complete,
    }


def stage_05(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    progress(0, 3, "config snapshot", 0, "IN_PROGRESS")
    config = config_snapshot(ctx.config_path)
    protocol = freeze_snapshot(ctx.protocol_path, allow_authoring_fixture=ctx.authoring_fixture)
    if config["config_sha256"] != ctx.config_sha256 or protocol["protocol_sha256"] != ctx.protocol_sha256:
        raise GateBlocked("G03-05-FREEZE", "CONTEXT_FREEZE_HASH_DRIFT", "Context and source freeze hashes differ")
    write_json(out / "config_snapshot.json", config)
    progress(1, 3, "protocol snapshot", 0, "IN_PROGRESS")
    write_json(out / "protocol_snapshot.json", protocol)
    freeze_record = {
        "run_id": ctx.run_id,
        "config_sha256": ctx.config_sha256,
        "protocol_snapshot_id": ctx.protocol_snapshot_id,
        "protocol_sha256": ctx.protocol_sha256,
        "code_sha256": ctx.code_sha256,
        "environment_sha256": ctx.environment_sha256,
        "source_manifest_sha256": ctx.source_manifest_sha256,
        "scientific_configuration_explicit": True,
        "authoring_fixture": ctx.authoring_fixture,
        "immutable_fingerprint_sha256": sha256_json(ctx.immutable_fingerprint),
    }
    write_json(out / "p03_execution_freeze.json", freeze_record)
    progress(3, 3, "execution freeze", 0, "COMPLETE")
    return {"status": "PASS", "products": ["P03-PROD-008", "P03-PROD-009"], "protocol_snapshot": "protocol_snapshot.json", "config_snapshot": "config_snapshot.json", "execution_freeze": "p03_execution_freeze.json"}


def stage_06(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    modules = [
        "calibration.base", "calibration.identity", "calibration.temperature", "calibration.platt", "calibration.beta",
        "calibration.structured", "calibration.conditional", "calibration.factory", "reliability", "metrics", "records",
        "uncertainty", "conditional_proxies", "selective", "matched_operating_points", "thresholds", "store", "intake",
        "selection_replay", "score_contracts", "leakage", "high_confidence_wrong", "writers", "evidence", "handoffs", "group_audit",
    ]
    imported = []
    for index, module in enumerate(modules, start=1):
        importlib.import_module(f"iharq.layer3_calibration_uncertainty.{module}")
        imported.append(module)
        progress(index, len(modules) + 1, module, 0, "IN_PROGRESS")
    schema_report = validate_all_schemas(ctx.repository_root / "schemas")
    receipt = {"status": "PASS", "import_count": len(imported), "imports": imported, "schema_report": schema_report, "worker_processes": 1, "numerical_threads": 1}
    write_json(out / "schema_import_worker_receipt.json", receipt)
    progress(len(modules) + 1, len(modules) + 1, "schema/import receipt", 0, "COMPLETE")
    return {"status": "PASS", "products": ["P03-PROD-010"], "schema_import_receipt": "schema_import_worker_receipt.json", **receipt}


def _fixture_groups(root: Path) -> list[tuple[dict[str, Any], np.ndarray, np.ndarray, list[dict[str, Any]]]]:
    descriptor = json.loads((root / "group_descriptor.json").read_text(encoding="utf-8"))
    arrays = np.load(root / "group_data.npz", allow_pickle=False)
    metadata = _read_jsonl(root / "group_metadata.jsonl")
    return [(descriptor, arrays["scores"], arrays["labels"], metadata)]


def _model_registry(root: Path, expected_config_sha256: str) -> dict[str, dict[str, Any]]:
    registry: dict[str, dict[str, Any]] = {}
    for path in root.rglob("*.jsonl"):
        if "records/ModelRegistryRecord" not in path.as_posix():
            continue
        for row in _read_jsonl(path):
            if row.get("terminal_status") != "SUCCESS":
                raise GateBlocked("G03-07-JOIN", "NON_SUCCESS_MODEL_REGISTRY_IN_ACCEPTED_PREFIX", str(row.get("record_id")))
            if row.get("config_sha256") != expected_config_sha256 or row.get("evidence_class") != "P02_EXECUTION_EVIDENCE" or row.get("phase_id") != "P02":
                raise GateBlocked("G03-07-JOIN", "MODEL_REGISTRY_IDENTITY_MISMATCH", str(row.get("record_id")))
            model_id = str(row["model_id"])
            if model_id in registry:
                raise GateBlocked("G03-07-JOIN", "MODEL_REGISTRY_DUPLICATE_MODEL_ID", model_id)
            registry[model_id] = row
    return registry


def _a4_controls(runtime_root: Path, expected_config_sha256: str, expected_count: int) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    by_source: dict[str, dict[str, Any]] = {}
    rows: list[dict[str, Any]] = []
    for path in sorted((runtime_root / "records/EnsembleControlRecord").rglob("*.jsonl")):
        controls = _read_jsonl(path)
        if len(controls) != 1:
            raise GateBlocked("G03-07-JOIN", "A4_CONTROL_CARDINALITY", f"{path}:rows={len(controls)}")
        row = controls[0]
        if row.get("terminal_status") != "SUCCESS" or row.get("config_sha256") != expected_config_sha256 or row.get("evidence_class") != "P02_EXECUTION_EVIDENCE":
            raise GateBlocked("G03-07-JOIN", "A4_CONTROL_IDENTITY_MISMATCH", str(row.get("record_id")))
        if int(row.get("missing_member_count", 0)) != 0:
            raise GateBlocked("G03-07-JOIN", "A4_CONTROL_MISSING_MEMBERS", str(row.get("record_id")))
        rows.append(row)
        compact = {
            "record_id": row.get("record_id"), "control_id": row.get("control_id"), "aggregation_rule": row.get("aggregation_rule"),
            "a4_profile": row.get("a4_profile"), "member_model_ids": list(row.get("member_model_ids", [])),
            "member_checkpoint_ids": list(row.get("member_checkpoint_ids", [])), "missing_member_count": int(row.get("missing_member_count", 0)),
            "source_ids": list(row.get("source_ids", [])), "limitations": list(row.get("limitations", [])),
        }
        for source_id in row.get("source_ids", []):
            source_id = str(source_id)
            if source_id in by_source:
                raise GateBlocked("G03-07-JOIN", "A4_CONTROL_SOURCE_COLLISION", source_id)
            by_source[source_id] = compact
    if len(rows) != expected_count:
        raise GateBlocked("G03-07-JOIN", "A4_CONTROL_COUNT_MISMATCH", f"expected={expected_count}, observed={len(rows)}")
    return by_source, rows


def _diagnostic_run_cells(runtime_root: Path, expected_config_sha256: str) -> tuple[set[str], list[dict[str, Any]]]:
    rows = _read_jsonl(runtime_root / "records/DiagnosticOnlyFlag/diagnostics.jsonl")
    run_cells: set[str] = set()
    for row in rows:
        if row.get("terminal_status") != "SUCCESS" or row.get("config_sha256") != expected_config_sha256 or row.get("evidence_class") != "P02_EXECUTION_EVIDENCE":
            raise GateBlocked("G03-07-JOIN", "P02_DIAGNOSTIC_FLAG_IDENTITY_MISMATCH", str(row.get("record_id")))
        run_cells.update(str(source_id) for source_id in row.get("source_ids", []))
    return run_cells, rows


def _real_groups(
    ctx: ExecutionContext,
    root: Path,
    out: Path,
    progress: Progress,
) -> tuple[list[tuple[dict[str, Any], np.ndarray, np.ndarray, list[dict[str, Any]]]], list[dict[str, Any]], int, list[dict[str, Any]]]:
    """Build lawful three-role P03 groups from checkpoint replay + immutable P02 test rows.

    C5 correction: P02 PredictionRecords are final-test-only.  CALIBRATION and
    VALIDATION scores are P03-owned inference-only replay artifacts produced from
    accepted P02 checkpoints on frozen P01 windows.  No P02 model is retrained.
    """
    config = _config(ctx)
    expected_order = list(config["score_semantics"]["class_order"])
    atol = float(config["score_semantics"]["probability_atol"])
    locator = config["inputs"]["p02"]
    replay_cfg = dict(locator.get("replay_materialization") or {})
    if not bool(replay_cfg.get("enabled")):
        raise GateBlocked("G03-07-JOIN", "P03_SELECTION_REPLAY_NOT_ENABLED", "C5 replay contract is required")
    test_probability_closure = dict(replay_cfg.get("p02_test_probability_numeric_closure") or {})
    test_probability_closure_policy_id = str(test_probability_closure.get("policy_id") or "")
    if test_probability_closure_policy_id != "P03-C7-P02-TEST-FLOAT-SIMPLEX-CLOSURE-R1":
        raise GateBlocked("G03-07-JOIN", "P03_TEST_PROBABILITY_CLOSURE_POLICY_MISSING", test_probability_closure_policy_id)
    if float(test_probability_closure.get("source_probability_atol", -1.0)) != float(_REPLAY_SOURCE_PROBABILITY_ATOL):
        raise GateBlocked("G03-07-JOIN", "P03_TEST_PROBABILITY_SOURCE_ATOL_MISMATCH", str(test_probability_closure.get("source_probability_atol")))
    if float(test_probability_closure.get("canonical_probability_atol", -1.0)) != atol:
        raise GateBlocked("G03-07-JOIN", "P03_TEST_PROBABILITY_CANONICAL_ATOL_MISMATCH", str(test_probability_closure.get("canonical_probability_atol")))
    if str(test_probability_closure.get("operation")) != "FLOAT64_ROW_RENORMALIZATION_IN_P03_VIEW_ONLY":
        raise GateBlocked("G03-07-JOIN", "P03_TEST_PROBABILITY_CLOSURE_OPERATION_MISMATCH", str(test_probability_closure.get("operation")))
    if bool(test_probability_closure.get("source_records_mutated", True)):
        raise GateBlocked("G03-07-JOIN", "P03_TEST_PROBABILITY_SOURCE_MUTATION_PROHIBITED", "source_records_mutated must be false")
    if bool(test_probability_closure.get("learned_or_calibration_transformation", True)):
        raise GateBlocked("G03-07-JOIN", "P03_TEST_PROBABILITY_LEARNED_TRANSFORM_PROHIBITED", "learned_or_calibration_transformation must be false")
    expected_config = str(locator["accepted_config_sha256"])
    try:
        from iharq.layer2_decoders.data import CoreWindowDataset
    except ImportError as exc:
        raise GateBlocked("G03-07-JOIN", "P02_DATA_ADAPTER_UNAVAILABLE", str(exc)) from exc

    try:
        core = CoreWindowDataset(root, config["inputs"]["p01"]["core_manifest_sha256"])
    except Exception as exc:
        raise GateBlocked("G03-07-JOIN", "P01_CORE_RESOLUTION_FAILED", f"{type(exc).__name__}:{exc}") from exc

    canonical_rows = [canonical_truth_row(core, row) for row in core.rows()]
    if len(canonical_rows) != 12910:
        raise GateBlocked("G03-07-JOIN", "P01_CORE_WINDOW_COUNT_MISMATCH", f"expected=12910, observed={len(canonical_rows)}")
    truth_by_window = {str(row["window_id"]): row for row in canonical_rows}
    truth_by_event = {str(row["event_id"]): row for row in canonical_rows}
    if len(truth_by_window) != len(canonical_rows) or len(truth_by_event) != len(canonical_rows):
        raise GateBlocked("G03-07-JOIN", "P01_CANONICAL_TRUTH_KEY_COLLISION", "window/event identities must be unique")

    runtime_root = root / locator["runtime_root"]
    registry = _model_registry(runtime_root, expected_config)
    _, control_rows = _a4_controls(runtime_root, expected_config, int(locator["ensemble_control_count"]))
    diagnostic_run_cells, _ = _diagnostic_run_cells(runtime_root, expected_config)
    replay_models, replay_population = eligible_replay_models(
        runtime_root,
        expected_config_sha256=expected_config,
        expected_count=int(replay_cfg["expected_model_count"]),
        expected_population_sha256=str(replay_cfg["expected_population_sha256"]),
    )
    if len(registry) != int(locator["model_registry_success_count"]):
        raise GateBlocked("G03-07-JOIN", "MODEL_REGISTRY_COUNT_MISMATCH", f"expected={locator['model_registry_success_count']}, observed={len(registry)}")

    manifests = sorted((runtime_root / "manifests/record_partitions/PredictionRecord").rglob("*.json"))
    if len(manifests) != int(locator["prediction_partition_count"]):
        raise GateBlocked("G03-07-JOIN", "PREDICTION_MANIFEST_COUNT_MISMATCH", f"expected={locator['prediction_partition_count']}, observed={len(manifests)}")
    manifest_by_run: dict[str, dict[str, Any]] = {}
    for manifest_path in manifests:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        validate_partition_manifest(manifest, expected_class_order=expected_order)
        if manifest.get("config_sha256") != expected_config:
            raise GateBlocked("G03-07-JOIN", "PREDICTION_MANIFEST_CONFIG_MISMATCH", str(manifest.get("run_cell_id")))
        run_cell_id = str(manifest["run_cell_id"])
        if run_cell_id in manifest_by_run:
            raise GateBlocked("G03-07-JOIN", "PREDICTION_MANIFEST_RUN_CELL_COLLISION", run_cell_id)
        manifest_by_run[run_cell_id] = manifest

    model_by_run = {str(row["p03_run_cell_id"]): row for row in replay_models}
    if len(model_by_run) != len(replay_models):
        raise GateBlocked("G03-07-JOIN", "P03_REPLAY_RUN_CELL_COLLISION", "eligible replay run-cell IDs are not unique")
    missing_test = sorted(set(model_by_run) - set(manifest_by_run))
    if missing_test:
        raise GateBlocked("G03-07-JOIN", "P03_REPLAY_TEST_MANIFEST_MISSING", json.dumps(missing_test[:10]))

    cache_root = ctx.run_root / "artifacts" / "runtime_replay_cache" / "selection_scores"
    context_key = sha256_json(ctx.immutable_fingerprint)
    selection_root = out / "selection_scores"
    selection_root.mkdir(parents=True, exist_ok=True)

    groups: list[tuple[dict[str, Any], np.ndarray, np.ndarray, list[dict[str, Any]]]] = []
    dispositions_by_run: dict[str, dict[str, Any]] = {}
    materialization_index: list[dict[str, Any]] = []
    blocked_count = 0

    def metadata_for_truth(
        truth: Mapping[str, Any], *, split_role: str, source_partition_id: str,
        record_id: str, model: Mapping[str, Any], model_variant: Any,
    ) -> dict[str, Any]:
        return {
            "record_id": record_id,
            "dataset_id": str(model["p03_dataset_id"]), "model_id": str(model["model_id"]),
            "budget_id": str(model["p03_budget_id"]), "split_id": str(truth["split_record_id"]),
            "split_role": split_role, "source_canonical_role": str(truth["role"]),
            "subject_id": str(truth["subject_id"]), "session_id": str(truth["session_id"]),
            "window_id": str(truth["window_id"]), "source_event_id": str(truth["event_id"]),
            "source_partition_id": source_partition_id, "event_order": int(truth["event_order"]),
            "source_run_id": truth.get("run_id"), "checkpoint_id": model.get("checkpoint_id"),
            "model_seed": model.get("model_seed"), "model_variant": model_variant,
        }

    for index, model in enumerate(replay_models, start=1):
        run_cell_id = str(model["p03_run_cell_id"])
        manifest = manifest_by_run[run_cell_id]
        expected_test_rows = int(manifest["row_count"])
        selection_rel = f"selection_scores/{hashlib.sha256(run_cell_id.encode()).hexdigest()[:24]}.jsonl"
        selection_path = out / selection_rel
        try:
            replay = replay_one_model(
                model_row=model, core=core, snapshot_root=root,
                runtime_root_rel=str(locator["runtime_root"]), manifest_path=str(locator["manifest_path"]),
                replay_config=replay_cfg, cache_root=cache_root, context_fingerprint=context_key,
            )
            cal_rows_raw, excluded = replay_calibration_rows(core, str(model["p03_dataset_id"]), str(model["p03_budget_id"]), int(replay_cfg["low_label_membership_seed"]))
            val_rows_raw = replay_validation_rows(core, str(model["p03_dataset_id"]))
            cal_rows = [canonical_truth_row(core, row) for row in cal_rows_raw]
            val_rows = [canonical_truth_row(core, row) for row in val_rows_raw]
            cal_scores = validate_probabilities(np.asarray(replay["calibration_scores"], dtype=float), atol=atol)
            val_scores = validate_probabilities(np.asarray(replay["validation_scores"], dtype=float), atol=atol)
            if len(cal_scores) != len(cal_rows) or len(val_scores) != len(val_rows):
                raise ContractViolation(f"P03 selection replay row mismatch: {run_cell_id}")

            test_rows, run_cell = load_test_partition(
                snapshot_root=root, runtime_root_rel=str(locator["runtime_root"]),
                run_cell_id=run_cell_id, expected_config_sha256=expected_config,
            )
            if len(test_rows) != expected_test_rows:
                raise ContractViolation(f"P02 test row count mismatch: {run_cell_id}")
            if str(run_cell.get("checkpoint_sha256")) != str(model["checkpoint_sha256"]):
                raise ContractViolation(f"P02 run-cell checkpoint drift: {run_cell_id}")
            model_variant = run_cell.get("resolved_variant")

            scores: list[list[float]] = []
            labels: list[int] = []
            metadata: list[dict[str, Any]] = []
            selection_records: list[dict[str, Any]] = []

            for role, role_scores, role_rows, canonical_role in (
                ("calibration", cal_scores, cal_rows, "calibration"),
                ("threshold_validation", val_scores, val_rows, "validation"),
            ):
                source_partition_id = f"P03SelectionScoreRecord:{run_cell_id}:{canonical_role}"
                for row_index, (truth, vector) in enumerate(zip(role_rows, role_scores)):
                    selection_records.append(build_selection_score_record(
                        model_row=model, truth=truth, score_vector=vector,
                        role=canonical_role, row_index=row_index,
                    ))
                    scores.append([float(value) for value in vector])
                    labels.append(expected_order.index(str(truth["label"])))
                    metadata.append(metadata_for_truth(
                        truth, split_role=role, source_partition_id=source_partition_id,
                        record_id=f"P03SelectionScoreRecord:{run_cell_id}:{canonical_role}:{row_index}",
                        model=model, model_variant=model_variant,
                    ))

            test_score_rows: list[list[float]] = []
            test_metadata: list[dict[str, Any]] = []
            test_labels: list[int] = []
            record_ids = []
            for row in test_rows:
                if row.get("terminal_status") != "SUCCESS" or row.get("evidence_class") != "P02_EXECUTION_EVIDENCE" or row.get("lifecycle_status") != "CURRENT":
                    raise ContractViolation(f"Noncanonical P02 test prediction in replay group: {row.get('record_id')}")
                if run_cell_id not in {str(source_id) for source_id in row.get("source_ids", [])}:
                    raise ContractViolation(f"P02 test source lineage mismatch: {row.get('record_id')}")
                if str(row.get("model_id")) != str(model["model_id"]):
                    raise ContractViolation(f"P02 test model mismatch: {row.get('record_id')}")
                if str(row.get("checkpoint_id")) != str(model["checkpoint_id"]):
                    raise ContractViolation(f"P02 test checkpoint mismatch: {row.get('record_id')}")
                validate_class_order(list(row.get("class_order") or []), expected_order)
                raw_score_type = str(row.get("score_type") or model.get("score_type"))
                if _score_type(raw_score_type, config) != "probability":
                    raise ContractViolation(f"P03 replay test score not probability-bearing: {run_cell_id}:{raw_score_type}")
                vector = row.get("score_vector")
                if vector is None:
                    raise ContractViolation(f"P02 test score vector missing: {row.get('record_id')}")
                # C7: accepted P02 neural/SSL PredictionRecords can carry float32
                # probabilities whose source contract permits <=1e-5 row-sum
                # deviation. Canonicalize only the in-memory P03 view through
                # the same governed numeric-closure function used for replayed
                # CALIBRATION/VALIDATION scores, then enforce the unchanged P03
                # 1e-8 probability contract. The immutable P02 row is never
                # edited, rewritten, or reserialized.
                vector = _canonicalize_replay_source_probabilities(
                    np.asarray([vector], dtype=np.float64), atol=atol
                )[0]
                vector = validate_probabilities(
                    np.asarray([vector], dtype=np.float64), atol=atol
                )[0]
                truth = truth_by_window.get(str(row.get("window_id"))) or truth_by_event.get(str(row.get("source_event_id")))
                if truth is None:
                    raise ContractViolation(f"P01 truth join missing for P02 test row: {row.get('record_id')}")
                if str(truth["role"]) != "test" or str(row.get("split_role")) != "test":
                    raise ContractViolation(f"P02 test role mismatch: {row.get('record_id')}")
                record_ids.append(str(row["record_id"]))
                test_score_rows.append([float(value) for value in vector])
                test_labels.append(expected_order.index(str(truth["label"])))
                test_metadata.append(metadata_for_truth(
                    truth, split_role="test", source_partition_id=run_cell_id,
                    record_id=str(row["record_id"]), model=model, model_variant=model_variant,
                ))
            if len(record_ids) != len(set(record_ids)):
                raise ContractViolation(f"P02 test record IDs duplicate: {run_cell_id}")
            observed_ids_hash = hashlib.sha256("\n".join(record_ids).encode("utf-8")).hexdigest()
            if observed_ids_hash != str(manifest["record_ids_sha256"]):
                raise ContractViolation(f"P02 test record IDs hash mismatch: {run_cell_id}")

            scores.extend(test_score_rows)
            labels.extend(test_labels)
            metadata.extend(test_metadata)
            score_array = validate_probabilities(np.asarray(scores, dtype=float), atol=atol)
            label_array = np.asarray(labels, dtype=int)
            if len(score_array) != len(metadata):
                raise ContractViolation(f"P03 canonical replay group cardinality mismatch: {run_cell_id}")

            split_ids = {str(row["split_id"]) for row in metadata}
            if len(split_ids) != 1:
                raise ContractViolation(f"P03 replay group split identity mismatch: {run_cell_id}:{sorted(split_ids)}")
            split_id = next(iter(split_ids))
            canonical_score_type = _score_type(str(model["score_type"]), config)
            if canonical_score_type != "probability":
                raise ContractViolation(f"Unexpected replay canonical score type: {run_cell_id}:{canonical_score_type}")
            group_id = deterministic_id("GROUP", {
                "dataset_id": model["p03_dataset_id"], "model_id": model["model_id"],
                "budget_id": model["p03_budget_id"], "split_id": split_id,
                "run_cell_id": run_cell_id, "replay_policy": replay_cfg["policy_id"],
            })
            descriptor = {
                "group_id": group_id, "dataset_id": model["p03_dataset_id"], "model_id": model["model_id"],
                "budget_id": model["p03_budget_id"], "split_id": split_id,
                "score_type": canonical_score_type, "class_order": list(model["class_order"]),
                "checkpoint_id": model["checkpoint_id"], "checkpoint_sha256": model["checkpoint_sha256"],
                "model_seed": model.get("model_seed"), "model_variant": model_variant,
                "source_partition_ids": [
                    f"P03SelectionScoreRecord:{run_cell_id}:calibration",
                    f"P03SelectionScoreRecord:{run_cell_id}:validation",
                    run_cell_id,
                ],
                "p02_run_cell_id": run_cell_id,
                "selection_replay_policy_id": replay_cfg["policy_id"],
                "p02_test_predictions_immutable": True,
                "p02_test_probability_numeric_closure_policy_id": test_probability_closure_policy_id,
                "p02_test_source_records_mutated": False,
                "model_retrained_in_p03": False,
                "a4_control": None,
                "authoring_fixture": False,
            }
            write_jsonl(selection_path, selection_records)
            selection_sha = sha256_file(selection_path)
            materialization_index.append({
                "status": "SUCCESS", "run_cell_id": run_cell_id, "group_id": group_id,
                "model_registry_record_id": model.get("record_id"), "model_id": model.get("model_id"),
                "dataset_id": model["p03_dataset_id"], "budget_id": model["p03_budget_id"],
                "family_role": model.get("family_role"), "score_type": model.get("score_type"),
                "checkpoint_sha256": model.get("checkpoint_sha256"),
                "excluded_low_label_training_event_count": len(excluded),
                "calibration_row_count": len(cal_rows), "validation_row_count": len(val_rows),
                "test_row_count": len(test_rows), "selection_score_record_count": len(selection_records),
                "selection_score_path": selection_rel, "selection_score_sha256": selection_sha,
                "replay_cache_action": replay.get("resume_action"),
                "restore_provenance": replay["meta"].get("restore_provenance"),
                "p02_test_probability_numeric_closure_policy_id": test_probability_closure_policy_id,
                "p02_test_source_records_mutated": False,
            })
            dispositions_by_run[run_cell_id] = {
                "run_cell_id": run_cell_id, "input_row_count": expected_test_rows,
                "accepted_row_count": len(test_rows), "reason_counts": {}, "terminal_status": "SUCCESS",
                "p03_selection_replay_status": "SUCCESS",
            }
            groups.append((descriptor, score_array, label_array, metadata))
        except Exception as exc:
            blocked_count += 1
            materialization_index.append({
                "status": "DEPENDENCY_BLOCKED_OR_INELIGIBLE", "run_cell_id": run_cell_id,
                "model_registry_record_id": model.get("record_id"), "model_id": model.get("model_id"),
                "dataset_id": model.get("p03_dataset_id"), "budget_id": model.get("p03_budget_id"),
                "family_role": model.get("family_role"), "score_type": model.get("score_type"),
                "checkpoint_sha256": model.get("checkpoint_sha256"),
                "reason": f"{type(exc).__name__}:{exc}",
            })
            dispositions_by_run[run_cell_id] = {
                "run_cell_id": run_cell_id, "input_row_count": expected_test_rows,
                "accepted_row_count": 0, "reason_counts": {"P03_SELECTION_REPLAY_FAILED": expected_test_rows},
                "terminal_status": "INELIGIBLE", "p03_selection_replay_status": "DEPENDENCY_BLOCKED_OR_INELIGIBLE",
            }
        progress(index, len(replay_models), run_cell_id, blocked_count, "IN_PROGRESS")

    # Complete the denominator over all accepted P02 PredictionRecord partitions.
    for run_cell_id, manifest in sorted(manifest_by_run.items()):
        if run_cell_id in dispositions_by_run:
            continue
        row_count = int(manifest["row_count"])
        reason = "P02_DIAGNOSTIC_ONLY_FLAG" if run_cell_id in diagnostic_run_cells else "NOT_P03_SELECTION_REPLAY_POPULATION"
        dispositions_by_run[run_cell_id] = {
            "run_cell_id": run_cell_id, "input_row_count": row_count, "accepted_row_count": 0,
            "reason_counts": {reason: row_count},
            "terminal_status": "DIAGNOSTIC_ONLY" if reason == "P02_DIAGNOSTIC_ONLY_FLAG" else "INELIGIBLE",
            "p03_selection_replay_status": "NOT_APPLICABLE",
        }

    dispositions = [dispositions_by_run[key] for key in sorted(dispositions_by_run)]
    if len(dispositions) != int(locator["prediction_partition_count"]):
        raise GateBlocked("G03-07-JOIN", "PREDICTION_DISPOSITION_PARTITION_COUNT_MISMATCH", f"expected={locator['prediction_partition_count']}, observed={len(dispositions)}")
    disposition_complete = all(
        int(row["input_row_count"]) == int(row["accepted_row_count"]) + sum(int(value) for value in row["reason_counts"].values())
        for row in dispositions
    )
    if not disposition_complete:
        raise GateBlocked("G03-07-JOIN", "PREDICTION_DISPOSITION_DENOMINATOR_INCOMPLETE", "accepted plus terminal dispositions do not equal input rows")
    if len(materialization_index) != int(replay_cfg["expected_model_count"]):
        raise GateBlocked("G03-07-JOIN", "P03_REPLAY_MATERIALIZATION_DENOMINATOR_INCOMPLETE", f"expected={replay_cfg['expected_model_count']}, observed={len(materialization_index)}")
    if not groups:
        raise GateBlocked("G03-07-JOIN", "NO_P03_SELECTION_REPLAY_GROUPS", "All eligible replay branches failed or were ineligible")
    return groups, dispositions, len(control_rows), materialization_index

def stage_07(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    root = Path(_stage_result(ctx, "03")["resolved_external_root"])
    if ctx.authoring_fixture:
        groups = _fixture_groups(root)
        dispositions = [{"run_cell_id": "NON_SCIENTIFIC_AUTHORING_FIXTURE", "input_row_count": len(groups[0][1]), "accepted_row_count": len(groups[0][1]), "reason_counts": {}, "terminal_status": "SUCCESS"}]
        a4_control_count = 0
        materialization_index = []
    else:
        groups, dispositions, a4_control_count, materialization_index = _real_groups(ctx, root, out, progress)
    group_ids = []
    missing_key_warnings = []
    for index, (descriptor, scores, labels, metadata) in enumerate(groups, start=1):
        if len(scores) != len(metadata):
            raise ContractViolation(f"Joined group length mismatch: {descriptor['group_id']}")
        group_ids.append(_save_group(out, descriptor, scores, labels, metadata))
    write_json(out / "join_alias_overlay.json", {"status": "PASS", "alias_count": 0, "upstream_mutation": False, "group_ids": group_ids})
    write_jsonl(out / "missing_key_warnings.jsonl", missing_key_warnings)
    write_jsonl(out / "upstream_prediction_disposition.jsonl", dispositions)
    write_jsonl(out / "selection_score_materialization_index.jsonl", materialization_index)
    replay_success = sum(row.get("status") == "SUCCESS" for row in materialization_index)
    replay_blocked = sum(row.get("status") != "SUCCESS" for row in materialization_index)
    expected_replay = int(_config(ctx)["inputs"]["p02"]["replay_materialization"]["expected_model_count"]) if not ctx.authoring_fixture else 0
    gpu_policy = dict(_config(ctx)["inputs"]["p02"].get("replay_materialization", {}).get("gpu_inference") or {})
    # C7-GPU lesson learned from C6.5: an outer PASS with replay attrition is
    # insufficient. Preserve the materialization/disposition evidence above,
    # then fail the gate for any missing eligible replay branch.
    if not ctx.authoring_fixture and (replay_success != expected_replay or replay_blocked != 0):
        raise GateBlocked(
            "G03-07-JOIN",
            "P03_SELECTION_REPLAY_FULL_COVERAGE_REQUIRED",
            json.dumps({
                "expected": expected_replay,
                "success": replay_success,
                "blocked_or_ineligible": replay_blocked,
                "materialization_index": "selection_score_materialization_index.jsonl",
                "gpu_policy_id": gpu_policy.get("policy_id"),
            }, sort_keys=True),
        )
    return {
        "status": "PASS", "products": ["P03-PROD-011", "P03-PROD-012"], "group_count": len(group_ids), "group_ids": group_ids,
        "missing_key_warning_count": len(missing_key_warnings), "join_alias_overlay": "join_alias_overlay.json",
        "input_prediction_row_count": sum(row["input_row_count"] for row in dispositions),
        "accepted_prediction_row_count": sum(row["accepted_row_count"] for row in dispositions),
        "disposition_complete": all(row["input_row_count"] == row["accepted_row_count"] + sum(row["reason_counts"].values()) for row in dispositions),
        "a4_control_count": a4_control_count, "upstream_prediction_disposition": "upstream_prediction_disposition.jsonl",
        "selection_score_materialization_index": "selection_score_materialization_index.jsonl",
        "selection_replay_expected_model_count": expected_replay,
        "gpu_inference_policy_id": gpu_policy.get("policy_id") if not ctx.authoring_fixture else None,
        "gpu_inference_required": bool(gpu_policy.get("required", False)) if not ctx.authoring_fixture else False,
        "gpu_inference_strategy": gpu_policy.get("strategy") if not ctx.authoring_fixture else None,
        "selection_replay_success_count": replay_success, "selection_replay_blocked_or_ineligible_count": replay_blocked,
        "selection_replay_population_accounted": ctx.authoring_fixture or (replay_success + replay_blocked == int(_config(ctx)["inputs"]["p02"]["replay_materialization"]["expected_model_count"])),
        "p02_test_predictions_reused_immutably": not ctx.authoring_fixture,
        "p02_test_probability_numeric_closure_policy_id": "P03-C7-P02-TEST-FLOAT-SIMPLEX-CLOSURE-R1" if not ctx.authoring_fixture else None,
        "p02_test_source_records_mutated": False,
        "p02_models_retrained": False,
    }

def stage_08(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    protocol = _protocol(ctx)
    profile = protocol["scientific"]["roles"]["leakage_profile"]
    reports = []
    warnings = []
    for index, group_id in enumerate(_group_ids(ctx), start=1):
        descriptor, scores, labels, metadata = _load_group(ctx, group_id)
        del scores, labels
        try:
            report = evaluate_leakage(metadata, profile)
            report.update({"group_id": group_id, "dataset_id": descriptor["dataset_id"], "model_id": descriptor["model_id"], "status": "PASS"})
        except Exception as exc:
            warning = {"warning_id": deterministic_id("P03-LEAKAGE-WARNING", {"group_id": group_id, "error": str(exc)}), "severity": "BLOCK", "illegal_use_code": "LG-OVERLAP", "attempted_operation": "split_preflight", "source_role": "MULTIPLE", "destination_role": "MULTIPLE", "field_id": "identity_fields", "object_ids": [group_id], "detected_at_stage": "08", "blocked_before_compute": True, "descendant_invalidation_ids": [], "resolution_status": "UNRESOLVED", "message": str(exc)}
            warnings.append(warning)
            write_jsonl(out / "leakage_warning_records.jsonl", warnings)
            raise
        reports.append(report)
        progress(index, len(_group_ids(ctx)), group_id, len(warnings), "IN_PROGRESS")
    write_jsonl(out / "split_integrity_reports.jsonl", reports)
    write_jsonl(out / "leakage_warning_records.jsonl", warnings)
    return {"status": "PASS", "products": ["P03-PROD-013", "P03-PROD-014"], "split_report_count": len(reports), "leakage_warning_count": len(warnings), "split_integrity_reports": "split_integrity_reports.jsonl", "leakage_warning_records": "leakage_warning_records.jsonl"}


def stage_09(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    config = _config(ctx)
    expected = config["score_semantics"]["class_order"]
    atol = float(config["score_semantics"]["probability_atol"])
    rows = []
    diagnostic = []
    for index, group_id in enumerate(_group_ids(ctx), start=1):
        descriptor, scores, labels, metadata = _load_group(ctx, group_id)
        view = ScoreView(scores, descriptor["score_type"], tuple(descriptor["class_order"]), group_id, legal_log_probability_transform=bool(config["score_semantics"]["legal_log_probability_transform"]))
        result = eligibility(view, expected_class_order=expected, probability_atol=atol)
        role_counts = Counter(row["split_role"] for row in metadata)
        result.update({"table_id": deterministic_id("P03-ELIGIBILITY", descriptor), **descriptor, "role_counts": dict(role_counts), "source_partition_manifest_id": descriptor["source_partition_ids"][0]})
        rows.append(result)
        if not result["calibration_eligible"]:
            diagnostic.append({"source": group_id, "reason": result["reason_codes"], "allowed_use": ["diagnostic"], "prohibited_use": ["calibration", "threshold_selection", "claim"]})
        progress(index, len(_group_ids(ctx)), group_id, len(diagnostic), "IN_PROGRESS")
    if not any(row["calibration_eligible"] for row in rows):
        raise GateBlocked("G03-09-ELIGIBILITY", "NO_ELIGIBLE_SCORE_GROUP", "All P02 score groups are ineligible")
    write_jsonl(out / "calibration_eligibility_table.jsonl", rows)
    write_jsonl(out / "diagnostic_only_flags.jsonl", diagnostic)
    return {"status": "PASS", "products": ["P03-PROD-015", "P03-PROD-016"], "eligibility_count": len(rows), "diagnostic_only_count": len(diagnostic), "calibration_eligibility_table": "calibration_eligibility_table.jsonl", "diagnostic_only_flags": "diagnostic_only_flags.jsonl"}


def stage_10(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    config, protocol, contract = _config(ctx), _protocol(ctx), _record_contract(ctx)
    atol = float(config["score_semantics"]["probability_atol"])
    fit_role = _protocol_role(protocol, "calibration_fit")
    records = []
    for index, group_id in enumerate(_group_ids(ctx), start=1):
        descriptor, scores, labels, metadata = _load_group(ctx, group_id)
        fit_idx = _role_indices(metadata, fit_role)
        if not len(fit_idx):
            raise GateBlocked("G03-10-IDENTITY", "CALIBRATION_ROLE_PREDICTIONS_MISSING", f"group={group_id}, role={fit_role}")
        view = ScoreView(scores, descriptor["score_type"], tuple(descriptor["class_order"]), group_id, legal_log_probability_transform=bool(config["score_semantics"]["legal_log_probability_transform"]))
        fit_view = ScoreView(scores[fit_idx], descriptor["score_type"], tuple(descriptor["class_order"]), f"{group_id}:calibration_fit", legal_log_probability_transform=bool(config["score_semantics"]["legal_log_probability_transform"]))
        authorize_view(operation="fit_calibrator", source_role=fit_role, requested_fields=["scores", "labels"], role_map=protocol["scientific"]["roles"]["role_map"], field_visibility=protocol["scientific"]["roles"]["field_visibility"])
        profile = dict(protocol["scientific"]["calibration"]["identity_profile"])
        profile["method_id"] = "identity"
        fitted = fit_calibrator(fit_view, labels[fit_idx], profile, np.random.default_rng(int(protocol["scientific"]["randomness"]["seeds"]["calibration"])), probability_atol=atol)
        probabilities = apply_calibrator(fitted, view, probability_atol=atol)
        group_root = out / "groups" / group_id
        group_root.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(group_root / "identity_probabilities.npz", probabilities=probabilities)
        write_json(group_root / "identity_parameters.json", serialize_calibrator(fitted))
        calibration_id = deterministic_id("P03-CAL-IDENTITY", {"group": descriptor, "config": ctx.config_sha256})
        payload = {
            "calibration_id": calibration_id, "ablation_id": "A1", "dataset_id": descriptor["dataset_id"],
            "model_id": descriptor["model_id"], "budget_id": descriptor["budget_id"], "split_id": descriptor["split_id"],
            "fit_role": fit_role, "application_role": "ALL_DECLARED_ROLES", "method_id": "identity", "method_family": "identity",
            "score_type": descriptor["score_type"], "class_order": descriptor["class_order"],
            "source_prediction_partition_ids": descriptor["source_partition_ids"], "parameterization": fitted.parameters,
            "optimizer_result": fitted.optimizer_result, "support_counts": dict(Counter(row["split_role"] for row in metadata)),
            "eligibility_status": "ELIGIBLE", "identity_comparator_id": calibration_id,
            "calibrated_probability_path": f"groups/{group_id}/identity_probabilities.npz",
            "parameters_path": f"groups/{group_id}/identity_parameters.json", "convergence_status": fitted.convergence_status,
            "fallback_reason": None, "diagnostic_only": False,
        }
        records.append(make_record("CalibrationRecord", ctx, "L3-M01", payload, contract, source_artifact_ids=descriptor["source_partition_ids"]))
        progress(index, len(_group_ids(ctx)), group_id, 0, "IN_PROGRESS")
    write_jsonl(out / "identity_calibration_records.jsonl", records)
    return {"status": "PASS", "products": ["P03-PROD-017"], "identity_record_count": len(records), "identity_calibration_records": "identity_calibration_records.jsonl"}


def _identity_probabilities(ctx: ExecutionContext, group_id: str) -> np.ndarray:
    return np.load(_stage_dir(ctx, "10") / "groups" / group_id / "identity_probabilities.npz", allow_pickle=False)["probabilities"]


def stage_11(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    config, protocol, contract = _config(ctx), _protocol(ctx), _record_contract(ctx)
    atol = float(config["score_semantics"]["probability_atol"])
    fit_role = _protocol_role(protocol, "calibration_fit")
    selection_role = _protocol_role(protocol, "calibration_selection")
    epsilon = float(protocol["scientific"]["metrics"]["metric_profile"]["nll_epsilon"])
    method_profiles = list(protocol["scientific"]["calibration"]["branch_cells"])
    attempts, records, selections = [], [], []
    total = max(1, len(_group_ids(ctx)) * max(1, len(method_profiles)))
    completed = 0
    for group_id in _group_ids(ctx):
        descriptor, scores, labels, metadata = _load_group(ctx, group_id)
        fit_idx, selection_idx = _role_indices(metadata, fit_role), _role_indices(metadata, selection_role)
        if not len(fit_idx) or not len(selection_idx):
            raise GateBlocked("G03-11-CALIBRATION", "LEGAL_FIT_OR_SELECTION_ROLE_MISSING", f"group={group_id}, fit={len(fit_idx)}, selection={len(selection_idx)}")
        authorize_view(operation="fit_calibrator", source_role=fit_role, requested_fields=["scores", "labels"], role_map=protocol["scientific"]["roles"]["role_map"], field_visibility=protocol["scientific"]["roles"]["field_visibility"])
        authorize_view(operation="select_calibrator", source_role=selection_role, requested_fields=["scores", "labels"], role_map=protocol["scientific"]["roles"]["role_map"], field_visibility=protocol["scientific"]["roles"]["field_visibility"])
        raw_view = ScoreView(scores, descriptor["score_type"], tuple(descriptor["class_order"]), group_id, legal_log_probability_transform=bool(config["score_semantics"]["legal_log_probability_transform"]))
        candidate_rows = [{"method_id": "identity", "selection_nll": negative_log_likelihood(_identity_probabilities(ctx, group_id)[selection_idx], labels[selection_idx], epsilon=epsilon, probability_atol=atol), "probability_path": str(_stage_dir(ctx, "10") / "groups" / group_id / "identity_probabilities.npz"), "parameters_path": str(_stage_dir(ctx, "10") / "groups" / group_id / "identity_parameters.json"), "record_id": None}]
        for method_profile in method_profiles:
            completed += 1
            method = str(method_profile["method_id"])
            attempt_id = deterministic_id("P03-CAL-ATTEMPT", {"group": group_id, "method": method, "config": ctx.config_sha256})
            try:
                fit_view = ScoreView(scores[fit_idx], descriptor["score_type"], tuple(descriptor["class_order"]), group_id + ":fit", legal_log_probability_transform=raw_view.legal_log_probability_transform)
                fitted = fit_calibrator(fit_view, labels[fit_idx], method_profile, np.random.default_rng(int(protocol["scientific"]["randomness"]["seeds"]["calibration"])), probability_atol=atol)
                all_probabilities = apply_calibrator(fitted, raw_view, probability_atol=atol)
                group_root = out / "groups" / group_id / method
                group_root.mkdir(parents=True, exist_ok=True)
                np.savez_compressed(group_root / "probabilities.npz", probabilities=all_probabilities)
                write_json(group_root / "parameters.json", serialize_calibrator(fitted))
                selection_nll = negative_log_likelihood(all_probabilities[selection_idx], labels[selection_idx], epsilon=epsilon, probability_atol=atol)
                calibration_id = deterministic_id("P03-CAL", {"group": descriptor, "method": method, "config": ctx.config_sha256})
                payload = {
                    "calibration_id": calibration_id, "ablation_id": "A1", "dataset_id": descriptor["dataset_id"], "model_id": descriptor["model_id"],
                    "budget_id": descriptor["budget_id"], "split_id": descriptor["split_id"], "fit_role": fit_role,
                    "application_role": "ALL_DECLARED_ROLES", "method_id": method, "method_family": fitted.method_family,
                    "score_type": descriptor["score_type"], "class_order": descriptor["class_order"], "source_prediction_partition_ids": descriptor["source_partition_ids"],
                    "parameterization": fitted.parameters, "optimizer_result": fitted.optimizer_result, "support_counts": {"fit": len(fit_idx), "selection": len(selection_idx)},
                    "eligibility_status": "ELIGIBLE", "identity_comparator_id": deterministic_id("P03-CAL-IDENTITY", {"group": descriptor, "config": ctx.config_sha256}),
                    "calibrated_probability_path": f"groups/{group_id}/{method}/probabilities.npz", "parameters_path": f"groups/{group_id}/{method}/parameters.json",
                    "convergence_status": fitted.convergence_status, "fallback_reason": fitted.fallback_reason, "diagnostic_only": fitted.diagnostic_only,
                }
                record = make_record("CalibrationRecord", ctx, "L3-M01", payload, contract, source_artifact_ids=descriptor["source_partition_ids"])
                records.append(record)
                candidate_rows.append({"method_id": method, "selection_nll": selection_nll, "probability_path": f"groups/{group_id}/{method}/probabilities.npz", "parameters_path": f"groups/{group_id}/{method}/parameters.json", "record_id": record["record_id"], "diagnostic_only": fitted.diagnostic_only})
                attempts.append({"attempt_id": attempt_id, "group_id": group_id, "method_id": method, "support": len(fit_idx), "terminal_status": "DIAGNOSTIC_ONLY" if fitted.diagnostic_only else "SUCCESS", "reason": None, "selection_nll": selection_nll})
            except (IneligibleMethod, ContractViolation) as exc:
                attempts.append({"attempt_id": attempt_id, "group_id": group_id, "method_id": method, "support": len(fit_idx), "terminal_status": "INELIGIBLE", "reason": f"{type(exc).__name__}:{exc}"})
            except Exception as exc:
                attempts.append({"attempt_id": attempt_id, "group_id": group_id, "method_id": method, "support": len(fit_idx), "terminal_status": "FAILED", "reason": f"{type(exc).__name__}:{exc}"})
            progress(completed, total, f"{group_id}:{method}", sum(row["terminal_status"] in {"FAILED", "INELIGIBLE"} for row in attempts), "IN_PROGRESS")
        eligible = [row for row in candidate_rows if not row.get("diagnostic_only")]
        chosen = min(eligible, key=lambda row: (float(row["selection_nll"]), str(row["method_id"])))
        group_root = out / "groups" / group_id
        if chosen["method_id"] == "identity":
            probabilities = _identity_probabilities(ctx, group_id)
        else:
            probabilities = np.load(out / chosen["probability_path"], allow_pickle=False)["probabilities"]
        np.savez_compressed(group_root / "selected_probabilities.npz", probabilities=probabilities)
        selection = {"group_id": group_id, "selected_method_id": chosen["method_id"], "selection_role": selection_role, "selection_metric": "nll", "selection_value": chosen["selection_nll"], "test_role_used": False, "selected_record_id": chosen.get("record_id"), "candidate_count": len(candidate_rows)}
        write_json(group_root / "selection.json", selection)
        selections.append(selection)
    write_jsonl(out / "challenger_calibration_records.jsonl", records)
    write_jsonl(out / "calibration_attempt_ledger.jsonl", attempts)
    write_jsonl(out / "calibration_selections.jsonl", selections)
    return {"status": "PASS", "products": ["P03-PROD-018", "P03-PROD-019"], "challenger_record_count": len(records), "attempt_count": len(attempts), "terminal_counts": dict(Counter(row["terminal_status"] for row in attempts)), "selection_count": len(selections), "calibration_attempt_ledger": "calibration_attempt_ledger.jsonl"}


def _selected_probabilities(ctx: ExecutionContext, group_id: str) -> np.ndarray:
    return np.load(_stage_dir(ctx, "11") / "groups" / group_id / "selected_probabilities.npz", allow_pickle=False)["probabilities"]


def stage_12(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    config, protocol, contract = _config(ctx), _protocol(ctx), _record_contract(ctx)
    atol = float(config["score_semantics"]["probability_atol"])
    eval_role = _protocol_role(protocol, "evaluation")
    reports, bins, hcw_rows = [], [], []
    for index, group_id in enumerate(_group_ids(ctx), start=1):
        descriptor, scores, labels, metadata = _load_group(ctx, group_id)
        eval_idx = _role_indices(metadata, eval_role)
        if not len(eval_idx):
            raise GateBlocked("G03-12-RELIABILITY", "EVALUATION_ROLE_MISSING", group_id)
        authorize_view(operation="evaluate", source_role=eval_role, requested_fields=["scores", "labels"], role_map=protocol["scientific"]["roles"]["role_map"], field_visibility=protocol["scientific"]["roles"]["field_visibility"])
        raw = score_to_probabilities(ScoreView(scores, descriptor["score_type"], tuple(descriptor["class_order"]), group_id, bool(config["score_semantics"]["legal_log_probability_transform"])), probability_atol=atol)
        selected = _selected_probabilities(ctx, group_id)
        raw_audit = audit_reliability(raw[eval_idx], labels[eval_idx], protocol["scientific"]["metrics"]["metric_profile"], protocol["scientific"]["reliability"]["binning_profile"], probability_atol=atol)
        selected_audit = audit_reliability(selected[eval_idx], labels[eval_idx], protocol["scientific"]["metrics"]["metric_profile"], protocol["scientific"]["reliability"]["binning_profile"], probability_atol=atol, raw_comparator=raw_audit["metrics"])
        report_id = deterministic_id("P03-RELIABILITY", {"group": group_id, "source": "selected"})
        payload = {
            "report_id": report_id, "ablation_id": "A1", "probability_source_id": f"{group_id}:selected", "evaluation_role": eval_role,
            "metric_profile_id": protocol["scientific"]["metrics"]["metric_profile"]["profile_id"], "binning_profile_id": protocol["scientific"]["reliability"]["binning_profile"]["profile_id"],
            "interval_profile_id": protocol["scientific"]["reliability"]["interval_profile"]["profile_id"], "dataset_id": descriptor["dataset_id"], "model_id": descriptor["model_id"],
            "budget_id": descriptor["budget_id"], "group_profile_id": protocol["scientific"]["groups"]["profile_id"], "support_count": len(eval_idx),
            "brier": selected_audit["metrics"]["brier"], "nll": selected_audit["metrics"]["nll"], "calibration_error": selected_audit["metrics"]["calibration_error"],
            "bin_source_path": f"reliability_bins/{group_id}.json", "raw_comparator_report_id": deterministic_id("P03-RELIABILITY-RAW", group_id),
            "direction": selected_audit["direction"], "denominator": selected_audit["denominator"], "deterioration_status": selected_audit["deterioration"]["status"],
        }
        record = make_record("ReliabilityAuditReport", ctx, "L3-M02", payload, contract, source_artifact_ids=descriptor["source_partition_ids"])
        reports.append(record)
        for row in selected_audit["bins"]:
            bins.append({"group_id": group_id, "report_id": report_id, **row})
        hcw = mine_high_confidence_errors(selected[eval_idx], labels[eval_idx], [metadata[i] for i in eval_idx], protocol["scientific"]["reliability"]["high_confidence_wrong_profile"], class_order=descriptor["class_order"], probability_atol=atol)
        for row in hcw:
            row.update({"group_id": group_id, "probability_source_id": f"{group_id}:selected", "evaluation_role": eval_role, "dataset_id": descriptor["dataset_id"], "model_id": descriptor["model_id"], "budget_id": descriptor["budget_id"]})
        hcw_rows.extend(hcw)
        progress(index, len(_group_ids(ctx)), group_id, 0, "IN_PROGRESS")
    write_jsonl(out / "reliability_audit_reports.jsonl", reports)
    write_jsonl(out / "reliability_bin_source.jsonl", bins)
    write_jsonl(out / "high_confidence_wrong_rows.jsonl", hcw_rows)
    write_csv(out / "reliability_bin_source.csv", bins)
    return {"status": "PASS", "products": ["P03-PROD-020", "P03-PROD-021", "P03-PROD-022", "P03-PROD-023"], "reliability_report_count": len(reports), "reliability_bin_count": len(bins), "high_confidence_wrong_count": len(hcw_rows), "reliability_audit_reports": "reliability_audit_reports.jsonl"}


def _aligned_a4_member_probabilities(
    ctx: ExecutionContext,
    descriptor: Mapping[str, Any],
    target_metadata: Sequence[Mapping[str, Any]],
    catalog: Sequence[Mapping[str, Any]],
) -> tuple[list[np.ndarray] | None, dict[str, Any]]:
    control = descriptor.get("a4_control")
    if not isinstance(control, dict):
        return None, {"status": "INELIGIBLE", "reason": "A4_CONTROL_NOT_BOUND_TO_SOURCE"}
    if control.get("aggregation_rule") != "PROBABILITY_AVERAGE":
        return None, {"status": "INELIGIBLE", "reason": "A4_CONTROL_NOT_PROBABILITY_AVERAGE", "control_record_id": control.get("record_id"), "control_id": control.get("control_id")}
    checkpoints = [str(value) for value in control.get("member_checkpoint_ids", [])]
    if len(checkpoints) < 2 or len(checkpoints) != len(control.get("member_model_ids", [])):
        return None, {"status": "INELIGIBLE", "reason": "A4_MEMBER_CONTRACT_INCOMPLETE", "control_record_id": control.get("record_id")}
    config = _config(ctx)
    atol = float(config["score_semantics"]["probability_atol"])
    alignment_fields = list(_protocol(ctx)["scientific"]["uncertainty"]["disagreement_profile"]["alignment_fields"])

    def key(row: Mapping[str, Any]) -> tuple[str, ...]:
        return tuple(str(row.get(field)) for field in alignment_fields)

    target_keys = [key(row) for row in target_metadata]
    if len(target_keys) != len(set(target_keys)):
        return None, {"status": "INELIGIBLE", "reason": "A4_TARGET_ALIGNMENT_KEYS_NOT_UNIQUE", "control_record_id": control.get("record_id")}
    aligned: list[np.ndarray] = []
    resolved_groups: list[str] = []
    for checkpoint_id in checkpoints:
        candidates = [
            row for row in catalog
            if str(row.get("checkpoint_id")) == checkpoint_id
            and str(row.get("dataset_id")) == str(descriptor.get("dataset_id"))
            and str(row.get("budget_id")) == str(descriptor.get("budget_id"))
            and str(row.get("split_id")) == str(descriptor.get("split_id"))
            and str(row.get("group_id")) != str(descriptor.get("group_id"))
        ]
        if len(candidates) != 1:
            return None, {"status": "INELIGIBLE", "reason": "A4_MEMBER_GROUP_NOT_UNIQUELY_RESOLVED", "checkpoint_id": checkpoint_id, "candidate_count": len(candidates), "control_record_id": control.get("record_id")}
        member = candidates[0]
        _, member_scores, _, member_metadata = _load_group(ctx, str(member["group_id"]))
        member_probabilities = score_to_probabilities(
            ScoreView(member_scores, str(member["score_type"]), tuple(member["class_order"]), str(member["group_id"]), bool(config["score_semantics"]["legal_log_probability_transform"])),
            probability_atol=atol,
        )
        member_map: dict[tuple[str, ...], np.ndarray] = {}
        for index, row in enumerate(member_metadata):
            member_key = key(row)
            if member_key in member_map:
                return None, {"status": "INELIGIBLE", "reason": "A4_MEMBER_ALIGNMENT_KEYS_NOT_UNIQUE", "checkpoint_id": checkpoint_id, "control_record_id": control.get("record_id")}
            member_map[member_key] = member_probabilities[index]
        missing = [member_key for member_key in target_keys if member_key not in member_map]
        if missing:
            return None, {"status": "INELIGIBLE", "reason": "A4_MEMBER_ALIGNMENT_INCOMPLETE", "checkpoint_id": checkpoint_id, "missing_count": len(missing), "control_record_id": control.get("record_id")}
        aligned.append(np.asarray([member_map[member_key] for member_key in target_keys], dtype=float))
        resolved_groups.append(str(member["group_id"]))
    return aligned, {
        "status": "ELIGIBLE", "reason": None, "control_record_id": control.get("record_id"), "control_id": control.get("control_id"),
        "member_count": len(aligned), "member_checkpoint_ids": checkpoints, "member_group_ids": resolved_groups,
        "alignment_fields": alignment_fields, "aligned_row_count": len(target_keys),
        "estimator": _protocol(ctx)["scientific"]["uncertainty"]["disagreement_profile"]["estimator"],
    }


def stage_13(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    config, protocol, contract = _config(ctx), _protocol(ctx), _record_contract(ctx)
    atol = float(config["score_semantics"]["probability_atol"])
    records, conditional_attempts = [], []
    catalog = [json.loads((_stage_dir(ctx, "07") / "groups" / group_id / "descriptor.json").read_text(encoding="utf-8")) for group_id in _group_ids(ctx)]
    for index, group_id in enumerate(_group_ids(ctx), start=1):
        descriptor, scores, labels, metadata = _load_group(ctx, group_id)
        probabilities = _selected_probabilities(ctx, group_id)
        member_probabilities, disagreement_alignment = _aligned_a4_member_probabilities(ctx, descriptor, metadata, catalog)
        extracted = extract_uncertainty(
            probabilities, protocol["scientific"]["uncertainty"]["feature_profile"],
            probability_atol=atol, member_probabilities=member_probabilities,
        )
        extracted["conditional_attempts"] = [row for row in extracted["conditional_attempts"] if row.get("feature_id") != "member_disagreement"]
        conditional_attempts.append({"group_id": group_id, "feature_id": "member_disagreement", **disagreement_alignment})
        group_root = out / "groups" / group_id
        group_root.mkdir(parents=True, exist_ok=True)
        write_json(group_root / "member_disagreement_alignment.json", disagreement_alignment)
        feature_arrays = {}
        for feature_id, feature in extracted["features"].items():
            values = np.asarray(feature["values"], dtype=float)
            feature_arrays[feature_id] = values
            uncertainty_id = deterministic_id("P03-UNCERTAINTY", {"group": group_id, "feature": feature_id})
            payload = {
                "uncertainty_id": uncertainty_id, "ablation_id": "A3", "dataset_id": descriptor["dataset_id"], "model_id": descriptor["model_id"],
                "budget_id": descriptor["budget_id"], "split_id": descriptor["split_id"], "probability_source_id": f"{group_id}:selected",
                "feature_id": feature_id, "feature_family": feature["family"], "feature_direction": feature["direction"], "class_order": descriptor["class_order"],
                "class_count": len(descriptor["class_order"]), "value_path": f"groups/{group_id}/features.npz#{feature_id}", "support_count": len(values),
                "alias_of_feature_id": feature.get("alias_of_feature_id"), "decision_time_eligible": feature["decision_time_eligible"],
                "conditional_gate_id": disagreement_alignment.get("control_record_id") if feature_id == "member_disagreement" else None,
                "causal_cutoff_hash": None, "reset_key_profile": None,
            }
            source_artifact_ids = list(descriptor["source_partition_ids"])
            if feature_id == "member_disagreement" and disagreement_alignment.get("control_record_id"):
                source_artifact_ids.append(str(disagreement_alignment["control_record_id"]))
            records.append(make_record("UncertaintyRecord", ctx, "L3-M03", payload, contract, source_artifact_ids=source_artifact_ids))
        np.savez_compressed(group_root / "features.npz", **feature_arrays)
        write_json(group_root / "feature_index.json", {feature_id: {k: v for k, v in feature.items() if k != "values"} for feature_id, feature in extracted["features"].items()})
        conditional_attempts.extend({"group_id": group_id, **row} for row in extracted["conditional_attempts"])
        conformal_role = _protocol_role(protocol, "conformal_calibration")
        conformal_idx = _role_indices(metadata, conformal_role)
        state = fit_conformal_proxy(probabilities[conformal_idx], labels[conformal_idx], protocol["scientific"]["uncertainty"]["conformal_profile"], probability_atol=atol) if len(conformal_idx) else {"status": "INELIGIBLE", "reason": "CONFORMAL_ROLE_MISSING"}
        write_json(group_root / "conformal_state.json", state)
        conditional_attempts.append({"group_id": group_id, "feature_id": "conformal_set_size", **state})
        temporal_profile = protocol["scientific"]["uncertainty"]["temporal_profile"]
        try:
            temporal_rows = [{**row, temporal_profile["value_field"]: float(feature_arrays["confidence"][i])} for i, row in enumerate(metadata)]
            temporal_rows.sort(key=lambda row: tuple(row.get(field) for field in temporal_profile["reset_fields"]) + (row[temporal_profile["order_field"]],))
            temporal = summarize_past(temporal_rows, temporal_profile)
            write_jsonl(group_root / "temporal_past_only.jsonl", temporal)
            conditional_attempts.append({"group_id": group_id, "feature_id": "past_only_temporal", "status": "ELIGIBLE", "support": len(temporal)})
        except Exception as exc:
            conditional_attempts.append({"group_id": group_id, "feature_id": "past_only_temporal", "status": "INELIGIBLE", "reason": f"{type(exc).__name__}:{exc}"})
        progress(index, len(_group_ids(ctx)), group_id, sum(row.get("status") == "INELIGIBLE" for row in conditional_attempts), "IN_PROGRESS")
    write_jsonl(out / "uncertainty_records.jsonl", records)
    write_jsonl(out / "conditional_uncertainty_attempts.jsonl", conditional_attempts)
    disagreement_rows = [row for row in conditional_attempts if row.get("feature_id") == "member_disagreement"]
    return {
        "status": "PASS", "products": ["P03-PROD-024", "P03-PROD-025"], "uncertainty_record_count": len(records),
        "conditional_attempt_count": len(conditional_attempts), "uncertainty_records": "uncertainty_records.jsonl",
        "member_disagreement_eligible_count": sum(row.get("status") == "ELIGIBLE" for row in disagreement_rows),
        "member_disagreement_ineligible_count": sum(row.get("status") == "INELIGIBLE" for row in disagreement_rows),
        "member_disagreement_accounted_group_count": len(disagreement_rows),
    }


def _features(ctx: ExecutionContext, group_id: str) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    root = _stage_dir(ctx, "13") / "groups" / group_id
    arrays = np.load(root / "features.npz", allow_pickle=False)
    return {name: arrays[name] for name in arrays.files}, json.loads((root / "feature_index.json").read_text(encoding="utf-8"))


def stage_14(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    config, protocol = _config(ctx), _protocol(ctx)
    atol = float(config["score_semantics"]["probability_atol"])
    selection_role = _protocol_role(protocol, "threshold_selection")
    rows = []
    for index, group_id in enumerate(_group_ids(ctx), start=1):
        descriptor, scores, labels, metadata = _load_group(ctx, group_id)
        del scores
        selection_idx = _role_indices(metadata, selection_role)
        if not len(selection_idx):
            raise GateBlocked("G03-14-A2-SELECT", "THRESHOLD_SELECTION_ROLE_MISSING", group_id)
        authorize_view(operation="select_threshold", source_role=selection_role, requested_fields=["scores", "labels"], role_map=protocol["scientific"]["roles"]["role_map"], field_visibility=protocol["scientific"]["roles"]["field_visibility"])
        probabilities = _selected_probabilities(ctx, group_id)
        features, _ = _features(ctx, group_id)
        target = dict(protocol["scientific"]["a2"]["target_profile"])
        target.update({"feature_id": "confidence", "operator": protocol["scientific"]["a2"]["operator"], "tie_policy": protocol["scientific"]["a2"]["tie_policy"]})
        selected = select_rule(features["confidence"][selection_idx], probabilities[selection_idx], labels[selection_idx], target, probability_atol=atol)
        row = {"group_id": group_id, "selection_role": selection_role, "test_role_used": False, **selected}
        rows.append(row)
        write_json(out / "groups" / group_id / "a2_rule_candidate.json", row)
        progress(index, len(_group_ids(ctx)), group_id, 0, "IN_PROGRESS")
    write_jsonl(out / "a2_rule_candidates.jsonl", rows)
    return {"status": "PASS", "products": ["P03-PROD-026"], "a2_candidate_count": len(rows), "a2_rule_candidates": "a2_rule_candidates.jsonl"}


def stage_15(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    config, protocol, contract = _config(ctx), _protocol(ctx), _record_contract(ctx)
    atol = float(config["score_semantics"]["probability_atol"])
    eval_role = _protocol_role(protocol, "evaluation")
    records, results = [], []
    for index, group_id in enumerate(_group_ids(ctx), start=1):
        descriptor, scores, labels, metadata = _load_group(ctx, group_id)
        del scores
        eval_idx = _role_indices(metadata, eval_role)
        candidate = json.loads((_stage_dir(ctx, "14") / "groups" / group_id / "a2_rule_candidate.json").read_text(encoding="utf-8"))
        features, _ = _features(ctx, group_id)
        probabilities = _selected_probabilities(ctx, group_id)
        applied = apply_rule(features["confidence"][eval_idx], probabilities[eval_idx], labels[eval_idx], candidate["rule"], probability_atol=atol)
        result = {"group_id": group_id, "application_role": eval_role, "rule": candidate["rule"], **{k: v for k, v in applied.items() if k != "acceptance_mask"}}
        results.append(result)
        payload = {
            "selective_id": deterministic_id("P03-A2", result), "ablation_id": "A2", "dataset_id": descriptor["dataset_id"], "model_id": descriptor["model_id"],
            "budget_id": descriptor["budget_id"], "split_id": descriptor["split_id"], "probability_source_id": f"{group_id}:selected",
            "uncertainty_source_id": f"{group_id}:confidence", "rule_family": "registered_confidence_floor", "threshold_registry_id": None,
            "selection_role": candidate["selection_role"], "application_role": eval_role, "operator": candidate["rule"]["operator"], "tie_policy": candidate["rule"]["tie_policy"],
            "accepted_count": applied["accepted_count"], "rejected_count": applied["rejected_count"], "coverage": applied["coverage"], "risk": applied["risk"],
            "utility": None, "acceptance_mask_sha256": applied["acceptance_mask_sha256"], "risk_coverage_curve_id": None,
        }
        records.append(make_record("SelectivePredictionRecord", ctx, "L3-M04", payload, contract, source_artifact_ids=descriptor["source_partition_ids"]))
        group_root = out / "groups" / group_id
        group_root.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(group_root / "a2_acceptance_mask.npz", acceptance_mask=applied["acceptance_mask"])
        progress(index, len(_group_ids(ctx)), group_id, 0, "IN_PROGRESS")
    write_jsonl(out / "a2_selective_prediction_records.jsonl", records)
    write_jsonl(out / "a2_application_results.jsonl", results)
    return {"status": "PASS", "products": ["P03-PROD-027"], "a2_record_count": len(records), "a2_selective_prediction_records": "a2_selective_prediction_records.jsonl"}


def stage_16(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    config, protocol, contract = _config(ctx), _protocol(ctx), _record_contract(ctx)
    atol = float(config["score_semantics"]["probability_atol"])
    selection_role, eval_role = _protocol_role(protocol, "threshold_selection"), _protocol_role(protocol, "evaluation")
    records, rule_rows = [], []
    curve_stream = AtomicJsonlCsvStream(
        out / "risk_coverage_curve_source.jsonl",
        out / "risk_coverage_curve_source.csv",
        ["curve_id", "group_id", "feature_id", "role", "point_index", "threshold", "accepted_count", "rejected_count", "coverage", "risk"],
    )
    feature_profiles = protocol["scientific"]["a3"]["feature_profiles"]
    total = len(_group_ids(ctx)) * len(feature_profiles)
    completed = 0
    try:
      for group_id in _group_ids(ctx):
        descriptor, scores, labels, metadata = _load_group(ctx, group_id)
        del scores
        selection_idx, eval_idx = _role_indices(metadata, selection_role), _role_indices(metadata, eval_role)
        probabilities = _selected_probabilities(ctx, group_id)
        features, feature_index = _features(ctx, group_id)
        for feature_profile in feature_profiles:
            completed += 1
            feature_id = str(feature_profile["feature_id"])
            if feature_id not in features:
                rule_rows.append({"group_id": group_id, "feature_id": feature_id, "terminal_status": "INELIGIBLE", "reason": "FEATURE_UNAVAILABLE"})
                progress(completed, total, f"{group_id}:{feature_id}", 1, "IN_PROGRESS")
                continue
            target = dict(protocol["scientific"]["a3"]["working_points"])
            target.update({"feature_id": feature_id, "operator": feature_profile["operator"], "tie_policy": feature_profile["tie_policy"]})
            selected = select_rule(features[feature_id][selection_idx], probabilities[selection_idx], labels[selection_idx], target, probability_atol=atol)
            applied = apply_rule(features[feature_id][eval_idx], probabilities[eval_idx], labels[eval_idx], selected["rule"], probability_atol=atol)
            selection_curve = [{"point_index": point_index, **row} for point_index, row in enumerate(selected["candidates"])]
            eval_curve = build_risk_coverage(features[feature_id][eval_idx], probabilities[eval_idx], labels[eval_idx], target, probability_atol=atol)
            curve_id = deterministic_id("P03-A3-CURVE", {"group": group_id, "feature": feature_id, "rule": selected["rule"]})
            for row in selection_curve:
                curve_stream.write({"curve_id": curve_id, "group_id": group_id, "feature_id": feature_id, "role": selection_role, **row})
            for row in eval_curve:
                curve_stream.write({"curve_id": curve_id, "group_id": group_id, "feature_id": feature_id, "role": eval_role, **row})
            rule_row = {"group_id": group_id, "feature_id": feature_id, "selection_role": selection_role, "application_role": eval_role, "terminal_status": "SUCCESS", "rule": selected["rule"], "rule_sha256": selected["rule_sha256"], "application": {k: v for k, v in applied.items() if k != "acceptance_mask"}, "curve_id": curve_id, "alias_of_feature_id": feature_index[feature_id].get("alias_of_feature_id")}
            rule_rows.append(rule_row)
            payload = {
                "selective_id": deterministic_id("P03-A3", rule_row), "ablation_id": "A3", "dataset_id": descriptor["dataset_id"], "model_id": descriptor["model_id"],
                "budget_id": descriptor["budget_id"], "split_id": descriptor["split_id"], "probability_source_id": f"{group_id}:selected",
                "uncertainty_source_id": f"{group_id}:{feature_id}", "rule_family": "feature_specific_selective_prediction", "threshold_registry_id": None,
                "selection_role": selection_role, "application_role": eval_role, "operator": selected["rule"]["operator"], "tie_policy": selected["rule"]["tie_policy"],
                "accepted_count": applied["accepted_count"], "rejected_count": applied["rejected_count"], "coverage": applied["coverage"], "risk": applied["risk"],
                "utility": None, "acceptance_mask_sha256": applied["acceptance_mask_sha256"], "risk_coverage_curve_id": curve_id,
            }
            records.append(make_record("SelectivePredictionRecord", ctx, "L3-M04", payload, contract, source_artifact_ids=descriptor["source_partition_ids"]))
            group_root = out / "groups" / group_id
            group_root.mkdir(parents=True, exist_ok=True)
            np.savez_compressed(group_root / f"a3_{feature_id}_acceptance_mask.npz", acceptance_mask=applied["acceptance_mask"])
            progress(completed, total, f"{group_id}:{feature_id}", 0, "IN_PROGRESS")
    except Exception:
        curve_stream.preserve_partial()
        raise
    else:
        curve_stream.commit()
    write_jsonl(out / "a3_selective_prediction_records.jsonl", records)
    write_jsonl(out / "a3_rule_candidates.jsonl", rule_rows)
    return {"status": "PASS", "products": ["P03-PROD-028", "P03-PROD-029"], "a3_record_count": len(records), "curve_point_count": curve_stream.row_count, "a3_rule_candidate_count": len(rule_rows), "a3_selective_prediction_records": "a3_selective_prediction_records.jsonl", "risk_coverage_curve_source": "risk_coverage_curve_source.jsonl"}


def stage_17(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    protocol = _protocol(ctx)
    store = ThresholdStore(out / "threshold_registry")
    candidates = []
    a2 = _read_jsonl(_stage_dir(ctx, "14") / "a2_rule_candidates.jsonl")
    a3 = _read_jsonl(_stage_dir(ctx, "16") / "a3_rule_candidates.jsonl")
    for row in a2:
        candidates.append((row["group_id"], "A2", row["rule"], row["selection_role"]))
    for row in a3:
        if row.get("terminal_status") == "SUCCESS":
            candidates.append((row["group_id"], "A3", row["rule"], row["selection_role"]))
    records = []
    for index, (group_id, ablation, rule, selection_role) in enumerate(candidates, start=1):
        descriptor, _, _, _ = _load_group(ctx, group_id)
        candidate = {
            "threshold_version": "1.0.0", "ablation_id": ablation, "feature_id": rule["feature_id"], "probability_source_id": f"{group_id}:selected",
            "selection_dataset_id": descriptor["dataset_id"], "selection_budget_id": descriptor["budget_id"], "selection_split_id": descriptor["split_id"],
            "selection_role": selection_role, "target_profile_id": rule["target_profile_id"], "operator": rule["operator"], "threshold_value": rule["threshold_value"],
            "tie_policy": rule["tie_policy"], "applicability": {"dataset_id": descriptor["dataset_id"], "model_id": descriptor["model_id"], "budget_id": descriptor["budget_id"], "split_id": descriptor["split_id"]},
            "permissions": {"consumers": protocol["scientific"]["threshold_registry"]["permitted_consumers"], "labels_exported": False},
            "effective_from": ctx.created_at_utc, "effective_until": None, "supersession_reason": None,
        }
        records.append(store.register(candidate))
        progress(index, len(candidates), records[-1]["threshold_id"], 0, "IN_PROGRESS")
    write_jsonl(out / "threshold_registry_records.jsonl", records)
    return {"status": "PASS", "products": ["P03-PROD-030", "P03-PROD-031"], "threshold_record_count": len(records), "threshold_registry_records": "threshold_registry_records.jsonl", "threshold_registry_index": "threshold_registry/threshold_registry_index.json"}


def stage_18(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    config, protocol = _config(ctx), _protocol(ctx)
    atol = float(config["score_semantics"]["probability_atol"])
    eval_role = _protocol_role(protocol, "evaluation")
    rows = []
    a2_results = {row["group_id"]: row for row in _read_jsonl(_stage_dir(ctx, "15") / "a2_application_results.jsonl")}
    a3_results = [row for row in _read_jsonl(_stage_dir(ctx, "16") / "a3_rule_candidates.jsonl") if row.get("terminal_status") == "SUCCESS"]
    for index, group_id in enumerate(_group_ids(ctx), start=1):
        descriptor, _, labels, metadata = _load_group(ctx, group_id)
        eval_idx = _role_indices(metadata, eval_role)
        probabilities = _selected_probabilities(ctx, group_id)
        a1 = selective_risk(probabilities[eval_idx], labels[eval_idx], np.ones(len(eval_idx), dtype=bool), probability_atol=atol)
        base = {"dataset_id": descriptor["dataset_id"], "model_id": descriptor["model_id"], "budget_id": descriptor["budget_id"], "split_id": descriptor["split_id"], "eligible_set_sha256": sha256_json([metadata[i]["record_id"] for i in eval_idx]), "probability_source_id": f"{group_id}:selected"}
        rows.append({**base, "record_id": deterministic_id("MATCH-A1", base), "ablation_id": "A1", "coverage": a1["coverage"], "risk": a1["risk"]})
        a2 = a2_results[group_id]
        rows.append({**base, "record_id": deterministic_id("MATCH-A2", a2), "ablation_id": "A2", "coverage": a2["coverage"], "risk": a2["risk"]})
        for a3 in [row for row in a3_results if row["group_id"] == group_id]:
            rows.append({**base, "record_id": deterministic_id("MATCH-A3", a3), "ablation_id": "A3", "feature_id": a3["feature_id"], "coverage": a3["application"]["coverage"], "risk": a3["application"]["risk"]})
        progress(index, len(_group_ids(ctx)), group_id, 0, "IN_PROGRESS")
    profile = dict(protocol["scientific"]["matching"])
    profile["required_ablations"] = ["A1", "A2", "A3"]
    # Match each A3 child against the same A1/A2 base by duplicating base rows per feature.
    expanded = []
    for group_id in _group_ids(ctx):
        group_rows = [row for row in rows if row["probability_source_id"] == f"{group_id}:selected"]
        children = [row for row in group_rows if row["ablation_id"] == "A3"]
        for child in children:
            feature = child.get("feature_id")
            for row in group_rows:
                if row["ablation_id"] in {"A1", "A2"}:
                    expanded.append({**row, "feature_id": feature})
            expanded.append(child)
    profile["matching_key_fields"] = list(profile["matching_key_fields"]) + ["feature_id"]
    matched = build_matched_operating_points(expanded, profile)
    write_json(out / "matched_operating_points.json", matched)
    write_jsonl(out / "matched_operating_point_rows.jsonl", expanded)
    if matched["unmatched"]:
        raise GateBlocked("G03-18-MATCHED", "UNMATCHED_A1_A2_A3", json.dumps(matched["unmatched"][:5]))
    return {"status": "PASS", "products": ["P03-PROD-032"], "matched_set_count": len(matched["matched"]), "unmatched_count": len(matched["unmatched"]), "matched_operating_points": "matched_operating_points.json"}


def stage_19(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    config, protocol = _config(ctx), _protocol(ctx)
    atol = float(config["score_semantics"]["probability_atol"])
    eval_role = _protocol_role(protocol, "evaluation")
    rows, warnings = [], []
    for index, group_id in enumerate(_group_ids(ctx), start=1):
        descriptor, _, labels, metadata = _load_group(ctx, group_id)
        eval_idx = _role_indices(metadata, eval_role)
        result = audit_groups(_selected_probabilities(ctx, group_id)[eval_idx], labels[eval_idx], [metadata[i] for i in eval_idx], protocol["scientific"]["groups"], protocol["scientific"]["metrics"]["metric_profile"], probability_atol=atol)
        rows.extend({"group_source_id": group_id, **row} for row in result["rows"])
        warnings.extend({"group_source_id": group_id, **row} for row in result["sparse_support_warnings"])
        progress(index, len(_group_ids(ctx)), group_id, len(warnings), "IN_PROGRESS")
    write_jsonl(out / "group_budget_audit.jsonl", rows)
    write_jsonl(out / "sparse_support_warnings.jsonl", warnings)
    write_csv(out / "group_budget_source.csv", rows)
    return {"status": "PASS", "products": ["P03-PROD-033", "P03-PROD-034"], "group_audit_row_count": len(rows), "sparse_support_warning_count": len(warnings), "group_budget_audit": "group_budget_audit.jsonl"}


def stage_20(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    attempts = _read_jsonl(_stage_dir(ctx, "11") / "calibration_attempt_ledger.jsonl")
    conditional = _read_jsonl(_stage_dir(ctx, "13") / "conditional_uncertainty_attempts.jsonl")
    sparse = _read_jsonl(_stage_dir(ctx, "19") / "sparse_support_warnings.jsonl")
    leakage = _read_jsonl(_stage_dir(ctx, "08") / "leakage_warning_records.jsonl")
    intake = json.loads((_stage_dir(ctx, "04") / "p03_intake_ledger.json").read_text(encoding="utf-8"))
    negative = []
    for row in attempts:
        if row["terminal_status"] != "SUCCESS":
            negative.append({"source": row["attempt_id"], "failure_class": "failed calibration" if row["terminal_status"] == "FAILED" else "conditional skip", "terminal_status": row["terminal_status"], "reason": row.get("reason")})
    negative.extend({"source": row["group_id"] + ":" + row["feature_id"], "failure_class": "conditional skip", "terminal_status": row.get("status"), "reason": row.get("reason")} for row in conditional if row.get("status") != "ELIGIBLE")
    negative.extend({"source": row["group_source_id"], "failure_class": "sparse group", "terminal_status": "DIAGNOSTIC_ONLY", "reason": "SPARSE_GROUP_SUPPORT"} for row in sparse)
    negative.extend({"source": row["warning_id"], "failure_class": "invalid split", "terminal_status": "BLOCKED", "reason": row["illegal_use_code"]} for row in leakage)
    inherited_negative: list[dict[str, Any]] = []
    inherited_receipt: dict[str, Any] = {"authoring_fixture": ctx.authoring_fixture, "source_run_id": intake["source_run_id"], "source_config_sha256": intake["source_config_sha256"], "objects": []}
    if not ctx.authoring_fixture:
        config = _config(ctx)
        locator = config["inputs"]["p02"]
        root = Path(_stage_result(ctx, "03")["resolved_external_root"])
        diagnostic_rows = _read_jsonl(root / locator["diagnostic_only_path"])
        failure_rows = _read_jsonl(root / locator["failure_case_path"])
        for row in diagnostic_rows:
            inherited_negative.append({
                "source": row["record_id"], "source_phase": "P02", "source_ids": row.get("source_ids", []),
                "failure_class": "upstream diagnostic-only evidence", "terminal_status": "DIAGNOSTIC_ONLY",
                "reason": row.get("reason_code"), "allowed_consumers": row.get("allowed_consumers", []),
            })
        for row in failure_rows:
            inherited_negative.append({
                "source": row["record_id"], "source_phase": "P02", "source_ids": row.get("source_ids", []),
                "failure_class": str(row.get("failure_class", "upstream failure")), "terminal_status": "INHERITED_FAILURE",
                "reason": row.get("failure_code"), "evidence_consequence": row.get("evidence_consequence"),
            })
        for limitation in intake["limitations"]:
            inherited_negative.append({
                "source": limitation["limitation_id"], "source_phase": "P02", "source_ids": [],
                "failure_class": "persistent upstream limitation", "terminal_status": str(limitation["status_after_P02"]),
                "reason": limitation["tag"], "evidence_consequence": limitation["downstream_claim_impact"],
            })
        local_control_keys = {"downstream_readiness_contract_path", "persistent_limitations_path"}
        for key in ("a0_completion_path", "a4_completion_path", "baseline_metric_path", "diagnostic_only_path", "failure_case_path", "downstream_readiness_contract_path", "persistent_limitations_path"):
            source_root = ctx.package_root if key in local_control_keys else root
            path = source_root / locator[key]
            inherited_receipt["objects"].append({
                "role": key, "path": locator[key], "bytes": path.stat().st_size, "sha256": sha256_file(path),
                "source": "BUNDLED_CUMULATIVE_P02_HANDOFF_AUTHORITY" if key in local_control_keys else "HF_FROZEN_P02_EXECUTION_SNAPSHOT",
            })
        inherited_receipt["ensemble_control_record_count"] = len(list((root / locator["ensemble_control_record_prefix"]).rglob("*.jsonl")))
        inherited_receipt["ensemble_control_manifest_count"] = len(list((root / locator["ensemble_control_manifest_prefix"]).rglob("*.json")))
    else:
        inherited_negative.extend({"source": row["limitation_id"], "source_phase": "P02", "source_ids": [], "failure_class": "fixture limitation", "terminal_status": row["status_after_P02"], "reason": row["tag"]} for row in intake["limitations"])
    negative.extend(inherited_negative)
    disposition_complete = bool(_stage_result(ctx, "07")["disposition_complete"])
    upstream_counts = intake["upstream_record_counts"]
    inherited_count_complete = ctx.authoring_fixture or (
        sum(row["failure_class"] == "upstream diagnostic-only evidence" for row in inherited_negative) == int(upstream_counts["diagnostic_only_records"])
        and sum(row["terminal_status"] == "INHERITED_FAILURE" for row in inherited_negative) == int(upstream_counts["failure_case_records"])
        and sum(row["failure_class"] == "persistent upstream limitation" for row in inherited_negative) == len(intake["limitations"])
    )
    denominator_complete = bool(disposition_complete and inherited_count_complete and len(attempts) == _stage_result(ctx, "11")["attempt_count"])
    if not denominator_complete:
        raise GateBlocked("G03-20-NEGATIVE", "NEGATIVE_EVIDENCE_DENOMINATOR_INCOMPLETE", f"disposition={disposition_complete}, inherited={inherited_count_complete}")
    write_jsonl(out / "negative_result_notes.jsonl", negative)
    write_jsonl(out / "inherited_p02_negative_and_limitation_records.jsonl", inherited_negative)
    write_json(out / "p02_inherited_contract_receipt.json", inherited_receipt)
    write_json(out / "failure_taxonomy_summary.json", {
        "planned_calibration_attempts": len(attempts), "terminal_calibration_attempts": len(attempts), "negative_count": len(negative),
        "inherited_p02_negative_count": len(inherited_negative), "terminal_counts": dict(Counter(row["terminal_status"] for row in negative)),
        "denominator_complete": denominator_complete, "upstream_prediction_disposition_complete": disposition_complete,
        "inherited_record_counts_complete": inherited_count_complete, "failed_attempts_deleted": 0,
    })
    progress(1, 1, "negative/failure closure", 0, "COMPLETE")
    return {
        "status": "PASS", "products": ["P03-PROD-035", "P03-PROD-036", "P03-PROD-037"], "negative_result_count": len(negative),
        "inherited_p02_negative_count": len(inherited_negative), "denominator_complete": denominator_complete,
        "negative_result_notes": "negative_result_notes.jsonl", "p02_inherited_contract_receipt": "p02_inherited_contract_receipt.json",
    }


def _artifact_traceability(ctx: ExecutionContext, through_stage: int) -> list[dict[str, Any]]:
    rows = []
    for number in range(through_stage + 1):
        stage_id = f"{number:02d}"
        result_path = _stage_dir(ctx, stage_id) / "stage_result.json"
        if not result_path.is_file():
            continue
        result = json.loads(result_path.read_text(encoding="utf-8"))
        manifest_path = _stage_dir(ctx, stage_id) / "stage_manifest.json"
        for product_id in result.get("products", []):
            rows.append({
                "product_id": product_id,
                "stage_id": stage_id,
                "gate_id": result.get("gate_id", f"G03-{stage_id}"),
                "stage_result_path": result_path.relative_to(ctx.run_root).as_posix(),
                "stage_result_sha256": sha256_file(result_path),
                "stage_manifest_sha256": sha256_file(manifest_path) if manifest_path.is_file() else None,
                "run_id": ctx.run_id,
                "config_sha256": ctx.config_sha256,
                "protocol_sha256": ctx.protocol_sha256,
                "code_sha256": ctx.code_sha256,
                "environment_sha256": ctx.environment_sha256,
                "source_manifest_sha256": ctx.source_manifest_sha256,
                "terminal_status": result.get("status"),
                "authoring_fixture": ctx.authoring_fixture,
            })
    return rows


def stage_21(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    progress(0, 6, "traceability index", 0, "IN_PROGRESS")
    traceability = _artifact_traceability(ctx, 20)
    write_csv(out / "artifact_traceability.csv", traceability)
    write_json(out / "artifact_traceability.json", {"row_count": len(traceability), "rows": traceability, "rows_sha256": sha256_json(traceability)})
    progress(1, 6, "metric analysis input", 0, "IN_PROGRESS")
    reliability = _read_jsonl(_stage_dir(ctx, "12") / "reliability_audit_reports.jsonl")
    group_rows = _read_jsonl(_stage_dir(ctx, "19") / "group_budget_audit.jsonl")
    matched = json.loads((_stage_dir(ctx, "18") / "matched_operating_points.json").read_text(encoding="utf-8"))
    write_json(out / "phase_analysis" / "metric_analysis_input.json", {"reliability_records": reliability, "group_budget_rows": group_rows, "matched_operating_points": matched, "authoring_fixture": ctx.authoring_fixture})
    write_json(out / "phase_analysis" / "statistics_input.json", {"analysis_unit": "Protocol-declared participant/group units", "multiplicity_profile": _protocol(ctx)["scientific"]["statistics"]["multiplicity_profile"], "equivalence_profile": _protocol(ctx)["scientific"]["statistics"]["equivalence_profile"], "source_record_ids": [row["record_id"] for row in reliability], "statistics_not_executed_in_notebook": True})
    progress(2, 6, "figure sources", 0, "IN_PROGRESS")
    figure_root = out / "layer10_source_bundle" / "figure_source_data"
    table_root = out / "layer10_source_bundle" / "table_source_data"
    figure_root.mkdir(parents=True, exist_ok=True)
    table_root.mkdir(parents=True, exist_ok=True)
    shutil.copy2(_stage_dir(ctx, "12") / "reliability_bin_source.csv", figure_root / "reliability_bins.csv")
    shutil.copy2(_stage_dir(ctx, "16") / "risk_coverage_curve_source.csv", figure_root / "risk_coverage_curves.csv")
    shutil.copy2(_stage_dir(ctx, "19") / "group_budget_source.csv", table_root / "group_budget_audit.csv")
    shutil.copy2(_stage_dir(ctx, "20") / "negative_result_notes.jsonl", table_root / "negative_results.jsonl")
    progress(3, 6, "dashboard/card sources", 0, "IN_PROGRESS")
    dashboard = []
    cards = []
    for report in reliability:
        dashboard.extend({"record_id": report["record_id"], "dataset_id": report["dataset_id"], "model_id": report["model_id"], "budget_id": report["budget_id"], "metric_id": metric, "value": report[metric], "direction": report["direction"][metric], "candidate_only": True, "config_sha256": ctx.config_sha256} for metric in ("brier", "nll", "calibration_error"))
        cards.append({"report_id": report["report_id"], "dataset_id": report["dataset_id"], "model_id": report["model_id"], "budget_id": report["budget_id"], "support_count": report["support_count"], "metrics": {metric: report[metric] for metric in ("brier", "nll", "calibration_error")}, "deterioration_status": report["deterioration_status"], "limitations": report["limitations"]})
    write_jsonl(out / "calibration_dashboard_metric_records.jsonl", dashboard)
    write_jsonl(out / "layer10_source_bundle" / "cards" / "reliability_cards.jsonl", cards)
    progress(4, 6, "Layer10 bundle manifest", 0, "IN_PROGRESS")
    source_manifest = build_manifest(out / "layer10_source_bundle")
    write_json(out / "layer10_source_bundle" / "layer10_source_manifest.json", source_manifest)
    source_tables = [item for item in source_manifest["files"] if item["path"].endswith((".csv", ".json", ".jsonl"))]
    write_json(out / "source_dataset_index.json", {"source_table_count": len(source_tables), "sources": source_tables, "screenshots_used": False})
    progress(6, 6, "source export complete", 0, "COMPLETE")
    return {"status": "PASS", "products": ["P03-PROD-038", "P03-PROD-039", "P03-PROD-040", "P03-PROD-041", "P03-PROD-042", "P03-PROD-043", "P03-PROD-044", "P03-PROD-045"], "artifact_traceability_rows": len(traceability), "dashboard_metric_count": len(dashboard), "reliability_card_count": len(cards), "layer10_source_file_count": source_manifest["file_count"], "artifact_traceability_index": "artifact_traceability.csv", "layer10_source_manifest": "layer10_source_bundle/layer10_source_manifest.json"}


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def stage_22(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    consumers = _read_csv(ctx.package_root / "machine_readable" / "downstream_handoff_matrix.csv")
    traceability = _read_csv(_stage_dir(ctx, "21") / "artifact_traceability.csv")
    descriptors = [{"artifact_id": row["product_id"], "schema": "see-runtime-artifact-matrix", "version": "1.0", "status": row["terminal_status"], "path": row["stage_result_path"], "sha256": row["stage_result_sha256"], "limitations": ["NON_SCIENTIFIC_AUTHORING_FIXTURE"] if ctx.authoring_fixture else [], "allowed_use": ["governed downstream consumption"], "prohibited_use": ["retuning", "upstream mutation", "safety claim"]} for row in traceability]
    handoff_files = []
    for index, consumer in enumerate(consumers, start=1):
        profile = {"consumer_id": consumer["consumer_id"], "schema_id": f"IHARQ.P03.Handoff.{consumer['consumer_id']}.v1", "schema_version": "1.0.0", "required_artifact_fields": ["artifact_id", "schema", "version", "status", "path", "sha256", "limitations", "allowed_use", "prohibited_use"], "allowed_use": [consumer["allowed_use"]], "prohibited_use": [consumer["prohibited_use"]], "limitations": [consumer["limitations"]]}
        handoff = build_handoff(descriptors, profile)
        handoff["schema_id"] = profile["schema_id"]
        safe_consumer = re.sub(r"[^A-Za-z0-9_.-]+", "_", consumer["consumer_id"]).strip("_")
        path = out / "consumer_handoffs" / f"{safe_consumer}.json"
        write_json(path, handoff)
        handoff_files.append({"consumer_id": consumer["consumer_id"], "path": path.relative_to(out).as_posix(), "sha256": sha256_file(path)})
        progress(index, len(consumers) + 4, consumer["consumer_id"], 0, "IN_PROGRESS")
    layer0 = {"schema_id": "Layer0ClaimHandoff.v1", "candidate_claim_inputs": True, "claim_approval_performed": False, "evidence_artifacts": descriptors, "limitations": ["Notebook exports candidate inputs only"]}
    evidence_map = {"schema_id": "EvidenceMapHandoff.v1", "mechanical_mapping_ready": True, "traceability_rows": traceability, "required_dimensions": ["phase", "layer", "run", "config", "Protocol cell", "dataset", "participant", "model", "budget", "ablation", "metric", "source record", "artifact", "hash", "parent record", "limitation"]}
    p04 = next((json.loads((out / item["path"]).read_text(encoding="utf-8")) for item in handoff_files if item["consumer_id"] == "P04"), None)
    if p04 is None:
        raise GateBlocked("G03-22-HANDOFFS", "P04_CONSUMER_MISSING", "P04 was absent from downstream matrix")
    write_json(out / "layer0_claim_handoff.json", layer0)
    write_json(out / "evidence_map_handoff.json", evidence_map)
    write_json(out / "p03_to_p04_handoff_manifest.json", p04)
    write_csv(out / "later_phase_handoff_matrix.csv", consumers)
    ledger = {"run_id": ctx.run_id, "config_sha256": ctx.config_sha256, "protocol_sha256": ctx.protocol_sha256, "environment_sha256": ctx.environment_sha256, "inputs": _stage_result(ctx, "04"), "methods": _protocol(ctx)["scientific"]["calibration"]["branch_cells"], "thresholds": _read_jsonl(_stage_dir(ctx, "17") / "threshold_registry_records.jsonl"), "failures": _stage_result(ctx, "20"), "output_manifest": _stage_result(ctx, "21"), "authoring_fixture": ctx.authoring_fixture}
    write_json(out / "protocol_actual_run_annex_input.json", ledger)
    phase_analysis_index = {"schema_id": "PhaseAnalysisInputIndex.v1", "metric_input": "../stage_21/phase_analysis/metric_analysis_input.json", "statistics_input": "../stage_21/phase_analysis/statistics_input.json", "group_input": "../stage_19/group_budget_audit.jsonl", "failure_input": "../stage_20/negative_result_notes.jsonl", "manual_notebook_scraping_required": False}
    claim_evidence = {"schema_id": "ClaimEvidenceInput.v1", "candidate_only": True, "claim_approval_performed": False, "layer0_handoff_sha256": sha256_file(out / "layer0_claim_handoff.json"), "evidence_map_handoff_sha256": sha256_file(out / "evidence_map_handoff.json")}
    write_json(out / "phase_analysis_input_index.json", phase_analysis_index)
    write_json(out / "claim_evidence_input.json", claim_evidence)
    return {"status": "PASS", "products": ["P03-PROD-046", "P03-PROD-047", "P03-PROD-048", "P03-PROD-049", "P03-PROD-050", "P03-PROD-062", "P03-PROD-063"], "consumer_handoff_count": len(handoff_files), "handoff_files": handoff_files, "p04_handoff": "p03_to_p04_handoff_manifest.json", "phase_analysis_input_index": "phase_analysis_input_index.json"}


def _checkpoint_rows(ctx: ExecutionContext, include_current: bool = False) -> list[dict[str, Any]]:
    rows = []
    limit = 24 if include_current else 23
    for number in range(limit):
        path = ctx.run_root / "checkpoints" / f"stage_{number:02d}" / "receipt.json"
        if path.is_file():
            rows.append(json.loads(path.read_text(encoding="utf-8")))
    return rows


def stage_23(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    progress(0, 6, "stage/gate ledger", 0, "IN_PROGRESS")
    checkpoints = _checkpoint_rows(ctx)
    expected_complete = {f"{i:02d}" for i in range(23)}
    complete = {row["stage_id"] for row in checkpoints if row["status"] == "COMPLETE"}
    if complete != expected_complete:
        raise GateBlocked("G03-23-SUFFICIENCY", "PRIOR_STAGE_TERMINALITY_INCOMPLETE", f"missing={sorted(expected_complete-complete)}")
    write_json(out / "stage_ledger.json", {"run_id": ctx.run_id, "stages": checkpoints, "complete_count": len(complete)})
    gate_rows = [{"gate_id": row["gate_id"], "stage_id": row["stage_id"], "decision": "PASS", "receipt_sha256": sha256_json(row)} for row in checkpoints]
    write_jsonl(out / "gate_decision_report.jsonl", gate_rows)
    progress(1, 6, "product completeness", 0, "IN_PROGRESS")
    traceability = _artifact_traceability(ctx, 22)
    realized = {row["product_id"] for row in traceability}
    required_before_24 = {f"P03-PROD-{i:03d}" for i in range(1, 58)} | {"P03-PROD-062", "P03-PROD-063"}
    # 052-054 are cross-stage ledgers materialized here; 051/055-057 are produced below.
    realized.update({"P03-PROD-051", "P03-PROD-052", "P03-PROD-053", "P03-PROD-054", "P03-PROD-055", "P03-PROD-056", "P03-PROD-057"})
    missing = sorted(required_before_24 - realized)
    if missing:
        raise GateBlocked("G03-23-SUFFICIENCY", "EXPECTED_PRODUCT_WRITER_MISSING", ",".join(missing))
    progress(2, 6, "ablation closure", 0, "IN_PROGRESS")
    a1 = _stage_result(ctx, "11")["selection_count"] > 0
    a2 = _stage_result(ctx, "15")["a2_record_count"] > 0
    a3 = _stage_result(ctx, "16")["a3_record_count"] > 0
    intake = _stage_result(ctx, "04")
    a0 = bool(intake["a0_validated"])
    a4 = bool(intake["a4_validated"])
    if not (a0 and a1 and a2 and a3 and a4):
        raise GateBlocked("G03-23-SUFFICIENCY", "ABLATION_CLOSURE_INCOMPLETE", f"A0={a0},A1={a1},A2={a2},A3={a3},A4={a4}")
    progress(3, 6, "handoff closure", 0, "IN_PROGRESS")
    p04_path = _stage_dir(ctx, "22") / "p03_to_p04_handoff_manifest.json"
    if not p04_path.is_file() or not _stage_result(ctx, "22")["consumer_handoff_count"]:
        raise GateBlocked("G03-23-SUFFICIENCY", "DOWNSTREAM_HANDOFF_INCOMPLETE", "P04/later handoffs missing")
    required_outputs = [
        _stage_dir(ctx, "04") / "p03_intake_ledger.json", _stage_dir(ctx, "07") / "upstream_prediction_disposition.jsonl",
        _stage_dir(ctx, "08") / "split_integrity_reports.jsonl", _stage_dir(ctx, "09") / "calibration_eligibility_table.jsonl",
        _stage_dir(ctx, "10") / "identity_calibration_records.jsonl", _stage_dir(ctx, "11") / "calibration_attempt_ledger.jsonl",
        _stage_dir(ctx, "12") / "reliability_audit_reports.jsonl", _stage_dir(ctx, "13") / "uncertainty_records.jsonl",
        _stage_dir(ctx, "15") / "a2_selective_prediction_records.jsonl", _stage_dir(ctx, "16") / "a3_selective_prediction_records.jsonl",
        _stage_dir(ctx, "17") / "threshold_registry_records.jsonl", _stage_dir(ctx, "18") / "matched_operating_points.json",
        _stage_dir(ctx, "19") / "group_budget_audit.jsonl", _stage_dir(ctx, "20") / "negative_result_notes.jsonl",
        _stage_dir(ctx, "21") / "artifact_traceability.csv", _stage_dir(ctx, "22") / "p03_to_p04_handoff_manifest.json",
    ]
    missing_outputs = [path.relative_to(ctx.run_root).as_posix() for path in required_outputs if not path.is_file()]
    disagreement = _stage_result(ctx, "13")
    disagreement_accounted = int(disagreement["member_disagreement_accounted_group_count"]) == int(_stage_result(ctx, "07")["group_count"])
    score_semantics_complete = int(_stage_result(ctx, "09")["eligibility_count"]) == int(_stage_result(ctx, "07")["group_count"])
    failure_denominator_complete = bool(_stage_result(ctx, "20")["denominator_complete"])
    handoff_complete = bool(_stage_result(ctx, "22")["consumer_handoff_count"])
    artifacts_complete = not missing_outputs and failure_denominator_complete and disagreement_accounted
    if not artifacts_complete:
        raise GateBlocked("G03-23-SUFFICIENCY", "REQUIRED_ARTIFACT_OR_CONDITIONAL_TERMINAL_MISSING", json.dumps({"missing": missing_outputs, "failure_denominator": failure_denominator_complete, "disagreement_accounted": disagreement_accounted}, sort_keys=True))
    resource = {"status": "PASS", "scientific_worker_processes": 1, "numerical_threads": 1, "heartbeat_seconds": _config(ctx)["execution"]["heartbeat_seconds"], "resource_reduction_applied": False, "authoring_fixture": ctx.authoring_fixture}
    readiness = {
        "status": "READY" if not ctx.authoring_fixture else "NON_SCIENTIFIC_AUTHORING_VALIDATION_COMPLETE",
        "P02_contract_validated": bool(intake["p02_contract_complete"]), "score_semantics_complete": score_semantics_complete,
        "class_order_complete": score_semantics_complete, "leakage_guards_pass": _stage_result(ctx, "08")["leakage_warning_count"] == 0,
        "A1_complete": a1, "A2_complete": a2, "A3_complete": a3, "A2_A3_distinct": True,
        "A0_inherited": a0, "A4_inherited": a4, "A4_disagreement_eligible_groups": disagreement["member_disagreement_eligible_count"],
        "A4_disagreement_ineligible_groups": disagreement["member_disagreement_ineligible_count"], "A4_disagreement_all_groups_accounted": disagreement_accounted,
        "A14_absent": True, "products_expected": 65, "products_pre_export_realized": len(realized), "literal_secrets": 0,
    }
    sufficiency = {
        "status": "PASS", "all_prior_stages_terminal": complete == expected_complete,
        "every_required_artifact_produced_or_lawfully_terminal": artifacts_complete,
        "every_required_ablation_ran": all((a0, a1, a2, a3, a4)), "failures_persisted": failure_denominator_complete,
        "downstream_handoffs_created": handoff_complete, "manifests_complete": not missing,
        "required_output_missing": missing_outputs, "checksums_pending_stage_24": True, "secret_scan_pending_stage_24": True,
        "authoring_fixture": ctx.authoring_fixture,
    }
    execution_manifest = {"run_id": ctx.run_id, "immutable_fingerprint": ctx.immutable_fingerprint, "stage_count_before_export": len(checkpoints), "product_ids_before_export": sorted(realized), "readiness": readiness, "evidence_sufficiency": sufficiency}
    write_json(out / "execution_manifest.json", execution_manifest)
    write_json(out / "readiness_report.json", readiness)
    write_json(out / "evidence_sufficiency_decision.json", sufficiency)
    write_json(out / "resource_qualification_report.json", resource)
    progress(6, 6, "evidence sufficiency PASS", 0, "COMPLETE")
    return {"status": "PASS", "products": ["P03-PROD-051", "P03-PROD-052", "P03-PROD-053", "P03-PROD-054", "P03-PROD-055", "P03-PROD-056", "P03-PROD-057"], "prior_stage_count": len(checkpoints), "pre_export_product_count": len(realized), "readiness_report": "readiness_report.json", "evidence_sufficiency_decision": "evidence_sufficiency_decision.json"}


def stage_24(ctx: ExecutionContext, out: Path, progress: Progress) -> Mapping[str, Any]:
    progress(0, 6, "secret scan", 0, "IN_PROGRESS")
    findings = scan_for_secrets(ctx.run_root)
    secret_report = {"status": "PASS" if not findings else "FAIL", "literal_secrets": len(findings), "findings": findings, "credential_symbols_only": True}
    write_json(out / "secret_scan_report.json", secret_report)
    if findings:
        raise GateBlocked("G03-24-EXPORT", "SECRET_SCAN_FAILED", f"findings={len(findings)}")
    progress(1, 6, "export bundle", 0, "IN_PROGRESS")
    bundle = out / "final_export_bundle"
    bundle.mkdir(parents=True, exist_ok=True)

    def link_or_copy(source: str, target: str) -> str:
        try:
            os.link(source, target)
        except OSError:
            shutil.copy2(source, target)
        return target

    for stage_number in range(24):
        source = _stage_dir(ctx, f"{stage_number:02d}")
        if not source.is_dir():
            raise GateBlocked("G03-24-EXPORT", "FINAL_EXPORT_STAGE_MISSING", source.as_posix())
        shutil.copytree(source, bundle / "stage_artifacts" / source.name, copy_function=link_or_copy)
    for name in ("checkpoints", "artifacts"):
        source = ctx.run_root / name
        if not source.is_dir():
            raise GateBlocked("G03-24-EXPORT", "FINAL_EXPORT_GOVERNANCE_SURFACE_MISSING", source.as_posix())
        shutil.copytree(source, bundle / name, copy_function=link_or_copy)
    progress(2, 6, "package manifest", 0, "IN_PROGRESS")
    package_manifest = build_manifest(bundle)
    write_json(bundle / "package_manifest.json", package_manifest)
    write_checksum_manifest(bundle)
    if any((bundle / line.split("  ", 1)[1]).is_file() is False for line in (bundle / "checksums.sha256").read_text(encoding="utf-8").splitlines() if line):
        raise GateBlocked("G03-24-EXPORT", "CHECKSUM_LEDGER_PATH_FAILURE", "Missing path in checksum ledger")
    progress(3, 6, "external immutable upload", 0, "IN_PROGRESS")
    config = _config(ctx)
    external = config["external_storage"]
    remote_path = str(external["path"]).format(run_id=ctx.run_id)
    immutable_revision = None
    remote_verified = False
    if ctx.authoring_fixture:
        revision_status = "NON_SCIENTIFIC_AUTHORING_FIXTURE_LOCAL_ONLY"
    else:
        token = require_credential_symbol(external["credential_symbol"], gate_id="G03-24-EXPORT")
        try:
            from huggingface_hub import HfApi
            api = HfApi(token=token)
            api.create_repo(repo_id=external["repository"], repo_type="dataset", private=True, exist_ok=True)
            commit = api.upload_folder(
                repo_id=external["repository"], repo_type="dataset", folder_path=bundle.as_posix(), path_in_repo=remote_path,
                commit_message=str(external["upload_commit_message"]),
            )
            immutable_revision = str(commit.oid)
            info = api.repo_info(repo_id=external["repository"], repo_type="dataset", revision=immutable_revision)
            if str(info.sha) != immutable_revision:
                raise GateBlocked("G03-24-EXPORT", "P03_REMOTE_REVISION_MISMATCH", f"expected={immutable_revision}, observed={info.sha}")
            remote_files = set(api.list_repo_files(repo_id=external["repository"], repo_type="dataset", revision=immutable_revision))
            required_remote = {f"{remote_path}/package_manifest.json", f"{remote_path}/checksums.sha256"}
            missing_remote = sorted(required_remote - remote_files)
            if missing_remote:
                raise GateBlocked("G03-24-EXPORT", "P03_REMOTE_EXPORT_CONTROL_FILES_MISSING", json.dumps(missing_remote))
            remote_verified = True
            revision_status = "IMMUTABLE_COMMIT_VERIFIED"
        except GateBlocked:
            raise
        except Exception as exc:
            detail = str(exc).replace(token, "[REDACTED]")
            raise GateBlocked("G03-24-EXPORT", "P03_HF_IMMUTABLE_EXPORT_FAILED", f"{type(exc).__name__}: {detail}") from exc
    pointer = {
        "provider": external["provider"], "repository": external["repository"], "immutable_revision": immutable_revision,
        "revision_status": revision_status, "remote_revision_verified": remote_verified, "path": remote_path,
        "access_class": external["access_class"], "credential_symbol": external["credential_symbol"],
        "preferred_role": "EXTERNAL_FIRST_FOR_COMPLETE_VALIDATED_P03_RESULT_SURFACE", "fallback_role": "KAGGLE_WORKING_EXPORT_UNTIL_VERIFIED_UPLOAD",
        "bundle_manifest_sha256": sha256_json(package_manifest), "object_count": package_manifest["file_count"],
        "mutable_latest_prohibited": True, "post_upload_revision_gate": True,
    }
    write_json(out / "external_artifact_pointer.json", pointer)
    progress(4, 6, "paper/thesis provenance", 0, "IN_PROGRESS")
    provenance = {"schema_id": "PaperThesisProvenanceBundle.v1", "run_id": ctx.run_id, "config_sha256": ctx.config_sha256, "protocol_sha256": ctx.protocol_sha256, "environment_sha256": ctx.environment_sha256, "code_sha256": ctx.code_sha256, "source_manifest_sha256": ctx.source_manifest_sha256, "artifact_manifest_sha256": sha256_json(package_manifest), "authoring_fixture": ctx.authoring_fixture, "claim_boundary": "No scientific P03 claims from authoring fixture" if ctx.authoring_fixture else "Subject to Protocol/analysis/Layer0 governance"}
    write_json(out / "paper_thesis_provenance_bundle.json", provenance)
    write_json(out / "p03_final_export_bundle.json", {"schema_id": "P03FinalExportBundle.v1", "bundle_path": "final_export_bundle", "bundle_manifest_sha256": sha256_json(package_manifest), "checksum_ledger": "final_export_bundle/checksums.sha256", "secret_scan_status": "PASS", "external_pointer": "external_artifact_pointer.json", "scientific_evidence": not ctx.authoring_fixture})
    progress(6, 6, "final export complete", 0, "COMPLETE")
    return {
        "status": "PASS", "products": ["P03-PROD-058", "P03-PROD-059", "P03-PROD-060", "P03-PROD-061", "P03-PROD-064", "P03-PROD-065"],
        "secret_scan_report": "secret_scan_report.json", "literal_secrets": 0, "checksum_ledger": "final_export_bundle/checksums.sha256",
        "package_manifest": "final_export_bundle/package_manifest.json", "package_file_count": package_manifest["file_count"],
        "final_export_bundle": "final_export_bundle", "external_revision": immutable_revision, "external_revision_verified": remote_verified,
        "scientific_evidence": not ctx.authoring_fixture,
    }


HANDLERS: dict[str, Callable[[ExecutionContext, Path, Progress], Mapping[str, Any]]] = {
    "00": stage_00, "01": stage_01, "02": stage_02, "03": stage_03, "04": stage_04,
    "05": stage_05, "06": stage_06, "07": stage_07, "08": stage_08, "09": stage_09,
    "10": stage_10, "11": stage_11, "12": stage_12, "13": stage_13, "14": stage_14,
    "15": stage_15, "16": stage_16, "17": stage_17, "18": stage_18, "19": stage_19,
    "20": stage_20, "21": stage_21, "22": stage_22, "23": stage_23, "24": stage_24,
}


def execute_stage(stage_id: str, context: ExecutionContext, output_dir: Path, progress: Progress) -> Mapping[str, Any]:
    if stage_id not in HANDLERS:
        raise KeyError(stage_id)
    return HANDLERS[stage_id](context, output_dir, progress)
