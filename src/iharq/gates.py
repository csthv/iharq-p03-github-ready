from __future__ import annotations
GATE_TOPICS={1:'authority_baseline',2:'paths',3:'schemas',4:'configs',5:'identity_hash_seed',6:'valid_fixtures',7:'invalid_fixtures',8:'validators',9:'ablations',10:'cross_layer_traceability',11:'policy_update',12:'frozen_evaluation',13:'layer0_foundation',14:'layer10_foundation',15:'manifests',16:'implementation_readiness',17:'local_reproduction',18:'governed_publication_and_closure'}
def evaluate(context:dict):
    rows=[]
    for n,key in GATE_TOPICS.items():
        if n==18: status='READY_TO_PASS_AFTER_VERIFIED_IMMUTABLE_PUBLICATION' if context.get(key) is not True else 'PASS'
        else: status='PASS' if context.get(key) is True else 'FAIL'
        rows.append({'gate_id':f'P0-GATE-{n:02d}','topic':key,'status':status,'authoritative_mapping':'Governance V4, current Build Book, and P00 publication decision','waiver_allowed':False})
    return rows
