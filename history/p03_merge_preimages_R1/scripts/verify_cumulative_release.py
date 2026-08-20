#!/usr/bin/env python3
from pathlib import Path
import csv, hashlib, json, re, subprocess, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def add(n,c,d=''): checks.append((n,bool(c),d))
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
 return h.hexdigest()
s=json.loads((ROOT/'CURRENT_PROJECT_STATUS.json').read_text())
add('state_ready',s.get('status')=='P00_P01_P02_POST_EXTENSION_MERGED_VALIDATED_READY_FOR_P03_INTAKE',s.get('status'))
add('completed_phases',s.get('completed_phase_scopes')==['P00','P01','P02'])
add('p02_complete',s.get('p02_execution_complete') is True)
add('p03_not_started',s.get('p03_execution_started') is False)
add('no_blockers',s.get('scientific_blockers')==0 and s.get('documentary_blockers')==0 and s.get('major_issues')==0)
add('budget_axis',s.get('p02_low_label_budget_axis')==[1,2,4,8,16,32,64,128,256])
add('canonical_G18_unchanged',s.get('p02_stage18')=='CANONICAL_G18_PASS_UNCHANGED_BY_EXTENSION')
for rel in [
 'docs/phase_00/final_documents/17_IHARQ_Phase_0_to_Phase_1_Authorization_and_Handoff.md',
 'docs/phase_01/analysis/IHARQ_Cumulative_Phase_Evidence_Results_and_Interpretation_Report_Through_P01_Current.md',
 'current/phase_02/kaggle_run_light/runtime/analysis_inputs/low_label_metric_source.csv',
 'current/phase_02/kaggle_run_light/runtime/table_source_data/p02/P02_Table_low_label_BACC.csv',
 'final_state/through_p02/analysis/P02_64_128_256_Extension_Addendum_R1.md',
 'final_state/through_p02/extension_annex/HEAVY_ARTIFACT_POINTERS.jsonl',
 'artifacts/handoffs/phase_02_to_phase_03/P02_64_128_256_EXTENSION_ANNEX_HANDOFF_R1.json',
 'artifacts/handoffs/phase_02_to_phase_03/P02_64_128_256_EXTENSION_ANNEX_LOCATION_INDEX.jsonl',
]: add('exists:'+rel,(ROOT/rel).is_file())
# Science-surface checks
with (ROOT/'current/phase_02/kaggle_run_light/runtime/analysis_inputs/low_label_metric_source.csv').open(newline='') as f: low=list(csv.DictReader(f))
add('low_label_rows',len(low)==324,str(len(low)))
add('low_label_budgets',sorted({int(r['budget_per_class']) for r in low})==[1,2,4,8,16,32,64,128,256])
add('low_label_metrics',sorted({r['metric_id'] for r in low})==['ACC','BACC','F1_MACRO'])
with (ROOT/'current/phase_02/kaggle_run_light/runtime/table_source_data/p02/P02_Table_low_label_BACC.csv').open(newline='') as f: br=list(csv.DictReader(f))
add('bacc_rows',len(br)==108,str(len(br)))
# External pointer composite
ptr=json.loads((ROOT/'external_artifact_pointer_manifest.json').read_text())
add('pointer_status',ptr.get('status')=='PASS')
add('extension_heavy_pointers',ptr.get('extension_annex',{}).get('heavy_pointer_items')==758)
add('heavy_not_duplicated',ptr.get('large_artifacts_are_not_duplicated') is True)
# Preimage preservation
spa=json.loads((ROOT/'artifacts/cumulative_state/p02_post_extension_merge_R3/source_preservation_audit.json').read_text())
add('preimages_preserved',spa.get('all_replaced_preimages_preserved') is True)
add('heavy_bytes_embedded_by_merge',spa.get('heavy_bytes_embedded_by_extension_merge')==0)
add('transient_bytecode_exclusion_record',(ROOT/'artifacts/cumulative_state/p02_post_extension_merge_R3/EXCLUDED_TRANSIENT_SOURCE_FILES.csv').is_file())
# Existing L2 promotion invariant
pm=json.loads((ROOT/'artifacts/cumulative_state/p02_final_merge_R2/root_layer2_promotion_manifest.json').read_text())
bad=[]
for r in pm['files']:
 a=ROOT/r['path']; b=ROOT/r['source_path']
 if not a.is_file() or not b.is_file(): bad.append(r['path']); continue
 if r['path'].endswith('/__init__.py'):
  txt=a.read_text(errors='ignore')
  if 'SCIENTIFIC_EXECUTION=False' not in txt or 'LAYER_ID="L2"' not in txt: bad.append(r['path'])
 elif sha(a)!=sha(b): bad.append(r['path'])
add('l2_promotion_byte_identity_except_declared_init_shim',not bad,str(bad[:5]))
# Final lifecycle historical docs remain present.
for rel in [
 'final_state/through_p02/authorities/protocol_v1/IHARQ_Protocol_v1_0_Final_Through_Phase_02_R1.md',
 'final_state/through_p02/analysis/IHARQ_Cumulative_Phase_Evidence_Results_and_Interpretation_Through_P02_Final_R1.md',
 'final_state/through_p02/layer0/Layer_0_Claim_Governance_Through_P02.md',
 'final_state/through_p02/evidence_map/IHARQ_Cumulative_Evidence_Map_Through_P02.md',
 'final_state/through_p02/layer10/Layer_10_Artifact_Package_Through_P02.md']:
 add('historical_final:'+rel,(ROOT/rel).is_file())
# Root manifest and checksum integrity
m=json.loads((ROOT/'CURRENT_CUMULATIVE_REPOSITORY_MANIFEST.json').read_text())
from concurrent.futures import ThreadPoolExecutor
computed={}; missing=[]; mismatch=[]
def _check_row(row):
 p=ROOT/row['path']
 if not p.is_file(): return row['path'],None,'missing'
 hh=sha(p)
 if p.stat().st_size!=row['bytes'] or hh!=row['sha256']: return row['path'],hh,'mismatch'
 return row['path'],hh,None
with ThreadPoolExecutor(max_workers=16) as ex:
 for rel,hh,err in ex.map(_check_row,m['files'],chunksize=64):
  if err=='missing': missing.append(rel)
  elif err=='mismatch': mismatch.append(rel)
  if hh is not None: computed[rel]=hh
add('manifest_integrity',not missing and not mismatch,f'missing={len(missing)} mismatch={len(mismatch)}')
bad=[]
for line in (ROOT/'REPOSITORY_CHECKSUMS.sha256').read_text().splitlines():
 if not line.strip(): continue
 hh,rel=line.split('  ',1); p=ROOT/rel
 if not p.is_file(): bad.append(rel); continue
 actual=computed.get(rel) or sha(p)
 if actual!=hh: bad.append(rel)
add('repository_checksums',not bad,str(bad[:5]))
# No literal private secrets. Use ripgrep for repository-scale performance.
patterns=[r'\bhf_[A-Za-z0-9_-]{20,}\b',r'\bgithub_pat_[A-Za-z0-9_]{20,}\b',r'\bgh[pousr]_[A-Za-z0-9]{30,}\b',r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----']
hits=[]
for pat in patterns:
 cp=subprocess.run(['rg','--hidden','-l','-P','--',pat,str(ROOT)],capture_output=True,text=True)
 if cp.returncode not in (0,1): hits.append('RG_SCAN_ERROR:'+cp.stderr.strip())
 else: hits.extend([x for x in cp.stdout.splitlines() if x.strip()])
add('secret_scan',not hits,str(hits[:8]))
trans=[str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and ('__pycache__' in p.parts or p.suffix=='.pyc')]
add('no_bytecode',not trans,str(trans[:5]))
passed=sum(c for _,c,_ in checks); failed=[x for x in checks if not x[1]]
print(f'PASS={passed} FAIL={len(failed)} TOTAL={len(checks)}')
for n,_,d in failed: print('FAIL',n,d)
if failed: sys.exit(1)
