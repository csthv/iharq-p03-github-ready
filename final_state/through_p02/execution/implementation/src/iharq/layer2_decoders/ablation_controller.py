def resolve(rows,result_observed=False):
 if result_observed:raise RuntimeError('RESULT_DEPENDENT_ABLATION_UNLOCK_PROHIBITED')
 extra=[]
 for r in rows:
  aid=r.get('ablation_id') or r.get('id');state=r.get('p02_state') or r.get('state')
  if aid not in {'A0','A4','A14'} and state=='FULL_EXECUTION_REQUIRED_IN_P02':extra.append(aid)
 return {'status':'PASS','additional_full_execution':sorted(extra),'decision':'NO_ADDITIONAL_FULL_EXECUTION_ABLATION_UNLOCKED' if not extra else 'ADDITIONAL_AUTHORIZED'}
