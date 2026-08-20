"""Resource qualification, bounded streaming, and read-only heartbeat support."""

from __future__ import annotations

import gc
import os
import shutil
import time
from pathlib import Path
from typing import Any, Iterator, Mapping, Sequence


def memory_snapshot() -> dict[str, Any]:
    result: dict[str, Any] = {"pid": os.getpid(), "cpu_count": os.cpu_count()}
    try:
        import resource
        result["max_rss_kib"] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    except (ImportError, AttributeError):
        result["max_rss_kib"] = None
    return result


def qualify_resources(run_root: str | Path, profile: Mapping[str, Any]) -> dict[str, Any]:
    usage = shutil.disk_usage(Path(run_root).parent)
    available_gib = usage.free / (1024**3)
    required_gib = float(profile["minimum_free_disk_gib"])
    result = {"free_disk_gib": available_gib, "minimum_free_disk_gib": required_gib, "disk_status": "PASS" if available_gib >= required_gib else "FAIL", **memory_snapshot()}
    if result["disk_status"] != "PASS":
        raise RuntimeError(f"Insufficient disk: {available_gib:.2f} GiB available, {required_gib:.2f} GiB required")
    return result


def bounded_batches(items: Sequence[Any], batch_size: int) -> Iterator[Sequence[Any]]:
    if batch_size < 1:
        raise ValueError("batch_size must be positive")
    for start in range(0, len(items), batch_size):
        yield items[start : start + batch_size]


def collect_after_partition() -> dict[str, Any]:
    before = gc.get_count()
    collected = gc.collect()
    return {"gc_count_before": list(before), "objects_collected": collected}


def progress_payload(completed: int, total: int, start_time: float, *, last_completed: str | None, error_count: int, checkpoint_state: str) -> dict[str, Any]:
    elapsed = max(0.0, time.monotonic() - start_time)
    percent = 100.0 * completed / total if total else 100.0
    eta = elapsed * (total - completed) / completed if completed and completed < total else 0.0
    return {"total_work_units": total, "completed_work_units": completed, "percent": percent, "elapsed_seconds": elapsed, "eta_seconds": eta, "last_completed": last_completed, "error_count": error_count, "checkpoint_state": checkpoint_state, **memory_snapshot()}

