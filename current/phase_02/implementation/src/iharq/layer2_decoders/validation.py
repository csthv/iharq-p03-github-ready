from pathlib import Path
import yaml,json

def planned_cells(p):
 d=yaml.safe_load(Path(p).read_text());r=d['rows'];ids=[x['planned_run_cell_id'] for x in r];a0=sum(x['ablation_id']=='A0' for x in r);a4=sum(x['ablation_id']=='A4' for x in r);exp_total=int(d['cell_count']);exp_a0=int(d['a0_cell_count']);exp_a4=int(d['a4_cell_count']);return {'status':'PASS' if len(r)==exp_total and len(ids)==len(set(ids)) and a0==exp_a0 and a4==exp_a4 else 'FAIL','total':len(r),'A0':a0,'A4':a4,'unique':len(set(ids)),'expected':{'total':exp_total,'A0':exp_a0,'A4':exp_a4}}
def stage_plan(p):
 d=yaml.safe_load(Path(p).read_text());s=d['stages'];return {'status':'PASS' if len(s)==26 and len({str(x['stage']) for x in s})==26 else 'FAIL','count':len(s)}
