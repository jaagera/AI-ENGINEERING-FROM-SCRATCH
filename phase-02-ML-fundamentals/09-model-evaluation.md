> A model is only as good as the way you measure it.

*** Model evaluation is where most ML projects go wrong. The wrong metric makes a bad model look good. The wrong split let6s a model cheat. The wrong comparison makes a pick the worse model. Gettting evaluation right is not optional. It is the differecne between a model that works in prodcution and one that fails the moment it sees real data.***

# Three splits, three purposes:

    1. Training set: the model learns from this data. It sees these examples during training.
    2. Validation set: used to tune hyperparameters and select between models. The model never trains on this data, but your decisions are influenced by it.
    3. Test set: touched exactly once, at the very end, to report final performance. If you look at test performance and then go back to change your model, it is no longer a test set. It has become a second validation set.

```
COMMON EVALUATION MISTAKES 
* Data Leakage: information from the test set leaks into training. Examples: fitting a scaler on the full dataset before splitting, including future data in time series prediction, using a feature that is derived from the target. Always split first, then preproces.

Class imbalance: 99% of transactions are legitimate, 1% are fraud. A model that always predicts "legitmate" gets 99% accuracy. Use precision, recall, F1, or AUC-ROC instead.

Wrong metric: optimizing accuracy when you should optimize recall (medical diagnosis), or optimizing RMSE when your data has heavy outliers (use MAE instead).

Not using stratified splits: with imbalanced data, a random split might put very few minority samples in the validation fold, giving unstable estimates.

Testing too often: Every time you look at test performance and adjust, you overfit to the test set. The test set is single-use. 
```

# NOTE: MEAN ABSOLUTE ERROR: Is used when an outlier is heavy.