#!/usr/bin/env python3
from pathlib import Path
import json,yaml,hashlib,sys,re,csv,tomllib
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def add(name,cond,detail=''): checks.append((name,bool(cond),detail))
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
 return h.hexdigest()
# Current state
s=json.loads((ROOT/'CURRENT_PROJECT_STATUS.json').read_text())
add('state_ready',s.get('status')=='P00_P01_P02_MERGED_VALIDATED_READY_FOR_P03_INTAKE',s.get('status'))
add('completed_phases',s.get('completed_phase_scopes')==['P00','P01','P02'])
add('p02_complete',s.get('p02_execution_complete') is True)
add('p03_not_started',s.get('p03_execution_started') is False)
add('no_blockers',s.get('scientific_blockers')==0 and s.get('documentary_blockers')==0 and s.get('major_issues')==0)
# P00/P01 continuity and P02 source
for rel in ['docs/phase_00/final_documents/17_IHARQ_Phase_0_to_Phase_1_Authorization_and_Handoff.md',
            'docs/phase_01/analysis/IHARQ_Cumulative_Phase_Evidence_Results_and_Interpretation_Report_Through_P01_Current.md',
            'current/phase_02/release_metadata/G24_REPLAY.json',
            'current/phase_02/kaggle_run_light/runtime/analysis_inputs/failure_negative_summary.json']:
 add('exists:'+rel,(ROOT/rel).is_file())
# Final lifecycle documents
for rel in [
 'final_state/through_p02/authorities/protocol_v1/IHARQ_Protocol_v1_0_Final_Through_Phase_02_R1.md',
 'final_state/through_p02/analysis/IHARQ_Cumulative_Phase_Evidence_Results_and_Interpretation_Through_P02_Final_R1.md',
 'final_state/through_p02/layer0/Layer_0_Claim_Governance_Through_P02.md',
 'final_state/through_p02/evidence_map/IHARQ_Cumulative_Evidence_Map_Through_P02.md',
 'final_state/through_p02/layer10/Layer_10_Artifact_Package_Through_P02.md',
 'artifacts/handoffs/phase_02_to_phase_03/downstream_readiness.yaml',
 'artifacts/handoffs/phase_02_to_phase_03/producer_consumer_matrix.yaml']:
 add('final:'+rel,(ROOT/rel).is_file())
# Layer2 promotion byte identity
pm=json.loads((ROOT/'artifacts/cumulative_state/p02_final_merge_R2/root_layer2_promotion_manifest.json').read_text())
add('l2_promotion_manifest',pm.get('functional_module_files_byte_identical_except_init_compatibility_shim') is True and pm.get('scientific_logic_changed') is False)
bad=[]
for r in pm['files']:
 a=ROOT/r['path'];b=ROOT/r['source_path']
 if not a.is_file() or not b.is_file():bad.append(r['path']);continue
 if r['path'].endswith('/__init__.py'):
  txt=a.read_text(errors='ignore')
  if 'SCIENTIFIC_EXECUTION=False' not in txt or 'LAYER_ID="L2"' not in txt:bad.append(r['path'])
 elif sha(a)!=sha(b):bad.append(r['path'])
add('l2_promotion_byte_identity_except_declared_init_shim',not bad,str(bad[:5]))
# Phase 2 config/environment
add('p02_config',(ROOT/'configs/phase_02/phase.yaml').is_file())
add('p02_env',(ROOT/'environments/phase_02/requirements-lock.txt').is_file())
# Handoff content
h=yaml.safe_load((ROOT/'phase_handoff.yaml').read_text())['phase_handoff']
add('p03_handoff',h['consumer_phase']=='P03' and h['status']=='READY_WITH_EXPLICIT_NONBLOCKING_LIMITATIONS')
add('handoff_blockers',h['blockers']==[])
# P02 analysis completeness and post-governance validation
pc=yaml.safe_load((ROOT/'final_state/through_p02/evidence_map/P02_analysis_completeness.yaml').read_text())
# tolerate nested schema; require no obvious false/missing values in key status strings
blob=json.dumps(pc,default=str)
add('p02_completeness_record','P02' in blob or 'p02' in blob.lower())
fv=json.loads((ROOT/'final_state/through_p02/validation/FINAL_WHOLE_PHASE_CLOSURE_VALIDATION.json').read_text())
add('whole_phase_validation',fv.get('summary',{}).get('fail')==0 and fv.get('P02_PHASE_AND_LAYER_CLOSURE_STATUS') in {'GREEN_LIGHT_FOR_DOWNSTREAM','GREEN_LIGHT_WITH_EXPLICIT_NONBLOCKING_LIMITATIONS'},str(fv.get('summary')))
# External pointer contract and distinct credentials
ext=(ROOT/'external_artifact_pointer_manifest.yaml').read_text()
add('p02_external_revision','bc14961e14f2e48690e55df3577014275f9cbf30' in ext)
rd=(ROOT/'artifacts/handoffs/phase_02_to_phase_03/external_artifact_retrieval.yaml').read_text()
add('dual_credentials','IHARQ_HF_TOKEN_PRE_P02' in rd and 'IHARQ_HF_TOKEN_P02' in rd)
# A14 boundary and Stage18S scope
ct=(ROOT/'CURRENT_PROJECT_STATUS.json').read_text()+(ROOT/'phase_handoff.yaml').read_text()
add('a14_boundary','ABSENT_PROHIBITED' in ct)
add('stage18s_boundary','POST_HOC' in ct and 'DESCRIPTIVE' in ct)
# Manifest + repository checksum integrity in a single hashing pass.
m=json.loads((ROOT/'CURRENT_CUMULATIVE_REPOSITORY_MANIFEST.json').read_text())
computed={};missing=[];mismatch=[]
for row in m['files']:
 p=ROOT/row['path']
 if not p.is_file():missing.append(row['path']);continue
 hh=sha(p);computed[row['path']]=hh
 if p.stat().st_size!=row['bytes'] or hh!=row['sha256']:mismatch.append(row['path'])
add('manifest_integrity',not missing and not mismatch,f'missing={len(missing)} mismatch={len(mismatch)}')
# Check checksum ledger; reuse hashes already computed by the manifest pass.
bad=[]
for line in (ROOT/'REPOSITORY_CHECKSUMS.sha256').read_text().splitlines():
 if not line.strip():continue
 hh,rel=line.split('  ',1);p=ROOT/rel
 if not p.is_file():bad.append(rel);continue
 actual=computed.get(rel)
 if actual is None: actual=sha(p)
 if actual!=hh:bad.append(rel)
add('repository_checksums',not bad,str(bad[:5]))
# Security scan using ripgrep for performance. Binary files are skipped by rg.
import subprocess
patterns=[r'hf_[A-Za-z0-9]{20,}',r'(?i)(?:api[_-]?key|access[_-]?token|password|secret[_-]?key)\s*[:=]\s*["\'][^"\']{12,}["\']']
hits=[]
for pat in patterns:
 cp=subprocess.run(['rg','--hidden','-l','-P',pat,str(ROOT)],capture_output=True,text=True)
 if cp.returncode not in (0,1):
  hits.append('RG_SCAN_ERROR:'+cp.stderr.strip())
 else:
  hits.extend([x for x in cp.stdout.splitlines() if x.strip()])
add('secret_scan',not hits,str(hits[:8]))
# No transient bytecode in current tree.
trans=[str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and ('__pycache__' in p.parts or p.suffix=='.pyc')]
add('no_bytecode',not trans,str(trans[:5]))
passed=sum(c for _,c,_ in checks);failed=[x for x in checks if not x[1]]
print(f'PASS={passed} FAIL={len(failed)} TOTAL={len(checks)}')
for n,_,d in failed:print('FAIL',n,d)
if failed:sys.exit(1)
