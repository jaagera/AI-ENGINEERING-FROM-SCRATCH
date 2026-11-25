> Normal is easy to define. Abnormal is whatever doesn't fit.

# Types of Anomalies
Not all anomalies are the same:

    1. Point anomalies. A single data point that is unusual regardless of context. A temperature reading of 500 degrees. A transaction of $50,000 from an account that normally spends $50.
    2. Contextual anomalies. A data point that is unusual given its context. A temperature of 90 degrees is normal in summer, anomalous in winter. Same value, different context.
    3. Collective anomalies. A sequence of data points that is unusual as a group, even though each individual point might be normal. Five login failures is normal. Fifty in a row is a brute-force attack.

# An anomaly is something that deviates from what is standard, normal, or expected.#

```
The Unsupervised Framing

In standard classification, you have labels for both classes. In anomaly detection, you typically have one of three situations:

    1. Fully unsupervised. No labels at all. You fit the detector on all data and hope anomalies are rare enough not to corrupt the "normal" model.
    2. Semi-supervised. You have a clean dataset of normal data only. You fit on this clean set and score everything else. This is the strongest setup when possible.
    3. Weakly supervised. You have a few labeled anomalies. Use them for evaluation, not training. Train unsupervised, then measure precision/recall on the labeled subset.
```

<The Unsupervised Framing

In standard classification, you have labels for both classes. In anomaly detection, you typically have one of three situations:

    - Fully unsupervised. No labels at all. You fit the detector on all data and hope anomalies are rare enough not to corrupt the "normal" model.
    - Semi-supervised. You have a clean dataset of normal data only. You fit on this clean set and score everything else. This is the strongest setup when possible.
    - Weakly supervised. You have a few labeled anomalies. Use them for evaluation, not training. Train unsupervised, then measure precision/recall on the labeled subset.

The key insight: anomaly detection is fundamentally different from classification. You are modeling the distribution of normal data, not the decision boundary between two classes.

<Supervised vs Unsupervised: The Tradeoff

If you do have labeled anomalies, should you use them for training (supervised classification) or for evaluation only (unsupervised detection)?

Supervised (treat as classification):

    - Catches the exact types of anomalies you have seen before
    - Higher precision on known anomaly types
    - Misses novel anomaly types entirely
    - Requires retraining when new anomaly types emerge
    - Needs enough anomaly examples (often too few)

Unsupervised (model normal, flag deviations):

    - Catches any deviation from normal, including novel types
    - Does not require labeled anomalies
    - Higher false positive rate (not everything unusual is bad)
    - More robust to distribution shift

> Key hyperparameters(settings you implement while training your model):

    1. n_estimators: Number of trees. 100 is usually enough. More trees give more stable scores but slower computation.
    2. max_samples: Number of samples per tree. 256 is the default in the original paper. Smaller values make individual trees less accurate but increase diversity. The subsampling is what makes Isolation Forest fast -- each tree sees a small fraction of the data.
    3. contamination: Expected fraction of anomalies. Used only for setting the threshold. Does not affect the scores themselves.

>Local Outlier Factor (LOF)
LOF compares the local density around a point to the density around its neighbors. A point in a sparse region surrounded by dense regions is anomalous.

How it works:
    For each point, find its kk nearest neighbors
    Compute the local reachability density (how dense is the neighborhood)
    Compare each point's density to its neighbors' densities
    If a point has much lower density than its neighbors, it is an outlier

