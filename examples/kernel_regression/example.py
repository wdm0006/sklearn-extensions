"""
Example from: https://raw.githubusercontent.com/jmetzen/kernel_regression/master/plot_kernel_regression.py

========================================================================
Comparison of kernel regression (KR) and support vector regression (SVR)
========================================================================

Toy example of 1D regression using kernel regression (KR) and support vector
regression (SVR). KR provides an efficient way of selecting a kernel's
bandwidth via leave-one-out cross-validation, which is considerably faster
that an explicit grid-search as required by SVR. The main disadvantages are
that it does not support regularization and is not robust to outliers.
"""

print(__doc__)

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