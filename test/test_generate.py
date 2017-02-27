from n5a import make_type
from n5a.generate import generate

from .test_definitions import get_pos3d_definition

def test_generate_string():
    s = generate(get_pos3d_definition())
    assert 'struct Pos3D' in s

def test_generate_file():
    s = generate(get_pos3d_definition())
    with open('test/test_cpp/generated/pos3d.hpp', 'w') as f:
        f.write(s)