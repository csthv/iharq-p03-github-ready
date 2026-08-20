from pathlib import Path
import yaml
ROOT=Path(__file__).parents[1]
def test_responsibility_and_expected_output_closure():
    r=yaml.safe_load((ROOT/'reports/phase_00_final_double_check/phase_0_responsibility_closure_matrix.yaml').read_text())['rows']
    o=yaml.safe_load((ROOT/'reports/phase_00_final_double_check/phase_0_expected_output_and_artifact_closure.yaml').read_text())['rows']
    assert len(r)==20 and sum(x['status']!='PASS' for x in r)==1
    assert len(o)==51 and not any(x['closure_status'] in {'MISSING','PARTIAL','INVALID','STALE_OR_SUPERSEDED'} for x in o)
