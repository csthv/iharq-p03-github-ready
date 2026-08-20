#!/usr/bin/env python3
from pathlib import Path
import json, yaml, hashlib, sys, csv, re, zipfile
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def add(name,cond,detail=''):
    checks.append((name,bool(cond),detail))

def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
# Core current-state files
req=['CURRENT_PROJECT_STATUS.json','CURRENT_CUMULATIVE_REPOSITORY_MANIFEST.json','REPOSITORY_CHECKSUMS.sha256','artifacts/cumulative_state/IHARQ_P00_P01_to_P02_Clean_Input_Handoff_R1.yaml','artifacts/cumulative_state/AuthorityManifest.json','artifacts/cumulative_state/EnvironmentManifest.json','artifacts/cumulative_state/ConfigSnapshot.json','artifacts/cumulative_state/InputManifest.json','docs/phase_00/final_documents/17_IHARQ_Phase_0_to_Phase_1_Authorization_and_Handoff.md','artifacts/phase_closure/IHARQ_Phase_01_Final_Handoff_and_Phase2_Readiness_R1.yaml','contracts/phases/p02/input_contract.yaml']
for r in req:add('exists:'+r,(ROOT/r).is_file())
# Status and P02 contract
s=json.loads((ROOT/'CURRENT_PROJECT_STATUS.json').read_text())
add('merged_status',s['status']=='P00_P01_MERGED_VALIDATED_READY_FOR_P02_ENTRY',s['status'])
add('p02_entry_green_light',s['p02_entry_green_light']=='YES')
add('p02_not_started',s['p02_execution_started'] is False)
h=yaml.safe_load((ROOT/'artifacts/cumulative_state/IHARQ_P00_P01_to_P02_Clean_Input_Handoff_R1.yaml').read_text())['cumulative_handoff']
add('handoff_ready',h['p02_entry_readiness']=='PASS')
add('handoff_no_blockers',h['open_blockers']==[])
add('p01_g15',h['p01_data_contract']['p01_gate_15']=='PASS')
add('window_count',h['p01_data_contract']['WindowRecord']==12910)
add('a14', 'A14 remains ABSENT_PROHIBITED.' in h['consumer_rules'])
# Required P02 input manifest types
ic=yaml.safe_load((ROOT/'contracts/phases/p02/input_contract.yaml').read_text())
for typ in ic['required_manifest_types']:
    mapping={'AuthorityManifest':'artifacts/cumulative_state/AuthorityManifest.json','RepositoryManifest':'CURRENT_CUMULATIVE_REPOSITORY_MANIFEST.json','EnvironmentManifest':'artifacts/cumulative_state/EnvironmentManifest.json','ConfigSnapshot':'artifacts/cumulative_state/ConfigSnapshot.json','InputManifest':'artifacts/cumulative_state/InputManifest.json'}
    add('p02_manifest:'+typ,(ROOT/mapping[typ]).is_file())
# Current authorities: governance + seven docs + README
cur=list((ROOT/'docs/authorities/current').glob('*'))
add('authority_count',len([p for p in cur if p.is_file()])==9,str(len(cur)))
add('governance_v6_1', (ROOT/'docs/authorities/current/00_IHARQ_Document_Stack_Governance_and_Creation_Guide_V6_1.md').is_file())
# P00 and P01 docs
add('p00_18_docs',len(list((ROOT/'docs/phase_00/final_documents').glob('[0-9][0-9]_*.md')))==18)
add('p01_protocol',(ROOT/'docs/phase_01/protocol/IHARQ_Experiment_Ablation_Evaluation_Protocol_v1_0_Current.md').is_file())
add('p01_analysis',(ROOT/'docs/phase_01/analysis/IHARQ_Cumulative_Phase_Evidence_Results_and_Interpretation_Report_Through_P01_Current.md').is_file())
add('p01_evidence_map',(ROOT/'docs/phase_01/evidence_map/IHARQ_Cumulative_Paper_and_Thesis_Evidence_Map_Through_P01_Current.md').is_file())
add('p01_layer10',(ROOT/'docs/phase_01/layer10/IHARQ_Cumulative_Layer10_Through_P01_Current.md').is_file())
# Environments separated
add('p00_env',(ROOT/'environments/phase_00/requirements-lock.txt').is_file())
add('p01_env',(ROOT/'environments/phase_01/requirements-lock.txt').is_file())
# No bytecode/transient in current tree except history none expected
trans=[p for p in ROOT.rglob('*') if p.is_file() and ('__pycache__' in p.parts or p.suffix=='.pyc')]
add('no_bytecode',not trans,str(len(trans)))
# Manifest integrity
m=json.loads((ROOT/'CURRENT_CUMULATIVE_REPOSITORY_MANIFEST.json').read_text())
missing=[]; mismatch=[]
for row in m['files']:
    p=ROOT/row['path']
    if not p.is_file():missing.append(row['path']);continue
    if p.stat().st_size!=row['bytes'] or sha(p)!=row['sha256']:mismatch.append(row['path'])
add('manifest_files',not missing and not mismatch,f'missing={len(missing)} mismatch={len(mismatch)}')
# Checksums file integrity; excludes self.
bad=[]
for line in (ROOT/'REPOSITORY_CHECKSUMS.sha256').read_text().splitlines():
    if not line.strip():continue
    hh,rel=line.split('  ',1);p=ROOT/rel
    if not p.is_file() or sha(p)!=hh:bad.append(rel)
add('repository_checksums',not bad,str(len(bad)))
# No obvious credentials or absolute container paths in current text-like surfaces.
secret_re=re.compile(r'(?i)(bearer\s+[A-Za-z0-9._-]{20,}|(?:kaggle_api_token|oauth[_ -]?token|api[_-]?key|password)\s*["\']?\s*[:=]\s*["\'](?!REDACTED|<|\$\{|None|null)[A-Za-z0-9._/-]{16,}["\'])')
hits=[]; pathhits=[]
for p in ROOT.rglob('*'):
    if not p.is_file() or p.suffix.lower() in {'.npz','.docx','.pdf','.png','.jpg','.jpeg','.zip'}:continue
    if p.stat().st_size>8_000_000:continue
    try:t=p.read_text(errors='ignore')
    except:continue
    if secret_re.search(t):hits.append(str(p.relative_to(ROOT)))
    if '/mnt/data/' in t and p.name!='verify_cumulative_release.py' and 'history' not in p.relative_to(ROOT).parts:pathhits.append(str(p.relative_to(ROOT)))
add('secret_scan',not hits,str(hits[:5]))
add('no_container_paths',not pathhits,str(pathhits[:5]))
# No active positive A14 in current status/readme/handoff.
ct=(ROOT/'README.md').read_text()+"\n"+(ROOT/'CURRENT_PROJECT_STATUS.json').read_text()+"\n"+(ROOT/'artifacts/cumulative_state/IHARQ_P00_P01_to_P02_Clean_Input_Handoff_R1.yaml').read_text()
add('a14_current_boundary','ABSENT_PROHIBITED' in ct and not re.search(r'\bA14\b.{0,50}\bACTIVE\b',ct,re.I|re.S))
# A4 effectiveness boundary
add('a4_boundary','effectiveness' in ct.lower() and s['a4_effectiveness_in_p01'] is False)
passed=sum(c for _,c,_ in checks); failed=[x for x in checks if not x[1]]
print(f'PASS={passed} FAIL={len(failed)} TOTAL={len(checks)}')
for n,_,d in failed:print('FAIL',n,d)
if failed:sys.exit(1)
