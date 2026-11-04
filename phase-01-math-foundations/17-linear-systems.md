> Solving Ax=bAx=b is the oldest problem in mathematics that still runs your neural network.

* In matrix form, "one solution" means AA is invertible. "No solution" means the system is inconsistent. "Infinite solutions" means AA has a null space.

> QR decomposition

QR decomposition factors AA into an orthogonal matrix QQ and an upper triangular matrix RR: A=QRA=QR.

 > Condition number

The condition number measures how sensitive the solution is to small changes in the input.

* CG(Conjugate Gradient) is used in:

    Large-scale optimization (Newton-CG method)
    Solving PDE discretizations
    Kernel methods where the kernel matrix is too large to factor
    Preconditioning for other iterative solvers

