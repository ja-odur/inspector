from setuptools import setup
from os import path

DIR = path.dirname(path.abspath(__file__))

DESCRIPTION = "Extract information about Python packages"

AUTHORS = 'J.A. Odur'

URL = 'https://github.com/ja-odur/introspector'

EMAIL = 'odurjoseph8@gmail.com'

with open(path.join(DIR, 'requirements.txt')) as f:
    INSTALL_PACKAGES = f.read().splitlines()

with open(path.join(DIR, 'README.md')) as f:
    README = f.read()

# get __version__ from _version.py
ver_file = path.join('introspector', '_version.py')
with open(ver_file) as f:
    exec(f.read())

VERSION = __version__

setup(
    name='introspector',
    packages=['introspector'],
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type='text/markdown',
    install_requires=INSTALL_PACKAGES,
    version=VERSION,
    url=URL,
    author=AUTHORS,
    author_email=EMAIL,
    keywords=['python-instrospection'],
    tests_require=[

    ],
    package_data={
        # include json and pkl files
        '': ['*.json', 'models/*.pkl', 'models/*.json'],
    },
    include_package_data=True,
    python_requires='>=3'
)
