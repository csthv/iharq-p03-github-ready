from pathlib import Path
import yaml
ROOT=Path(__file__).parents[1]
def test_historical_preliminary_and_current_closure_boundaries():
 hist=yaml.safe_load((ROOT/'history/phase_00/github_ready_R2/manifests/preliminary_closure_boundaries.yaml').read_text())
 assert hist['layer0']=='LAYER_0_TEMPLATE_NOT_DISPOSITION'
 assert hist['handoff']=='BLOCKED_HANDOFF_TEMPLATE'
 cur=yaml.safe_load((ROOT/'manifests/current_closure_boundaries.yaml').read_text())
 assert cur['layer0']=='FINALIZED_CUMULATIVE_THROUGH_P02'
 assert cur['handoff']=='P02_TO_P03_READY_WITH_EXPLICIT_NONBLOCKING_LIMITATIONS'
 assert cur['p03_execution']=='NOT_STARTED'
