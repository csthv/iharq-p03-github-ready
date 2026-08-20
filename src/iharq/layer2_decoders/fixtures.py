from __future__ import annotations
import hashlib,numpy as np
DATASET='PhysioNetMI';N_CHANS=8
def _seed(x):return int(hashlib.sha256(x.encode()).hexdigest()[:8],16)
def _sig(ev,label,n):
 rng=np.random.default_rng(_seed(ev));t=np.linspace(0,1,n,endpoint=False);y=1 if label=='right_hand' else -1;x=rng.normal(0,.35,(N_CHANS,n)).astype('float32');x[0]+=y*.9*np.sin(2*np.pi*10*t);x[1]+=y*.5*np.cos(2*np.pi*18*t);x[2]+=y*.25;return x
def _rows(role,n,subs,offset):
 out=[]
 for lab in ('left_hand','right_hand'):
  for i in range(n):
   ev=f'FIXTURE:{role}:{lab}:{offset+i:04d}';out.append({'window_record_id':f'FX-WR-{role}-{lab}-{i}','window_id':f'FX-WIN-{role}-{lab}-{i}','dataset_id':DATASET,'subject_id':f'FX-{role[:2]}-{i%subs:02d}','session_id':'S1','run_id':'R1','event_id':ev,'role':role,'label':lab,'split_record_id':'FIXTURE-SPLIT','fixture':True})
 return out
class SyntheticCoreDataset:
 def __init__(self):self._index=_rows('train',24,6,0)+_rows('calibration',32,4,100)+_rows('validation',12,6,200)+_rows('test',12,6,300)
 def rows(self,dataset_id=None,role=None):return [r for r in self._index if (dataset_id is None or r['dataset_id']==dataset_id) and (role is None or r['role']==role)]
 def load_rows(self,rows):
  rows=list(rows);return np.stack([_sig(r['event_id'],r['label'],480) for r in rows]),np.array([r['label']=='right_hand' for r in rows],int),rows
class SyntheticA4Dataset:
 def __init__(self,core):self.core=core;self._rows=[{**r,'a4_component':'LONGER_WINDOW'} for r in core.rows()];self._map={r['event_id']:r for r in self._rows}
 def rows(self,dataset_id=None,role=None):return [r for r in self._rows if (dataset_id is None or r['dataset_id']==dataset_id) and (role is None or r['role']==role)]
 def parent_ids(self):return set(self._map)
 def load_rows(self,rows,member_index=None):
  rows=list(rows);x=np.stack([_sig(r['event_id'],r['label'],560) for r in rows]);
  if member_index is not None:
   a,b={1:(0,320),2:(120,440),3:(240,560)}[int(member_index)];x=x[...,a:b]
  return x,np.array([r['label']=='right_hand' for r in rows],int),rows
 def verify_parent_match(self,core):
  c={r['event_id'] for r in core.rows()};a=self.parent_ids();return {'core':len(c),'a4':len(a),'missing_a4':sorted(c-a),'unexpected_a4':sorted(a-c),'status':'PASS' if a==c else 'FAIL','fixture':True}
def fixture_identity():return {'fixture':True,'scientific_evidence':False,'labels':['FIXTURE','NON_SCIENTIFIC','NOT_P02_EVIDENCE']}
