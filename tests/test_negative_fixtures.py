from pathlib import Path
from iharq.validation import load_bundle,validate_bundle
ROOT=Path(__file__).parents[1]
def test_every_negative_fixture_fails():
    paths=list((ROOT/'fixtures/invalid').glob('*.json'));assert len(paths)>=30
    for p in paths: assert validate_bundle(load_bundle(p),ROOT),p
