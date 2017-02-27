import json
from n5a import n5a_type_marker

def _serialize_transform(obj):
    if hasattr(obj, n5a_type_marker):
        return _serialize_transform(obj._asdict())
    if isinstance(obj, dict):
        return {k: _serialize_transform(v) for k, v in obj.items()}
    return obj

def serialize_to_json(obj):
    return json.dumps(_serialize_transform(obj))
