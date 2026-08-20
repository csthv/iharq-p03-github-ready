from __future__ import annotations

from pathlib import Path
from typing import Any, Callable
import hashlib
import inspect
import json
import logging
import os
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor

POLICY = {
    "policy_id": "P01-L1-KAGGLE-THREE-SOURCE-DATASETS-R6",
    "policy_kind": "THREE_ATTACHED_KAGGLE_SOURCE_DATASETS_ONLY",
    "runtime_revision": "R26",
    "runtime_compatibility_revision": "R34-BNCI-EXACT-NATIVE-LOAD-CHECKSUM-AND-DOWNSTREAM-CONTRACT-CLOSURE",
    "scientific_freeze_unchanged": "P01-L1-OFFICIAL-RUN-FREEZE-R2",
    "active_sources": ["PhysioNetMI", "BNCI2014_001", "Lee2019_MI"],
    "physionet_public_handle": "gamalasran/physionet-eeg-motor-movement-imagery",
    "source_manifest_filename": "IHARQ_P01_L1_SOURCE_DATASET_MANIFEST.json",
    "required_file_counts": {"PhysioNetMI": 327, "BNCI2014_001": 18, "Lee2019_MI": 108},
    "moabb_downloader_used": False,
    "moabb_downloader_fallback_allowed": False,
    "source_network_download_allowed": False,
    "moabb_final_resolution_and_loading": True,
    "loading_remains_sequential": True,
    "loading_parallelism_scope": "BOUNDED_CROSS_SUBJECT_ONLY",
    "checksum_verification_unchanged": True,
    "exact_subject_provenance_unchanged": True,
    "subject_88_special_handling_unchanged": True,
    "ordinal_prefix_resolution_supported": True,
}

_PATCHED: set[type] = set()
_LOCK = threading.Lock()
_SOURCE_MAP: dict[str, dict[Any, Path]] = {}
_SOURCE_REPORT: dict[str, Any] = {"status": "NOT_PREPARED"}
_PRIVATE_INVENTORY: dict[str, dict[str, Any]] = {}
_RESOLUTION_FILE: Path | None = None


def _atomic_json(path: Path, payload: Any) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, default=str) + "\n", encoding="utf-8")
    temporary.replace(path)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _aggregate_file_digest(rows: list[dict[str, Any]]) -> str:
    h = hashlib.sha256()
    for row in sorted(rows, key=lambda x: x["relative_path"]):
        h.update(str(row["relative_path"]).encode("utf-8")); h.update(b"\0")
        h.update(str(row["sha256"]).encode("ascii")); h.update(b"\0")
        h.update(str(row["bytes"]).encode("ascii")); h.update(b"\n")
    return h.hexdigest()


def _get(value: Any, name: str, default: Any = None) -> Any:
    if isinstance(value, dict):
        return value.get(name, default)
    return getattr(value, name, default)


def _dataset_id(adapter: Any) -> str:
    profile = _get(adapter, "profile")
    identifier = _get(profile, "dataset_id")
    if not identifier:
        raise RuntimeError(f"Adapter {type(adapter).__name__} has no dataset_id.")
    return str(identifier)


def _call_filtered(original: Callable[..., Any], self: Any, args: tuple[Any, ...], kwargs: dict[str, Any], forced: dict[str, Any] | None = None) -> Any:
    signature = inspect.signature(original)
    parameters = signature.parameters
    accepts_var_kwargs = any(
        parameter.kind is inspect.Parameter.VAR_KEYWORD
        for parameter in parameters.values()
    )
    cleaned = dict(kwargs) if accepts_var_kwargs else {k: v for k, v in kwargs.items() if k in parameters}
    for key, value in (forced or {}).items():
        if accepts_var_kwargs or key in parameters:
            cleaned[key] = value
    bound = signature.bind_partial(self, *args, **cleaned)
    return original(*bound.args, **bound.kwargs)


def _resolve_manifest_payload_file(manifest_path: Path, canonical_relative: str, expected_bytes: int, expected_sha256: str) -> Path:
    """Resolve exact names and Kaggle ordinal-prefixed names without ambiguity."""
    base = manifest_path.parent
    canonical = Path(canonical_relative)
    candidates: list[Path] = []
    direct = base / canonical
    if direct.is_file():
        candidates.append(direct)
    leaf = canonical.name
    for pattern in (leaf, f"*_{leaf}"):
        candidates.extend(path for path in base.rglob(pattern) if path.is_file())
    # Preserve order but remove duplicates.
    unique: list[Path] = []
    seen: set[str] = set()
    for path in candidates:
        key = str(path.resolve())
        if key not in seen:
            seen.add(key); unique.append(path)
    sized = [path for path in unique if path.stat().st_size == int(expected_bytes)]
    if not sized:
        raise RuntimeError(
            "SOURCE_DATASET_FILE_MISSING_OR_SIZE_MISMATCH: "
            f"manifest={manifest_path}; canonical={canonical_relative}; expected_bytes={expected_bytes}"
        )
    verified = []
    for path in sized:
        observed = _sha256(path)
        if observed == str(expected_sha256).lower():
            verified.append(path)
    if len(verified) != 1:
        raise RuntimeError(
            "SOURCE_DATASET_FILE_RESOLUTION_AMBIGUOUS: "
            f"canonical={canonical_relative}; size_matches={len(sized)}; hash_matches={len(verified)}; "
            f"candidates={[str(p) for p in sized[:10]]}"
        )
    return verified[0]


def _discover_physionet(input_root: Path) -> dict[Any, Path]:
    selected: dict[tuple[int, int], Path] = {}
    for path in input_root.rglob("*.edf"):
        match = re.fullmatch(r"S(\d{3})R(\d{2})\.edf", path.name, flags=re.IGNORECASE)
        if not match:
            continue
        subject, run = int(match.group(1)), int(match.group(2))
        if not (1 <= subject <= 109 and run in {4, 8, 12}):
            continue
        key = (subject, run)
        if key in selected and selected[key].resolve() != path.resolve():
            raise RuntimeError(f"PHYSIONET_DUPLICATE_ATTACHED_SOURCE: key={key}")
        selected[key] = path
    expected = {(s, r) for s in range(1, 110) for r in (4, 8, 12)}
    missing = sorted(expected - set(selected))
    if missing:
        raise RuntimeError(
            "PHYSIONET_ATTACHED_DATASET_INCOMPLETE: "
            f"required=327; observed={len(selected)}; missing_sample={missing[:10]}"
        )
    return selected


def _load_private_source_manifests(input_root: Path) -> tuple[dict[Any, Path], dict[Any, Path], list[dict[str, Any]]]:
    """Resolve and SHA-256 verify private source files with one directory scan.

    Quality is unchanged: every declared physical byte stream is still checked
    against its manifest SHA-256. Speed comes from eliminating repeated rglob
    scans and hashing independent files concurrently with a bounded pool.
    """
    global _PRIVATE_INVENTORY
    marker = POLICY["source_manifest_filename"]
    manifests: list[dict[str, Any]] = []
    bnci: dict[tuple[int, str], Path] = {}
    lee: dict[tuple[int, int], Path] = {}
    inventories: dict[str, dict[str, Any]] = {}

    manifest_paths = sorted(input_root.rglob(marker))
    selected_manifests: list[tuple[Path, dict[str, Any]]] = []
    for path in manifest_paths:
        manifest = json.loads(path.read_text(encoding="utf-8"))
        if manifest.get("cache_kind") != "IHARQ_P01_L1_SOURCE_DATASET":
            continue
        if manifest.get("scientific_freeze") != POLICY["scientific_freeze_unchanged"]:
            raise RuntimeError(f"SOURCE_DATASET_FREEZE_MISMATCH: {path}")
        source_id = manifest.get("source_id")
        if source_id not in {"BNCI2014_001", "Lee2019_MI"}:
            continue
        if not manifest.get("complete_for_official_run"):
            raise RuntimeError(f"SOURCE_DATASET_NOT_COMPLETE: {source_id}; {path}")
        selected_manifests.append((path, manifest))

    if len([1 for _, m in selected_manifests if m.get("source_id") == "BNCI2014_001"]) != 1:
        raise RuntimeError("Attach exactly one BNCI2014_001 source Dataset.")
    if len([1 for _, m in selected_manifests if m.get("source_id") == "Lee2019_MI"]) != 1:
        raise RuntimeError("Attach exactly one Lee2019_MI source Dataset.")

    hash_workers = max(1, min(
        int(os.environ.get("IHARQ_SOURCE_HASH_WORKERS", "8")),
        os.cpu_count() or 1,
        8,
    ))

    for path, manifest in selected_manifests:
        source_id = str(manifest["source_id"])
        declared_rows = list(manifest.get("files", []))
        base = path.parent

        # One physical-tree scan per attached Dataset, rather than two rglob
        # operations for every manifest row.
        physical_files = [candidate for candidate in base.rglob("*") if candidate.is_file()]
        by_leaf: dict[str, list[Path]] = {}
        for candidate in physical_files:
            by_leaf.setdefault(candidate.name, []).append(candidate)

        resolution_jobs: list[tuple[dict[str, Any], list[Path]]] = []
        for row in declared_rows:
            canonical_relative = str(row["relative_path"])
            canonical_name = Path(canonical_relative).name
            expected_bytes = int(row["bytes"])
            candidates: list[Path] = []
            direct = base / Path(canonical_relative)
            if direct.is_file():
                candidates.append(direct)
            candidates.extend(by_leaf.get(canonical_name, []))
            suffix = "_" + canonical_name
            candidates.extend(
                candidate
                for leaf, paths in by_leaf.items()
                if leaf.endswith(suffix)
                for candidate in paths
            )
            unique: list[Path] = []
            seen: set[str] = set()
            for candidate in candidates:
                key = str(candidate.resolve())
                if key not in seen:
                    seen.add(key)
                    unique.append(candidate)
            sized = [candidate for candidate in unique if candidate.stat().st_size == expected_bytes]
            if not sized:
                raise RuntimeError(
                    "SOURCE_DATASET_FILE_MISSING_OR_SIZE_MISMATCH: "
                    f"manifest={path}; canonical={canonical_relative}; expected_bytes={expected_bytes}"
                )
            resolution_jobs.append((row, sized))

        hash_tasks: list[tuple[int, Path]] = []
        for row_index, (_, candidates) in enumerate(resolution_jobs):
            for candidate in candidates:
                hash_tasks.append((row_index, candidate))

        def hash_task(item: tuple[int, Path]) -> tuple[int, Path, str]:
            row_index, candidate = item
            return row_index, candidate, _sha256(candidate)

        hashed_by_row: dict[int, list[tuple[Path, str]]] = {}
        with ThreadPoolExecutor(max_workers=hash_workers, thread_name_prefix="iharq-source-sha256") as pool:
            for row_index, candidate, observed_sha in pool.map(hash_task, hash_tasks):
                hashed_by_row.setdefault(row_index, []).append((candidate, observed_sha))

        canonical_rows: list[dict[str, Any]] = []
        for row_index, (row, candidates) in enumerate(resolution_jobs):
            canonical_relative = str(row["relative_path"])
            canonical_name = Path(canonical_relative).name
            expected_sha = str(row["sha256"]).lower()
            verified = [
                candidate
                for candidate, observed_sha in hashed_by_row.get(row_index, [])
                if observed_sha.lower() == expected_sha
            ]
            if len(verified) != 1:
                raise RuntimeError(
                    "SOURCE_DATASET_FILE_RESOLUTION_AMBIGUOUS: "
                    f"canonical={canonical_relative}; size_matches={len(candidates)}; "
                    f"hash_matches={len(verified)}; candidates={[str(p) for p in candidates[:10]]}"
                )
            source = verified[0]
            canonical_rows.append({
                "relative_path": canonical_relative,
                "runtime_path_class": "KAGGLE_INPUT",
                "runtime_path": str(source),
                "sha256": expected_sha,
                "bytes": int(row["bytes"]),
                "canonical_filename": canonical_name,
                "physical_filename": source.name,
                "ordinal_prefix_resolved": source.name != canonical_name,
            })
            if source_id == "BNCI2014_001":
                match = re.fullmatch(r"A(\d{2})(T|E)\.mat", canonical_name)
                if not match:
                    raise RuntimeError(f"BNCI_SOURCE_FILENAME_INVALID: {canonical_name}")
                key = (int(match.group(1)), match.group(2))
                if key in bnci:
                    raise RuntimeError(f"BNCI_DUPLICATE_SOURCE_FILE: {key}")
                bnci[key] = source
            else:
                match = re.fullmatch(r"sess(\d{2})_subj(\d{2})_EEG_MI\.mat", canonical_name)
                if not match:
                    raise RuntimeError(f"LEE_SOURCE_FILENAME_INVALID: {canonical_name}")
                session, subject = int(match.group(1)), int(match.group(2))
                key = (subject, session)
                if key in lee:
                    raise RuntimeError(f"LEE_DUPLICATE_SOURCE_FILE: {key}")
                lee[key] = source

        aggregate = _aggregate_file_digest(canonical_rows)
        inventories[source_id] = {
            "files": canonical_rows,
            "count": len(canonical_rows),
            "aggregate_sha256": aggregate,
            "observed_checksum": aggregate,
            "expected_checksum": aggregate,
            "checksum_status": "VERIFIED_FROM_SOURCE_DATASET_MANIFEST_AND_PHYSICAL_BYTES",
            "manifest_path": str(path),
            "verification_strategy": "ONE_SCAN_BOUNDED_PARALLEL_SHA256",
            "hash_workers": hash_workers,
        }
        manifests.append({
            "source_id": source_id,
            "dataset_handle": manifest.get("dataset_handle"),
            "manifest": str(path),
            "file_count": len(canonical_rows),
            "bytes": sum(int(row["bytes"]) for row in canonical_rows),
            "aggregate_sha256": aggregate,
            "ordinal_prefixed_files": sum(bool(row["ordinal_prefix_resolved"]) for row in canonical_rows),
            "verification_strategy": "ONE_SCAN_BOUNDED_PARALLEL_SHA256",
            "hash_workers": hash_workers,
        })

    if len(bnci) != 18:
        raise RuntimeError(f"BNCI_ATTACHED_DATASET_INCOMPLETE: required=18; observed={len(bnci)}")
    if len(lee) != 108:
        raise RuntimeError(f"LEE_ATTACHED_DATASET_INCOMPLETE: required=108; observed={len(lee)}")
    _PRIVATE_INVENTORY = inventories
    return bnci, lee, manifests


def _serialize_source_map(path: Path) -> None:
    payload = {
        "policy_id": POLICY["policy_id"],
        "sources": {
            dataset: {"|".join(str(x) for x in key): str(value) for key, value in mapping.items()}
            for dataset, mapping in _SOURCE_MAP.items()
        },
        "private_inventory": _PRIVATE_INVENTORY,
    }
    _atomic_json(path, payload)


def _load_source_map(path: Path) -> None:
    global _SOURCE_MAP, _PRIVATE_INVENTORY
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    result: dict[str, dict[Any, Path]] = {}
    for dataset, mapping in payload["sources"].items():
        converted: dict[Any, Path] = {}
        for raw_key, raw_path in mapping.items():
            parts = raw_key.split("|")
            if dataset == "BNCI2014_001":
                key = (int(parts[0]), parts[1])
            else:
                key = (int(parts[0]), int(parts[1]))
            converted[key] = Path(raw_path)
        result[dataset] = converted
    _SOURCE_MAP = result
    _PRIVATE_INVENTORY = dict(payload.get("private_inventory", {}))


def _prepare_sources(runner: Any, child_mode: bool = False, resolution_file: Path | None = None) -> dict[str, Any]:
    global _SOURCE_MAP, _SOURCE_REPORT, _RESOLUTION_FILE

    # Optional same-session worker restart fast path. The source-resolution
    # file was created only after full per-file SHA-256 verification, and all
    # referenced source bytes live under Kaggle's read-only input mount.
    # Reuse is accepted only when the caller supplies the exact resolution-file
    # SHA-256 and the complete frozen source cardinalities still match.
    reuse_raw = os.environ.get("IHARQ_REUSE_VERIFIED_SOURCE_RESOLUTION_FILE")
    if not child_mode and reuse_raw:
        reuse_path = Path(reuse_raw).resolve()
        expected_resolution_sha256 = os.environ.get(
            "IHARQ_REUSE_VERIFIED_SOURCE_RESOLUTION_SHA256", ""
        ).strip().lower()
        if not reuse_path.is_file():
            raise RuntimeError(
                "R34_REUSED_SOURCE_RESOLUTION_MISSING: "
                f"{reuse_path}"
            )
        observed_resolution_sha256 = _sha256(reuse_path)
        if (
            not re.fullmatch(r"[0-9a-f]{64}", expected_resolution_sha256)
            or observed_resolution_sha256 != expected_resolution_sha256
        ):
            raise RuntimeError(
                "R34_REUSED_SOURCE_RESOLUTION_SHA256_MISMATCH: "
                f"expected={expected_resolution_sha256!r}; "
                f"observed={observed_resolution_sha256}"
            )

        _load_source_map(reuse_path)
        expected_counts = {
            "PhysioNetMI": 327,
            "BNCI2014_001": 18,
            "Lee2019_MI": 108,
        }
        observed_counts = {
            key: len(value)
            for key, value in _SOURCE_MAP.items()
        }
        if observed_counts != expected_counts:
            raise RuntimeError(
                "R34_REUSED_SOURCE_RESOLUTION_COUNT_MISMATCH: "
                f"expected={expected_counts}; observed={observed_counts}"
            )

        input_root = Path(getattr(runner, "input_root", "/kaggle/input")).resolve()
        invalid_paths = []
        for dataset_id, mapping in _SOURCE_MAP.items():
            for source_path in mapping.values():
                source_path = Path(source_path).resolve()
                if (
                    not source_path.is_file()
                    or not source_path.is_relative_to(input_root)
                ):
                    invalid_paths.append(
                        {
                            "dataset_id": dataset_id,
                            "path": str(source_path),
                        }
                    )
        if invalid_paths:
            raise RuntimeError(
                "R34_REUSED_SOURCE_RESOLUTION_PATH_INVALID: "
                + json.dumps(invalid_paths[:20], indent=2)
            )

        private_counts = {
            dataset_id: int(
                _PRIVATE_INVENTORY.get(dataset_id, {}).get("count", -1)
            )
            for dataset_id in ("BNCI2014_001", "Lee2019_MI")
        }
        if private_counts != {
            "BNCI2014_001": 18,
            "Lee2019_MI": 108,
        }:
            raise RuntimeError(
                "R34_REUSED_PRIVATE_INVENTORY_COUNT_MISMATCH: "
                f"{private_counts}"
            )

        _RESOLUTION_FILE = reuse_path
        _SOURCE_REPORT = {
            "status": "PASS",
            "mode": "SAME_SESSION_SHA256_BOUND_READ_ONLY_SOURCE_REUSE",
            "resolution_file": str(reuse_path),
            "resolution_sha256": observed_resolution_sha256,
            "source_counts": observed_counts,
            "private_inventory_counts": private_counts,
            "source_network_download_allowed": False,
            "moabb_downloader_allowed": False,
            "full_physical_byte_verification_performed_earlier_same_session": True,
            "read_only_input_paths_revalidated": True,
            "scientific_scope_changed": False,
        }
        _atomic_json(
            runner.pipeline.bundle_root
            / "reports"
            / "phase_01"
            / "runtime"
            / "attached_source_datasets"
            / "source_dataset_intake_reused.json",
            _SOURCE_REPORT,
        )
        return _SOURCE_REPORT

    if child_mode:
        if resolution_file is None:
            raise RuntimeError("STREAMING_CHILD_SOURCE_RESOLUTION_FILE_MISSING")
        _load_source_map(Path(resolution_file))
        _SOURCE_REPORT = {
            "status": "PASS",
            "mode": "CHILD_REUSE_PARENT_VERIFIED_SOURCE_MAP",
            "resolution_file": str(resolution_file),
            "source_counts": {k: len(v) for k, v in _SOURCE_MAP.items()},
        }
        return _SOURCE_REPORT

    input_root = Path(getattr(runner, "input_root", "/kaggle/input"))
    if not input_root.exists():
        input_root = Path("/kaggle/input")
    physio = _discover_physionet(input_root)
    bnci, lee, private_manifests = _load_private_source_manifests(input_root)
    _SOURCE_MAP = {"PhysioNetMI": physio, "BNCI2014_001": bnci, "Lee2019_MI": lee}
    resolution_file = Path(getattr(runner, "work_root", "/kaggle/working/iharq_p01_l1")) / "streaming_runtime" / "source_resolution_r26.json"
    _serialize_source_map(resolution_file)
    _RESOLUTION_FILE = resolution_file
    _SOURCE_REPORT = {
        "status": "PASS",
        "input_root": str(input_root),
        "source_counts": {k: len(v) for k, v in _SOURCE_MAP.items()},
        "private_manifests": private_manifests,
        "source_resolution_file": str(resolution_file),
        "physionet_public_dataset_required": POLICY["physionet_public_handle"],
        "source_network_download_allowed": False,
        "moabb_downloader_allowed": False,
        "private_source_bytes_sha256_verified": True,
        "ordinal_prefix_resolution_supported": True,
    }
    _atomic_json(
        runner.pipeline.bundle_root / "reports" / "phase_01" / "runtime" / "attached_source_datasets" / "source_dataset_intake.json",
        _SOURCE_REPORT,
    )
    return _SOURCE_REPORT


def _patch_base_dataset_get_data() -> dict[str, Any]:
    """Install a lossless MOABB subject-key compatibility boundary.

    MOABB guarantees a nested subject -> session -> run mapping, but project
    adapters and MOABB releases have not always represented the top-level
    subject identifier with the same Python type. This wrapper preserves the
    returned mapping and its iteration order while allowing equivalent subject
    identifiers (1, "1", "01", "sub-01", "subject_01", "A01", "S01") to
    resolve to the original key. For a call that explicitly requests exactly
    one subject and returns exactly one subject subtree, the requested subject
    is also safely aliased to that sole result.
    """
    from collections.abc import KeysView, Mapping
    from numbers import Integral
    from moabb.datasets.base import BaseDataset

    ambiguous = object()

    def subject_token(value: Any) -> int | None:
        if isinstance(value, bool):
            return None
        if isinstance(value, Integral):
            return int(value)
        text = str(value).strip()
        match = re.fullmatch(
            r"(?i)(?:sub(?:ject)?|participant|[as])?[-_ ]*0*(\d+)",
            text,
        )
        return int(match.group(1)) if match else None

    class SubjectKeyCompatKeysView(KeysView):
        def __contains__(self, key: object) -> bool:
            return key in self._mapping

    class SubjectKeyCompatDict(dict):
        """Dictionary with alias-only lookup; contents and iteration are unchanged."""

        def __init__(self, payload: Mapping[Any, Any], requested_subjects: Any):
            super().__init__(payload)
            aliases: dict[int, Any] = {}
            for original_key in dict.keys(self):
                token = subject_token(original_key)
                if token is None:
                    continue
                previous = aliases.get(token)
                if previous is None:
                    aliases[token] = original_key
                elif previous != original_key:
                    aliases[token] = ambiguous

            if requested_subjects is None:
                requested = []
            elif isinstance(requested_subjects, (str, bytes, Integral)):
                requested = [requested_subjects]
            else:
                try:
                    requested = list(requested_subjects)
                except TypeError:
                    requested = [requested_subjects]

            # A single-request/single-result fallback is unambiguous and does
            # not fabricate, merge, or discard any subject data.
            if len(requested) == 1 and dict.__len__(self) == 1:
                token = subject_token(requested[0])
                if token is not None:
                    current = aliases.get(token)
                    if current is None or current is ambiguous:
                        aliases[token] = next(dict.__iter__(self))

            self._iharq_subject_aliases = aliases
            self._iharq_requested_subjects = requested

        def _resolve_key(self, key: Any) -> Any:
            if dict.__contains__(self, key):
                return key
            token = subject_token(key)
            if token is None:
                return ambiguous
            return self._iharq_subject_aliases.get(token, ambiguous)

        def __contains__(self, key: object) -> bool:
            return self._resolve_key(key) is not ambiguous

        def __getitem__(self, key: Any) -> Any:
            resolved = self._resolve_key(key)
            if resolved is ambiguous:
                raise KeyError(key)
            return dict.__getitem__(self, resolved)

        def get(self, key: Any, default: Any = None) -> Any:
            resolved = self._resolve_key(key)
            if resolved is ambiguous:
                return default
            return dict.__getitem__(self, resolved)

        def keys(self):
            return SubjectKeyCompatKeysView(self)

        def pop(self, key: Any, *default: Any) -> Any:
            resolved = self._resolve_key(key)
            if resolved is ambiguous:
                if default:
                    return default[0]
                raise KeyError(key)
            return dict.pop(self, resolved)

        def copy(self):
            return SubjectKeyCompatDict(self, self._iharq_requested_subjects)

    with _LOCK:
        if getattr(BaseDataset, "_iharq_r31_subject_key_compat", False):
            return {
                "status": "ALREADY_PATCHED",
                "revision": "R34",
                "subject_key_aliasing": True,
            }

        original = BaseDataset.get_data
        signature = inspect.signature(original)
        supported = set(signature.parameters)
        accepts_var_kwargs = any(
            parameter.kind is inspect.Parameter.VAR_KEYWORD
            for parameter in signature.parameters.values()
        )

        def compatible_get_data(self, *args, **kwargs):
            cleaned = dict(kwargs)
            if not accepts_var_kwargs:
                for key in list(cleaned):
                    if key not in supported:
                        cleaned.pop(key)

            requested_subjects = cleaned.get("subjects")
            if requested_subjects is None:
                try:
                    bound = signature.bind_partial(self, *args, **cleaned)
                    requested_subjects = bound.arguments.get("subjects")
                except TypeError:
                    requested_subjects = None

            result = original(self, *args, **cleaned)
            if isinstance(result, Mapping) and not isinstance(result, SubjectKeyCompatDict):
                result = SubjectKeyCompatDict(result, requested_subjects)
            return result

        compatible_get_data.__name__ = getattr(original, "__name__", "get_data")
        compatible_get_data.__doc__ = getattr(original, "__doc__", None)
        compatible_get_data.__wrapped__ = original

        # Cheap contract test before publishing the monkey-patch.
        probe_value = object()
        probe = SubjectKeyCompatDict({"01": probe_value}, [1])
        if not (
            probe.get(1) is probe_value
            and probe.get("sub-001") is probe_value
            and 1 in probe
            and "subject_1" in probe.keys()
            and list(probe) == ["01"]
            and list(probe.keys()) == ["01"]
            and len(probe) == 1
        ):
            raise RuntimeError("R34_MOABB_SUBJECT_KEY_COMPAT_SELF_TEST_FAILED")

        BaseDataset.get_data = compatible_get_data
        BaseDataset._iharq_r26_get_data_compat = True
        BaseDataset._iharq_r31_subject_key_compat = True
        BaseDataset._iharq_r31_original_get_data = original

    return {
        "status": "PATCHED",
        "revision": "R34",
        "original_parameters": sorted(supported),
        "unsupported_keywords_filtered": True,
        "subject_key_aliasing": True,
        "mapping_contents_and_iteration_unchanged": True,
        "keys_view_alias_membership": True,
        "single_subject_single_result_fallback": True,
        "installation_self_test": "PASS",
    }


def _bnci_session_selected(session_id: Any, selected_sessions: Any) -> bool:
    """Match MOABB session keys such as ``0train``/``1test`` to frozen selectors 0/1."""
    if selected_sessions is None:
        return True
    try:
        selected = list(selected_sessions)
    except TypeError:
        selected = [selected_sessions]
    selected_tokens = {str(value).strip() for value in selected}
    text = str(session_id).strip()
    if text in selected_tokens:
        return True
    match = re.match(r"^(\d+)", text)
    return bool(match and match.group(1) in selected_tokens)


def _bnci_task_event_count(raw: Any, event_id: dict[str, Any]) -> int:
    """Count only frozen task annotations, excluding optional artifact markers."""
    descriptions = {str(key) for key in event_id}
    annotations = getattr(raw, "annotations", None)
    if annotations is None:
        return 0
    return sum(str(value) in descriptions for value in annotations.description)


def _exact_bnci_adapter_load(self: Any, files: list[Path]):
    """Load BNCI through MOABB's native MAT converter without the empty get_data mapping.

    MOABB's ``_get_single_subject_data`` is the dataset-native conversion path.
    The same default ``SetRawAnnotations`` transformation used by ``get_data`` is
    then applied explicitly to each run. No signal, trial, class, session, run,
    or artifact value is invented or changed.
    """
    from collections.abc import Mapping
    from iharq.layer1_data_protocol.adapters.base import SourceAccessError
    from moabb.datasets.preprocessing import SetRawAnnotations

    dataset = self._make_dataset()
    event_id = dict(getattr(dataset, "event_id", {}) or {})
    interval = tuple(getattr(dataset, "interval", ()) or ())
    selected_sessions = getattr(dataset, "_selected_sessions", None)
    if not event_id or len(interval) != 2:
        raise SourceAccessError(
            "R34_BNCI_DATASET_EVENT_CONTRACT_MISSING: "
            f"event_id={event_id!r}; interval={interval!r}"
        )

    annotator = SetRawAnnotations(event_id, interval=interval)
    out = []
    diagnostics: list[dict[str, Any]] = []

    for subject in self._subjects():
        try:
            subtree = dataset._get_single_subject_data(int(subject))
        except Exception as exc:
            raise SourceAccessError(
                "R34_BNCI_NATIVE_SUBJECT_CONVERSION_FAILED: "
                f"subject={subject}; error={type(exc).__name__}: {exc}"
            ) from exc

        if not isinstance(subtree, Mapping):
            raise SourceAccessError(
                "R34_BNCI_NATIVE_SUBTREE_INVALID: "
                f"subject={subject}; type={type(subtree).__name__}"
            )

        exact_files = getattr(self, "_resolved_files_by_subject", {}).get(
            int(subject), []
        )
        if not exact_files:
            raise SourceAccessError(
                "exact source-file provenance missing for subject "
                f"{subject}; generic substring matching is forbidden"
            )
        source_file = ";".join(str(path) for path in exact_files)

        subject_diagnostic = {
            "subject": int(subject),
            "native_sessions": [str(key) for key in subtree.keys()],
            "selected_sessions": (
                None if selected_sessions is None else [str(v) for v in selected_sessions]
            ),
            "sessions": [],
        }

        for session_id, runs in subtree.items():
            session_selected = _bnci_session_selected(session_id, selected_sessions)
            session_row = {
                "session_id": str(session_id),
                "selected": bool(session_selected),
                "native_run_count": len(runs) if isinstance(runs, Mapping) else None,
                "runs": [],
            }
            subject_diagnostic["sessions"].append(session_row)
            if not session_selected:
                continue
            if not isinstance(runs, Mapping):
                raise SourceAccessError(
                    "R34_BNCI_RUN_MAPPING_INVALID: "
                    f"subject={subject}; session={session_id!r}; "
                    f"type={type(runs).__name__}"
                )

            for run_id, raw in runs.items():
                raw_run_id = str(run_id)
                run_row = {
                    "run_id": raw_run_id,
                    "included": bool(self._include_run(raw_run_id)),
                    "task_events_before": _bnci_task_event_count(raw, event_id),
                }
                session_row["runs"].append(run_row)
                if not run_row["included"]:
                    continue

                try:
                    raw = annotator.transform(raw)
                except Exception as exc:
                    raise SourceAccessError(
                        "R34_BNCI_ANNOTATION_TRANSFORM_FAILED: "
                        f"subject={subject}; session={session_id!r}; "
                        f"run={raw_run_id!r}; error={type(exc).__name__}: {exc}"
                    ) from exc

                task_events = _bnci_task_event_count(raw, event_id)
                run_row["task_events_after"] = int(task_events)
                run_row["annotation_count_after"] = int(
                    len(getattr(raw, "annotations", ()) or ())
                )
                if task_events <= 0:
                    raise SourceAccessError(
                        "R34_BNCI_TASK_EVENTS_EMPTY_AFTER_NATIVE_CONVERSION: "
                        f"subject={subject}; session={session_id!r}; "
                        f"run={raw_run_id!r}; event_id={event_id!r}; "
                        f"diagnostic={json.dumps(run_row, default=str)}"
                    )

                canonical_run_id = self._canonical_run_id(raw_run_id)
                recording = self._raw_to_recording(
                    raw,
                    int(subject),
                    str(session_id),
                    canonical_run_id,
                    source_file,
                    self._run_metadata(raw_run_id),
                )
                if not getattr(recording, "events", None):
                    raise SourceAccessError(
                        "R34_BNCI_PROJECT_RECORDING_EVENTS_EMPTY: "
                        f"subject={subject}; session={session_id!r}; "
                        f"run={raw_run_id!r}"
                    )
                out.append(recording)

        diagnostics.append(subject_diagnostic)

    if not out:
        raise SourceAccessError(
            "R34_BNCI_NO_RECORDINGS_AFTER_EXACT_NATIVE_LOAD: "
            + json.dumps(diagnostics, indent=2, default=str)
        )
    return out


def _patch_bnci_project_adapter_load() -> dict[str, Any]:
    """Install the exact loader on the active IHARQ BNCI adapter class."""
    from iharq.layer1_data_protocol import adapters as adapters_module

    candidates = []
    for adapter_key, adapter_class in adapters_module.ADAPTERS.items():
        identity = (
            f"{adapter_key} {adapter_class.__module__} "
            f"{adapter_class.__name__} "
            f"{getattr(adapter_class, 'dataset_class_name', '')}"
        ).lower()
        if "bnci2014_001" in identity or "bnci2014001" in identity:
            candidates.append(adapter_class)
    candidates = list(dict.fromkeys(candidates))
    if not candidates:
        raise RuntimeError("R34_BNCI_PROJECT_ADAPTER_CLASS_NOT_FOUND")

    patched = []
    for adapter_class in candidates:
        adapter_class.load = _exact_bnci_adapter_load
        adapter_class._iharq_r32_exact_native_bnci_load = True
        patched.append(f"{adapter_class.__module__}.{adapter_class.__name__}")

    # Installation-time contract checks: selection semantics and explicit marker.
    if not (
        _bnci_session_selected("0train", [0, 1])
        and _bnci_session_selected("1test", [0, 1])
        and not _bnci_session_selected("2other", [0, 1])
        and all(
            getattr(cls, "_iharq_r32_exact_native_bnci_load", False)
            for cls in candidates
        )
    ):
        raise RuntimeError("R34_BNCI_ADAPTER_LOAD_INSTALLATION_SELF_TEST_FAILED")

    return {
        "status": "PATCHED",
        "revision": "R34",
        "adapter_classes": patched,
        "moabb_native_subject_conversion": True,
        "moabb_default_annotation_transform_reapplied": True,
        "frozen_session_selection_preserved": True,
        "exact_source_provenance_preserved": True,
        "signals_or_labels_modified": False,
        "installation_self_test": "PASS",
    }

def _patch_source_contracts() -> dict[str, Any]:
    from moabb.datasets import BNCI2014_001, Lee2019_MI, PhysionetMI
    with _LOCK:
        if not getattr(PhysionetMI, "_iharq_r26_source_patch", False):
            original_init = PhysionetMI.__init__
            def exact_physionet_init(self, *args, **kwargs):
                result = _call_filtered(original_init, self, args, kwargs, {"imagined": True, "executed": False})
                if hasattr(self, "runs"): self.runs = [4, 8, 12]
                if hasattr(self, "hand_runs"): self.hand_runs = [4, 8, 12]
                if hasattr(self, "feet_runs"): self.feet_runs = []
                return result
            def paths(subject: int, runs: Any) -> list[str]:
                if not hasattr(runs, "__iter__"): runs = [runs]
                result = []
                for run in runs:
                    key = (int(subject), int(run)); value = _SOURCE_MAP["PhysioNetMI"].get(key)
                    if value is None: raise RuntimeError(f"PHYSIONET_ATTACHED_FILE_MISSING: {key}")
                    result.append(str(value))
                return result
            def data_path(self, subject, path=None, force_update=False, update_path=None, verbose=None):
                return paths(subject, [4, 8, 12])
            def load_data(self, subject, runs, path=None, force_update=False, verbose=None):
                return paths(subject, runs)
            PhysionetMI.__init__ = exact_physionet_init
            PhysionetMI.data_path = data_path
            if hasattr(PhysionetMI, "_load_data"): PhysionetMI._load_data = load_data
            PhysionetMI._iharq_r26_source_patch = True

        if not getattr(BNCI2014_001, "_iharq_r26_source_patch", False):
            original_bnci_init = BNCI2014_001.__init__
            def exact_bnci_init(self, *args, **kwargs):
                return _call_filtered(original_bnci_init, self, args, kwargs)
            def data_path(self, subject, path=None, force_update=False, update_path=None, verbose=None):
                result = []
                for session in ("T", "E"):
                    key = (int(subject), session); value = _SOURCE_MAP["BNCI2014_001"].get(key)
                    if value is None: raise RuntimeError(f"BNCI_ATTACHED_FILE_MISSING: {key}")
                    result.append(str(value))
                return result
            BNCI2014_001.__init__ = exact_bnci_init
            BNCI2014_001.data_path = data_path
            BNCI2014_001._iharq_r26_source_patch = True

        if not getattr(Lee2019_MI, "_iharq_r26_source_patch", False):
            original_lee_init = Lee2019_MI.__init__
            def exact_lee_init(self, *args, **kwargs):
                return _call_filtered(original_lee_init, self, args, kwargs, {"train_run": True, "test_run": False})
            def data_path(self, subject, path=None, force_update=False, update_path=None, verbose=None):
                result = []
                for session in (1, 2):
                    key = (int(subject), session); value = _SOURCE_MAP["Lee2019_MI"].get(key)
                    if value is None: raise RuntimeError(f"LEE_ATTACHED_FILE_MISSING: {key}")
                    result.append(str(value))
                return result
            Lee2019_MI.__init__ = exact_lee_init
            Lee2019_MI.data_path = data_path
            Lee2019_MI._iharq_r26_source_patch = True

    # R26 controlled correction:
    # MOABB PhysionetMI exposes the three imagined-hand recordings under
    # internal run keys 0, 1, 2. The IHARQ canonical source identities are
    # PhysioNet runs 4, 8, 12. MOABBAdapterBase checks _include_run twice:
    # first with the internal key and again with the canonical source run.
    # Therefore the adapter must lawfully recognize both representations
    # while always canonicalizing to the frozen source set {4, 8, 12}.
    from iharq.layer1_data_protocol import adapters as adapters_module

    moabb_key_to_source_run = {0: 4, 1: 8, 2: 12}
    frozen_physionet_source_runs = frozenset(
        moabb_key_to_source_run.values()
    )

    def normalize_physionet_run_token(value: Any) -> int | None:
        match = re.search(
            r"(\d+)(?!.*\d)",
            str(value).strip(),
        )
        return int(match.group(1)) if match else None

    def configured_physionet_source_runs(adapter: Any) -> set[int]:
        profile = getattr(adapter, "profile", None)
        options = getattr(profile, "adapter_options", {}) or {}
        if not isinstance(options, dict):
            options = dict(options)

        configured_raw = options.get("runs")
        if configured_raw is None:
            run_policy = (
                getattr(profile, "run_policy", {})
                or options.get("run_policy", {})
                or {}
            )
            if not isinstance(run_policy, dict):
                run_policy = dict(run_policy)
            configured_raw = run_policy.get("include_runs")

        if configured_raw is None:
            configured_raw = sorted(
                frozen_physionet_source_runs
            )
        if isinstance(configured_raw, (str, int)):
            configured_raw = [configured_raw]

        configured = {
            normalized
            for normalized in (
                normalize_physionet_run_token(value)
                for value in configured_raw
            )
            if normalized is not None
        }

        if configured != set(
            frozen_physionet_source_runs
        ):
            raise RuntimeError(
                "R26_PHYSIONET_RUN_POLICY_CONFIG_MISMATCH: "
                f"expected={sorted(frozen_physionet_source_runs)}; "
                f"configured={sorted(configured)}"
            )

        return configured

    physionet_adapter_classes = []
    for adapter_key, adapter_class in (
        adapters_module.ADAPTERS.items()
    ):
        identity = (
            f"{adapter_key} "
            f"{adapter_class.__module__} "
            f"{adapter_class.__name__}"
        ).lower()
        if "physio" in identity:
            physionet_adapter_classes.append(
                adapter_class
            )

    physionet_adapter_classes = list(
        dict.fromkeys(physionet_adapter_classes)
    )
    if not physionet_adapter_classes:
        raise RuntimeError(
            "R26_PHYSIONET_ADAPTER_CLASS_NOT_FOUND"
        )

    for adapter_class in physionet_adapter_classes:
        def exact_physionet_include_run(
            self,
            run_id: Any,
            _internal_to_source: dict[int, int] = (
                moabb_key_to_source_run
            ),
            _source_runs: frozenset[int] = (
                frozen_physionet_source_runs
            ),
        ) -> bool:
            configured_physionet_source_runs(self)
            token = normalize_physionet_run_token(
                run_id
            )
            return (
                token in _internal_to_source
                or token in _source_runs
            )

        def exact_physionet_canonical_run_id(
            self,
            run_id: Any,
            _internal_to_source: dict[int, int] = (
                moabb_key_to_source_run
            ),
            _source_runs: frozenset[int] = (
                frozen_physionet_source_runs
            ),
        ) -> str:
            configured_physionet_source_runs(self)
            token = normalize_physionet_run_token(
                run_id
            )

            if token in _internal_to_source:
                source_run = _internal_to_source[
                    token
                ]
            elif token in _source_runs:
                source_run = token
            else:
                raise ValueError(
                    "MOABB PhysioNet run key is outside "
                    "the frozen imagined-hand branch: "
                    f"{run_id!r}"
                )

            return str(source_run)

        def exact_physionet_run_metadata(
            self,
            run_id: Any,
            _internal_to_source: dict[int, int] = (
                moabb_key_to_source_run
            ),
            _source_runs: frozenset[int] = (
                frozen_physionet_source_runs
            ),
        ) -> dict[str, Any]:
            configured_physionet_source_runs(self)
            token = normalize_physionet_run_token(
                run_id
            )

            if token in _internal_to_source:
                source_run = _internal_to_source[
                    token
                ]
                moabb_key = token
            elif token in _source_runs:
                source_run = token
                reverse = {
                    value: key
                    for key, value
                    in _internal_to_source.items()
                }
                moabb_key = reverse[token]
            else:
                raise ValueError(
                    "MOABB PhysioNet run key is outside "
                    "the frozen imagined-hand branch: "
                    f"{run_id!r}"
                )

            return {
                "moabb_run_key": str(moabb_key),
                "physionet_source_run": source_run,
            }

        adapter_class._include_run = (
            exact_physionet_include_run
        )
        adapter_class._canonical_run_id = (
            exact_physionet_canonical_run_id
        )
        adapter_class._run_metadata = (
            exact_physionet_run_metadata
        )
        adapter_class._iharq_r26_physionet_dual_run_key_contract_r2 = (
            True
        )


    # R26 local-source correction for MOABB BNCI2014_001.
    #
    # The BNCI loader invokes a module-level data_path function rather than
    # the Dataset class method. Route both module-level symbols to the
    # SHA-256-verified attached Kaggle source map.
    from moabb.datasets.bnci import base as bnci_base_module
    from moabb.datasets.bnci import bnci_2014 as bnci_2014_module

    def attached_bnci_2014_001_data_path(
        url,
        path=None,
        force_update=False,
        update_path=None,
        verbose=None,
    ):
        match = re.search(
            r"A(\d{2})(T|E)\.mat(?:$|[?#])",
            str(url),
            flags=re.IGNORECASE,
        )
        if not match:
            raise RuntimeError(
                "BNCI_ATTACHED_URL_NOT_IN_FROZEN_SCOPE: "
                f"{url!r}"
            )

        key = (
            int(match.group(1)),
            match.group(2).upper(),
        )
        value = _SOURCE_MAP[
            "BNCI2014_001"
        ].get(key)

        if value is None:
            raise RuntimeError(
                "BNCI_ATTACHED_FILE_MISSING: "
                f"{key}"
            )

        value = Path(value)
        if not value.is_file():
            raise RuntimeError(
                "BNCI_ATTACHED_FILE_NOT_READABLE: "
                f"{value}"
            )

        return [str(value)]

    bnci_base_module.data_path = (
        attached_bnci_2014_001_data_path
    )
    bnci_2014_module.data_path = (
        attached_bnci_2014_001_data_path
    )
    bnci_base_module._iharq_r26_attached_router = True
    bnci_2014_module._iharq_r26_attached_router = True


    # R26 MOABB-1.5 compatibility boundary for optional BNCI metadata only.
    # Signal/event conversion remains the unmodified MOABB implementation.
    from moabb.datasets.bnci import base as bnci_metadata_module

    if not getattr(
        bnci_metadata_module,
        "_iharq_r26_optional_metadata_compat",
        False,
    ):
        original_enrich_run_with_metadata = (
            bnci_metadata_module._enrich_run_with_metadata
        )
        original_finalize_raw = (
            bnci_metadata_module._finalize_raw
        )

        def compatible_enrich_run_with_metadata(
            raw,
            run,
            dataset_code,
            subject_id,
        ):
            if dataset_code != "BNCI2014-001":
                return original_enrich_run_with_metadata(
                    raw,
                    run,
                    dataset_code,
                    subject_id,
                )

            try:
                return original_enrich_run_with_metadata(
                    raw,
                    run,
                    dataset_code,
                    subject_id,
                )
            except (
                AttributeError,
                TypeError,
                ValueError,
                OverflowError,
            ) as exc:
                # This wrapper is reached only after _convert_run has already
                # produced the Raw signal and event annotations. Re-finalize
                # the valid Raw without inventing demographic/artifact values.
                original_finalize_raw(
                    raw,
                    dataset_code,
                    subject_id,
                )
                current = raw.info.get("description") or ""
                raw.info["description"] = (
                    current
                    + "IHARQ: optional BNCI demographic/artifact "
                    + "metadata unavailable or incompatible under "
                    + "MOABB 1.5; no value was imputed; "
                    + f"reason={type(exc).__name__}: {exc}; "
                )
                return None

        bnci_metadata_module._enrich_run_with_metadata = (
            compatible_enrich_run_with_metadata
        )
        bnci_metadata_module._iharq_r26_optional_metadata_compat = True

    bnci_adapter_load = _patch_bnci_project_adapter_load()

    return {
        "PhysioNetMI": {"subjects": "1-109", "runs": [4, 8, 12]},
        "BNCI2014_001": {"subjects": "1-9", "sessions": ["T", "E"], "unsupported_constructor_keywords_filtered": True, "module_level_attached_router": True, "optional_metadata_compatibility": "NO_IMPUTATION_SIGNAL_PRESERVING", "project_adapter_load": bnci_adapter_load},
        "Lee2019_MI": {"subjects": "1-54", "sessions": [1, 2], "train_run": True, "test_run": False},
    }


def _install_downloader_guard() -> dict[str, Any]:
    from moabb.datasets import download as download_module
    def prohibited(*args, **kwargs):
        raise RuntimeError("MOABB_SOURCE_DOWNLOADER_PROHIBITED_R26: attach all source bytes as Kaggle Datasets.")
    download_module.data_dl = prohibited
    guarded = ["moabb.datasets.download.data_dl"]
    for module_name in ["moabb.datasets.physionet_mi", "moabb.datasets.bnci", "moabb.datasets.Lee2019"]:
        try:
            module = __import__(module_name, fromlist=["data_dl"])
            if hasattr(module, "data_dl"):
                module.data_dl = prohibited; guarded.append(f"{module_name}.data_dl")
        except Exception:
            pass
    return {"status": "PASS", "guarded_functions": guarded}


def _validate_resolved(dataset_id: str, files: list[Any], allow_subset: bool) -> dict[str, Any]:
    unique = {str(Path(path).resolve()) for path in files}
    missing = [path for path in unique if not Path(path).is_file()]
    legal = {str(path.resolve()) for path in _SOURCE_MAP[dataset_id].values()}
    foreign = sorted(unique - legal)
    expected = POLICY["required_file_counts"][dataset_id]
    expected_subset = {"PhysioNetMI": 3, "BNCI2014_001": 2, "Lee2019_MI": 2}[dataset_id]
    count_ok = len(unique) == expected_subset if allow_subset else len(unique) == expected
    result = {
        "dataset_id": dataset_id,
        "expected_files_full_run": expected,
        "observed_unique_files": len(unique),
        "subset_mode": allow_subset,
        "expected_files_for_this_resolution": expected_subset if allow_subset else expected,
        "missing_files": missing,
        "foreign_files": foreign,
        "pass": count_ok and not missing and not foreign,
    }
    if not result["pass"]:
        raise RuntimeError("ATTACHED_SOURCE_POST_RESOLUTION_VALIDATION_FAILED: " + json.dumps(result, indent=2))
    return result


def _wrap_adapter(adapter_class: type, runner: Any, child_mode: bool) -> None:
    patch_key = (adapter_class, bool(child_mode))
    if patch_key in _PATCHED:
        return
    original_resolve = adapter_class.resolve_files
    original_verify = adapter_class.verify_files

    def attached_only_resolve(self, _original=original_resolve):
        dataset_id = _dataset_id(self)
        files = list(_original(self))
        validation = _validate_resolved(dataset_id, files, allow_subset=child_mode)
        if not child_mode:
            _atomic_json(
                runner.pipeline.bundle_root / "reports" / "phase_01" / "runtime" / "attached_source_datasets" / f"{dataset_id}_post_resolution.json",
                {"policy_id": POLICY["policy_id"], "validation": validation, "moabb_final_loader_preserved": True},
            )
        return files

    def verified_inventory(
        self,
        files,
        _original=original_verify,
    ):
        dataset_id = _dataset_id(self)

        if (
            dataset_id in _PRIVATE_INVENTORY
            and not child_mode
        ):
            inventory = json.loads(
                json.dumps(
                    _PRIVATE_INVENTORY[
                        dataset_id
                    ]
                )
            )

            expected_raw = str(
                _get(
                    _get(self, "profile"),
                    "expected_checksum",
                    "",
                )
                or ""
            ).strip().lower()

            observed = str(
                inventory[
                    "observed_checksum"
                ]
            ).strip().lower()

            explicit_sha256 = bool(
                re.fullmatch(
                    r"[0-9a-f]{64}",
                    expected_raw,
                )
            )

            accepted_policy_sentinels = {
                "",
                "compute_or_verify_per_frozen_policy",
                "compute_or_freeze_per_frozen_policy",
                "compute_and_freeze",
                "compute_at_runtime",
                "computed_at_runtime",
                "none",
                "null",
            }

            if (
                explicit_sha256
                and expected_raw != observed
            ):
                raise RuntimeError(
                    "SOURCE_CHECKSUM_MISMATCH: "
                    f"dataset={dataset_id}; "
                    f"expected={expected_raw}; "
                    f"observed={observed}"
                )

            if (
                not explicit_sha256
                and expected_raw
                not in accepted_policy_sentinels
            ):
                raise RuntimeError(
                    "SOURCE_CHECKSUM_POLICY_UNRECOGNIZED: "
                    f"dataset={dataset_id}; "
                    f"declared={expected_raw!r}"
                )

            inventory[
                "declared_expected_checksum"
            ] = expected_raw or None

            inventory[
                "expected_checksum"
            ] = (
                expected_raw
                if explicit_sha256
                else observed
            )

            inventory[
                "checksum_evidence_status"
            ] = (
                "VERIFIED_EXPLICIT_SHA256"
                if explicit_sha256
                else (
                    "COMPUTED_AND_FROZEN_FOR_RUN_"
                    "FROM_SHA256_VERIFIED_SOURCE_"
                    "DATASET_MANIFEST"
                )
            )

            # The frozen Stage 07 contract accepts this canonical
            # status. The stronger physical-byte verification detail remains
            # recorded separately in checksum_evidence_status and
            # checksum_policy_resolution.
            inventory[
                "checksum_status"
            ] = "COMPUTED_AND_FROZEN_FOR_RUN"

            inventory[
                "checksum_policy_resolution"
            ] = {
                "mode": (
                    "EXPLICIT_SHA256"
                    if explicit_sha256
                    else (
                        "FROZEN_OBSERVED_AGGREGATE_"
                        "UNDER_DECLARED_POLICY"
                    )
                ),
                "physical_files_verified_against_"
                "source_dataset_manifest": True,
                "aggregate_sha256": observed,
                "scientific_scope_changed": False,
            }

            return inventory

        return _original(
            self,
            files,
        )


    adapter_class.resolve_files = attached_only_resolve
    adapter_class.verify_files = verified_inventory
    _PATCHED.add(patch_key)


def _suppress_provider_log_noise() -> None:
    for name in ["mne", "moabb", "pooch", "urllib3"]:
        logger = logging.getLogger(name)
        for handler in list(logger.handlers): logger.removeHandler(handler)
        logger.addHandler(logging.NullHandler()); logger.propagate = False; logger.setLevel(logging.WARNING)


def install_acquisition_acceleration(runner: Any, *, child_mode: bool = False, resolution_file: str | Path | None = None) -> dict[str, Any]:
    source_report = _prepare_sources(runner, child_mode=child_mode, resolution_file=Path(resolution_file) if resolution_file else None)
    compatibility = _patch_base_dataset_get_data()
    from moabb.datasets.base import BaseDataset
    if not getattr(BaseDataset, "_iharq_r31_subject_key_compat", False):
        raise RuntimeError("R34_MOABB_SUBJECT_KEY_COMPAT_NOT_INSTALLED")
    source_contracts = _patch_source_contracts()
    guard = _install_downloader_guard()
    _suppress_provider_log_noise()
    from iharq.layer1_data_protocol import adapters as adapters_module
    patched = []
    for adapter_class in set(adapters_module.ADAPTERS.values()):
        _wrap_adapter(adapter_class, runner, child_mode)
        patched.append(f"{adapter_class.__module__}.{adapter_class.__name__}")
    installation = {
        "policy": POLICY,
        "installed_at_unix": time.time(),
        "child_mode": child_mode,
        "source_report": source_report,
        "compatibility": compatibility,
        "source_contracts": source_contracts,
        "downloader_guard": guard,
        "patched_adapter_classes": sorted(patched),
        "quality_boundary": {
            "same_active_sources": True,
            "same_subjects": True,
            "same_sessions": True,
            "same_physionet_runs": True,
            "same_moabb_native_signal_conversion": True,
            "same_moabb_default_annotation_transform": True,
            "bnci_empty_processed_mapping_bypassed": True,
            "moabb_subject_key_representation_compatibility": True,
            "moabb_mapping_contents_and_iteration_unchanged": True,
            "same_stage07_checksum_inventory": True,
            "same_exact_subject_provenance": True,
            "same_subject88_handling": True,
            "same_preprocessing_splits_budgets_windows": True,
            "same_records_cards_manifests_gates_handoffs": True,
            "source_network_downloading_removed": True,
        },
    }
    if not child_mode:
        _atomic_json(
            runner.pipeline.bundle_root / "reports" / "phase_01" / "runtime" / "attached_source_datasets" / "installation.json",
            installation,
        )
    return installation


def source_resolution_file() -> str | None:
    return str(_RESOLUTION_FILE) if _RESOLUTION_FILE else None
