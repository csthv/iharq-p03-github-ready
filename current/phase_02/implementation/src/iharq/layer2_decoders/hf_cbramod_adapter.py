from __future__ import annotations
import io,copy,numpy as np

class IHARQCBraModAdapter:
 score_type='NATIVE_SOFTMAX_PROBABILITY';resolved_variant='CBraMod-HF-Braindecode';supports_class_weights=False
 def __init__(self,checkpoint_path,config):
  self.checkpoint_path=str(checkpoint_path);self.config=dict(config or {});self.model=None;self.device='cpu';self._shape=None
 def _resample(self,X):
  from scipy.signal import resample_poly
  src=int(self.config.get('source_sampling_hz',160));dst=int(self.config.get('target_sampling_hz',200))
  if src==dst:return np.asarray(X,np.float32)
  import math;g=math.gcd(src,dst);return resample_poly(np.asarray(X,np.float32),dst//g,src//g,axis=-1).astype(np.float32)
 def _build(self,n_chans=None,n_times=None):
  from braindecode.models import CBraMod
  nc=int(n_chans or self._shape[0]);nt=int(n_times or self._shape[1]);patch=int(self.config.get('patch_size',200))
  if bool(self.config.get('strict_patch_alignment',True)) and nt%patch!=0:raise RuntimeError(f'INPUT_INCOMPATIBLE:CBRAMOD_PATCH_ALIGNMENT:{nt}%{patch}')
  local=self.config.get('pretrained_local_dir')
  if not local:raise RuntimeError('CHECKPOINT_BLOCKED:CBRAMOD_LOCAL_SNAPSHOT_MISSING')
  # Maintained Braindecode HubMixin loads the converted immutable pretrained checkpoint and rebuilds the task head.
  try:return CBraMod.from_pretrained(local,n_outputs=2,n_chans=nc,n_times=nt,sfreq=float(self.config.get('target_sampling_hz',200)))
  except Exception as exc:raise RuntimeError(f'CHECKPOINT_BLOCKED:CBRAMOD_PRETRAINED_LOAD:{type(exc).__name__}:{str(exc)[:180]}') from exc
 def fit(self,X,y,epochs=100,lr=1e-3,weight_decay=0.0,batch_size=64,effective_batch_target=64,device='cpu',X_val=None,y_val=None,patience=12,min_delta=0.0,restore_best=True,**kw):
  import torch
  from torch.utils.data import DataLoader,TensorDataset
  X=self._resample(X);Xv=self._resample(X_val) if X_val is not None else None;self._shape=(X.shape[1],X.shape[2]);self.model=self._build().to(device);self.device=device
  ds=TensorDataset(torch.as_tensor(X,dtype=torch.float32),torch.as_tensor(y,dtype=torch.long));loader=DataLoader(ds,batch_size=int(batch_size),shuffle=True)
  opt=torch.optim.AdamW(self.model.parameters(),lr=float(lr),weight_decay=float(weight_decay));lossf=torch.nn.CrossEntropyLoss();best=None;best_bacc=-1.;bad=0
  for _ in range(int(epochs)):
   self.model.train()
   for xb,yb in loader:
    xb,yb=xb.to(device),yb.to(device);opt.zero_grad(set_to_none=True);z=self.model(xb);z=z[0] if isinstance(z,(tuple,list)) else z;loss=lossf(z,yb);loss.backward();opt.step()
   if Xv is not None:
    pv=self.predict(X_val,device=device)
    from sklearn.metrics import balanced_accuracy_score
    b=float(balanced_accuracy_score(y_val,pv))
    if b>best_bacc+float(min_delta):best_bacc=b;best={k:v.detach().cpu().clone() for k,v in self.model.state_dict().items()};bad=0
    else:bad+=1
    if bad>=int(patience):break
  if restore_best and best is not None:self.model.load_state_dict(best,strict=True)
  return self
 def _scores(self,X,device=None):
  import torch
  X=self._resample(X);d=device or self.device;self.model.eval()
  with torch.no_grad():
   z=self.model(torch.as_tensor(X,dtype=torch.float32,device=d));z=z[0] if isinstance(z,(tuple,list)) else z
   return torch.softmax(z,dim=1).cpu().numpy()
 def predict_scores(self,X,device=None,**kw):return self._scores(X,device)
 def predict(self,X,device=None,**kw):return np.argmax(self._scores(X,device),axis=1)
 def export_iharq_checkpoint_bytes(self):
  import torch
  if self.model is None:raise RuntimeError('MODEL_NOT_FIT')
  b=io.BytesIO();torch.save({'state_dict':{k:v.detach().cpu() for k,v in self.model.state_dict().items()},'shape':self._shape},b);return b.getvalue()
 def reload_iharq_checkpoint_bytes(self,payload):
  import torch
  try:d=torch.load(io.BytesIO(payload),map_location='cpu',weights_only=True)
  except TypeError:d=torch.load(io.BytesIO(payload),map_location='cpu')
  q=IHARQCBraModAdapter(self.checkpoint_path,self.config);q._shape=tuple(d['shape']);q.model=q._build();q.model.load_state_dict(d['state_dict'],strict=True);q.model.eval();q.device='cpu';return q

def build_iharq_adapter(branch_id,checkpoint_path,config):
 if branch_id!='SSL-CBRAMOD':raise RuntimeError('CBRAMOD_ADAPTER_BRANCH_MISMATCH')
 return IHARQCBraModAdapter(checkpoint_path,config)
