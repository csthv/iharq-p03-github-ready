from typer.testing import CliRunner
from iharq.config import validate_phase_config
from iharq.cli import app
def test_strict_phase_config(): assert validate_phase_config('configs/phases/p00.yaml').phase_id=='P00'
def test_cli_validate():
    r=CliRunner().invoke(app,['phase','validate-inputs','--phase','P00','--profile','configs/phases/p00.yaml']);assert r.exit_code==0,r.output
def test_close_fails_closed():
    r=CliRunner().invoke(app,['phase','close','--phase','P00','--evaluation','LOCAL']);assert r.exit_code==3
