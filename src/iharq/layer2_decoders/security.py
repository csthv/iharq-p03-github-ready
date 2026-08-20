from __future__ import annotations
from pathlib import Path
import re,zipfile,os
TOK=[re.compile(r'\bKGAT_[A-Za-z0-9_-]{20,}\b'),re.compile(r'\bhf_[A-Za-z0-9_-]{20,}\b'),re.compile(r'(?i)bearer\s+[A-Za-z0-9._~+/=-]{20,}')]
ASSIGN=re.compile(r'''(?ix)\b(?:kaggle_api_token|api[_-]?key|access[_-]?token|refresh[_-]?token|oauth[_-]?token|password|secret)\b\s*[:=]\s*["']?([A-Za-z0-9._~+/=-]{16,})''')
TEXT={'.py','.md','.json','.jsonl','.yaml','.yml','.csv','.txt','.toml','.ipynb','.sha256'}
def scan_text(t):
 hits=[f'PATTERN_{i}' for i,r in enumerate(TOK) if r.search(t)]
 for m in ASSIGN.finditer(t):
  v=m.group(1)
  if v.upper() not in {'REDACTED','NOT_SET','PLACEHOLDER','NONE'}:hits.append('CREDENTIAL_ASSIGNMENT')
 return sorted(set(hits))
def scan_tree(root,live=()):
 hits=[];root=Path(root)
 for p in root.rglob('*'):
  if not p.is_file() or p.suffix.lower() not in TEXT or p.stat().st_size>20_000_000:continue
  t=p.read_text(errors='ignore');
  for h in scan_text(t):hits.append({'path':p.relative_to(root).as_posix(),'kind':h})
  for s in live:
   if s and s in t:hits.append({'path':p.relative_to(root).as_posix(),'kind':'LIVE_SECRET_EXACT'})
 return {'status':'PASS' if not hits else 'FAIL','hits':hits}
def scan_zip(path,live=()):
 hits=[]
 with zipfile.ZipFile(path) as z:
  for n in z.namelist():
   b=z.read(n);t=b.decode(errors='ignore') if Path(n).suffix.lower() in TEXT else ''
   for h in scan_text(t):hits.append({'member':n,'kind':h})
   for s in live:
    if s and s.encode() in b:hits.append({'member':n,'kind':'LIVE_SECRET_EXACT'})
 return {'status':'PASS' if not hits else 'FAIL','hits':hits}
def credential_summary():
 names=[k for k in os.environ if re.search(r'(?i)(token|secret|password|api[_-]?key|oauth)',k)];return {'credential_required':bool(names),'credential_available':bool(names),'credential_source_type':'ENVIRONMENT_SECRET_PROVIDER' if names else 'NONE'}
