"""Kaggle/local source discovery, immutable overlay application, and context creation."""

from __future__ import annotations

import importlib.metadata
import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any, Iterable, Sequence

import yaml

from .identity import deterministic_id, sha256_file, sha256_json, utc_now
from .models import ExecutionContext
from .writers import build_manifest, write_json


def _deterministic_tree_files(root: str | Path, *, suffixes: set[str] | None = None) -> list[dict[str, Any]]:
    """Content-only tree inventory for stable fingerprints.

    Runtime bytecode/cache products are deliberately excluded so compileall or a
    kernel restart cannot create a new official run identity for unchanged source.
    """
    root = Path(root).resolve()
    files: list[dict[str, Any]] = []
    if not root.exists():
        return files
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        relative = path.relative_to(root)
        if "__pycache__" in relative.parts or path.suffix in {".pyc", ".pyo"}:
            continue
        if suffixes is not None and path.suffix not in suffixes:
            continue
        files.append({"path": relative.as_posix(), "bytes": path.stat().st_size, "sha256": sha256_file(path)})
    return files


def _capable(root: Path, relatives: Sequence[str]) -> bool:
    return all((root / relative).exists() for relative in relatives)


def discover_unique_root(search_roots: Iterable[str | Path], relatives: Sequence[str], label: str) -> Path:
    matches: set[Path] = set()
    for search_root in map(Path, search_roots):
        if not search_root.exists():
            continue
        if _capable(search_root, relatives):
            matches.add(search_root.resolve())
        anchor = Path(relatives[0]).name
        for path in search_root.rglob(anchor):
            candidate = path
            for _ in Path(relatives[0]).parts:
                candidate = candidate.parent
            if _capable(candidate, relatives):
                matches.add(candidate.resolve())
    if len(matches) != 1:
        raise RuntimeError(f"{label}_RESOLUTION_EXPECTED_ONE: found={len(matches)} candidates={[p.as_posix() for p in sorted(matches)]}")
    return next(iter(matches))


def discover_cumulative_repository(search_roots: Iterable[str | Path]) -> Path:
    return discover_unique_root(search_roots, ["pyproject.toml", "src/iharq/layer2_decoders/__init__.py", "src/iharq/layer3_calibration_uncertainty/__init__.py"], "CUMULATIVE_P02_REPOSITORY")


def discover_companion_package(search_roots: Iterable[str | Path]) -> Path:
    return discover_unique_root(search_roots, ["repository_patch/src/iharq/layer3_calibration_uncertainty/stages.py", "machine_readable/runtime_artifact_matrix.csv", "IHARQ_Phase_03_Layer_03_Complete_Execution_R2.ipynb"], "P03_COMPANION_PACKAGE")


def validate_bundled_repository_base(companion_root: str | Path) -> dict[str, Any]:
    """Verify the accepted, executable P02 repository surface bundled with P03.

    This is code/config/schema provenance only. P02 scientific/runtime artifacts are
    never sourced from this directory; Stage 03 retrieves those from the frozen HF
    dataset revision.
    """
    companion_root = Path(companion_root).resolve()
    base = companion_root / "repository_base"
    manifest_path = companion_root / "machine_readable" / "cumulative_repository_base_manifest.json"
    if not base.is_dir() or not manifest_path.is_file():
        raise RuntimeError("BUNDLED_CUMULATIVE_REPOSITORY_BASE_MISSING")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    failures = []
    for item in manifest.get("files", []):
        relative = Path(str(item["path"]))
        target = (base / relative).resolve()
        if base not in target.parents or not target.is_file():
            failures.append({"path": relative.as_posix(), "reason": "MISSING_OR_UNSAFE"})
        elif target.stat().st_size != int(item["size_bytes"]):
            failures.append({"path": relative.as_posix(), "reason": "SIZE_MISMATCH"})
        elif sha256_file(target) != str(item["sha256"]):
            failures.append({"path": relative.as_posix(), "reason": "SHA256_MISMATCH"})
    if len(manifest.get("files", [])) != int(manifest.get("file_count", -1)) or failures:
        raise RuntimeError(f"BUNDLED_CUMULATIVE_REPOSITORY_BASE_INTEGRITY_FAILED: {failures[:5]}")
    required = ["pyproject.toml", "src/iharq/layer2_decoders/__init__.py", "src/iharq/layer3_calibration_uncertainty/__init__.py"]
    if not _capable(base, required):
        raise RuntimeError("BUNDLED_CUMULATIVE_REPOSITORY_BASE_CAPABILITY_FAILED")
    return {
        "status": "PASS",
        "base_root": base.as_posix(),
        "file_count": manifest["file_count"],
        "manifest_sha256": sha256_file(manifest_path),
        "scientific_runtime_artifacts_included": False,
    }


def prepare_working_repository(cumulative_root: str | Path, companion_root: str | Path, destination: str | Path) -> dict[str, Any]:
    """Copy the executable repository surface and apply the additive P03 overlay.

    A recognized prior P03 working-repository copy may be rebuilt when the bundled
    base/overlay fingerprint changes (for example, a governed C2 -> C3 repair).
    Unrecognized directories are never overwritten.
    """
    cumulative_root, companion_root, destination = Path(cumulative_root), Path(companion_root), Path(destination)
    base_receipt = None
    if cumulative_root.resolve() == (companion_root.resolve() / "repository_base"):
        base_receipt = validate_bundled_repository_base(companion_root)
    patch = companion_root / "repository_patch"
    expected_overlay_sha = sha256_json(_deterministic_tree_files(patch))
    expected_base_manifest_sha = base_receipt.get("manifest_sha256") if base_receipt else None
    repository_rebuilt = False
    superseded_overlay_sha = None
    if destination.exists():
        marker = destination / ".p03_overlay_receipt.json"
        if not marker.is_file():
            raise RuntimeError(f"Refusing to overwrite unrecognized working repository: {destination}")
        prior = json.loads(marker.read_text(encoding="utf-8"))
        prior_overlay_sha = prior.get("overlay_manifest_sha256")
        prior_base_sha = (prior.get("bundled_base_validation") or {}).get("manifest_sha256")
        if prior_overlay_sha == expected_overlay_sha and (expected_base_manifest_sha is None or prior_base_sha == expected_base_manifest_sha):
            return prior
        superseded_overlay_sha = prior_overlay_sha
        shutil.rmtree(destination)
        repository_rebuilt = True
    destination.mkdir(parents=True)
    for name in ("src", "schemas", "configs"):
        source = cumulative_root / name
        if source.exists():
            shutil.copytree(source, destination / name)
    for name in ("pyproject.toml", "LICENSE", "README.md"):
        source = cumulative_root / name
        if source.is_file():
            shutil.copy2(source, destination / name)
    for name in ("src", "schemas", "configs", "tests"):
        source = patch / name
        if source.exists():
            shutil.copytree(source, destination / name, dirs_exist_ok=True)
    for name in ("requirements-p03-lock.txt", "pyproject.p03.overlay.toml"):
        source = patch / name
        if source.is_file():
            shutil.copy2(source, destination / name)
    receipt = {
        "status": "PASS",
        "cumulative_source_root": cumulative_root.resolve().as_posix(),
        "companion_package_root": companion_root.resolve().as_posix(),
        "working_repository_root": destination.resolve().as_posix(),
        "upstream_source_mutated": False,
        "overlay_manifest_sha256": expected_overlay_sha,
        "repository_rebuilt_due_to_overlay_change": repository_rebuilt,
        "superseded_overlay_manifest_sha256": superseded_overlay_sha,
        "bundled_base_validation": base_receipt,
        "p02_package_preserved": (destination / "src/iharq/layer2_decoders").is_dir(),
        "p03_stub_replaced": "SCIENTIFIC_EXECUTION = False" not in (destination / "src/iharq/layer3_calibration_uncertainty/__init__.py").read_text(encoding="utf-8"),
    }
    write_json(destination / ".p03_overlay_receipt.json", receipt)
    return receipt


def _environment_identity() -> dict[str, Any]:
    names = ["moabb", "mne", "numpy", "scipy", "pandas", "scikit-learn", "h5py", "pooch", "PyYAML", "pydantic", "jsonschema", "nbformat", "pytest", "typer", "huggingface-hub", "torch", "torchaudio", "torchvision", "braindecode", "pyriemann", "safetensors"]
    versions = {}
    for name in names:
        try:
            versions[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            versions[name] = None
    # C7-GPU: hardware is part of the exact execution environment because GPU
    # inference is an explicitly governed numerical execution path.  This keeps
    # replay caches/run identities from crossing GPU models or device counts.
    gpu = {"available": False, "device_count": 0, "devices": [], "torch_cuda": None, "cudnn": None}
    try:
        import torch
        gpu["available"] = bool(torch.cuda.is_available())
        gpu["device_count"] = int(torch.cuda.device_count()) if gpu["available"] else 0
        gpu["torch_cuda"] = torch.version.cuda
        gpu["cudnn"] = None if not gpu["available"] else int(torch.backends.cudnn.version() or 0)
        if gpu["available"]:
            for index in range(gpu["device_count"]):
                props = torch.cuda.get_device_properties(index)
                gpu["devices"].append({
                    "index": index,
                    "name": str(props.name),
                    "capability": [int(props.major), int(props.minor)],
                    "total_memory_bytes": int(props.total_memory),
                    "multi_processor_count": int(props.multi_processor_count),
                })
    except Exception as exc:
        gpu["probe_error"] = f"{type(exc).__name__}:{exc}"
    return {"python": sys.version.split()[0], "packages": versions, "platform": sys.platform, "gpu": gpu}


def create_execution_context(
    *,
    repository_root: str | Path,
    package_root: str | Path,
    working_root: str | Path,
    config_path: str | Path,
    protocol_path: str | Path,
    authoring_fixture: bool = False,
) -> ExecutionContext:
    repository_root, package_root, working_root = Path(repository_root).resolve(), Path(package_root).resolve(), Path(working_root).resolve()
    config_path, protocol_path = Path(config_path).resolve(), Path(protocol_path).resolve()
    with config_path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    with protocol_path.open("r", encoding="utf-8") as handle:
        protocol = yaml.safe_load(handle)
    config_sha, protocol_sha = sha256_json(config), sha256_json(protocol)
    code_manifest = _deterministic_tree_files(
        repository_root / "src" / "iharq" / "layer3_calibration_uncertainty",
        suffixes={".py"},
    )
    code_sha = sha256_json(code_manifest)
    environment_sha = sha256_json(_environment_identity())
    source_manifest_path = package_root / "machine_readable" / "source_intake_manifest.json"
    source_manifest_sha = sha256_file(source_manifest_path)
    identity = {"config": config_sha, "protocol": protocol_sha, "code": code_sha, "environment": environment_sha, "sources": source_manifest_sha, "fixture": authoring_fixture}
    prefix = "P03-L3-AUTHORING-FIXTURE" if authoring_fixture else "P03-L3-OFFICIAL"
    run_id = deterministic_id(prefix, identity, length=16)
    runtime_relative = Path(config["paths"]["runtime_root"])
    run_root = working_root / runtime_relative / run_id
    run_root.mkdir(parents=True, exist_ok=True)
    context = ExecutionContext(
        run_id=run_id,
        run_root=run_root,
        repository_root=repository_root,
        package_root=package_root,
        config_path=config_path,
        protocol_path=protocol_path,
        config_sha256=config_sha,
        protocol_snapshot_id=str(protocol.get("protocol_id", "UNPOPULATED-P03-PROTOCOL")),
        protocol_sha256=protocol_sha,
        code_sha256=code_sha,
        environment_sha256=environment_sha,
        source_manifest_sha256=source_manifest_sha,
        created_at_utc=utc_now(),
        authoring_fixture=authoring_fixture,
    )
    write_json(run_root / "execution_context.json", {**context.immutable_fingerprint, "run_root": run_root.as_posix(), "repository_root": repository_root.as_posix(), "package_root": package_root.as_posix(), "config_path": config_path.as_posix(), "protocol_path": protocol_path.as_posix(), "created_at_utc": context.created_at_utc, "authoring_fixture": authoring_fixture})
    return context


def context_from_record(path: str | Path) -> ExecutionContext:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return ExecutionContext(
        run_id=payload["run_id"], run_root=Path(payload["run_root"]), repository_root=Path(payload["repository_root"]), package_root=Path(payload["package_root"]),
        config_path=Path(payload["config_path"]), protocol_path=Path(payload["protocol_path"]), config_sha256=payload["config_sha256"],
        protocol_snapshot_id=load_yaml_id(payload["protocol_path"]), protocol_sha256=payload["protocol_sha256"], code_sha256=payload["code_sha256"],
        environment_sha256=payload["environment_sha256"], source_manifest_sha256=payload["source_manifest_sha256"], created_at_utc=payload["created_at_utc"], authoring_fixture=bool(payload["authoring_fixture"]),
    )


def load_yaml_id(path: str | Path) -> str:
    with Path(path).open("r", encoding="utf-8") as handle:
        return str(yaml.safe_load(handle).get("protocol_id", "UNPOPULATED-P03-PROTOCOL"))
