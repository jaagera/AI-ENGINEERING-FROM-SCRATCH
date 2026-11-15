> Find the widest street between two classes. That is the entire idea.

```
Real data is rarely perfectly separable. Some points may be on the wrong side of the boundary, or inside the margin. The soft margin formulation allows violations by introducing slack variables.

```

# C value	                    Behavior
Large 
C                               Penalizes violations heavily. Narrow margin, fewer misclassifications. Overfits

Small 
C	                            Allows more violations. Wide margin, more misclassifications. Underfits

*** 
The dual only inovles dot products between data points. This is the key insight. Replace every dot product with a kernel function K and the SVM can learn nonlinear boundaries without ever computing the transformation explicitly.
***

## SVM FOR REGRESSION(SVR)
Support Vector Regression fits a tube a width around the data. Points inside the tub have zero loss. Points outside the tube are penalized lineraly.


* SVMs still win in these situations:

Small datasets (hundreds to low thousands of samples)
High-dimensional sparse data (text with TF-IDF features)
When you need mathematical guarantees (margin bounds)
When training time must be minimal (linear SVM is very fast)
Binary classification with clear margin structure
Anomaly detection (one-class SVM) ***

