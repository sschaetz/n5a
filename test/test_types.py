import pytest

from n5a import N5AType, N5AValue, N5ACollection

def test_define_incomplete_type():
    # This should fail.
    with pytest.raises(TypeError):
        x = N5AType()

def test_define_complete_type():
    # This should not fail.
    t = N5AType(name='myname', cpptype='int32_t', pytype=int)
    assert t.name == "myname"

def test_collection():
    # This should not fail.
    LongInt = N5AType(name='longint', cpptype='int32_t', pytype=int)

    x = N5AValue(name='x', type=LongInt)
    y = N5AValue(name='y', type=LongInt)
    z = N5AValue(name='z', type=LongInt)

    Pos3D = N5ACollection(name='Pos3D', members=[x, y , z])

    z = Pos3D

    for i, k in enumerate(z):
        if i == 0:
            assert k == 'Pos3D'
        elif i == 1:
            assert isinstance(k, list)
        elif i > 1:
            assert False