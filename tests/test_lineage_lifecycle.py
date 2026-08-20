from iharq.lineage import missing_sources,descendants
from iharq.lifecycle import transition_allowed,reusable_for_acceptance
def test_lineage():
 r=[{'record_id':'a','source_ids':[]},{'record_id':'b','source_ids':['a']},{'record_id':'c','source_ids':['b']}];assert missing_sources(r)=={};assert descendants(r,{'a'})=={'b','c'}
def test_lifecycle(): assert transition_allowed('VALIDATED','ACCEPTED') and not transition_allowed('INVALIDATED','ACCEPTED') and not reusable_for_acceptance('SUPERSEDED')
