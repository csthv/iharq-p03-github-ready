from __future__ import annotations
from pathlib import Path
import zipfile,json,yaml
from .identity import sha256_file
from .data import find_unique,CORE_MANIFEST,A4_MANIFEST
def resolve_inputs(root,spec):
 root=Path(root);req=spec['required'];zips=[p for p in root.rglob('*.zip') if p.is_file() and sha256_file(p)==req['cumulative_project']['sha256']]
 if len(zips)!=1:raise RuntimeError(f'CUMULATIVE_ZIP_EXPECTED_ONE:{len(zips)}')
 core=find_unique(root,req['p01_core']['resolver_file'],req['p01_core']['manifest_sha256']).parent;a4=find_unique(root,req['p01_a4']['resolver_file'],req['p01_a4']['manifest_sha256']).parent
 return {'cumulative_zip':str(zips[0]),'core_root':str(core),'a4_root':str(a4),'status':'PASS'}
def verify_cumulative(z):
 with zipfile.ZipFile(z) as x:
  bad=x.testzip();names=x.namelist();st=[n for n in names if n.endswith('CURRENT_PROJECT_STATUS.json')];ho=[n for n in names if n.endswith('IHARQ_P00_P01_to_P02_Clean_Input_Handoff_R1.yaml')]
  if bad or len(st)!=1 or len(ho)!=1:raise RuntimeError('CUMULATIVE_ZIP_INVALID')
  s=json.loads(x.read(st[0]));h=yaml.safe_load(x.read(ho[0]))['cumulative_handoff']
  if s.get('status')!='P00_P01_MERGED_VALIDATED_READY_FOR_P02_ENTRY' or h.get('p02_entry_readiness')!='PASS' or h.get('open_blockers'):raise RuntimeError('CUMULATIVE_STATE_NOT_READY')
 return {'status':'PASS','project_status':s['status'],'p02_entry_readiness':'PASS'}


def _within(base,p):
 base=Path(base).resolve(); p=Path(p).resolve()
 try:p.relative_to(base);return True
 except ValueError:return False

def resolve_conditional_assets(root,base_bindings,filename='IHARQ_P02_CONDITIONAL_MODEL_ASSETS.json'):
 """Resolve optional immutable conditional-model assets without notebook/source editing."""
 root=Path(root);hits=[p for p in root.rglob(filename) if p.is_file()]
 if len(hits)>1:raise RuntimeError(f'CONDITIONAL_ASSET_MANIFEST_EXPECTED_AT_MOST_ONE:{len(hits)}')
 out=json.loads(json.dumps(base_bindings));evidence={'status':'NOT_ATTACHED','manifest':None,'branches':{}}
 if not hits:return out,evidence
 mf=hits[0];d=json.loads(mf.read_text());branches=d.get('branches',{})
 if not isinstance(branches,dict):raise RuntimeError('CONDITIONAL_ASSET_BRANCH_OBJECT_REQUIRED')
 base=mf.parent;allowed=set(out);unknown=sorted(set(branches)-allowed)
 if unknown:raise RuntimeError(f'CONDITIONAL_ASSET_UNKNOWN_BRANCHES:{unknown}')
 def resolve_entry(branch,v):
  if not isinstance(v,dict):raise RuntimeError(f'CONDITIONAL_ASSET_BRANCH_OBJECT_REQUIRED:{branch}')
  q={k:v[k] for k in v if k not in {'module_file','checkpoint_file','python_path'}}
  py=v.get('python_path')
  if py:
   pp=(base/py).resolve()
   if not _within(base,pp) or not pp.exists():raise RuntimeError(f'CONDITIONAL_ASSET_UNSAFE_PYTHON_PATH:{branch}')
   q['python_path']=str(pp)
  modf=v.get('module_file')
  if modf:
   mp=(base/modf).resolve()
   if not _within(base,mp) or not mp.is_file():raise RuntimeError(f'CONDITIONAL_ASSET_MODULE_FILE_MISSING:{branch}')
   exp=v.get('module_sha256')
   if not exp or sha256_file(mp)!=exp:raise RuntimeError(f'CONDITIONAL_ASSET_MODULE_HASH_MISMATCH:{branch}')
   q['module_file']=str(mp);q['module_sha256']=exp
   if 'python_path' not in q:q['python_path']=str(mp.parent)
  chk=v.get('checkpoint_file')
  if chk:
   cp=(base/chk).resolve()
   if not _within(base,cp) or not cp.is_file():raise RuntimeError(f'CONDITIONAL_ASSET_CHECKPOINT_MISSING:{branch}')
   exp=v.get('checkpoint_sha256')
   if not exp or sha256_file(cp)!=exp:raise RuntimeError(f'CONDITIONAL_ASSET_CHECKPOINT_HASH_MISMATCH:{branch}')
   q['checkpoint_path']=str(cp);q['checkpoint_sha256']=exp
  return q
 for b,v in branches.items():
  baseq=dict(out.get(b,{}) or {})
  if b=='DNN-SEQ' and 'dbconformer' in v:
   inner=resolve_entry(b+':dbconformer',v['dbconformer']); merged=dict(baseq.get('dbconformer',{}) or {});merged.update(inner);baseq['dbconformer']=merged
   for k,val in v.items():
    if k!='dbconformer':baseq[k]=val
   q=baseq
  else:
   q=baseq;q.update(resolve_entry(b,v))
  out[b]=q;evidence['branches'][b]={'status':'VERIFIED','implementation_module':(q.get('dbconformer') or {}).get('implementation_module') if b=='DNN-SEQ' else q.get('implementation_module'),'module_sha256':(q.get('dbconformer') or {}).get('module_sha256') if b=='DNN-SEQ' else q.get('module_sha256'),'checkpoint_sha256':q.get('checkpoint_sha256'),'license_status':q.get('license_status') or (q.get('dbconformer') or {}).get('license_status')}
 evidence.update(status='PASS',manifest=str(mf),manifest_sha256=sha256_file(mf))
 return out,evidence


def resolve_conditional_assets_hybrid(root,base_bindings,hf_spec,hf_work_root,hf_token=None,hf_token_source="NONE"):
 """Offline/pre-attached assets first, then HF for still-governed eligible branches."""
 attached,e1=resolve_conditional_assets(root,base_bindings)
 from .hf_assets import resolve_hf_assets
 merged,e2=resolve_hf_assets(attached,hf_spec,hf_work_root,token=hf_token,token_source=hf_token_source)
 return merged,{'status':'PASS','pre_attached':e1,'huggingface':e2,'resolution_order':['PRE_ATTACHED_VERIFIED_ASSET','HUGGING_FACE_GOVERNED_RETRIEVAL'],'token_value_persisted':False}
