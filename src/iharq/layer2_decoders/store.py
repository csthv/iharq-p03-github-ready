from __future__ import annotations
from pathlib import Path
import json
from .writers import atomic_json,atomic_jsonl

class Store:
 def __init__(self,root,config_sha256=None):
  self.root=Path(root);self.root.mkdir(parents=True,exist_ok=True);self.config_sha256=config_sha256
  for d in ['records','metrics','checkpoints','run_cells','failures','raw_outputs','analysis_inputs','figure_source_data','table_source_data','manifests','gate_results','handoffs','diagnostics']:(self.root/d).mkdir(parents=True,exist_ok=True)
 def terminal_path(self,c):return self.root/'run_cells'/f"{c['planned_run_cell_id']}.json"
 def terminal(self,c):
  p=self.terminal_path(c)
  if not p.exists():return None
  d=json.loads(p.read_text())
  if self.config_sha256 and d.get('config_sha256')!=self.config_sha256:return None
  return d
 def write_terminal(self,c,status,**kw):
  payload={'run_cell_id':c['planned_run_cell_id'],'ablation_id':c['ablation_id'],'terminal_status':status,**kw}
  if self.config_sha256:payload['config_sha256']=self.config_sha256
  atomic_json(self.terminal_path(c),payload);return self.terminal(c)
 def partition(self,fam,c):return self.root/'records'/fam/f"dataset={c.get('dataset_id','NA')}"/f"branch={c.get('branch_slot','NA')}"/f"budget={c.get('budget_id','NA')}"/f"{c['planned_run_cell_id']}.jsonl"
 def write_records(self,fam,c,rows):
  rows=list(rows);p=self.partition(fam,c);ids=[r.get('record_id') for r in rows]
  if any(x is None for x in ids) or len(ids)!=len(set(ids)):raise ValueError(f'RECORD_PARTITION_IDENTITY_INVALID:{fam}:{c["planned_run_cell_id"]}')
  atomic_jsonl(p,rows);mp=self.root/'manifests'/'record_partitions'/fam/f"{c['planned_run_cell_id']}.json";fields=sorted(set().union(*(set(r) for r in rows))) if rows else []
  atomic_json(mp,{'record_family':fam,'run_cell_id':c['planned_run_cell_id'],'row_count':len(rows),'record_ids_sha256':__import__('hashlib').sha256('\n'.join(ids).encode()).hexdigest(),'fields':fields,'config_sha256':self.config_sha256,'partition_path':str(p.relative_to(self.root))});return p
 def metric(self,c,payload):p=self.root/'metrics'/f"{c['planned_run_cell_id']}.json";atomic_json(p,{'config_sha256':self.config_sha256,**payload} if self.config_sha256 else payload);return p
 def failure(self,c,payload):p=self.root/'failures'/f"{c['planned_run_cell_id']}.json";atomic_json(p,{'config_sha256':self.config_sha256,**payload} if self.config_sha256 else payload);return p
