import json
import pytest

from n5a import make_type
from n5a.serialize import serialize_to_json, _serialize_transform

from .test_definitions import get_pos3d_definition

def test_serialization():
    Pos3DT = make_type(get_pos3d_definition())
    t = Pos3DT(x=0, y=1, z=2)
    s = serialize_to_json(dict(root=dict(data=t)))

    # Note that serialization from Python is currently a one-way street.
    json.loads(s) == _serialize_transform(t)