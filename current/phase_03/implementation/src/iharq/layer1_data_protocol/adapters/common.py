from __future__ import annotations
from pathlib import Path
from typing import Any
import numpy as np
from ..models import RawRecording, Event
from .base import BaseDatasetAdapter, SourceAccessError

def _identity_from_path(path:Path,options:dict[str,Any])->tuple[str,str,str]:
    pattern=options.get("identity_regex")
    if pattern:
        import re
        m=re.search(pattern,path.as_posix())
        if m: return (m.groupdict().get("subject","unknown"),m.groupdict().get("session","session1"),m.groupdict().get("run",path.stem))
    return (path.parent.parent.name or "unknown",path.parent.name or "session1",path.stem)

def _load_npz(path:Path,dataset_id:str,options:dict[str,Any])->RawRecording:
    data=np.load(path,allow_pickle=False)
    signal=np.asarray(data[options.get("signal_key","signal")],dtype=np.float64)
    if signal.ndim!=2: raise SourceAccessError("NPZ signal must be channels x samples")
    sampling=float(np.asarray(data[options.get("sampling_key","sampling_hz")]).item())
    channels=[str(x) for x in np.asarray(data[options.get("channels_key","channel_names")]).tolist()]
    starts=np.asarray(data[options.get("event_start_key","event_starts")],dtype=int)
    stops=np.asarray(data[options.get("event_stop_key","event_stops")],dtype=int)
    labels=np.asarray(data[options.get("event_label_key","event_labels")]).astype(str)
    subject,session,run=_identity_from_path(path,options)
    events=[Event(f"{dataset_id}:{subject}:{session}:{run}:event:{i}",int(a),int(b),str(l)) for i,(a,b,l) in enumerate(zip(starts,stops,labels))]
    return RawRecording(dataset_id,subject,session,run,str(path),sampling,channels,signal,events,{"format":"NPZ"})

def _load_mne(path:Path,dataset_id:str,options:dict[str,Any])->RawRecording:
    import mne
    suffix=path.suffix.lower()
    if suffix==".edf": raw=mne.io.read_raw_edf(path,preload=True,verbose="ERROR")
    elif suffix==".gdf": raw=mne.io.read_raw_gdf(path,preload=True,verbose="ERROR")
    elif suffix==".fif": raw=mne.io.read_raw_fif(path,preload=True,verbose="ERROR")
    else: raise SourceAccessError(f"unsupported MNE source extension {suffix}")
    signal=raw.get_data().astype(np.float64,copy=False)
    ann=raw.annotations
    events=[]
    for i,(onset,duration,label) in enumerate(zip(ann.onset,ann.duration,ann.description)):
        start=max(0,int(round(float(onset)*raw.info["sfreq"])))
        stop=max(start+1,int(round((float(onset)+max(float(duration),1.0/raw.info["sfreq"]))*raw.info["sfreq"])))
        events.append(Event(f"{dataset_id}:{path.stem}:event:{i}",start,stop,str(label)))
    subject,session,run=_identity_from_path(path,options)
    return RawRecording(dataset_id,subject,session,run,str(path),float(raw.info["sfreq"]),list(raw.ch_names),signal,events,{"format":suffix[1:].upper()})

def _load_mat(path:Path,dataset_id:str,options:dict[str,Any])->RawRecording:
    from scipy.io import loadmat
    mat=loadmat(path,squeeze_me=True,struct_as_record=False)
    sk=options.get("signal_key"); lk=options.get("labels_key"); ek=options.get("event_starts_key"); srk=options.get("sampling_key")
    if not all([sk,lk,ek,srk]): raise SourceAccessError("MAT adapter requires signal_key, labels_key, event_starts_key and sampling_key")
    signal=np.asarray(mat[sk],dtype=np.float64)
    if signal.ndim!=2: raise SourceAccessError("MAT signal must be 2-D")
    if options.get("samples_first",True): signal=signal.T
    labels=np.asarray(mat[lk]).reshape(-1).astype(str)
    starts=np.asarray(mat[ek]).reshape(-1).astype(int)
    sampling=float(np.asarray(mat[srk]).item())
    duration=int(options.get("event_duration_samples") or 1)
    subject,session,run=_identity_from_path(path,options)
    channels=[str(x) for x in options.get("channel_names",[f"CH{i+1}" for i in range(signal.shape[0])])]
    events=[Event(f"{dataset_id}:{subject}:{session}:{run}:event:{i}",int(a),int(a+duration),str(l)) for i,(a,l) in enumerate(zip(starts,labels))]
    return RawRecording(dataset_id,subject,session,run,str(path),sampling,channels,signal,events,{"format":"MAT"})

class AttachmentDatasetAdapter(BaseDatasetAdapter):
    def load(self,files:list[Path])->list[RawRecording]:
        out=[]; options=self.profile.adapter_options
        allowed=set(str(x).lower() for x in options.get("extensions",[".npz",".edf",".gdf",".fif",".mat"]))
        for path in files:
            if path.suffix.lower() not in allowed: continue
            if path.suffix.lower()==".npz": out.append(_load_npz(path,self.profile.dataset_id,options))
            elif path.suffix.lower()==".mat": out.append(_load_mat(path,self.profile.dataset_id,options))
            else: out.append(_load_mne(path,self.profile.dataset_id,options))
        if not out: raise SourceAccessError("no supported source files were loaded")
        return out
