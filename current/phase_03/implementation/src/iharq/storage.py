from __future__ import annotations
from pathlib import Path
import json
from .manifests import file_digest

def pointer_manifest(path:str|Path,artifact_id:str,source_commit:str='LOCAL_NO_GIT_COMMIT'):
    p=Path(path)
    return {'artifact_id':artifact_id,'uri':p.resolve().as_uri(),'sha256':file_digest(p),'bytes':p.stat().st_size,'source_commit':source_commit,'lifecycle_status':'CREATED','evidence_status':'LOCAL_CANDIDATE'}
def atomic_json(path:str|Path,obj):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); tmp=p.with_suffix(p.suffix+'.tmp'); tmp.write_text(json.dumps(obj,indent=2)+'\n'); tmp.replace(p)
