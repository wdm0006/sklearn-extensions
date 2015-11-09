Extreme Learning Machines
=========================

Usage
-----

The extreme learning machines module ships with a large number of estimators and helper classes for building these
estimators:

 * extreme_learning_machines.ELMRegressor()
 * extreme_learning_machines.ELMClassifier()
 * extreme_learning_machines.GenELMRegressor()
 * extreme_learning_machines.GenELMClassifier()
 * extreme_learning_machines.RandomLayer()
 * extreme_learning_machines.GRBFRandomLayer()
 * extreme_learning_machines.RBFRandomLayer()
 * extreme_learning_machines.MLPRandomLayer()

For a detailed example, see below.

Examples
--------

An example comparing various ELM models.

.. code-block:: python

    import numpy as np
    from sklearn.datasets import make_moons, make_circles, make_classification
    from sklearn.preprocessing import StandardScaler
    from sklearn.cross_validation import train_test_split
    from sklearn.linear_model import LogisticRegression

    from sklearn_extensions.extreme_learning_machines.elm import GenELMClassifier
    from sklearn_extensions.extreme_learning_machines.random_layer import RBFRandomLayer, MLPRandomLayer


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

Which yields the output:

.. code-block:: bash

    Dataset: 0
    Model ELM(10,tanh) score: 0.9125
    Model ELM(10,tanh,LR) score: 0.8875
    Model ELM(10,sinsq) score: 0.7875
    Model ELM(10,tribas) score: 0.8
    Model ELM(hardlim) score: 0.825
    Model ELM(20,rbf(0.1)) score: 0.9

    Dataset: 1
    Model ELM(10,tanh) score: 0.8375
    Model ELM(10,tanh,LR) score: 0.7125
    Model ELM(10,sinsq) score: 0.9
    Model ELM(10,tribas) score: 0.725
    Model ELM(hardlim) score: 0.7875
    Model ELM(20,rbf(0.1)) score: 0.9375

    Dataset: 2
    Model ELM(10,tanh) score: 0.9125
    Model ELM(10,tanh,LR) score: 0.875
    Model ELM(10,sinsq) score: 0.85
    Model ELM(10,tribas) score: 0.8125
    Model ELM(hardlim) score: 0.9
    Model ELM(20,rbf(0.1)) score: 0.9125


Third Party Docs
----------------

The original unmodified version of this module's code can be found here: `Extreme Learning Machines <https://github.com/dclambert/Python-ELM>`_