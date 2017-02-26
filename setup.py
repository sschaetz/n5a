from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='n5a',
    version='0.0.1',
    description=u"C++, Python JSON serialization code generator",
    long_description=long_description,
    license='MIT',
    classifiers=[],
    keywords='',
    author=u"Sebastian Schaetz",
    author_email='seb.schaetz@gmail.com',
    url='https://github.com/sschaetz/n5a',
    packages=find_packages(exclude=['test']),
    include_package_data=False,
    zip_safe=False,
    install_requires=[],
    extras_require=
    {
        'test': ['pytest'],
    },
    entry_points=
    """
        [console_scripts]
        n5a=n5a.gen.gen:gen
    """,
)