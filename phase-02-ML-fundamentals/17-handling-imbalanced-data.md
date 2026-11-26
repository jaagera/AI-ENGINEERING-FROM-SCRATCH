> When 99% of your data is "normal," accuracy is a lie.

```
Sampling Strategies Compared

Random Oversampling: duplicate minority samples to match majority count.

    Pros: simple, no information loss
    Cons: exact duplicates cause overfitting, increases training time

Random Undersampling: remove majority samples to match minority count.

    Pros: fast training, simple
    Cons: throws away potentially useful majority data, higher variance

SMOTE: create synthetic minority samples via interpolation.

    Pros: generates new data points, reduces overfitting compared to random oversampling
    Cons: can create noisy samples near the decision boundary, does not account for majority class distribution

```

# Threshold Tuning

Most classifiers output a probability. The default threshold is 0.5: if P(positive)≥0.5P(positive)≥0.5, predict positive. But 0.5 is arbitrary. When classes are imbalanced, the optimal threshold is usually much lower.

The process:

    1. Train a model
    2. Get predicted probabilities on the validation set
    3. Sweep thresholds from 0.0 to 1.0
    4. Compute F1 (or your chosen metric) at each threshold
    5. Pick the threshold that maximizes your metric


# Sampling strategies
>Strategy              |     What changes                 |  Risk                       |    When
Random oversampling    |    Minority duplicated           | Overfitting                 |   Small data, moderate imbalance
Random undersampling   |    Majority removed              | Throws away information     |   Large data, want speed
SMOTE                  |    Synthetic minority added      | Noise near the boundary     |   Moderate imbalance, enough minority points for k-NN

