from __future__ import annotations
from pathlib import Path
import os,tempfile,json,yaml,csv,io

def _atomic(p,b):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);fd,tmp=tempfile.mkstemp(prefix=p.name+'.',suffix='.tmp',dir=p.parent)
 try:
  with os.fdopen(fd,'wb') as f:f.write(b);f.flush();os.fsync(f.fileno())
  os.replace(tmp,p)
 finally:
  if os.path.exists(tmp):os.unlink(tmp)
def atomic_json(p,v):_atomic(p,(json.dumps(v,indent=2,ensure_ascii=False,default=str)+'\n').encode())
def atomic_yaml(p,v):_atomic(p,yaml.safe_dump(v,sort_keys=False,allow_unicode=True).encode())
def atomic_text(p,v):_atomic(p,str(v).encode())
def atomic_bytes(p,v):_atomic(p,bytes(v))
def atomic_jsonl(p,rows):_atomic(p,''.join(json.dumps(r,sort_keys=True,ensure_ascii=False,default=str,separators=(',',':'))+'\n' for r in rows).encode())
def atomic_csv(p,rows,fieldnames=None):
 rows=list(rows); fns=fieldnames or (list(rows[0]) if rows else []);s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fns);w.writeheader();w.writerows(rows);_atomic(p,s.getvalue().encode())
atomic_write_json=atomic_json;atomic_write_yaml=atomic_yaml;atomic_write_text=atomic_text
