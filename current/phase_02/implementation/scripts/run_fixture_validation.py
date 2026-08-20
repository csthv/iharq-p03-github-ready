#!/usr/bin/env python3
from pathlib import Path
import json, tempfile, zipfile, shutil, sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from iharq.layer2_decoders.kaggle_entry import authoring_fixture_simulation
from iharq.layer2_decoders.bundle import verify

def main():
    tmp=Path(tempfile.mkdtemp(prefix='p02_fixture_'))
    try:
        r=authoring_fixture_simulation(ROOT,tmp)
        assert r['status']=='PASS' and len(r['stages'])==26 and all(x['status']=='SUCCESS' for x in r['stages'])
        s15=json.loads((tmp/'stage_ledger/stage_15.json').read_text())['outputs']
        s18=json.loads((tmp/'stage_ledger/stage_18.json').read_text())['outputs']
        s18u=json.loads((tmp/'stage_ledger/stage_18U.json').read_text())['outputs']
        assert s15['stage15_a0_closure']=='COMPLETE' and s15['required_closure_outputs_missing']==0
        assert s15['training_policy_challenger_closure']['status']=='PASS'
        assert s15['training_policy_challenger_closure']['planned_cells']>=1
        assert s15['training_policy_challenger_closure']['terminal_cells']==s15['training_policy_challenger_closure']['planned_cells']
        assert s18['closure']['role_control_incomplete']==0 and s18['closure']['c4_c5_incomplete']==0
        assert s18['c4_vs_strongest']=='COMPLETE' and s18['c5_vs_strongest']=='COMPLETE'
        assert s18u['decision']=='NO_ADDITIONAL_FULL_EXECUTION_ABLATION_UNLOCKED'
        for sid in ['19','20','21','22','23','24']:
            assert json.loads((tmp/f'stage_ledger/stage_{sid}.json').read_text())['status']=='SUCCESS'
        for rel in ['analysis_inputs/a0_closure_source_manifest.json','analysis_inputs/a4_role_control_statistics.json','analysis_inputs/a4_c4_c5_statistics.json','analysis_inputs/a4_c4_c5_comparison_artifacts.jsonl','figure_source_data/a4_c4_c5_statistics.json','figure_source_data/a4_c4_c5_comparison_artifacts.jsonl','table_source_data/a4_c4_c5_statistics.json','table_source_data/a4_c4_c5_comparison_artifacts.jsonl','handoffs/runtime_evidence_index.json','manifests/config_snapshot.yaml','manifests/scientific_freeze_snapshot.yaml','manifests/input_and_run_cell_manifest.json','analysis_inputs/training_policy_challenger_completion.json','analysis_inputs/training_policy_challenger_terminal_states.jsonl','analysis_inputs/training_policy_sr_probability_selection.json','analysis_inputs/training_policy_sr_probability_calibration_candidates.jsonl','protocol_change_required/P02_PREEXECUTION_TRAINING_POLICY_AMENDMENT_R2.yaml','protocol_change_required/P02_FUTURE_PROTOCOL_BUILD_BOOK_SYNC_NOTE_R2.md']:
            assert (tmp/'runtime'/rel).is_file(),rel
        cv=verify(tmp/'runtime'); assert cv['status']=='PASS'
        zp=Path(r['finalization']['zip']['path'])
        with zipfile.ZipFile(zp) as z:
            assert z.testzip() is None
            assert all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist())
        assert len(list((tmp/'runtime/gate_results').glob('*.json')))==26
        assert len(list((tmp/'runtime/logs').glob('stage_*.log')))>=26
        fixture_copy=ROOT/'validation/FIXTURE_NON_SCIENTIFIC_RUNTIME_BUNDLE.zip'
        shutil.copy2(zp,fixture_copy)
        rep={'status':'PASS','label':'FIXTURE_NON_SCIENTIFIC_NOT_P02_EVIDENCE','scientific_evidence':False,'stages':26,'stage15_a0_closure':'PASS','stage15_training_policy_closure':'PASS','future_protocol_sync_artifacts':'PASS','stage18_a4_execution':'PASS','c1_c2_c3_vs_c0_closure':'PASS','c4_c5_vs_strongest_closure':'PASS','stage18u':'PASS','late_stage_chain':'PASS','runtime_checksums':cv,'runtime_zip':{k:v for k,v in r['finalization']['zip'].items() if k!='path'},'fixture_bundle_path':'validation/FIXTURE_NON_SCIENTIFIC_RUNTIME_BUNDLE.zip'}
        (ROOT/'validation/full_stage_graph_synthetic_integration.json').write_text(json.dumps(rep,indent=2)+'\n')
        print(json.dumps(rep,indent=2))
    finally:
        shutil.rmtree(tmp,ignore_errors=True)
if __name__=='__main__':main()
