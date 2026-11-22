> Hyperparameters are the knobs you turn before training starts. Turning them well is the difference between a mediocre model and a great one.

* Why random beats grid (Bergstra & Bengio, 2012):

    1. Most hyperparameters have low effective dimensionality. Only 1-2 of 6 hyperparameters usually matter for a given problem.
    2. Grid search wastes evaluations on unimportant dimensions.
    3. Random search covers the important dimensions more densely for the same budget.
    4. At 60 random trials, you have a 95% chance of finding a point within 5% of the optimum (if one exists in the search space).

# Bayesian optimization uses past evaluations to decide where to search next.

***
Hyperparameter Importance

Not all hyperparameters matter equally. Research on random forests (Probst et al., 2019) and gradient boosting shows consistent patterns:

High importance:

    * Learning rate (always tune first)
    * Number of estimators / epochs (use early stopping instead of tuning)
    * Regularization strength

Medium importance:

    * Max depth / number of layers
    * Min samples per leaf / weight decay
    * Subsample ratio

Low importance:

    * Max features (for random forests)
    * Specific activation function choice
    * Batch size (within reasonable range)
***

# Optuna is the recommended library for serious hyperparameter tuning. It supports pruning, distributed search, and visualization out of the box.

```
Common Mistakes in Hyperparameter Tuning

- Data leakage through preprocessing. If you fit a scaler on the full dataset before cross-validation, information from the validation fold leaks into training. Always put preprocessing inside a Pipeline so it is fit only on the training fold.

- Overfitting to the validation set. Running thousands of trials effectively trains on the validation set. Use nested cross-validation for final performance estimates, or hold out a separate test set that you never touch during tuning.

- Searching too narrow a range. If your best value is at the boundary of your search space, you have not searched widely enough. The optimal value might be outside your range. Always check if the best parameters are at the edges.

- Ignoring interaction effects. Learning rate and number of estimators interact strongly in boosting. A low learning rate needs more estimators. Tuning them independently gives worse results than tuning them together.

- Not using early stopping for iterative models. For gradient boosting and neural networks, set n_estimators or epochs to a high value and use early stopping. This is strictly better than tuning the number of iterations as a hyperparameter.

```