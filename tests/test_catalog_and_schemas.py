from pathlib import Path
import json,yaml
from jsonschema import Draft202012Validator
ROOT=Path(__file__).parents[1]
def test_all_catalog_records_have_valid_schemas():
    rows=yaml.safe_load((ROOT/'catalogs/record_family_catalog.yaml').read_text())['records']
    assert len(rows)>=55
    for r in rows:
        p=ROOT/'schemas/records'/f"{r['record_type']}.schema.json";assert p.exists(),r['record_type'];Draft202012Validator.check_schema(json.loads(p.read_text()))
def test_catalog_unique():
    rows=yaml.safe_load((ROOT/'catalogs/record_family_catalog.yaml').read_text())['records'];names=[r['record_type'] for r in rows];assert len(names)==len(set(names))
