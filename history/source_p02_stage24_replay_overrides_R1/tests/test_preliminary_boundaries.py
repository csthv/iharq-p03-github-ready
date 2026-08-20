from pathlib import Path
import yaml
ROOT=Path(__file__).parents[1]
def test_preliminary_labels():
 d=yaml.safe_load((ROOT/'manifests/preliminary_closure_boundaries.yaml').read_text());assert d['layer0']=='LAYER_0_TEMPLATE_NOT_DISPOSITION';assert d['handoff']=='BLOCKED_HANDOFF_TEMPLATE'
