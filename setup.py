from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name='sklearn-extensions',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    author='Will McGinnis',
    install_requires=[
        'numpy>=1.9.0',
        'patsy>=0.4',
        'lda>=1.0.2',
        'sklearn-compiledtrees>=1.2'
    ],
    depedency_links=[
        'https://github.com/jmetzen/kernel_regression.git',
        'https://github.com/jmetzen/sparse-filtering.git',
        'https://github.com/all-umass/metric-learn.git',
        'https://github.com/nicodv/kmodes.git',
        'https://github.com/amueller/patsylearn.git',
        'https://github.com/predikto/pyculearn.git'
    ],
    author_email='will@pedalwrencher.com'
)