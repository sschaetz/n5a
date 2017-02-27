import pytest

from n5a import N5AType, make_type

from .test_definitions import get_pos3d_definition


def test_define_incomplete_type():
    # This should fail.
    with pytest.raises(TypeError):
        x = N5AType()

def test_define_complete_type():
    # This should not fail.
    t = N5AType(name='myname', cpptype='int32_t', pytype=int)
    assert t.name == "myname"

def test_collection():
    z = get_pos3d_definition()

    for i, k in enumerate(z):
        if i == 0:
            assert k == 'Pos3D'
        elif i == 1:
            assert isinstance(k, list)
        elif i > 1:
            assert False

def test_make_type():
    Pos3DT = make_type(get_pos3d_definition())
    t = Pos3DT(x=0, y=1, z=2)
    assert t.x == 0
    assert t.y == 1
    assert t.z == 2