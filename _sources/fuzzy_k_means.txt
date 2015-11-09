Fuzzy K-Means
=============

Usage
-----

The fuzzy k-means module has 3 seperate models that can be imported as:

.. code-block:: python

    import sklearn_extensions as ske

    mdl = ske.fuzzy_kmeans.FuzzyKMeans()
    mdl.fit_predict(X, y)

    mdl = ske.fuzzy_kmeans.KMeans()
    mdl.fit_predict(X, y)

    mdl = ske.fuzzy_kmeans.KMedians()
    mdl.fit_predict(X, y)

Examples
--------

.. code-block:: python

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

Yields the result:

.. code-block:: python

    KMEANS
    [[ 0.74279904  0.94377717]
     [ 1.22177014  1.00196511]
     [-0.00873034 -0.99593489]]
    KMEDIANS
    [[ 0.99538235 -1.01070379]
     [ 0.96275935  0.98959938]
     [-0.97974863 -0.99788949]]
    FUZZY_KMEANS
    [[ 0.98642164 -1.0000844 ]
     [ 0.97111065  0.99339691]
     [-0.98862482 -0.99082696]]


Third Party Docs
----------------

The original unmodified version of this module's code can be found here: `Fuzzy K-Means <https://gist.github.com/mblondel/1451300>`_