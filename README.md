Scikit-Learn Extensions
=======================

v0.0.1

Scikit-Learn Extensions (sklearn_extensions) is a single source repository for extensions to [scikit-learn](https://github.com/sklearn/sklearn). It is intended
to compliment the slower more cautious approach of scikit-learn with regard to adding new predictors and modules, with a 
separate pip-installable source for sklearn-compatible modules that may not meet those standards. 

In particular, this project is interested in smaller one-off projects or even gists, rather than larger more established ones (such as pylearn2).
Other than larger projects, we will shy away from projects with significant external dependencies (i.e. wrappers around 
vowpal wabbit or xgboost), and rather prefer more python/numpy/scipy based projects. 

Due to these guiding goals, the modules included here may not be as well tested, production ready, or stable as those included 
directly in sklearn.  This is pretty much the wild west, test anything that uses this package heavily.

Docs to be at: 

[http://wdm0006.github.io/sklearn-extensions](http://wdm0006.github.io/sklearn-extensions)

Installation / Usage
--------------------

We aim to first support python 3, and are hosted on pypi, so to install just:
 
    pip install sklearn-extensions

Note that the install here will install all underlying packages, and is therefore pretty big.  It is recommended that 
you do this in a virtualenv.

Extensions Included So Far
--------------------------

 * [Kernel Regression](https://github.com/jmetzen/kernel_regression)
 * [Sparse Filtering](https://github.com/jmetzen/sparse-filtering)
 * [Compiled Trees](https://github.com/ajtulloch/sklearn-compiledtrees/)
 * [Metric Learning](https://github.com/all-umass/metric-learn.git)
 * [Latent Dirichlet Allocation](https://github.com/ariddell/lda)
 * [KModes](https://github.com/nicodv/kmodes)
 * [Patsy-Learn](https://github.com/amueller/patsylearn)
 * [Pyculearn](https://github.com/predikto/pyculearn)
 * [Fuzzy K-Means](https://gist.github.com/mblondel/1451300)
 
TODO
----

A number of packages have been identified but not yet added due to python 3 incompatibility, not being
pip installable, or otherwise not trivial to add. If anyone would like to get involved with this project
a great way to start is to add one of these.

 * [Extreme Learning Machines](https://github.com/dclambert/Python-ELM)
 * [Optimal Path Forest Classifiers](https://github.com/LibOPF/LibOPF)
 * [Random Output Trees](https://github.com/arjoly/random-output-trees)
 * [Simple MLP](https://gist.github.com/amueller/2061456)
 * [Non-negative Garotte](https://gist.github.com/agramfort/2351057)
 * [Kernel SGD](https://gist.github.com/mblondel/2573392)
 * [Kernel K-Means](https://gist.github.com/mblondel/6230787)
 * [Non-Negative Least Squares](https://gist.github.com/mblondel/4421380)
 * [Non-Negative Matrix Factorization](https://gist.github.com/omangin/8801846)
 * [K-means Feature Mapper](https://gist.github.com/larsmans/5996074)
 * [NMF via Coordinate Descent](https://gist.github.com/mblondel/09648344984565f9477a)
 * [HDBSCAN](https://github.com/lmcinnes/hdbscan)
 * [Pegasos](https://github.com/ejlb/pegasos)
 * [Gaussian Processes](https://github.com/jmetzen/skgp)
 * [Pinch Ratio Clustering](https://github.com/rsbowman/sklearn-prc)
 
If you have any more suggestions, please feel free to add them, or let me know and I will try to. 

Contributing
------------

If you have an extension that you'd like to add, please submit a pull request and we can throw it in.  If modifications
to a project are required, please continue development in the project's own repo rather than submit changes here. If a 
project comes from a gist or some other snippet and therefore cannot be simply imported, then please create a new repo 
which can be simply imported here.

There are two methods for adding extensions into sklearn\_extensions:

 * If the extension is pip-installable, just add it to the requirements.txt file here, add a subdirectory for the new project, and import the relevant classes/methods
 * If the extension is not-pip installable, either make it so, or add the source into the subdirectory here directly. 
 
If there is a package that is useful but does not comply with the sklearn API, feel free to include a wrapped version of
it here as well, but include some tests.

We intend to add a consolidated source of tests for the included packages here as well, but that has not been formalized 
yet.


License
-------

In most cases, all that sklearn\_extensions does with external projects is import them. In those cases we add the license
of the source project in its subdirectory just for safe-keeping. 

All material specific to this project (specifically any docs, tests, examples or original code) is released under the 
BSD 3-clause license. Any packages included in the bundle retain their original licences (as included in their subdirectories)