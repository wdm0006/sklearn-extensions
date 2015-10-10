.. sklearn-extensions documentation master file, created by
   sphinx-quickstart on Sat Oct 10 14:23:11 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to sklearn-extensions's documentation!
==============================================

Scikit-Learn Extensions (sklearn_extensions) is a single source repository for extensions to `scikit-learn <https://github.com/sklearn/sklearn>`_ . It is intended
to compliment the slower more cautious approach of scikit-learn with regard to adding new predictors and modules, with a
separate pip-installable source for sklearn-compatible modules that may not meet those standards.

In particular, this project is interested in smaller one-off projects or even gists, rather than larger more established ones (such as pylearn2).
Other than larger projects, we will shy away from projects with significant external dependencies (i.e. wrappers around
vowpal wabbit or xgboost), and rather prefer more python/numpy/scipy based projects.

Due to these guiding goals, the modules included here may not be as well tested, production ready, or stable as those included
directly in sklearn.  This is pretty much the wild west, test anything that uses this package heavily.

Below is an index of the included packages, many of which have their own documentation.

Contents:

.. toctree::
   :maxdepth: 1

   compiled_trees
   fuzzy_k_means
   kernel_regression
   kmodes
   latent_dirichlet_allocation
   metric_learning
   patsy_learn
   pyculearn
   sparse_filtering


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

