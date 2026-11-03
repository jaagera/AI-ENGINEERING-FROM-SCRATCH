> Your distance function defines what "similar" means. Choose wrong and everything downstream breaks.

* A norm measures the "size" of a vector. Every distance function between two vectors can be written as the norm of their difference: d(a,b)=∥a−b∥d(a,b)=∥a−b∥. So understanding norms is understanding distances.

> When to use L1:

    High-dimensional sparse data (text features, one-hot encodings)
    When you want robustness to outliers (a single huge difference does not dominate)
    Feature selection problems (L1 regularization promotes sparsity)

> When to use L2:

    Low-to-medium dimensional continuous data
    When the feature scales are comparable
    Physical distances (spatial data, sensor readings)
    Image similarity at the pixel level

> When to use L-infinity:

    When the worst-case deviation in any single dimension matters
    Game boards (a king in chess moves in L-infinity: one step in any direction costs 1)
    Manufacturing tolerances (every dimension must be within spec)

> When to use cosine similarity:

    Text similarity (TF-IDF vectors, word embeddings, sentence embeddings)
    Any domain where magnitude is noise and direction is signal
    Recommendation systems (user preference vectors)
    Embedding search (vector databases almost always use cosine or dot product)

* When to use Mahalanobis distance:

    Outlier detection (points with large Mahalanobis distance from the mean are outliers)
    Classification when features have different scales and correlations
    When you have enough data to estimate a reliable covariance matrix
    Quality control in manufacturing (multivariate process monitoring)

> Jaccard similarity measures overlap between two sets. 

When to use Jaccard:

    Comparing sets of tags, categories, or features
    Document similarity based on word presence (not frequency)
    Near-duplicate detection (MinHash approximation of Jaccard)
    Comparing binary feature vectors (presence/absence data)
    Evaluating segmentation models (Intersection over Union = Jaccard)

When you see KL divergence:

    VAEs (the KL term in the ELBO pushes the latent distribution toward a prior)
    Knowledge distillation (student tries to match teacher's distribution)
    RLHF (the KL penalty keeps the fine-tuned model close to the base model)
    Policy gradient methods (constraining policy updates)

* Why Wasserstein matters:

    It is a true metric (symmetric, satisfies triangle inequality)
    It provides gradients even when distributions do not overlap (KL divergence goes to infinity)
    This property made it central to Wasserstein GANs (WGANs), which solved the training instability of original GANs

* When to use Wasserstein:

    GAN training (WGAN, WGAN-GP)
    Comparing distributions that may not overlap
    Optimal transport problems
    Image retrieval (comparing color histograms)

> HNSW (Hierarchical Navigable Small World) is the dominant algorithm in modern vector databases.

### Wasserstein Distance (Earth Mover's Distance)

Wasserstein distance measures the minimum "work" needed to transform one probability distribution into another. 

* Why Wasserstein matters:
- It is a true metric (symmetric, satisfies triangle inequality)
- It provides gradients even when distributions do not overlap (KL divergence goes to infinity)
- This property made it central to Wasserstein GANs (WGANs), which solved the training instability of original GANs

* When to use Wasserstein:
- GAN training (WGAN, WGAN-GP)
- Comparing distributions that may not overlap
- Optimal transport problems
- Image retrieval (comparing color histograms)