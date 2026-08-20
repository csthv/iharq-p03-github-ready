from __future__ import annotations
REVIEW_ROLES=['Authority Reconstruction LLM','Implementation Evidence LLM','Adversarial Red-Team LLM','Gate and Reproducibility LLM','Final Governance LLM']
LAYER0_ROLES=['Evidence Sufficiency LLM','Claim Safety LLM','Adversarial Claim LLM']
def quorum(verdicts:dict[str,str],roles:list[str]=REVIEW_ROLES)->bool:
    return all(verdicts.get(r)=='PASS' for r in roles)
def layer0_quorum(verdicts:dict[str,str])->bool: return quorum(verdicts,LAYER0_ROLES)
