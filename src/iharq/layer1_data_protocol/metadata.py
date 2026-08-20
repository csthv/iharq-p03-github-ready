from __future__ import annotations
from collections import Counter
from typing import Any
from .models import RawRecording

def normalize_metadata(recordings:list[RawRecording])->tuple[list[RawRecording],dict[str,Any]]:
    missing=[]
    for r in recordings:
        for field,value in [("subject_id",r.subject_id),("session_id",r.session_id),("run_id",r.run_id),("sampling_hz",r.sampling_hz)]:
            if value in {None,""}: missing.append({"source_file":r.source_file,"field":field})
        if not r.channel_names: missing.append({"source_file":r.source_file,"field":"channel_names"})
        if not r.events: missing.append({"source_file":r.source_file,"field":"events"})
    summary={
        "subjects":sorted({r.subject_id for r in recordings}),"sessions":sorted({r.session_id for r in recordings}),"runs":sorted({r.run_id for r in recordings}),
        "event_count":sum(len(r.events) for r in recordings),"channel_sets":sorted({"|".join(r.channel_names) for r in recordings}),
        "sampling_hz":sorted({str(r.sampling_hz) for r in recordings}),"completeness":{"missing_count":len(missing),"missing":missing},
    }
    return recordings,summary
