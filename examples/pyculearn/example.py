"""
This is an extremely simple example using the sample data provided in the pyculiarity and pyculearn projects themselves.
"""


from sklearn_extensions.pyculearn import PycuAnom
import pandas as pd

raw_data = pd.read_csv('midnight_test_data.csv')
tf = PycuAnom(datetimestr_col='date')
out = tf.fit_transform(raw_data)
print(out.head(10))