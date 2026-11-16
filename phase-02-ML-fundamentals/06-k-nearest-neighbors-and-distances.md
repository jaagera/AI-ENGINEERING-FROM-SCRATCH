> Store everything. Predict by looking at your neighbors. The simplest algorithm that actually works.

```
KNN stands for k-Nearest Neighbors, a simple, supervised machine learning algorithm used for both classification and regression tasks. It works by finding the closest data points to a new input and predicting its outcome based on the majority vote or average of those neighbors. The KNN also shows up everywhere in modern AI, just under different names. 
```

# Choosing K
K is the single hyperparameter. It controls the bias-variance trade-off:

>K	   |         |   Behavior
K=1K=1           |   Decision boundary follows every point. Zero training error. High variance. Overfits
Small K (3-5)	 |  Sensitive to local structure. Can capture complex boundaries
Large K	         |  Smoother boundaries. More robust to noise. May underfit
K=NK=N	         |  Predicts the majority class for every point. Maximum bias

### Distance metrics

The distance function defines what "near" means. Different metrics produce different neighbors, different predictions.


### Lazy learning vs eager learning

KNN is a lazy learner: it does no work at training time and all work at prediction time. Most other algorithms (linear regression, SVMs, neural networks) are eager learners: they do heavy computation at training time to build a compact model, then predictions are fast.


