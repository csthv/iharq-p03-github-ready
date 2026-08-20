"""Notebook controller with one persistent scientific worker for Stages 07-20; CUDA-safe spawn for GPU replay."""

from __future__ import annotations

import json
import multiprocessing as mp
import queue
import threading
import time
import traceback
from pathlib import Path
from typing import Any

from .constants import DEFAULT_TIMEOUT_SECONDS, EXTENDED_TIMEOUTS_SECONDS, HEARTBEAT_SECONDS, SCIENTIFIC_WORKER_STAGES
from .models import ExecutionContext
from .stage_runner import STAGE_META, StageRunner
from .stages import HANDLERS
from .writers import write_json


def _worker_main(context: ExecutionContext, commands: mp.Queue, responses: mp.Queue) -> None:
    runner = StageRunner(context)
    while True:
        command = commands.get()
        if command is None:
            return
        stage_id = command["stage_id"]
        try:
            result = runner.run(stage_id, HANDLERS[stage_id])
            responses.put({"stage_id": stage_id, "ok": True, "payload": result})
        except Exception as exc:
            responses.put({"stage_id": stage_id, "ok": False, "exception_type": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc()})


class NotebookController:
    def __init__(self, context: ExecutionContext):
        self.context = context
        self.runner = StageRunner(context)
        self._commands: mp.Queue | None = None
        self._responses: mp.Queue | None = None
        self._worker: mp.Process | None = None

    def _ensure_worker(self) -> None:
        if self._worker is not None and self._worker.is_alive():
            return
        # C8.1: Stage-07 neural/SSL replay uses CUDA. Forking a process after
        # the notebook parent has initialized CUDA is prohibited by PyTorch.
        # Use a clean spawned child for the one governed persistent scientific
        # worker. This is an execution-transport repair only.
        methods = mp.get_all_start_methods()
        if "spawn" not in methods:
            raise RuntimeError(
                "P03_C8_CUDA_SAFE_SPAWN_UNAVAILABLE:"
                f"available_start_methods={methods}"
            )
        context = mp.get_context("spawn")
        self._commands = context.Queue()
        self._responses = context.Queue()
        self._worker = context.Process(
            target=_worker_main,
            args=(self.context, self._commands, self._responses),
            name="IHARQ-P03-L3-Scientific-Worker",
            daemon=True,
        )
        self._worker.start()

    def _heartbeat(self, stage_id: str, stop: threading.Event) -> None:
        while not stop.wait(HEARTBEAT_SECONDS):
            attempts = sorted((self.context.run_root / "attempts" / f"stage_{stage_id}").glob("attempt_*/progress.json"))
            if not attempts:
                print(json.dumps({"stage_id": stage_id, "heartbeat": "WAITING_FOR_PROGRESS_RECEIPT"}, sort_keys=True), flush=True)
                continue
            payload = json.loads(attempts[-1].read_text(encoding="utf-8"))
            payload["stage_id"] = stage_id
            payload["heartbeat_read_only"] = True
            print(json.dumps(payload, sort_keys=True), flush=True)

    def _verify_prerequisite(self, stage_id: str) -> None:
        index = int(stage_id)
        if index == 0:
            return
        previous = self.runner.receipt_path(f"{index - 1:02d}")
        if not previous.is_file() or json.loads(previous.read_text(encoding="utf-8")).get("status") != "COMPLETE":
            raise RuntimeError(f"STAGE_PREREQUISITE_NOT_COMPLETE:{index - 1:02d}")

    def run_stage(self, stage_id: str) -> dict[str, Any]:
        stage_id = f"{int(stage_id):02d}"
        if stage_id not in STAGE_META:
            raise KeyError(stage_id)
        self._verify_prerequisite(stage_id)
        if stage_id not in SCIENTIFIC_WORKER_STAGES:
            result = self.runner.run(stage_id, HANDLERS[stage_id])
            if stage_id == "24":
                self.shutdown()
            return result
        self._ensure_worker()
        assert self._commands is not None and self._responses is not None and self._worker is not None
        timeout = EXTENDED_TIMEOUTS_SECONDS.get(stage_id, DEFAULT_TIMEOUT_SECONDS)
        stop = threading.Event()
        heartbeat = threading.Thread(target=self._heartbeat, args=(stage_id, stop), daemon=True)
        heartbeat.start()
        self._commands.put({"stage_id": stage_id})
        try:
            response = self._responses.get(timeout=timeout)
        except queue.Empty as exc:
            failure = {"stage_id": stage_id, "terminal_status": "FAILED", "failure_class": "resource failure", "reason_code": "STAGE_TIMEOUT", "timeout_seconds": timeout, "worker_pid": self._worker.pid, "checkpoint_preserved": True}
            write_json(self.context.run_root / "artifacts" / "negative_and_failed_results" / "phase_03" / f"stage_{stage_id}_worker_timeout.json", failure)
            self._worker.terminate()
            self._worker.join(timeout=30)
            self._worker = None
            raise TimeoutError(f"P03 stage {stage_id} exceeded {timeout} seconds; partial attempt preserved") from exc
        finally:
            stop.set()
            heartbeat.join(timeout=2)
        if response["stage_id"] != stage_id:
            raise RuntimeError(f"Worker response order mismatch: expected {stage_id}, got {response['stage_id']}")
        if not response["ok"]:
            raise RuntimeError(f"{response['exception_type']}: {response['message']}\n{response['traceback']}")
        if stage_id == "20":
            self.shutdown()
        return response["payload"]

    def run_all(self, stop_after: str = "24") -> list[dict[str, Any]]:
        results = []
        for number in range(int(stop_after) + 1):
            results.append(self.run_stage(f"{number:02d}"))
        return results

    def recover(self) -> dict[str, Any]:
        """Read-only recovery view; run_stage performs exact-fingerprint reuse."""
        ledger = self.runner.ledger()
        complete = [row["stage_id"] for row in ledger["stages"] if row["status"] == "COMPLETE"]
        next_stage = f"{len(complete):02d}" if len(complete) < 25 else None
        return {"run_id": self.context.run_id, "complete_stages": complete, "next_stage": next_stage, "exact_fingerprint": self.context.immutable_fingerprint}

    def shutdown(self) -> None:
        if self._worker is not None:
            if self._worker.is_alive() and self._commands is not None:
                self._commands.put(None)
                self._worker.join(timeout=30)
            if self._worker.is_alive():
                self._worker.terminate()
                self._worker.join(timeout=10)
            self._worker = None

    def __enter__(self) -> "NotebookController":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.shutdown()
