from collections import namedtuple

N5AType = namedtuple('N5AType', ['name', 'cpptype', 'pytype'])
N5AValue = namedtuple('N5AValue', ['name', 'type'])
N5ACollection = namedtuple('N5AType', ['name', 'members'])

def make_type(collection):
    # Generate list of members.
    members = []
    for m in collection.members:
        members.append(m.name)
    r = namedtuple(collection.name, members)
    r.__is_n5a_type__ = True
    return r
