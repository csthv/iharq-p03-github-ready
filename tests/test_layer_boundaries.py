import importlib

def test_all_layer_packages_non_scientific():
 names=['claim_governance','data_protocol','decoders','calibration_uncertainty','iharq','regimerisk','readiness_policy','closed_loop','stressforge','embodiment','reproducibility']
 for i,n in enumerate(names):
  m=importlib.import_module(f'iharq.layer{i}_{n}');assert m.SCIENTIFIC_EXECUTION is False
