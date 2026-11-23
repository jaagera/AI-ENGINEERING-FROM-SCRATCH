> A model is not a product. A pipeline is. The pipeline is everything from raw data to deployed prediction, and every step must be reproducible.

# What a Pipeline Is
A pipeline is an ordered sequence of data transformations followed by a model. Each step takes the output of the previous step as input.

```
Data leakage happens when information from the test set or future data contaminates training. Pipelines prevent the most common forms.
```

> DVC stores the actual data in remote storage (S3, GCS, Azure) and keeps a small .dvc file in git that records the hash. When you checkout a git commit, dvc checkout restores the exact data that was used.

This means every git commit pins both the code and the data. Full reproducibility.
 
*** A reproducible experiment requires four things:

    - Fixed random seeds: Set seeds for numpy, random, and the framework (torch, sklearn)
    - Pinned dependencies: requirements.txt or poetry.lock with exact versions
    - Versioned data: DVC or similar
    - Config files: All hyperparameters in a config, not hardcoded *** 

# A pipeline chains every transformation and the model into one object: the sample enters raw and each stage reshapes it before handing it on. All statistics (medians, means, category maps) are fitted once, on training data only, then frozen. Serving runs the identical chain, which is what closes off data leakage and train-serve skew.

```
When someone asks about ML pipelines, preprocessing, or deployment:

1. Check for data leakage first. The most common forms:
   - Fitting transformers (scaler, imputer, encoder) on the full dataset before splitting
   - Target encoding without proper cross-validation
   - Feature selection using the test set
   - Time-series data shuffled before splitting (future leaking into past)
   - Validation metrics computed on data the model saw during training

2. Verify the pipeline structure:
   - All preprocessing steps are inside the Pipeline object, not outside
   - ColumnTransformer handles different column types correctly
   - handle_unknown="ignore" is set for categorical encoders
   - Cross-validation wraps the entire pipeline, not just the model

3. Check for training/serving skew:
   - Is the same Pipeline object used for training and inference?
   - Are feature engineering steps duplicated between training and serving code?
   - Does the serving code handle missing values the same way as training?
   - Are there any features that are available at training time but not at inference time?

4. Verify reproducibility:
   - Random seeds set for all sources of randomness
   - Dependencies pinned to exact versions
   - Data versioned (DVC or similar)
   - Hyperparameters in config files, not hardcoded

```

