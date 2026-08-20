from __future__ import annotations
from pathlib import Path
from importlib import metadata
from packaging.utils import canonicalize_name
import argparse,json
ROOT=Path(__file__).parents[1]

def read_lock(path:Path)->dict[str,str]:
    out={}
    for raw in path.read_text(encoding='utf-8').splitlines():
        line=raw.strip()
        if not line or line.startswith('#'): continue
        if '==' not in line: raise ValueError(f'non-exact requirement: {line}')
        n,v=line.split('==',1);out[canonicalize_name(n)] = v
    return out

def verify(path:Path)->dict:
    expected=read_lock(path); observed={};missing=[];mismatched=[]
    for name,version in expected.items():
        try: actual=metadata.version(name)
        except metadata.PackageNotFoundError: missing.append(name);continue
        observed[name]=actual
        if actual!=version:mismatched.append({'name':name,'expected':version,'observed':actual})
    return {'lock':str(path),'expected_count':len(expected),'observed_count':len(observed),'missing':missing,'mismatched':mismatched,'status':'PASS' if not missing and not mismatched else 'FAIL'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--lock',default='requirements-lock.txt');ap.add_argument('--json-out');args=ap.parse_args()
    result=verify(ROOT/args.lock)
    if args.json_out: Path(args.json_out).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2));raise SystemExit(0 if result['status']=='PASS' else 1)
