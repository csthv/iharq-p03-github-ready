from __future__ import annotations
from pathlib import Path
import json,subprocess,sys,typer
from .config import validate_phase_config
from .validation import load_bundle,validate_bundle
ROOT=Path(__file__).parents[2]
app=typer.Typer(help='IHARQ governed Phase 0 CLI')
phase=typer.Typer();local=typer.Typer();package=typer.Typer()
app.add_typer(phase,name='phase');app.add_typer(local,name='local');app.add_typer(package,name='package')
def bounded(cmd:list[str],timeout:int=600)->int:
 try:return subprocess.run(cmd,cwd=ROOT,timeout=timeout).returncode
 except subprocess.TimeoutExpired:return 124
@phase.command('plan')
def plan(phase_id:str=typer.Option(...,'--phase'),state:Path=typer.Option(...,'--state'),dry_run:bool=True):typer.echo(json.dumps({'phase':phase_id,'state_path':str(state),'dry_run':dry_run,'status':'PLANNED'},indent=2))
@phase.command('validate-inputs')
def validate_inputs(phase_id:str=typer.Option(...,'--phase'),profile:Path=typer.Option(...,'--profile')):
 cfg=validate_phase_config(profile)
 if cfg.phase_id!=phase_id:raise typer.Exit(2)
 typer.echo(json.dumps({'phase':phase_id,'profile':str(profile),'status':'VALID'},indent=2))
@phase.command('run')
def run(phase_id:str=typer.Option(...,'--phase'),mode:str=typer.Option('real','--mode'),fixture:Path=typer.Option(Path('fixtures/valid/all_record_families.json'),'--fixture'),dry_run:bool=False):
 if phase_id!='P00' or mode not in {'smoke','real'}:raise typer.Exit(2)
 if dry_run:typer.echo(json.dumps({'status':'DRY_RUN','fixture':str(fixture),'mode':mode}));return
 errors=validate_bundle(load_bundle(fixture),ROOT)
 typer.echo(json.dumps({'phase':phase_id,'mode':mode,'errors':errors,'status':'PASS' if not errors else 'FAIL'},indent=2))
 if errors:raise typer.Exit(1)
@phase.command('gate')
def gate(phase_id:str=typer.Option(...,'--phase'),run_id:str=typer.Option(...,'--run')):typer.echo(json.dumps({'phase':phase_id,'run_id':run_id,'status':'SEE_LOCAL_FIRST_GATE_PROFILE'}))
@phase.command('analyze')
def analyze(phase_id:str=typer.Option(...,'--phase'),evaluation:str=typer.Option(...,'--evaluation')):typer.echo(json.dumps({'phase':phase_id,'evaluation':evaluation,'status':'SAFEGUARDED_HOOK_NOT_FINAL_ANALYSIS'}))
@phase.command('close')
def close(phase_id:str=typer.Option(...,'--phase'),evaluation:str=typer.Option(...,'--evaluation')):
 typer.echo(json.dumps({'phase':phase_id,'evaluation':evaluation,'status':'BLOCKED_GOVERNED_CLOSURE_DEFERRED'}));raise typer.Exit(3)
@local.command('test')
def local_test():
 rc=bounded([sys.executable,'-m','pytest','-q']);raise typer.Exit(rc)
@local.command('reproduce')
def local_reproduce():
 rc=bounded([sys.executable,'scripts/run_local_reproduction.py','--no-write-report'],1200);raise typer.Exit(rc)
@package.command('build')
def package_build(output:Path=typer.Option(...,'--output')):
 rc=bounded([sys.executable,'scripts/build_local_package.py','--output',str(output)],1200);raise typer.Exit(rc)
@package.command('verify')
def package_verify(archive:Path=typer.Option(...,'--archive')):
 rc=bounded([sys.executable,'scripts/verify_local_package.py','--archive',str(archive)],600);raise typer.Exit(rc)
if __name__=='__main__':app()
