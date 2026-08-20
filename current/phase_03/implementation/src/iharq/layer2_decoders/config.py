from __future__ import annotations
from pathlib import Path
import yaml
from .identity import semantic_hash

def load_yaml(p):
 d=yaml.safe_load(Path(p).read_text());
 if not isinstance(d,dict): raise ValueError(f'YAML_OBJECT_REQUIRED:{p}')
 return d
def load_config(root):
 r=Path(root); names=['phase','data','split_visibility','budgets','seeds','metrics','resources','outputs','gates','inputs']
 d={n:load_yaml(r/f'{n}.yaml') for n in names};d['models']=load_yaml(r/'models/portfolio.yaml');d['training_policy']=load_yaml(r/'training_policy_authority_bindings.yaml');d['implementation_bindings']=load_yaml(r/'models/implementation_bindings.yaml');d['implementation_parameters']=load_yaml(r/'models/implementation_parameters.yaml');d['a4_selection']=load_yaml(r/'controls/a4_representative_selection.yaml')
 ph=d['phase']; required={'phase_id':'P02','layer_id':'L2','build_book_id':'IHARQ-P02-L2-INTEGRATED-BUILD-BOOK-R4','notebook_id':'IHARQ-P02-COMPLETE-EXECUTION-AND-ANALYSIS-R4','scientific_freeze_id':'P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R5','one_notebook':True,'a14':'ABSENT_PROHIBITED'}
 for k,v in required.items():
  if ph.get(k)!=v: raise ValueError(f'P02_CONFIG_FREEZE_MISMATCH:{k}:{ph.get(k)}')
 return d,semantic_hash(d)
