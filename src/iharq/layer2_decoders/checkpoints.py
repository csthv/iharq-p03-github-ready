from __future__ import annotations
from pathlib import Path
import io,pickle,copy,numpy as np
from .identity import sha256_file
from .writers import atomic_bytes

def _torch_target(model):
    # Built-in neural adapters keep the actual torch module on .model. The governed
    # sequence slot resolves to a delegate; checkpoint the resolved implementation.
    target=getattr(model,'delegate',None) or model
    mod=getattr(target,'model',None)
    if mod is None:return None
    try:
        import torch
        return target if isinstance(mod,torch.nn.Module) else None
    except ImportError:
        return None

def _torch_state_roundtrip(model,X,path):
    import torch
    target=_torch_target(model)
    if target is None:return None
    # Save tensors/state only. Architecture is reconstructed from the already frozen
    # adapter/config, then state is loaded with weights_only where supported.
    state={k:v.detach().cpu() for k,v in target.model.state_dict().items()}
    bio=io.BytesIO();torch.save(state,bio);p=Path(path).with_suffix('.state_dict.pt');atomic_bytes(p,bio.getvalue());sha=sha256_file(p)
    try:
        raw=p.read_bytes()
        try:loaded=torch.load(io.BytesIO(raw),map_location='cpu',weights_only=True)
        except TypeError:loaded=torch.load(io.BytesIO(raw),map_location='cpu')
        fresh=target._build().cpu();fresh.load_state_dict(loaded,strict=True);fresh.eval()
        old=target.model;old_device=getattr(target,'device','cpu')
        # Compare predictions through a clean adapter copy that owns only reconstructed state.
        clone=copy.copy(target);clone.model=fresh;clone.device='cpu'
        a=np.asarray(target.predict(X,device=old_device));b=np.asarray(clone.predict(X,device='cpu'));ok=np.array_equal(a,b)
    except (RuntimeError,ValueError,KeyError,TypeError,AttributeError) as e:
        return {'status':'FAIL','reason':type(e).__name__,'message':str(e)[:200],'checkpoint_sha256':sha,'checkpoint_bytes':p.stat().st_size,'path':str(p),'checkpoint_format':'PYTORCH_STATE_DICT_WEIGHTS_ONLY'}
    return {'status':'PASS' if ok else 'FAIL','reason':None if ok else 'PREDICTION_EQUIVALENCE_MISMATCH','checkpoint_sha256':sha,'checkpoint_bytes':p.stat().st_size,'path':str(p),'checkpoint_format':'PYTORCH_STATE_DICT_WEIGHTS_ONLY'}

def _external_roundtrip(model,X,path):
    target=getattr(model,'plugin',None)
    if target is None:return None
    export=getattr(target,'export_iharq_checkpoint_bytes',None);reload=getattr(target,'reload_iharq_checkpoint_bytes',None)
    if not callable(export) or not callable(reload):
        return {'status':'FAIL','reason':'EXTERNAL_SAFE_CHECKPOINT_INTERFACE_MISSING','checkpoint_sha256':None,'checkpoint_bytes':0,'path':str(path),'checkpoint_format':'EXTERNAL_GOVERNED_INTERFACE_REQUIRED'}
    try:
        payload=export();
        if not isinstance(payload,(bytes,bytearray)):raise TypeError('EXTERNAL_CHECKPOINT_BYTES_REQUIRED')
        p=Path(path).with_suffix('.external.chk');atomic_bytes(p,bytes(payload));sha=sha256_file(p);clone=reload(p.read_bytes());a=np.asarray(target.predict(X));b=np.asarray(clone.predict(X));ok=np.array_equal(a,b)
    except (RuntimeError,ValueError,TypeError,AttributeError,ImportError) as e:
        return {'status':'FAIL','reason':type(e).__name__,'message':str(e)[:200],'checkpoint_sha256':sha if 'sha' in locals() else None,'checkpoint_bytes':p.stat().st_size if 'p' in locals() and p.exists() else 0,'path':str(path),'checkpoint_format':'EXTERNAL_GOVERNED_INTERFACE'}
    return {'status':'PASS' if ok else 'FAIL','reason':None if ok else 'PREDICTION_EQUIVALENCE_MISMATCH','checkpoint_sha256':sha,'checkpoint_bytes':p.stat().st_size,'path':str(p),'checkpoint_format':'EXTERNAL_GOVERNED_INTERFACE'}

def save_roundtrip(model,X,path):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    tr=_torch_state_roundtrip(model,X,p)
    if tr is not None:return tr
    er=_external_roundtrip(model,X,p)
    if er is not None:return er
    # Classical/riemannian estimators are trusted project-generated objects inside the
    # pinned environment. Arbitrary external pickle is never accepted here.
    atomic_bytes(p,pickle.dumps(model,protocol=5));sha=sha256_file(p)
    try:
        m=pickle.loads(p.read_bytes());a=np.asarray(model.predict(X));b=np.asarray(m.predict(X));ok=np.array_equal(a,b)
    except (pickle.PickleError,EOFError,AttributeError,TypeError,ValueError,ImportError,RuntimeError) as e:
        return {'status':'FAIL','reason':type(e).__name__,'message':str(e)[:200],'checkpoint_sha256':sha,'checkpoint_bytes':p.stat().st_size,'path':str(p),'checkpoint_format':'TRUSTED_PROJECT_PICKLE_PINNED_ENVIRONMENT'}
    return {'status':'PASS' if ok else 'FAIL','reason':None if ok else 'PREDICTION_EQUIVALENCE_MISMATCH','checkpoint_sha256':sha,'checkpoint_bytes':p.stat().st_size,'path':str(p),'checkpoint_format':'TRUSTED_PROJECT_PICKLE_PINNED_ENVIRONMENT'}
