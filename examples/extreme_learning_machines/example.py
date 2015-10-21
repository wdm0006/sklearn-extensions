#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
======================
ELM Classifiers Comparison
======================
A comparison of a several ELMClassifiers with different types of hidden
layer activations.

ELMClassifier is a classifier based on the Extreme Learning Machine,
a single layer feedforward network with random hidden layer components
and least squares fitting of the hidden->output weights by default [1][2]

The point of this example is to illustrate the nature of decision boundaries
with different hidden layer activation types and regressors.

This should be taken with a grain of salt, as the intuition conveyed by
these examples does not necessarily carry over to real datasets.

In particular in high dimensional spaces data can more easily be separated
linearly and the simplicity of classifiers such as naive Bayes and linear SVMs
might lead to better generalization.

The plots show training points in solid colors and testing points
semi-transparent. The lower right shows the classification accuracy on the test
set.

References
__________
.. [1] http://www.extreme-learning-machines.org
.. [2] G.-B. Huang, Q.-Y. Zhu and C.-K. Siew, "Extreme Learning Machine:
          Theory and Applications", Neurocomputing, vol. 70, pp. 489-501,
          2006.

===============================================================================
Basis Functions:
  gaussian rbf  : exp(-gamma * (||x-c||/r)^2)
  tanh          : np.tanh(a)
  sinsq         : np.power(np.sin(a), 2.0)
  tribas        : np.clip(1.0 - np.fabs(a), 0.0, 1.0)
  hardlim       : np.array(a > 0.0, dtype=float)

     where x   : input pattern
           a   : dot_product(x, c) + b
           c,r : randomly generated components

Label Legend:
  ELM(10,tanh)      :10 tanh units
  ELM(10,tanh,LR)   :10 tanh units, LogisticRegression
  ELM(10,sinsq)     :10 sin*sin units
  ELM(10,tribas)    :10 tribas units
  ELM(10,hardlim)   :10 hardlim units
  ELM(20,rbf(0.1))  :20 rbf units gamma=0.1

"""

# Code source: Gael Varoqueux
#              Andreas Mueller
# Modified for Documentation merge by Jaques Grobler
# Modified for Extreme Learning Machine Classifiers by David Lambert
# Modified for Sklearn-Extensions by Will McGinnis
# License: BSD

import numpy as np
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn_extensions.extreme_learning_machines.elm import GenELMClassifier
from sklearn_extensions.extreme_learning_machines.random_layer import RBFRandomLayer, MLPRandomLayer

print(__doc__)


def make_datasets():
    """

    :return:
    """

    return [make_moons(n_samples=200, noise=0.3, random_state=0),
            make_circles(n_samples=200, noise=0.2, factor=0.5, random_state=1),
            make_linearly_separable()]


def make_classifiers():
    """

    :return:
    """

    names = ["ELM(10,tanh)", "ELM(10,tanh,LR)", "ELM(10,sinsq)", "ELM(10,tribas)", "ELM(hardlim)", "ELM(20,rbf(0.1))"]

    nh = 10

    # pass user defined transfer func
    sinsq = (lambda x: np.power(np.sin(x), 2.0))
    srhl_sinsq = MLPRandomLayer(n_hidden=nh, activation_func=sinsq)

    # use internal transfer funcs
    srhl_tanh = MLPRandomLayer(n_hidden=nh, activation_func='tanh')
    srhl_tribas = MLPRandomLayer(n_hidden=nh, activation_func='tribas')
    srhl_hardlim = MLPRandomLayer(n_hidden=nh, activation_func='hardlim')

    # use gaussian RBF
    srhl_rbf = RBFRandomLayer(n_hidden=nh*2, rbf_width=0.1, random_state=0)
    log_reg = LogisticRegression()

    classifiers = [GenELMClassifier(hidden_layer=srhl_tanh),
                   GenELMClassifier(hidden_layer=srhl_tanh, regressor=log_reg),
                   GenELMClassifier(hidden_layer=srhl_sinsq),
                   GenELMClassifier(hidden_layer=srhl_tribas),
                   GenELMClassifier(hidden_layer=srhl_hardlim),
                   GenELMClassifier(hidden_layer=srhl_rbf)]

    return names, classifiers


def make_linearly_separable():
    """

    :return:
    """

    X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2, random_state=1, n_clusters_per_class=1)
    rng = np.random.RandomState(2)
    X += 2 * rng.uniform(size=X.shape)
    return (X, y)


if __name__ == '__main__':
    # generate some datasets
    datasets = make_datasets()
    names, classifiers = make_classifiers()

    # iterate over datasets
    for idx, ds in enumerate(datasets):
        # pre-process dataset, split into training and test part
        X, y = ds
        X = StandardScaler().fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.4, random_state=0)
        y_test = y_test.reshape(-1, )
        y_train = y_train.reshape(-1, )

        # iterate over classifiers
        print('Dataset: %s' % (idx, ))
        for name, clf in zip(names, classifiers):
            clf.fit(X_train, y_train)
            score = clf.score(X_test, y_test)
            print('Model %s score: %s' % (name, score))

