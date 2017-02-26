from collections import namedtuple

N5AType = namedtuple('N5AType', ['name', 'cpptype', 'pytype'])
N5AValue = namedtuple('N5AValue', ['name', 'type'])
N5ACollection = namedtuple('N5AType', ['name', 'members'])
