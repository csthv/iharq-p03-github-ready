#!/usr/bin/env python3
from pathlib import Path
import csv, hashlib, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def add(name, ok, detail=''): checks.append((name,bool(ok),detail))
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''): h.update(b)
 return h.hexdigest()
status=json.loads((ROOT/'CURRENT_PROJECT_STATUS.json').read_text())
add('state_ready',status.get('status')=='P00_P01_P02_P03_POST_EXTENSION_MERGED_VALIDATED_READY_FOR_P04_INTAKE',status.get('status'))
add('completed_phases',status.get('completed_phase_scopes')==['P00','P01','P02','P03'])
add('p03_complete',status.get('p03_execution_complete') is True)
add('no_blockers',status.get('scientific_blockers')==0 and status.get('documentary_blockers')==0 and status.get('major_issues')==0)
ps=json.loads((ROOT/'current/phase_03/CURRENT_PHASE_STATUS.json').read_text())
add('p03_claim_boundary',ps.get('candidate_claims_approved') is False and ps.get('claim_approval_performed') is False)
add('p03_selection_boundary',ps.get('test_used_for_selection') is False and ps.get('threshold_reselection') is False and ps.get('threshold_retuning') is False)
for rel in [
 'final_state/through_p02/analysis/P02_64_128_256_Extension_Addendum_R1.md',
 'current/phase_03/implementation/configs/phases/p03.yaml',
 'current/phase_03/post_extension_64_128_256/execution_context.json',
 'current/phase_03/release_metadata/EXTERNAL_ARTIFACT_POINTERS.jsonl',
 'artifacts/handoffs/phase_03_to_phase_04/p03_handoff_manifest.json',
 'final_state/through_p03/p03_final_export_bundle.json',
 'src/iharq/layer3_calibration_uncertainty/stages.py']:
 add('exists:'+rel,(ROOT/rel).is_file())
# Exhaustive P03 mapped-source integrity.
rows=list(csv.DictReader((ROOT/'artifacts/cumulative_state/p03_post_extension_merge_R1/SOURCE_TO_CUMULATIVE_PATH_MAP.csv').open(newline='')))
bad=[]
for r in rows:
 p=ROOT/r['destination_path']
 if not p.is_file() or p.stat().st_size!=int(r['bytes']) or sha(p)!=r['sha256']: bad.append(r['source_path'])
add('all_3447_p03_source_files_preserved',len(rows)==3447 and not bad,f'rows={len(rows)} bad={len(bad)}')
# Root promotion identity.
prom=list(csv.DictReader((ROOT/'artifacts/cumulative_state/p03_post_extension_merge_R1/ROOT_IMPLEMENTATION_PROMOTION.csv').open(newline='')))
bad=[]
for r in prom:
 a=ROOT/r['path']; b=ROOT/r['source_path']
 if not a.is_file() or not b.is_file(): bad.append(r['path']); continue
 if r['status']=='PROMOTED_WITH_CUMULATIVE_NONEXECUTION_COMPATIBILITY_SHIM':
  txt=a.read_text(errors='ignore')
  if 'SCIENTIFIC_EXECUTION = False' not in txt or 'LAYER_ID' not in txt: bad.append(r['path'])
 elif r['status']=='CUMULATIVE_METADATA_REFRESH_P03':
  txt=a.read_text(errors='ignore')
  if 'version = "0.3.0"' not in txt or 'PHASE_03_SCOPE_FINALIZED_READY_FOR_P04_INTAKE' not in txt: bad.append(r['path'])
 elif sha(a)!=sha(b): bad.append(r['path'])
add('root_l3_promotion_identity_except_declared_init_shim',not bad,str(bad[:5]))
# Preservation audit is the exhaustive baseline audit created during merge.
a=json.loads((ROOT/'artifacts/cumulative_state/p03_post_extension_merge_R1/source_preservation_audit.json').read_text())
add('baseline_and_p03_preservation_audit',a.get('status')=='PASS' and a.get('baseline_unpreserved_files')==0 and a.get('p03_unpreserved_files')==0)
# Canonical vs extension same-name science surfaces are distinct.
ca=ROOT/'artifacts/phase_analysis_handoff/phase_03/metrics/metric_analysis_input.json'
ex=ROOT/'current/phase_03/post_extension_64_128_256/artifacts/phase_analysis_handoff/phase_03/metrics/metric_analysis_input.json'
add('canonical_extension_scope_separation',ca.is_file() and ex.is_file() and sha(ca)!=sha(ex))
# Manifest / checksum structural consistency and exact path coverage.
m=json.loads((ROOT/'CURRENT_CUMULATIVE_REPOSITORY_MANIFEST.json').read_text())
manifest={r['path']:(r['sha256'],r['bytes']) for r in m['files']}
actual={p.relative_to(ROOT).as_posix():p for p in ROOT.rglob('*') if p.is_file()}
expected_paths=set(actual)-{'CURRENT_CUMULATIVE_REPOSITORY_MANIFEST.json','REPOSITORY_CHECKSUMS.sha256'}
add('manifest_path_coverage',set(manifest)==expected_paths,f'manifest={len(manifest)} expected={len(expected_paths)}')
badsize=[rel for rel,(h,n) in manifest.items() if not (ROOT/rel).is_file() or (ROOT/rel).stat().st_size!=n]
add('manifest_size_integrity',not badsize,str(badsize[:5]))
ledger={}
for line in (ROOT/'REPOSITORY_CHECKSUMS.sha256').read_text().splitlines():
 if line.strip():
  h,rel=line.split('  ',1);ledger[rel]=h
expected_ledger=set(actual)-{'REPOSITORY_CHECKSUMS.sha256'}
add('checksum_path_coverage',set(ledger)==expected_ledger,f'ledger={len(ledger)} expected={len(expected_ledger)}')
mismatch=[rel for rel,(h,n) in manifest.items() if ledger.get(rel)!=h]
add('manifest_checksum_agreement',not mismatch,str(mismatch[:5]))
# Critical generated/control files are rehashed independently against ledger.
critical=['README.md','CURRENT_PROJECT_STATUS.json','project_state_manifest.yaml','phase_handoff.yaml','current_document_index.md','current_artifact_index.csv','external_artifact_pointer_manifest.json','external_artifact_pointer_manifest.yaml','artifacts/cumulative_state/p03_post_extension_merge_R1/final_merge_validation.json','artifacts/cumulative_state/p03_post_extension_merge_R1/source_preservation_audit.json','CURRENT_CUMULATIVE_REPOSITORY_MANIFEST.json']
badcrit=[rel for rel in critical if ledger.get(rel)!=sha(ROOT/rel)]
add('critical_control_hashes',not badcrit,str(badcrit[:5]))
# No transient bytecode and no obvious private secret token patterns.
trans=[str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and ('__pycache__' in p.parts or p.suffix=='.pyc')]
add('no_bytecode',not trans,str(trans[:5]))
patterns=[r'\bhf_[A-Za-z0-9_-]{20,}\b',r'\bgithub_pat_[A-Za-z0-9_]{20,}\b',r'\bgh[pousr]_[A-Za-z0-9]{30,}\b',r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----']
hits=[]
for pat in patterns:
 cp=subprocess.run(['rg','--hidden','-l','-P','--',pat,str(ROOT)],capture_output=True,text=True)
 if cp.returncode not in (0,1): hits.append('RG_SCAN_ERROR:'+cp.stderr.strip())
 else: hits.extend(x for x in cp.stdout.splitlines() if x.strip())
add('secret_scan',not hits,str(hits[:8]))
failed=[x for x in checks if not x[1]]
print(f'PASS={len(checks)-len(failed)} FAIL={len(failed)} TOTAL={len(checks)}')
for n,_,d in failed:print('FAIL',n,d)
if failed:sys.exit(1)
