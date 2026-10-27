> Derivatives tell you which way is downhill. That is all a neural network needs to learn.
** Each weight is known as a "KNOB" **
Without calculus, training a neural network would mean trying random changes and hoping for the best.
> DERIVATIVE: Measures the rate of change. ***NOTE: Training a neural network is optimization.

DIFF. BTW NUMERICAL & ANALYTICAL DERIVATIVES
Numerical: are slower but work for any function
Analytical: are fast but require you to derive the formula

Approximation order    What it captures    Optimization method
-------------------    -----------------   -------------------
0th order (constant)   Just the value      Random search
1st order (linear)     Slope               Gradient descent
2nd order (quadratic)  Curvature           Newton's method
Higher orders          Finer structure     Rarely used in ML

(VAE = Variational Autoencoders)

## THE JACOBIAN MATRIX: 
Is a matrix of all first-order partial derivatives of a vector-valued function. if a layer maps RnRn to RmRm, its Jacobian is m×nm×n. The gradient flows backward through the transpose of this matrix.

