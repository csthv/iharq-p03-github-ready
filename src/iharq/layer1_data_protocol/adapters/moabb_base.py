from __future__ import annotations
from pathlib import Path
from typing import Any
import os, re
import numpy as np
from .base import BaseDatasetAdapter, SourceAccessError
from ..models import RawRecording, Event

class MOABBAdapterBase(BaseDatasetAdapter):
    dataset_class_name=""
    def _import_dataset_class(self):
        try:
            from moabb import datasets
        except Exception as exc: raise SourceAccessError(f"MOABB 1.5.0 import failed: {exc}") from exc
        cls=getattr(datasets,self.dataset_class_name,None)
        if cls is None: raise SourceAccessError(f"MOABB dataset class unavailable: {self.dataset_class_name}")
        return cls
    def _dataset_kwargs(self)->dict[str,Any]: return {}
    def _subjects(self)->list[int]:
        raw=self.profile.adapter_options.get("subjects",[])
        if isinstance(raw,str) and re.fullmatch(r"\d+\-\d+",raw):
            a,b=map(int,raw.split('-')); return list(range(a,b+1))
        return [int(x) for x in raw]
    def _make_dataset(self): return self._import_dataset_class()(**self._dataset_kwargs())
    def resolve_files(self)->list[Path]:
        if self.profile.adapter_options.get("allow_byte_equivalent_attachment_fallback", False):
            raise SourceAccessError("R6 official execution forbids the previously advertised generic attachment fallback; use the frozen MOABB provider-download route")
        os.environ.setdefault("MNE_DATA",str(self.cache_root))
        dataset=self._make_dataset(); files=[]; self._resolved_files_by_subject={}
        for subject in self._subjects():
            try:
                paths=dataset.data_path(subject,path=str(self.cache_root),force_update=False,update_path=True,verbose=False)
            except TypeError:
                paths=dataset.data_path(subject,path=str(self.cache_root),force_update=False,update_path=True)
            subject_files=[]
            for p in paths if isinstance(paths,(list,tuple)) else [paths]:
                pp=Path(p)
                if pp.is_file(): subject_files.append(pp)
                elif pp.is_dir(): subject_files.extend(x for x in pp.rglob('*') if x.is_file())
            exact=sorted(set(subject_files)); self._resolved_files_by_subject[int(subject)]=exact; files.extend(exact)
        return sorted(set(files))
    def _label_for_annotation(self,label:str,run_id:str)->str: return str(label)
    def _include_run(self,run_id:str)->bool: return True
    def _canonical_run_id(self,run_id:str)->str: return str(run_id)
    def _run_metadata(self,run_id:str)->dict[str,Any]: return {"moabb_run_key":str(run_id)}
    def _raw_to_recording(self,raw,subject:int,session_id:str,run_id:str,source_file:str,source_run_metadata:dict[str,Any]|None=None)->RawRecording:
        if not self._include_run(run_id): raise SourceAccessError(f"run excluded by frozen source policy: {run_id}")
        sf=float(raw.info['sfreq']); signal=raw.get_data().astype(np.float64,copy=False)
        ch_types=list(raw.get_channel_types()); events=[]
        for i,(onset,duration,label) in enumerate(zip(raw.annotations.onset,raw.annotations.duration,raw.annotations.description)):
            start=max(0,int(round(float(onset)*sf))); dur=max(1,int(round(max(float(duration),1.0/sf)*sf))); mapped=self._label_for_annotation(str(label),str(run_id))
            events.append(Event(f"{self.profile.dataset_id}:{subject}:{session_id}:{run_id}:event:{i}",start,start+dur,mapped,{"source_annotation":str(label),"original_source_event_sample":start,"original_onset_seconds":float(onset),"source_duration_seconds":float(duration)}))
        if not events:
            try:
                import mne
                arr,event_id=mne.events_from_annotations(raw,verbose='ERROR')
                inv={v:k for k,v in event_id.items()}
                for i,row in enumerate(arr):
                    label=inv.get(int(row[2]),str(int(row[2]))); mapped=self._label_for_annotation(str(label),str(run_id)); start=int(row[0])
                    events.append(Event(f"{self.profile.dataset_id}:{subject}:{session_id}:{run_id}:event:{i}",start,start+1,mapped,{"source_annotation":str(label),"original_source_event_sample":start,"original_onset_seconds":start/sf}))
            except Exception: pass
        return RawRecording(self.profile.dataset_id,str(subject),str(session_id),str(run_id),source_file,sf,list(raw.ch_names),signal,events,
             {"format":"MOABB_MNE_RAW","channel_types":ch_types,"source_native_preprocessing":self.profile.source_native_preprocessing,"_mne_raw":raw.copy(),"source_class":self.dataset_class_name,**(source_run_metadata or {})})
    def load(self,files:list[Path])->list[RawRecording]:
        dataset=self._make_dataset(); out=[]
        for subject in self._subjects():
            data=dataset.get_data(subjects=[subject],n_jobs=1)
            subtree=data.get(subject) or data.get(str(subject))
            if subtree is None: raise SourceAccessError(f"MOABB returned no data for subject {subject}")
            exact_files=getattr(self,'_resolved_files_by_subject',{}).get(int(subject),[])
            if not exact_files:
                raise SourceAccessError(f"exact source-file provenance missing for subject {subject}; generic substring matching is forbidden")
            source_file=';'.join(str(p) for p in exact_files)
            for session_id,runs in subtree.items():
                for run_id,raw in runs.items():
                    raw_run_id=str(run_id)
                    if not self._include_run(raw_run_id): continue
                    canonical_run_id=self._canonical_run_id(raw_run_id)
                    out.append(self._raw_to_recording(raw,subject,str(session_id),canonical_run_id,source_file,self._run_metadata(raw_run_id)))
        if not out: raise SourceAccessError(f"no recordings loaded by {self.dataset_class_name}")
        return out
