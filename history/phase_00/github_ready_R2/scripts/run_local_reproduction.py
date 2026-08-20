from __future__ import annotations
import argparse, json, os, re, shutil, subprocess, sys, tempfile, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser(); ap.add_argument('--report',default='reports/phase_00/public_clean_reproduction.json'); ap.add_argument('--no-write-report',action='store_true'); args=ap.parse_args()
REPORT=(ROOT/args.report).resolve() if not Path(args.report).is_absolute() else Path(args.report)
rows=[]
def sanitize(value, temp_root=None):
    if isinstance(value,str):
        replacements=[(str(ROOT),'${REPOSITORY_ROOT}'),('/opt/pyvenv','${VERIFIED_RUNTIME_ROOT}'),('/home/oai','${USER_HOME}'),('/mnt/data','${LOCAL_WORKSPACE_ROOT}'),('/tmp','${TEMP_ROOT}')]
        if temp_root: replacements.insert(0,(str(temp_root),'${CLEAN_REPRO_ROOT}'))
        for a,b in replacements:value=value.replace(a,b)
        value=re.sub(r'https://[^\s]+@packages\.applied-caas-gateway1\.internal\.api\.openai\.org/artifactory/api/pypi/pypi-public/simple','${PACKAGE_INDEX_REDACTED}',value)
        return value
    if isinstance(value,list):return [sanitize(x,temp_root) for x in value]
    if isinstance(value,dict):return {k:sanitize(v,temp_root) for k,v in value.items()}
    return value
def run(name,cmd,cwd,timeout=600,temp_root=None):
    t=time.time(); p=subprocess.run(cmd,cwd=cwd,text=True,capture_output=True,timeout=timeout,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
    rows.append({'name':name,'command':sanitize(cmd,temp_root),'returncode':p.returncode,'seconds':round(time.time()-t,3),'stdout_tail':sanitize(p.stdout[-1500:],temp_root),'stderr_tail':sanitize(p.stderr[-1500:],temp_root)})
    if p.returncode: raise SystemExit(f'{name} failed: {p.stdout[-800:]} {p.stderr[-800:]}')
with tempfile.TemporaryDirectory(prefix='iharq-public-repro-') as td:
    temp_root=Path(td);dest=temp_root/ROOT.name
    shutil.copytree(ROOT,dest,ignore=shutil.ignore_patterns('.git','.venv','venv','.pytest_cache','__pycache__','*.pyc','build','dist','*.egg-info'))
    run('install-editable',[sys.executable,'-m','pip','install','-e','.', '--no-deps','--no-build-isolation'],dest,temp_root=temp_root)
    run('public-tests',[sys.executable,'-m','pytest','-q','-p','no:cacheprovider'],dest,temp_root=temp_root)
    run('publication-verify',[sys.executable,'scripts/verify_publication_tree.py'],dest,temp_root=temp_root)
obj={'report_id':'P00-PUBLIC-CLEAN-REPRODUCTION-R2','status':'PASS','github_ci_used':False,'commands':rows}
if not args.no_write_report:
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps({'status':'PASS','steps':len(rows)},indent=2))
