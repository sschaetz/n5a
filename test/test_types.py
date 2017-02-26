import pytest

from n5a import N5AType

def test_define_incomplete_type():
    # This should fail.
    with pytest.raises(TypeError):
        x = N5AType()

def test_define_complete_type():
    # This should not fail.
    t = N5AType(name='myname', cpptype='int32_t', pytype=int)
    assert t.name == "myname"