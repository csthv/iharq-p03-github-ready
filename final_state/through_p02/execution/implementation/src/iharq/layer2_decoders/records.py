from __future__ import annotations
import json,datetime
from pathlib import Path
from .identity import semantic_hash

def load_schemas(p):return __import__('yaml').safe_load(Path(p).read_text())['records']
def make_record(family,payload,schema,config_sha,source_ids):
 base={'schema_id':schema['schema_id'],'record_version':'1','producer':'IHARQ_P02_L2','owner':'L2','phase_id':'P02','layer_id':'L2','config_sha256':config_sha,'source_ids':list(source_ids),'evidence_class':'P02_EXECUTION_EVIDENCE','limitations':[],'lifecycle_status':'CURRENT','terminal_status':'SUCCESS','created_at_utc':datetime.datetime.now(datetime.UTC).isoformat()}
 d={**base,**payload};d['record_id']=f'{family}:{semantic_hash({"family":family,"payload":payload,"sources":source_ids})[:24]}';d['payload_sha256']=semantic_hash(payload)
 required=schema['required_fields'];missing=[x for x in required if x not in d]
 if missing:raise ValueError(f'{family}_MISSING_REQUIRED:{missing}')
 if not schema.get('additional_properties',True):
  extra=sorted(set(d)-set(required))
  if extra:raise ValueError(f'{family}_UNKNOWN_FIELDS:{extra}')
 return d
