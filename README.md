# n5a
C++, Python JSON serialization code generator

Note that this is still in flux (pre-alpha), no interfaces are fixed yet.

CI:
[![Build Status](https://travis-ci.org/sschaetz/n5a.svg?branch=master)](https://travis-ci.org/sschaetz/n5a)


## How it works

Define types in C++ like so:

```python
from n5a import N5AType, N5AValue, N5ACollection, make_type

LongInt = N5AType(name='longint', cpptype='int32_t', pytype=int)

x = N5AValue(name='x', n5atype=LongInt)
y = N5AValue(name='y', n5atype=LongInt)
z = N5AValue(name='z', n5atype=LongInt)

Pos3D = N5ACollection(name='Pos3D', members=[x, y, z])
```

Work with this in python:

```python
Pos3DType = make_type(Pos3D)
s = serialize_to_json(dict(root=dict(data=Pos3DType(x=0, y=1, z=2))))
```

Work with this in C++ by generating a C++ header file:

```python
s = generate(Pos3D)
with open('pos3d.hpp', 'w') as f:
    f.write(s)
```

Which yelds a file like containing this:

```cpp
/*
 * This file is generated automatically. Modifications of this file will be overwritten.
 * Generated with n5a - https://github.com/sschaetz/n5a
 */

#include <cereal/cereal.hpp>

struct Pos3D
{
	int32_t x;
	int32_t y;
	int32_t z;

	template <class Archive>
	void save(Archive& ar, std::uint32_t const version) const
	{
		(void)(version);
		ar(::cereal::make_nvp("x", x));
		ar(::cereal::make_nvp("y", y));
		ar(::cereal::make_nvp("z", z));
	}

	template <class Archive>
	void load(Archive& ar, std::uint32_t const version)
	{
		(void)(version);
		ar(::cereal::make_nvp("x", x));
		ar(::cereal::make_nvp("y", y));
		ar(::cereal::make_nvp("z", z));
	}
};
```

Which can be used in C++ like so:

```cpp
#include "pos3d.hpp"
#include <cereal/archives/json.hpp>

Pos3D p_out;
p_out.x = 4;
p_out.y = 1;
p_out.z = 2;

std::ofstream out("pos3d.json");
cereal::JSONOutputArchive archive(out);
archive(::cereal::make_nvp("pos3d", p_out));
```

:tada::tada::tada::tada:
