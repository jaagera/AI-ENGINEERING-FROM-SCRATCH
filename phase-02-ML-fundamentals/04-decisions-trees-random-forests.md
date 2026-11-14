TOPIC: Decision Trees and Random Forests

> A decision tree is just a flowchart. But a forest of them is one of the most powerful tools in ML.

```
What a decision tree does
A decision tree partitions the feature space into rectangular regions by asking a sequence of yes/no questions.

```
*** Two sources of randomness make the trees diverse:

Bagging (bootstrap aggregating): Each tree is trained on a bootstrap sample, a random sample with replacement from the training data. About 63% of the original samples appear in each bootstrap (the rest are out-of-bag samples that can be used for validation).

Feature randomization: At each split, only a random subset of features is considered. For classification, the default is 
n
features
n 
features
​
 
​
 . For regression, 
n
features
/
3
n 
features
​
 /3. This prevents all trees from splitting on the same dominant feature.

The key insight: averaging many decorrelated trees reduces variance without increasing bias. Each individual tree may be mediocre. The ensemble is strong.

*** 