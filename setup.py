from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name='sklearn-extensions',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    author='Will McGinnis',
    author_email='will@pedalwrencher.com'
)