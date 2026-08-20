from pathlib import Path
import yaml
ROOT=Path(__file__).parents[1]
def test_a0_a13_readiness_unlocks_and_a14_rejection():
    m=yaml.safe_load((ROOT/'reports/phase_00_final_double_check/phase_0_ablation_readiness_manifest.yaml').read_text())
    rows=m['rows']; assert [r['ablation_id'] for r in rows]==[f'A{i}' for i in range(14)]
    assert all(r['phase0_foundation_state']=='FOUNDATION_READY' for r in rows)
    assert all(r['final_status']=='TECHNICALLY_UNLOCKED_FOR_FUTURE_PROTOCOL' for r in rows)
    assert all(not r['activated_in_p00'] and not r['executed_in_p00'] and r['remaining_activation_conditions'] for r in rows)
    assert m['a14_rejection']['final_status']=='REJECTED'
