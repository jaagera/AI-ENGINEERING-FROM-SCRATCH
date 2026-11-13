TOPIC: LOGISTIC REGRESSION

> Logistic regression bends a straight line into an S-curve to answer yes-or-no questions with probabilities.

*** The sigmoid function is an S-shaped mathematical curve that maps any real-valued number into a bounded range between 0 and 1. ***

> Classification needs a function that:

    * Outputs values between 0 and 1 (probabilities)
    * Creates a sharp transition (a decision boundary)
    * Is not distorted by outliers far from the boundary

* Binary Cross-Entropy Loss

You cannot use MSE for logistic regression. MSE with a sigmoid creates a non-convex cost surface with many local minima. Instead, use binary cross-entropy (log loss).

> The ROC curve (Receiver Operating Characteristic curve) is a graph showing the performance of a binary classification model across all classification thresholds, while AUC (Area Under the Curve) summarizes that performance into a single score between 0 and 1.

```
Classification needs a function that:
- Outputs values between 0 and 1 (probabilities)
- Creates a sharp transition (a decision boundary)
- Is not distorted by outliers far from the boundary

```

**Confusion Matrix**:

| | Predicted Positive | Predicted Negative |
|---|---|---|
| Actually Positive | True Positive (TP) | False Negative (FN) |
| Actually Negative | False Positive (FP) | True Negative (TN) |