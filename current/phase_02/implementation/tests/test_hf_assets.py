from __future__ import annotations
import hashlib,sys,types,json
from pathlib import Path
import yaml,nbformat
from iharq.layer2_decoders.hf_assets import resolve_hf_assets
from iharq.layer2_decoders.security import scan_text

PKG=Path(__file__).resolve().parents[1]

def _sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def test_public_hf_asset_resolves_without_token_and_verifies_hash(tmp_path,monkeypatch):
    payload=b'governed-cbramod-fixture'; expected=hashlib.sha256(payload).hexdigest(); calls=[]
    def fake(**kw):
        calls.append(kw);p=Path(kw['local_dir'])/kw['filename'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(payload);return str(p)
    monkeypatch.setitem(sys.modules,'huggingface_hub',types.SimpleNamespace(hf_hub_download=fake))
    spec={'policy_id':'X','assets':{'SSL-CBRAMOD':{'enabled':True,'eligibility':'ELIGIBLE_CURRENT_P02','gated':False,'repo_id':'org/model','repo_type':'model','revision':'a'*40,'files':[{'filename':'model.safetensors','sha256':expected,'required':True}],'implementation_module':'iharq.layer2_decoders.hf_cbramod_adapter','license_status':'CAN_EXECUTE','source_recipe_verified':True,'corpus_overlap_status':'PASS','input_compatibility_status':'PASS','channel_montage_status':'PASS','sampling_adapter_verified':True,'target_sampling_hz':200,'checkpoint_file':'model.safetensors','checkpoint_sha256':expected,'plugin_config':{}}}}
    bindings={'SSL-CBRAMOD':{'checkpoint_required':True}}
    out,ev=resolve_hf_assets(bindings,spec,tmp_path,token=None)
    assert ev['branches']['SSL-CBRAMOD']['status']=='VERIFIED'
    assert calls[0]['revision']=='a'*40 and calls[0]['token'] is None
    assert _sha(out['SSL-CBRAMOD']['checkpoint_path'])==expected
    assert 'token' not in json.dumps(ev).lower() or 'token_used' in json.dumps(ev)

def test_gated_asset_missing_token_is_auth_required_without_download(tmp_path,monkeypatch):
    called=[]
    monkeypatch.setitem(sys.modules,'huggingface_hub',types.SimpleNamespace(hf_hub_download=lambda **kw: called.append(kw)))
    spec={'policy_id':'X','assets':{'G':{'enabled':True,'eligibility':'ELIGIBLE_CURRENT_P02','gated':True,'repo_id':'gated/repo','files':[]}}}
    _,ev=resolve_hf_assets({'G':{}},spec,tmp_path,token=None)
    assert ev['branches']['G']['status']=='AUTH_REQUIRED' and called==[]

def test_scientifically_blocked_reve_never_downloads_even_with_token(tmp_path,monkeypatch):
    called=[]
    monkeypatch.setitem(sys.modules,'huggingface_hub',types.SimpleNamespace(hf_hub_download=lambda **kw: called.append(kw)))
    spec={'policy_id':'X','assets':{'SSL-REVE':{'enabled':True,'eligibility':'BLOCKED_KNOWN_P02_PRETRAINING_CORPUS_OVERLAP','gated':True,'repo_id':'brain-bzh/reve-base','corpus_overlap_status':'BLOCKED_KNOWN_P02_OVERLAP','license_status':'POINTER_ONLY_GATED_NO_REDISTRIBUTION','corpus_overlap_basis':'known overlap'}}}
    out,ev=resolve_hf_assets({'SSL-REVE':{}},spec,tmp_path,token='secret-in-memory')
    assert ev['branches']['SSL-REVE']['download_attempted'] is False and called==[]
    assert out['SSL-REVE']['corpus_overlap_status']=='BLOCKED_KNOWN_P02_OVERLAP'

def test_hf_token_pattern_is_security_scanned():
    fake='hf_'+'A'*40
    assert scan_text('x='+fake)

def test_notebook_has_hidden_prompt_and_no_hardcoded_hf_token():
    nb=nbformat.read(PKG/'notebook/IHARQ_Phase_02_Complete_Execution_and_Analysis_R4_HF_R1.ipynb',as_version=4)
    cell=next(c for c in nb.cells if c.id=='hf-auth-run')
    assert 'getpass.getpass' in cell.source and 'UserSecretsClient' in cell.source and 'HF_TOKEN' in cell.source
    assert not any(('hf_'+'A'*20) in c.source for c in nb.cells)
    assert all(c.get('execution_count') is None and not c.get('outputs',[]) for c in nb.cells if c.cell_type=='code')

def test_current_hf_policy_is_governed_and_reve_overlap_blocked():
    d=yaml.safe_load((PKG/'configs/phase_02/models/huggingface_assets.yaml').read_text())
    c=d['assets']['SSL-CBRAMOD'];r=d['assets']['SSL-REVE']
    assert c['revision']=='584cdc415913739a05d84bf0c1cb3db397764507'
    assert c['checkpoint_sha256']=='a939ace9aa1e229f08391ad8bb2d197b507ae2c519a50addf087f0151b2df5c3'
    assert r['eligibility'].startswith('BLOCKED_') and r['download_policy']=='DO_NOT_DOWNLOAD_CURRENT_P02'

def test_hf_evidence_records_source_type_but_never_token_value(tmp_path,monkeypatch):
    payload=b'asset'; expected=hashlib.sha256(payload).hexdigest()
    def fake(**kw):
        p=Path(kw['local_dir'])/kw['filename'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(payload);return str(p)
    monkeypatch.setitem(sys.modules,'huggingface_hub',types.SimpleNamespace(hf_hub_download=fake))
    spec={'policy_id':'X','assets':{'SSL-CBRAMOD':{'enabled':True,'eligibility':'ELIGIBLE_CURRENT_P02','gated':False,'repo_id':'org/model','repo_type':'model','revision':'a'*40,'files':[{'filename':'model.safetensors','sha256':expected,'required':True}],'implementation_module':'iharq.layer2_decoders.hf_cbramod_adapter','license_status':'CAN_EXECUTE','source_recipe_verified':True,'corpus_overlap_status':'PASS','input_compatibility_status':'PASS','channel_montage_status':'PASS','sampling_adapter_verified':True,'target_sampling_hz':200,'checkpoint_file':'model.safetensors','checkpoint_sha256':expected,'plugin_config':{}}}}
    secret='hf_'+'Z'*40
    _,ev=resolve_hf_assets({'SSL-CBRAMOD':{}},spec,tmp_path,token=secret,token_source='KAGGLE_SECRET:HF_TOKEN')
    blob=json.dumps(ev)
    assert ev['token']['credential_source_type']=='KAGGLE_SECRET:HF_TOKEN'
    assert ev['token']['credential_value']=='REDACTED'
    assert secret not in blob


def test_notebook_clears_hf_token_immediately_after_stage03():
    nb=nbformat.read(PKG/'notebook/IHARQ_Phase_02_Complete_Execution_and_Analysis_R4_HF_R1.ipynb',as_version=4)
    c=next(c for c in nb.cells if c.id=='stage-03-run')
    assert 'SESSION.clear_hf_token()' in c.source
    assert 'HF_TOKEN = None' in c.source
    assert 'huggingface_credential_retained_after_stage03' in c.source
