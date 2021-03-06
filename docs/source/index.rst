.. sklearn-extensions documentation master file, created by
   sphinx-quickstart on Sat Oct 10 14:23:11 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to sklearn-extensions's documentation!
==============================================

Scikit-Learn Extensions (sklearn_extensions) is a single source repository for extensions to [scikit-learn](https://github.com/sklearn/sklearn). It is intended
to compliment the slower more cautious approach of scikit-learn with regard to adding new predictors and modules, with a
separate pip-installable source for sklearn-compatible modules that may not meet those standards.

In particular, this project is interested in smaller one-off projects, particularly even gists, rather than larger more
established ones (such as pylearn2, lifeline, or lightning). Other than larger projects, we will shy away from projects
with significant external dependencies (i.e. wrappers around vowpal wabbit or xgboost), and rather prefer more
python/numpy/scipy based projects.

Due to these guiding goals, the modules included here may not be as well tested, production ready, or stable as those included
directly in sklearn.  This is pretty much the wild west, test anything that uses this package heavily.

Installation / Usage
--------------------

We aim to first support python 3, and are hosted on pypi, so to install just:

    pip install sklearn-extensions

Note that the install here will install all underlying packages, and is therefore pretty big.  It is recommended that
you do this in a virtualenv.

Extensions Included So Far
--------------------------

 * `Kernel Regression <https://github.com/jmetzen/kernel_regression>`_
    * kernel_regression.KernelRegression()
 * `Fuzzy K-Means <https://gist.github.com/mblondel/1451300>`_
    * fuzzy_kmeans.KMeans()
    * fuzzy_kmeans.KMedians()
    * fuzzy_kmeans.FuzzyKMeans()
 * `Sparse Filtering <https://github.com/jmetzen/sparse-filtering>`_
    * sparse_filtering.SparseFiltering()
 * `Extreme Learning Machines <https://github.com/dclambert/Python-ELM>`_
    * extreme_learning_machines.ELMRegressor()
    * extreme_learning_machines.ELMClassifier()
    * extreme_learning_machines.GenELMRegressor()
    * extreme_learning_machines.GenELMClassifier()
    * extreme_learning_machines.RandomLayer()
    * extreme_learning_machines.GRBFRandomLayer()
    * extreme_learning_machines.RBFRandomLayer()
    * extreme_learning_machines.MLPRandomLayer()
 * `Non-negative Garotte <https://gist.github.com/agramfort/2351057>`_
    * non_negative_garotte.NonNegativeGarrote()
 * `Kernel SGD <https://gist.github.com/mblondel/2573392>`_
    * kernel_sgd.HingeLoss()
    * kernel_sgd.KernelSGD()
    * kernel_sgd.GaussianKernel()

TODO
----

A number of packages have been identified but not been added yet. As a general rule for identifying potential projects
to add to sklearn-extensions, if it cannot be pip-installed: it may be a candidate here

 * `Optimal Path Forest Classifiers <https://github.com/LibOPF/LibOPF>`_
 * `Random Output Trees <https://github.com/arjoly/random-output-trees>`_
 * `Simple MLP <https://gist.github.com/amueller/2061456>`_
 * `Kernel K-Means <https://gist.github.com/mblondel/6230787>`_
 * `Non-Negative Least Squares <https://gist.github.com/mblondel/4421380>`_
 * `Non-Negative Matrix Factorization <https://gist.github.com/omangin/8801846>`_
 * `K-means Feature Mapper <https://gist.github.com/larsmans/5996074>`_
 * `NMF via Coordinate Descent <https://gist.github.com/mblondel/09648344984565f9477a>`_
 * `Pegasos <https://github.com/ejlb/pegasos>`_
 * `Gaussian Processes <https://github.com/jmetzen/skgp>`_
 * `Pinch Ratio Clustering <https://github.com/rsbowman/sklearn-prc>`_
 * `py-soft-impute <https://github.com/travisbrady/py-soft-impute>`_

If you have any more suggestions, please feel free to add them, or let me know and I will try to.

Contributing
------------

If you have an extension that you'd like to add, please submit a pull request and we can throw it in.  A major benefit of
this package is that we will aim to consolidate requirements among the disparate projects, therefore, for the sake of
management, the code for the projects will be replicated here. In the spirit of OSS, we will also aim to contribute any
meaningful changes back to the original projects as well.

A complete addition of a new package has a few components:

 * Actual addition of package into sklearn\_extensions directory
 * Documentation of the included transformers/predictors in the sklearn\_extensions docs
 * An example or two (included in the aforementioned docs as well) in the examples directory
 * A test or two, more if the source package has poor testing coverage

License
-------

In most cases, all that sklearn\_extensions does with external projects is include them. All of the projects will remain
segregated into their own subdirectory, and will carry their original licenses in those subdirectories.

All material specific to this project (specifically any docs, tests, examples or original code) is released under the
BSD 3-clause license. Any packages included in the bundle retain their original licences (as included in thir subdirectories)


Contents:

.. toctree::
   :maxdepth: 1

   fuzzy_k_means
   kernel_regression
   sparse_filtering
   extreme_learning_machines
   kernel_sgd
   non_negative_garotte


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

