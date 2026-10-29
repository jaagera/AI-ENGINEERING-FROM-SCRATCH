> Training a neural network is nothing more than finding the bottom of a valley.

* Optimization is finding the input values that minimize (or maximize) a function.
* In machine learning, the function is the loss. The inputs are the model's weights. Training is optimization.

> Stochastic gradient descent (SGD) computes the gradient on a single random sample and steps immediately. It is noisy but fast.

* CONVEX: A convex function has no bad local minima: every local minimum is a global minimum. 

* NON CONVEX: Neural network loss functions are non-convex. They have many local minima, saddle points, and flat regions.

> Adam (Adaptive Moment Estimation) is a popular gradient-based optimization algorithm in machine learning that automatically adjusts individual learning rates for every single parameter in a model. Which basically tracks; (a) like momentum and (b) gradient magnitude.

* Guides the user through choosing the right optimizer for their specific machine learning problem**

> A mini-batch is a small subset of the training dataset processed together by a machine learning or deep learning model to calculate the loss, compute gradients, and update model parameters in a single iteration. (which everyone uses a mini-batch)