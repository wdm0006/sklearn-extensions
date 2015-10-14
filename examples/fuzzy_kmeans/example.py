"""
An example of the 3 algorithms included in fuzzy_kmeans, code modified from:

    https://gist.github.com/mblondel/1451300
    Copyright Mathieu Blondel December 2011
    License: BSD 3 clause

"""

import numpy as np
from sklearn_extensions.fuzzy_kmeans import KMedians, FuzzyKMeans, KMeans
from sklearn.datasets.samples_generator import make_blobs

np.random.seed(0)

batch_size = 45
centers = [[1, 1], [-1, -1], [1, -1]]
n_clusters = len(centers)
X, labels_true = make_blobs(n_samples=1200, centers=centers, cluster_std=0.3)

kmeans = KMeans(k=3)
kmeans.fit(X)

kmedians = KMedians(k=3)
kmedians.fit(X)

fuzzy_kmeans = FuzzyKMeans(k=3, m=2)
fuzzy_kmeans.fit(X)

print('KMEANS')
print(kmeans.cluster_centers_)

print('KMEDIANS')
print(kmedians.cluster_centers_)

print('FUZZY_KMEANS')
print(fuzzy_kmeans.cluster_centers_)