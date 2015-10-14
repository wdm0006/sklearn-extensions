"""
This is an extremely simple example using some generated data to demonstrate how to write an example for
sklearn-extensions. This can be used as a template for writing other examples.  Note that these aren't tests, just
quick and simple examples of how something might be used.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits
from sklearn.metrics import classification_report

# first grab a dataset
digits = load_digits()
X_digits = digits.data
y_digits = digits.target

# then instantiate the classifier
clf = LogisticRegression()

# fit it
clf.fit(X_digits, y_digits)

# apply it (reusing the same data for an example)
y = clf.predict(X_digits)

# and print some info about it (should be extremely over-fit)
print(classification_report(y_digits, y))
