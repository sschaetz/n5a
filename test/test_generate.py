from n5a import make_type
from n5a.generate import generate

from .test_definitions import get_pos3d_definition

def test_serialization():
    s = generate(get_pos3d_definition())
    assert 'struct Pos3D' in s