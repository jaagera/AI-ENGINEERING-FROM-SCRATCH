> A good feature is worth a thousand data points.

```
Numerical Features

Raw numbers are rarely model-ready. Common transforms:

Scaling: Put features on the same range so distance-based algorithms (K-Means, KNN, SVM) treat all features equally. Min-max scaling maps to [0, 1]. Standardization (z-score) maps to mean=0, std=1.

Log transform: Compresses right-skewed distributions (income, population, word counts). Turns multiplicative relationships into additive ones.

Binning: Converts continuous values into categories. Useful when the relationship between feature and target is non-linear but step-wise (e.g., age groups).

Polynomial features: Creates x2x2, x3x3, x1x2x1​x2​ terms. Lets linear models capture non-linear relationships at the cost of more features.
```

```
Categorical Features

Models need numbers. Categories need encoding.

One-hot encoding: Creates a binary column for each category. "color = red/blue/green" becomes three columns: is_red, is_blue, is_green. Works well for low-cardinality features but explodes with many categories.

Label encoding: Maps each category to an integer: red=0, blue=1, green=2. Introduces false ordering (the model might think green > blue > red). Only appropriate for tree-based models that split on individual values.

Target encoding: Replaces each category with the mean of the target variable for that category. Powerful but dangerous: high risk of data leakage. Must be computed only on training data and applied to test data.
```

```
Text Features

Count vectorizer: Counts how many times each word appears in a document. "the cat sat on the mat" becomes {the: 2, cat: 1, sat: 1, on: 1, mat: 1}.

TF-IDF: Term Frequency-Inverse Document Frequency. Weighs words by how unique they are across documents. Common words like "the" get low weight. Rare, distinctive words get high weight.
```

# binning (also called bucketing) is the process of grouping a range of continuous or individual values into smaller, discrete intervals called "bins" or "buckets."

*** outlier is a data point or value that is significantly different from the rest of the values in a dataset ***

