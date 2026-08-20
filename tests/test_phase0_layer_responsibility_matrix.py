from pathlib import Path
import yaml
ROOT=Path(__file__).parents[1]
def test_all_layers_have_phase0_foundation_dispositions():
    rows=yaml.safe_load((ROOT/'reports/phase_00_final_double_check/phase_0_layer_responsibility_matrix.yaml').read_text())['rows']
    assert {r['layer_id'] for r in rows}=={f'L{i}' for i in range(11)}
    assert all(r['status']=='PASS' and r['scientific_execution'] is False for r in rows)
