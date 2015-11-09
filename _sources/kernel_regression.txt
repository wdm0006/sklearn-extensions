Kernel Regression
=================

Usage
-----

The kernel regression module can be imported as:

.. code-block:: python

    import sklearn_extensions as ske

    mdl = ske.kernel_regression.KernelRegression()
    mdl.fit_predict(X, y)

Examples
--------

.. code-block:: python

    import time
    import numpy as np
    from sklearn.svm import SVR
    from sklearn.grid_search import GridSearchCV
    from sklearn_extensions.kernel_regression import KernelRegression

    np.random.seed(0)

    # Generate sample data
    X = np.sort(5 * np.random.rand(100, 1), axis=0)
    y = np.sin(X).ravel()

    # Add noise to targets
    y += 0.5 * (0.5 - np.random.rand(y.size))

    # Fit regression models
    svr = GridSearchCV(SVR(kernel='rbf'), cv=5, param_grid={"C": [1e-1, 1e0, 1e1, 1e2], "gamma": np.logspace(-2, 2, 10)})

    kr = KernelRegression(kernel="rbf", gamma=np.logspace(-2, 2, 10))
    t0 = time.time()
    y_svr = svr.fit(X, y).predict(X)

    print("SVR complexity and bandwidth selected and model fitted in %.3f s" % (time.time() - t0))

    t0 = time.time()
    y_kr = kr.fit(X, y).predict(X)

    print("KR including bandwith fitted in %.3f s" % (time.time() - t0))

Which yields the output:

.. code-block:: python

    SVR complexity and bandwidth selected and model fitted in 0.660 s
    KR including bandwith fitted in 0.005 s


Third Party Docs
----------------

The original unmodified version of this module's code is from a github repo that can be found at: `Kernel Regression <https://github.com/jmetzen/kernel_regression>`_