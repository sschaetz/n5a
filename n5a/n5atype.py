from collections import namedtuple

from n5a import n5a_type_marker

N5AType = namedtuple('N5AType', ['name', 'cpptype', 'pytype'])
N5AValue = namedtuple('N5AValue', ['name', 'n5atype'])
N5ACollection = namedtuple('N5AType', ['name', 'members'])

def make_type(collection):
    # Generate list of members.
    members = []
    for m in collection.members:
        members.append(m.name)
    r = namedtuple(collection.name, members)
    r.n5a_type_marker = True
    return r
