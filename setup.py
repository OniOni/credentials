from setuptools import setup

with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='credentials',
    description='Credential Manager',
    long_description=LONG_DESCRIPTION,
    author='Mathieu Sabourin',
    author_email='mathieu.c.sabourin@gmail.com',
    url='https://github.com/OniOni/credentials',
    packages=['credentials'],
    version=1.1,
    license='LGPLv3'
)
