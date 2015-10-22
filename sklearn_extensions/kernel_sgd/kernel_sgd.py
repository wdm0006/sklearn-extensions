# Mathieu Blondel, May 2012
# Modified by Will McGinnis for sklearn-extensions
# License: BSD 3 clause

import numpy as np
from sklearn.base import BaseEstimator


def euclidean_distances(X, Y=None, squared=False):
    """

    :param X:
    :param Y:
    :param Y_norm_squared:
    :param squared:
    :return:
    """

    XX = np.sum(X * X, axis=1)[:, np.newaxis]
    YY = np.sum(Y ** 2, axis=1)[np.newaxis, :]
    distances = np.dot(X, Y.T)
    distances *= -2
    distances += XX
    distances += YY
    np.maximum(distances, 0, distances)

    if X is Y:
        # Ensure that distances between vectors and themselves are set to 0.0.
        # This may not be the case due to floating point rounding errors.
        distances.flat[::distances.shape[0] + 1] = 0.0

    return distances if squared else np.sqrt(distances)


class GaussianKernel(object):
    """

    """
    def __init__(self, gamma=1.0):
        """

        :param gamma:
        :return:
        """

        self.gamma = gamma

    def compute(self, X, Y):
        """

        :param X:
        :param Y:
        :return:
        """

        K = euclidean_distances(X, Y, squared=True)
        K *= -self.gamma

        # exponentiate K in-place
        np.exp(K, K)

        return K


class HingeLoss(object):
    """

    """
    def __init__(self, threshold=1):
        """

        :param threshold:
        :return:
        """

        # a.k.a geometrical margin
        self.threshold = threshold

    def get_update(self, p, y):
        """

        :param p:
        :param y:
        :return:
        """

        z = p * y
        if z <= self.threshold:
            return y

        return 0.0


class LogLoss(object):
    """

    """
    def get_update(self, p, y):
        """

        :param p:
        :param y:
        :return:
        """

        z = p * y

        # approximately equal and saves the computation of the log
        if z > 18.0:
            return np.exp(-z) * y
        if z < -18.0:
            return y

        return y / (np.exp(z) + 1.0)

class SquaredLoss(object):
    """

    """
    def get_update(self, p, y):
        """

        :param p:
        :param y:
        :return:
        """

        return -p + y


class KernelSGD(BaseEstimator):
    """
    Note: eta (learning rate) and lmbda (regularization) have no
    impact if loss=HingeLoss(threshold=0).
    """
    def __init__(self, eta=1, lmbda=0.01, kernel=GaussianKernel(), loss=HingeLoss(), n_iter=1):
        """

        :param eta:
        :param lmbda:
        :param kernel:
        :param loss:
        :param n_iter:
        :return:
        """

        self.eta = eta
        self.lmbda = lmbda
        self.kernel = kernel
        self.loss = loss
        self.n_iter = n_iter
        self.alpha = None
        self.sv = None

    def fit(self, X, y):
        """

        :param X:
        :param y:
        :return:
        """
        n_samples, n_features = X.shape
        self.alpha = np.zeros(n_samples, dtype=np.float64)

        # Gram matrix
        K = self.kernel.compute(X, X)

        for t in range(self.n_iter):
            for i in range(n_samples):
                pred = np.dot(K[:, i], self.alpha)

                # Update wrt to loss term.
                update = self.loss.get_update(pred, y[i])
                if update != 0:
                    self.alpha[i] += update * self.eta

                # Update wrt to regularization term.
                self.alpha *= (1 - self.eta * self.lmbda)

        # Support vectors
        sv = self.alpha != 0

        self.alpha = self.alpha[sv]
        self.sv = X[sv]

        print("%d support vectors out of %d points" % (len(self.alpha), n_samples))

    def decision_function(self, X):
        if self.sv is None:
            raise Exception('Fit must be called before decision_function can be generated')

        K = self.kernel.compute(X, self.sv)

        return np.dot(K, self.alpha)

    def predict(self, X):
        """

        :param X:
        :return:
        """

        if self.sv is None:
            raise Exception('Fit must be called before predictions can be generated')

        return np.sign(self.decision_function(X))
