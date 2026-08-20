from __future__ import annotations

import hashlib
import inspect
import multiprocessing as mp
import traceback

from iharq.layer3_calibration_uncertainty.stage_runner import StageRunner
from iharq.layer3_calibration_uncertainty.stages import HANDLERS as BASE_HANDLERS
import iharq_p03_l3_norule_runtime_amendment_r1 as r1

R2_ID = 'P03-L3-EXEC-TRANSPORT-AMEND-NO-RULE-SPAWN-R2'
R1_ID = 'P03-L3-IMPL-AMEND-NO-RULE-R1'
R1_OVERLAY_SHA256 = '4b4aa2d0fd0d648c1a852c80465a5aa823a4464daf276ec2c4d7c4301694e01c'
AFFECTED_STAGES = ('14', '15', '16', '17', '18', '20', '23')


def _handler_table():
    handlers = dict(BASE_HANDLERS)
    for sid in AFFECTED_STAGES:
        handlers[sid] = getattr(r1, f"stage_{sid}")
    return handlers


def _worker_main(context, commands, responses):
    # Spawned child imports this module from the governed R2 amendment path.
    # No notebook-memory inheritance is assumed.
    handlers = _handler_table()
    runner = StageRunner(context)
    while True:
        command = commands.get()
        if command is None:
            return
        stage_id = command["stage_id"]
        try:
            result = runner.run(stage_id, handlers[stage_id])
            responses.put({"stage_id": stage_id, "ok": True, "payload": result})
        except Exception as exc:
            responses.put({
                "stage_id": stage_id,
                "ok": False,
                "exception_type": type(exc).__name__,
                "message": str(exc),
                "traceback": traceback.format_exc(),
            })


def _probe_worker(response_queue):
    handlers = _handler_table()
    rows = {}
    for sid in AFFECTED_STAGES:
        fn = handlers[sid]
        src = inspect.getsource(fn)
        rows[sid] = {
            "module": fn.__module__,
            "source_file": inspect.getsourcefile(fn),
            "source_sha256": hashlib.sha256(src.encode("utf-8")).hexdigest(),
        }
    response_queue.put({
        "start_method": mp.get_start_method(),
        "r1_module_file": r1.__file__,
        "r1_overlay_file_sha256": _sha_file(r1.__file__),
        "handlers": rows,
    })


def _sha_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()
