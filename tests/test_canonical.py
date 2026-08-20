import pytest
from iharq.canonical import canonical_bytes,semantic_hash,CanonicalizationError
def test_key_order_and_hash(): assert semantic_hash({'b':2,'a':1})==semantic_hash({'a':1,'b':2})
def test_unicode_preserved_not_normalized(): assert canonical_bytes({'x':'é'})!=canonical_bytes({'x':'e\u0301'})
def test_utf16_ordering_vector(): assert canonical_bytes({'😀':1,'a':2}).startswith(b'{"a"')
def test_nonfinite_negativezero_float_and_large_integer_rejected():
    for v in [float('nan'),float('inf'),-0.0,1.25,9007199254740992]:
        with pytest.raises(CanonicalizationError): canonical_bytes({'x':v})
