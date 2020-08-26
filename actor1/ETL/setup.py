import os
from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='dossier-etl',
    description='Django plugin to execute ETL scripts only.',
    # long_description=read('README.md'),
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
