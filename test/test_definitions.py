from n5a import N5AType, N5AValue, N5ACollection, make_type

def get_pos3d_definition():
    # This should not fail.
    LongInt = N5AType(name='longint', cpptype='int32_t', pytype=int)

    x = N5AValue(name='x', n5atype=LongInt)
    y = N5AValue(name='y', n5atype=LongInt)
    z = N5AValue(name='z', n5atype=LongInt)

    return N5ACollection(name='Pos3D', members=[x, y, z])