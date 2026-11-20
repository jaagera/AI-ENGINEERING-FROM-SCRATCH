> Every model error comes from one of three sources: bias, variance, or noise. You can only control the first two.

# Practical rule: if your base model has high variance (deep trees, high-degree polynomials), use bagging. If your base model has high bias (shallow stumps, simple linear models), use boosting.

* mean_pred is E[f^(x)]E[f^​(x)] estimated from bootstrap samples
* bias_sq is the squared gap between average prediction and truth
* variance is the average spread of predictions across bootstrap samples
* total_error should approximately equal bias2+variance+noisebias2+variance+noise

*** 
This sweeps regularization strength for a fixed model complexity. You will see the same bias-variance tradeoff: low alpha means high variance, high alpha means high bias.
***

# Putting It All Together: A Complete Diagnostic Workflow
In practice, you run these diagnostics in sequence:

    1. Train your model. Compute train and test error.
    2. If both are high: you have a bias problem. Skip to step 4.
    3. If train is low but test is high: you have a variance problem. Generate a learning curve to see if more data will help. If not, regularize.
    4. Generate a validation curve sweeping your main complexity parameter. Find the sweet spot.
    5. At the sweet spot, generate a learning curve. If the gap is still large, you need more data or regularization.
    6. Try Ridge/Lasso with different alpha values using cross_val_score. Pick the alpha where cross-validated error is lowest.

*** This takes 10-15 minutes of compute for most tabular datasets and saves hours of guessing.

At low alpha, the degree-15 polynomial is nearly unconstrained. Variance dominates because the model chases noise in each bootstrap sample. At high alpha, the penalty is so strong that the model effectively becomes a near-constant function. Bias dominates. The optimal alpha sits between these extremes.

This is the same U-curve from varying polynomial degree, but controlled by a continuous knob instead of a discrete one. In practice, regularization is the preferred way to control the tradeoff because it allows fine-grained control without changing the feature set. ***

# N.B: To learn to split a model’s error into three sources, and to use that split to decide what to try next: a more complex model, a simpler one, more data, or better features.

```
1. Bias: systematic error

Train the same model on many different training sets and average its predictions. Bias is the gap between that average and the truth. High bias means the model is too rigid: a straight line fit to a parabola misses the curve however much data you give it. This is underfitting. Train error high, test error high, small gap.

2. Variance: sensitivity to the training set

Variance is how much the predictions change from one training set to another. A degree-20 polynomial threads every training point, then swings wildly between them, and it would swing differently on a different sample. This is overfitting. Train error low, test error high, large gap.

3. The decomposition

At a point x, under squared loss:

Expected error = Bias² + Variance + Noise (σ²)

Bias² = (average prediction − true value)²
Variance = how spread out the predictions are around their own average
Noise = randomness in the data itself. No model can beat σ².

```
