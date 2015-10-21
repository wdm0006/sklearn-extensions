"""
Non-Negative Garotte implementation with the scikit-learn
"""

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Jaques Grobler (__main__ script) <jaques.grobler@inria.fr>
#
# Modified by Will McGinnis for sklearn-extensions
# License: BSD Style.

import numpy as np

from sklearn.linear_model.base import LinearModel
from sklearn.linear_model import LinearRegression, Lasso, lars_path


def non_negative_garotte(X, y, alpha, tol=0.001):
    """

    :param X:
    :param y:
    :param alpha:
    :param tol:
    :return:
    """

    coef_ols = LinearRegression(fit_intercept=False).fit(X, y).coef_

    X = X * coef_ols[np.newaxis, :]
    shrink_coef = Lasso(alpha=alpha, fit_intercept=False,
                        positive=True, normalize=False,
                        tol=tol).fit(X, y).coef_

    # Shrunken betas
    coef = coef_ols * shrink_coef

    # Residual Sum of Squares
    rss = np.sum((y - np.dot(X, coef)) ** 2)
    return coef, shrink_coef, rss


def non_negative_garotte_path(X, y):
    """

    :param X:
    :param y:
    :return:
    """

    coef_ols = LinearRegression(fit_intercept=False).fit(X, y).coef_

    X = X * coef_ols[np.newaxis, :]

    # Use lars_path even if it does not support positivity (much faster)
    _, _, shrink_coef_path = lars_path(X, y, method='lasso')
    coef_path = shrink_coef_path * coef_ols[:, None]

    # Residual Sum of Squares
    rss_path = np.sum((y[:, None] - np.dot(X, coef_path)) ** 2, axis=0)

    return coef_path, shrink_coef_path, rss_path


class NonNegativeGarrote(LinearModel):
    """
    NonNegativeGarrote

    Ref:
    Breiman, L. (1995), "Better Subset Regression Using the Nonnegative
    Garrote," Technometrics, 37, 373-384. [349,351]
    """
    def __init__(self, alpha=0.01, fit_intercept=True, tol=1e-4, normalize=False, copy_X=True):
        """

        :param alpha:
        :param fit_intercept:
        :param tol:
        :param normalize:
        :param copy_X:
        :return:
        """

        self.alpha = alpha
        self.fit_intercept = fit_intercept
        self.tol = tol
        self.normalize = normalize
        self.copy_X = copy_X

    def fit(self, X, y):
        """

        :param X:
        :param y:
        :return:
        """

        X, y, X_mean, y_mean, X_std = self._center_data(X, y, self.fit_intercept, self.normalize, self.copy_X)
        self.coef_, self.shrink_coef_, self.rss_ = non_negative_garotte(X, y, self.alpha)
        self._set_intercept(X_mean, y_mean, X_std)