from pathlib import Path
from iharq.validation import load_bundle,validate_bundle
ROOT=Path(__file__).parents[1]
def test_valid_and_integrated_bundles():
    paths=list((ROOT/'fixtures/valid').glob('*.json'))+list((ROOT/'fixtures/integrated').glob('*.json'))
    assert len(paths)>=5
    for p in paths: assert validate_bundle(load_bundle(p),ROOT)==[],(p,validate_bundle(load_bundle(p),ROOT))
