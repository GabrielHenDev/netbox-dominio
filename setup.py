import codecs
import os.path

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name='netbox-domino',
    version=get_version('netbox_domino/version.py'),
    description='Domain inventory plugin for NetBox',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/gestao-dominio/netbox_domino',
    author='Gestão Domínio',
    author_email='contato@gestaodomino.local',
    packages=find_packages(),
    include_package_data=True,
    min_version='4.4.0',
    max_version='4.4.99',
    install_requires=[],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ]
)
