> High-dimensional data has structure. You find it by looking from the right angle.

# AIM: To learn how to squash data with hundreds of features down to a handful, while keeping the structure that matters.

* Choosing the number of components
  Three strategies:

    . Threshold. Keep enough components to explain 90-95% of the variance.
    . Elbow method. Plot explained variance per component. Look for a sharp drop-off.
    . Downstream performance. Use PCA as preprocessing. Sweep kk and measure your model's accuracy. The best kk is wherever accuracy plateaus.

    > t-SNE (t-Distributed Stochastic Neighbor Embedding) is a non-linear dimensionality reduction technique used in machine learning and programming to visualize complex, high-dimensional datasets in 2D or 3D scatter plots. It's for visualization as well

* Uniform Manifold Approximation and Projection (UMAP) works similarly to t-SNE but with two advantages:

    # Faster. It uses approximate nearest-neighbor graphs instead of computing all pairwise distances.
    # Better global structure. The relative positions of clusters in the output tend to be more meaningful than in t-SNE.

> Principal Component Analysis (PCA) is a linear dimensionality reduction technique that transforms high-dimensional data into a smaller set of uncorrelated variables—called principal components—while retaining as much of the data's original variance as possible.

* Why eigenvectors work here: the covariance matrix is symmetric, so its eigenvectors are perpendicular, giving a clean new coordinate system.

> Goal	                                                Use
Preprocessing or compression before a model	            PCA
Quick look at the data	                                PCA
Pretty 2D plot of cluster structure (small data)	    t-SNE
2D plot of big data	                                    UMAP

