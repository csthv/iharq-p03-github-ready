from __future__ import annotations
import json,sys
from datetime import datetime,timezone

def event(code:str,message:str,**fields):
    forbidden={k for k in fields if any(x in k.lower() for x in ['secret','token','password','credential'])}
    if forbidden: raise ValueError(f"secret-like log fields forbidden: {sorted(forbidden)}")
    obj={'timestamp':datetime.now(timezone.utc).isoformat(),'code':code,'message':message,**fields}
    print(json.dumps(obj,sort_keys=True),file=sys.stderr)
