from pathlib import Path
from .writers import atomic_yaml,atomic_json
def generate(root,context,evidence):
 r=Path(root);r.mkdir(parents=True,exist_ok=True);common={'phase_id':'P02','run_id':context['run_id'],'config_sha256':context['config_sha256'],'scientific_freeze_id':'P02-PLANNED-SCIENTIFIC-EXECUTION-FREEZE-R5','evidence_status':context['evidence_status']};payloads={
 'protocol_v1_handoff':{**common,'actual_execution_values':'POPULATED_AT_RUNTIME','evidence':evidence},
 'phase_analysis_handoff':{**common,'scientific_recompute_required':False,'evidence':evidence},
 'layer0_handoff':{**common,'claim_approval_performed':False,'evidence':evidence},
 'evidence_map_handoff':{**common,'stable_identity_required':True,'evidence':evidence},
 'layer10_source_handoff':{**common,'read_only':True,'scientific_recompute_required':False,'evidence':evidence},
 'p03_handoff':{**common,'raw_prediction_substrate_required':True,'evidence':evidence},}
 out={}
 for k,v in payloads.items():p=r/f'{k}.yaml';atomic_yaml(p,v);out[k]=p.name
 atomic_json(r/'runtime_evidence_index.json',{'status':'PASS','evidence':evidence,'manual_reconstruction_required':False});return out
