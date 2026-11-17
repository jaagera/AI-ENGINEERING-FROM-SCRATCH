> No labels, no teacher. The algorithm finds structure on its own.

```Unsupervised learning finds patterns without being told what to look for. It groups similar data points, discovers hidden structures, and surfaces anomalies(i.e deviate from what is standard they are also called "OUTLIERS"). 
```


***
K-Means: The Workhorse

K-Means partitions data into exactly K clusters. Each cluster has a centroid (its center of mass), and every point belongs to the nearest centroid.

Lloyd's algorithm:

    Pick K random points as initial centroids
    Assign each data point to the nearest centroid
    Recompute each centroid as the mean of its assigned points
    Repeat steps 2-3 until assignments stop changing
***

> Two parameters:

    eps: the radius of a neighborhood
    min_samples: the minimum number of points needed to form a dense region

> Three types of points:

    Core point: has at least min_samples points within eps distance
    Border point: within eps of a core point but not itself a core point
    Noise point: neither core nor border. These are outliers.

** 
Clustering naturally supports anomaly detection:

    K-Means: points far from any centroid are anomalies
    DBSCAN: noise points are anomalies by definition
    GMM: points with low probability under all Gaussians are anomalies
**


