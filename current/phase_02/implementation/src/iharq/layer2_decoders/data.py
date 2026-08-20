from __future__ import annotations
from pathlib import Path
import json,re,hashlib,numpy as np
from .identity import sha256_file
CORE_MANIFEST='IHARQ_P01_L1_DERIVED_WINDOW_DATASET_MANIFEST.json';CORE_INDEX='IHARQ_P01_L1_WINDOW_INDEX.jsonl';CORE_LOC='IHARQ_P01_L1_WINDOW_TO_SHARD_INDEX.jsonl';A4_MANIFEST='IHARQ_P01_L1_A4_DERIVED_WINDOW_DATASET_MANIFEST.json';A4_INDEX='IHARQ_P01_L1_A4_WINDOW_INDEX.jsonl'
def _match(p,n):return p.name==n or bool(re.fullmatch(rf'\d+_{re.escape(n)}',p.name))
def find_unique(root,n,sha=None):
 xs=[p.resolve() for p in Path(root).rglob('*') if p.is_file() and _match(p,n)];
 if sha:xs=[p for p in xs if sha256_file(p)==sha]
 if len(xs)!=1:raise RuntimeError(f'FILE_RESOLUTION_EXPECTED_ONE:{n}:{len(xs)}')
 return xs[0]
def rows_jsonl(p):return [json.loads(x) for x in Path(p).read_text().splitlines() if x.strip()]
class CoreWindowDataset:
 def __init__(self,root,manifest_sha=None):
  self.root=Path(root);self.manifest_path=find_unique(root,CORE_MANIFEST,manifest_sha);self.manifest=json.loads(self.manifest_path.read_text())
  if self.manifest.get('scientific_freeze')!='P01-L1-OFFICIAL-RUN-FREEZE-R2':raise RuntimeError('CORE_FREEZE_MISMATCH')
  self.index=rows_jsonl(find_unique(root,CORE_INDEX));self.locations={r['window_record_id']:r for r in rows_jsonl(find_unique(root,CORE_LOC))};self.shards={r['filename']:r for r in self.manifest.get('shards',[])};self.verified=set()
  expected=int(self.manifest.get('window_count',-1));
  if expected<=0 or len(self.index)!=expected or len(self.locations)!=expected or len({r['window_record_id'] for r in self.index})!=expected:raise RuntimeError('CORE_INDEX_COUNT_MISMATCH')
 def rows(self,dataset_id=None,role=None):return [r for r in self.index if (dataset_id is None or r['dataset_id']==dataset_id) and (role is None or r['role']==role)]
 def _shard(self,n):
  p=find_unique(self.root,n);s=self.shards[n]
  if n not in self.verified:
   if p.stat().st_size!=int(s['bytes']) or sha256_file(p)!=s['sha256']:raise RuntimeError(f'CORE_SHARD_INTEGRITY:{n}')
   self.verified.add(n)
  return p
 def load_rows(self,rows):
  import h5py
  rows=list(rows); by={};out=[None]*len(rows)
  for i,r in enumerate(rows):
   loc=self.locations[r['window_record_id']];by.setdefault(loc['shard_filename'],[]).append((i,loc))
  for n,items in by.items():
   with h5py.File(self._shard(n),'r') as h:
    for i,loc in items:out[i]=np.asarray(h[f'{loc["hdf5_group"]}/signals'][int(loc['hdf5_row'])],dtype='float32')
  return np.stack(out),np.array([r['label']=='right_hand' for r in rows],int),rows
class A4WindowDataset:
 def __init__(self,root,manifest_sha=None):
  self.root=Path(root);self.manifest_path=find_unique(root,A4_MANIFEST,manifest_sha);self.manifest=json.loads(self.manifest_path.read_text())
  fam=self.manifest.get('a4_window_family',{})
  if fam.get('window_family_id')!='P01-L1-A4-WINDOW-FAMILY-FREEZE-R2':raise RuntimeError('A4_FREEZE_MISMATCH')
  self.index=rows_jsonl(find_unique(root,A4_INDEX));self.long=[r for r in self.index if r['a4_component']=='LONGER_WINDOW'];self.map={r['event_id']:r for r in self.long};self.shards={r['filename']:r for r in self.manifest.get('shards',[])};self.verified=set();self.member_slices={int(x['member_index']):(int(x['slice_start']),int(x['slice_stop'])) for x in fam.get('multi_window_profile',{}).get('member_slices',[])}
  expected_rows=int(self.manifest.get('a4_window_record_count',-1));expected_parents=int(self.manifest.get('materialized_matched3p5s_event_count',-1));long_rows=int(self.manifest.get('longer_window_record_count',-1));
  if expected_rows<=0 or expected_parents<=0 or len(self.index)!=expected_rows or len(self.map)!=expected_parents or len(self.long)!=long_rows or long_rows!=expected_parents:raise RuntimeError('A4_INDEX_COUNT_MISMATCH')
 def rows(self,dataset_id=None,role=None):return [r for r in self.long if (dataset_id is None or r['dataset_id']==dataset_id) and (role is None or r['role']==role)]
 def parent_ids(self):return set(self.map)
 def _shard(self,n):
  p=find_unique(self.root,n);s=self.shards[n]
  if n not in self.verified:
   if p.stat().st_size!=int(s['bytes']) or sha256_file(p)!=s['sha256']:raise RuntimeError(f'A4_SHARD_INTEGRITY:{n}')
   self.verified.add(n)
  return p
 def load_rows(self,rows,member_index=None):
  import h5py
  rows=list(rows);by={};out=[None]*len(rows);span=None if member_index is None else self.member_slices[int(member_index)]
  for i,r in enumerate(rows):by.setdefault(r['external_shard_filename'],[]).append((i,r))
  for n,items in by.items():
   with h5py.File(self._shard(n),'r') as h:
    for i,r in items:
     x=np.asarray(h[f'{r["hdf5_group"]}/signals'][int(r['hdf5_row'])],dtype='float32');out[i]=x if span is None else x[...,span[0]:span[1]]
  return np.stack(out),np.array([r['label']=='right_hand' for r in rows],int),rows
 def verify_parent_match(self,core):
  c={r['event_id'] for r in core.rows()};a=self.parent_ids();expected=int(self.manifest.get('materialized_matched3p5s_event_count',-1));return {'core':len(c),'a4':len(a),'expected':expected,'missing_a4':sorted(c-a),'unexpected_a4':sorted(a-c),'status':'PASS' if c==a and len(c)==expected else 'FAIL'}
def frozen_budget_memberships(core,budgets,seed):
 from collections import defaultdict
 g=defaultdict(list)
 for r in core.rows(role='calibration'):g[(r['dataset_id'],r['label'])].append(r)
 out={}
 for ds in sorted({x[0] for x in g}):
  for b in budgets:
   ids=[]
   for lab in ('left_hand','right_hand'):
    q=sorted(g[(ds,lab)],key=lambda r:hashlib.sha256(f'{seed}|{ds}|{r["subject_id"]}|{r["session_id"]}|{r["run_id"]}|{r["event_id"]}'.encode()).hexdigest())
    if len(q)<b:raise RuntimeError(f'FROZEN_BUDGET_INSUFFICIENT:{ds}:{lab}:{b}')
    ids += [r['event_id'] for r in q[:b]]
   out[f'{ds}:budget-{b}-seed-{seed}']=set(ids)
 return out
