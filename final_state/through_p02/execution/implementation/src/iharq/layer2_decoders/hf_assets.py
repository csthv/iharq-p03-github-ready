from __future__ import annotations
from pathlib import Path
import copy,hashlib,json

def _sha(path):
 h=hashlib.sha256()
 with open(path,'rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()

def _safe_error(exc):
 # Never preserve request headers, URLs containing tokens, or reprs with credentials.
 return f"{type(exc).__name__}:{str(exc)[:240]}".replace('hf_','[HF_TOKEN_REDACTED_PREFIX]')

def token_summary(token,source='NONE'):
 return {'credential_required':False,'credential_available':bool(token),'credential_source_type':source if token else 'NONE','credential_value':'REDACTED' if token else 'NOT_SET'}

def resolve_hf_assets(base_bindings,spec,work_root,token=None,token_source="NONE"):
 """Resolve eligible governed HF assets. Never persists or returns token values."""
 out=copy.deepcopy(base_bindings); evidence={'policy_id':spec['policy_id'],'status':'PASS','token':token_summary(token,token_source),'branches':{}}
 cache=Path(work_root)/'_hf_runtime'; cache.mkdir(parents=True,exist_ok=True)
 try:
  from huggingface_hub import hf_hub_download
 except Exception as exc:
  # Only eligible HF branches are dependency-blocked; mandatory baseline remains unaffected.
  for branch,a in spec.get('assets',{}).items():
   evidence['branches'][branch]={'status':'DEPENDENCY_BLOCKED' if a.get('eligibility')=='ELIGIBLE_CURRENT_P02' else a.get('eligibility'),'reason':'huggingface_hub unavailable' if a.get('eligibility')=='ELIGIBLE_CURRENT_P02' else 'NONCREDENTIAL_SCIENTIFIC_GATE'}
  return out,evidence
 for branch,a in spec.get('assets',{}).items():
  if not a.get('enabled',False):
   evidence['branches'][branch]={'status':'DISABLED_BY_FROZEN_POLICY'};continue
  if a.get('eligibility')!='ELIGIBLE_CURRENT_P02':
   # Important: do not prompt/download a gated model that already fails a scientific gate.
   q=dict(out.get(branch,{}) or {});q['corpus_overlap_status']=a.get('corpus_overlap_status',q.get('corpus_overlap_status'));q['license_status']=a.get('license_status',q.get('license_status'));out[branch]=q
   evidence['branches'][branch]={'status':a.get('eligibility'),'repo_id':a.get('repo_id'),'gated':bool(a.get('gated')),'download_attempted':False,'token_used':False,'reason':a.get('corpus_overlap_basis') or 'NONCREDENTIAL_GATE'};continue
  if a.get('gated') and not token:
   evidence['branches'][branch]={'status':'AUTH_REQUIRED','repo_id':a['repo_id'],'gated':True,'download_attempted':False,'token_used':False};continue
  local=cache/branch;local.mkdir(parents=True,exist_ok=True);files={};failure=None
  for f in a.get('files',[]):
   try:
    p=Path(hf_hub_download(repo_id=a['repo_id'],repo_type=a.get('repo_type'),filename=f['filename'],revision=a['revision'],token=token,local_dir=str(local)))
    got=_sha(p);exp=f.get('sha256')
    if exp and got.lower()!=str(exp).lower():raise RuntimeError(f"HF_ASSET_SHA256_MISMATCH:{branch}:{f['filename']}")
    files[f['filename']]={'sha256':got,'bytes':p.stat().st_size,'required':bool(f.get('required',True)),'path':str(p)}
   except Exception as exc:
    failure=_safe_error(exc);break
  if failure:
   evidence['branches'][branch]={'status':'DOWNLOAD_BLOCKED','repo_id':a['repo_id'],'revision':a.get('revision'),'gated':bool(a.get('gated')),'download_attempted':True,'token_used':bool(token),'reason':failure};continue
  chk=files[a['checkpoint_file']]['path'];q=dict(out.get(branch,{}) or {});q.update({
   'implementation_module':a['implementation_module'],'license_status':a['license_status'],'checkpoint_required':True,'checkpoint_path':chk,
   'checkpoint_sha256':a['checkpoint_sha256'],'corpus_overlap_status':a['corpus_overlap_status'],'input_compatibility_status':a['input_compatibility_status'],
   'channel_montage_status':a['channel_montage_status'],'source_recipe_verified':bool(a['source_recipe_verified']),'sampling_adapter_verified':bool(a['sampling_adapter_verified']),
   'target_sampling_hz':a['target_sampling_hz'],'plugin_config':{**dict(q.get('plugin_config',{}) or {}),**dict(a.get('plugin_config',{}) or {}),'hf_repo_id':a['repo_id'],'hf_revision':a['revision'],'pretrained_local_dir':str(local)}
  });out[branch]=q
  evidence['branches'][branch]={'status':'VERIFIED','repo_id':a['repo_id'],'revision':a['revision'],'gated':bool(a.get('gated')),'download_attempted':True,'token_used':bool(token),'files':{k:{x:y for x,y in v.items() if x!='path'} for k,v in files.items()},'cache_policy':'EPHEMERAL_EXCLUDED_FROM_EXECUTION_BUNDLE','license_status':a['license_status'],'corpus_overlap_status':a['corpus_overlap_status']}
 return out,evidence
