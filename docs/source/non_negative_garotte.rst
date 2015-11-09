Non Negative Garotte
====================

Usage
-----

The non-negative-garotte module can be imported as:

.. code-block:: python

    import sklearn_extensions as ske

    mdl = ske.non_negative_garotte.NonNegativeGarotte()
    mdl.fit_predict(X, y)


Examples
--------

.. code-block:: python

    import numpy as np
    from sklearn import datasets
    from sklearn_extensions.non_negative_garotte import NonNegativeGarrote

    # Load the diabetes dataset
    diabetes = datasets.load_diabetes()


    # Use only one feature
    diabetes_X = diabetes.data[:, np.newaxis]
    diabetes_X_temp = diabetes_X[:, :, 2]

    # Split the data into training/testing sets
    diabetes_X_train = diabetes_X_temp[:-20]
    diabetes_X_test = diabetes_X_temp[-20:]

    # Split the targets into training/testing sets
    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]

    # Create linear regression object
    regr = NonNegativeGarrote(alpha=0.1, fit_intercept=True, tol=1e-6, normalize=True)

    # Train the model using the training sets
    regr.fit(diabetes_X_train, diabetes_y_train)

    # The coefficients
    print('Coefficients: \n', regr.coef_)

    # The mean square error
    print("Residual sum of squares: %.2f" % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))

Which yields the output:

.. code-block:: python

    Coefficients:
     [ 938.19079764]
    Residual sum of squares: 2548.13


Third Party Docs
----------------

The original unmodified version of this code can be found at: `Non-negative Garotte <https://gist.github.com/agramfort/2351057>`_