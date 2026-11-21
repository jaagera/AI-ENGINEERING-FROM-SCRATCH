> A group of weak learners, combined correctly, becomes a strong learner. This is not a metaphor. It is a theorem.

If all models make the same errors, combining them helps nothing. Ensembles work because they produce diverse models through:

    * Different training subsets (bagging)
    * Different feature subsets (random forests)
    * Sequential error correction (boosting)
    * Different model families (stacking)

***
Bagging (Bootstrap Aggregating)

Bagging creates diversity by training each model on a different bootstrap sample of the training data.
***

```
AdaBoost
AdaBoost (Adaptive Boosting) was the first practical boosting algorithm. It works with any base learner, typically decision stumps (depth-1 trees).

```
....
XGBoost: Why It Dominates Tabular Data
XGBoost (eXtreme Gradient Boosting) is gradient boosting with engineering optimizations that make it fast, accurate, and resistant to overfitting:

1. Regularized objective: L1 and L2 penalties on leaf weights prevent individual trees from being too confident
2. Second-order approximation: Uses both first and second derivatives of the loss, giving better split decisions
3. Sparsity-aware splits: Handles missing values natively by learning the best direction for missing data at each split
4. Column subsampling: Like random forests, samples features at each split for diversity
Weighted quantile sketch: Efficiently finds split points for continuous features on distributed data
5. Cache-aware block structure: Memory layout optimized for CPU cache lines
For tabular data, XGBoost (and its successor LightGBM) consistently outperforms neural networks. This is not changing anytime soon. If your data fits in a table with rows and columns, start with gradient boosting.
.....
