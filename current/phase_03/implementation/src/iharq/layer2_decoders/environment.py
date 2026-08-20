import importlib.metadata as md,platform
from pathlib import Path

def verify(requirements,strict=False):
    rows=[];bad=[]
    for l in Path(requirements).read_text().splitlines():
        if '==' not in l:continue
        k,v=l.split('==',1);k=k.strip();v=v.strip()
        try:a=md.version(k);probe='PASS'
        except md.PackageNotFoundError:a=None;probe='NOT_INSTALLED'
        except Exception as e:a=None;probe=f'PROBE_FAILED:{type(e).__name__}:{str(e)[:120]}'
        ok=a==v;rows.append({'distribution':k,'expected':v,'actual':a,'probe_status':probe,'status':'PASS' if ok else 'MISMATCH'});bad += [] if ok else [k]
    if strict and bad:raise RuntimeError(f'ENVIRONMENT_PIN_MISMATCH:{bad}')
    return {'status':'PASS' if not bad else 'MISMATCH','packages':rows,'python':platform.python_version()}
