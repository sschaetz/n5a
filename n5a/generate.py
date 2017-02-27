def _generate_save_load(obj, signature, nl, tab):
    s = '{nl}{tab}template <class Archive>{nl}'.format(nl=nl, tab=tab)
    s += '{tab}{signature}{nl}{tab}{{{nl}'.format(
        signature=signature, nl=nl, tab=tab
    )
    for member in obj.members:
        s += '{tab}{tab}ar(::cereal::make_nvp("{name}", {name}));{nl}'.format(
            name=member.name,
            nl=nl,
            tab=tab
        )
    s += '{tab}}}{nl}'.format(nl=nl, tab=tab)
    return s

def generate(obj, header=None, footer=None, nl='\n', tab='\t'):
    s = ''
    if header is not None:
        s+=header

    s += '{nl}struct {name}{nl}{{{nl}'.format(name=obj.name, nl=nl)

    # Generate members in struct.
    for member in obj.members:
        s += '{tab}{n5atype} {name};{nl}'.format(
            n5atype=member.n5atype.cpptype,
            name=member.name,
            nl=nl,
            tab=tab
        )

    # Generate save method.
    s += _generate_save_load(
        obj,
        'void save(Archive& ar, std::uint32_t const version) const',
        nl,
        tab
    )

    # Generate load method.
    s += _generate_save_load(
        obj,
        'void load(Archive& ar, std::uint32_t const version)',
        nl,
        tab
    )

    s += '}};{0}'.format(nl)

    if footer is not None:
        s += footer
    return s
