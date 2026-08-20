from __future__ import annotations
from pathlib import Path
import yaml

def load_record_catalog(root:str|Path="catalogs/record_family_catalog.yaml"):
    return yaml.safe_load(Path(root).read_text(encoding="utf-8"))["records"]
def by_type(root:str|Path="catalogs/record_family_catalog.yaml"):
    return {x["record_type"]:x for x in load_record_catalog(root)}
