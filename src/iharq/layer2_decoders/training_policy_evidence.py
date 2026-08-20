from __future__ import annotations
from pathlib import Path
import json,csv
import numpy as np
from .metrics import evaluate
from .statistics import wilcoxon_paired,paired_bootstrap
from .writers import atomic_json,atomic_jsonl

def _jl(p): return [json.loads(x) for x in Path(p).read_text().splitlines() if x.strip()]
def close_training_policy_challenger(core,store,cells,primary_lookup,freeze,expected=None):
    rows=[]; participant_rows=[]; incomplete=[]; terminal_rows=[]
    for c in cells:
        t=store.terminal(c); primary=primary_lookup(c)
        if not t:
            incomplete.append(c['planned_run_cell_id']); continue
        terminal_rows.append({'run_cell_id':c['planned_run_cell_id'],'terminal_status':t.get('terminal_status'),'reason':t.get('reason'),'comparison_reference':c.get('comparison_reference'),'primary_terminal_status':None if not primary else primary.get('terminal_status')})
        if t.get('terminal_status')!='SUCCESS' or not primary or primary.get('terminal_status')!='SUCCESS':
            # Diagnostic challenger closure is terminal-state complete, not success-only.
            # A matched primary failure/skip is preserved as negative evidence and does not mutate the primary/A0 floor.
            continue
        cm=json.loads((store.root/t['metric_source']).read_text()); pm=json.loads((store.root/primary['metric_source']).read_text())
        r={'challenger_run_cell_id':c['planned_run_cell_id'],'primary_run_cell_id':c['comparison_reference'],'dataset_id':c['dataset_id'],'model_repeat_index':c['model_repeat_index'],'model_seed':c['seed_id'],'condition_id':c['condition_id'],'primary_metrics':pm['metrics'],'challenger_metrics':cm['metrics'],'delta_BACC':float(cm['metrics']['BACC']-pm['metrics']['BACC']),'delta_F1_MACRO':float(cm['metrics']['F1_MACRO']-pm['metrics']['F1_MACRO']),'delta_ACC':float(cm['metrics']['ACC']-pm['metrics']['ACC']),'diagnostic_only':True}
        rows.append(r)
        cp={x['source_event_id']:x for x in _jl(store.root/t['prediction_partition'])}; pp={x['source_event_id']:x for x in _jl(store.root/primary['prediction_partition'])}; truth={x['event_id']:x for x in core.rows(dataset_id=c['dataset_id'],role='test')}; common=sorted(set(cp)&set(pp)&set(truth))
        subjects=sorted({truth[e]['subject_id'] for e in common})
        for sub in subjects:
            ev=[e for e in common if truth[e]['subject_id']==sub]
            y=[int(truth[e]['label']=='right_hand') for e in ev]; pc=[cp[e]['y_pred'] for e in ev]; p0=[pp[e]['y_pred'] for e in ev]
            if len(set(y))<2: continue
            mc=evaluate(y,pc,None,None); m0=evaluate(y,p0,None,None)
            participant_rows.append({'challenger_run_cell_id':c['planned_run_cell_id'],'primary_run_cell_id':c['comparison_reference'],'dataset_id':c['dataset_id'],'model_repeat_index':c['model_repeat_index'],'subject_id':sub,'matched_events':len(ev),'primary_BACC':m0['BACC'],'challenger_BACC':mc['BACC'],'delta_BACC':mc['BACC']-m0['BACC']})
    if expected is not None and len(cells)!=int(expected): raise RuntimeError(f'TRAINING_POLICY_CHALLENGER_CELL_COUNT_MISMATCH:{len(cells)}:{expected}')
    stats={}
    for ds in sorted({r['dataset_id'] for r in participant_rows}):
        q=[r for r in participant_rows if r['dataset_id']==ds]; a=[r['challenger_BACC'] for r in q]; b=[r['primary_BACC'] for r in q]; dif=[r['delta_BACC'] for r in q]
        stats[ds]={'participant_rows':len(q),'wilcoxon':wilcoxon_paired(a,b,5),'bootstrap_delta_BACC':paired_bootstrap(dif,20260804,10000,.95) if dif else {'status':'DESCRIPTIVE_ONLY','n':0}}
    root=store.root/'analysis_inputs'; root.mkdir(parents=True,exist_ok=True)
    atomic_jsonl(root/'training_policy_challenger_seed_comparisons.jsonl',rows); atomic_jsonl(root/'training_policy_challenger_participant_comparisons.jsonl',participant_rows); atomic_jsonl(root/'training_policy_challenger_terminal_states.jsonl',terminal_rows); atomic_json(root/'training_policy_challenger_statistics.json',stats)
    summary={'status':'PASS' if not incomplete else 'INCOMPLETE','planned_cells':len(cells),'terminal_cells':len(terminal_rows),'successful_comparisons':len(rows),'non_success_terminal_cells':sum(x['terminal_status']!='SUCCESS' for x in terminal_rows),'incomplete_cells':incomplete,'diagnostic_only':True,'condition_id':(cells[0]['condition_id'] if cells else 'P02-TRAIN-AUG-SR-EEGNET-FULL-R2-VALIDATION-RESOLVED'),'not_an_A_number':True,'does_not_replace_primary_A0':True,'does_not_enter_A4_selection':True,'analysis_sources':['analysis_inputs/training_policy_challenger_terminal_states.jsonl','analysis_inputs/training_policy_challenger_seed_comparisons.jsonl','analysis_inputs/training_policy_challenger_participant_comparisons.jsonl','analysis_inputs/training_policy_challenger_statistics.json','analysis_inputs/training_policy_sr_probability_selection.json','analysis_inputs/training_policy_sr_probability_calibration_candidates.jsonl']}
    atomic_json(root/'training_policy_challenger_completion.json',summary); return summary
