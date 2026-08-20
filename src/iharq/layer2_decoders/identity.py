from __future__ import annotations
import hashlib,json
from pathlib import Path

def canonical_json(v): return json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False,default=str)
def semantic_hash(v): return hashlib.sha256(canonical_json(v).encode()).hexdigest()
def sha256_file(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(4*1024*1024),b''): h.update(b)
 return h.hexdigest()
def derive_seed(master,*parts):
 x=int(hashlib.sha256('|'.join(map(str,(master,*parts))).encode()).hexdigest()[:8],16)%(2**31-1)
 return x or 1
