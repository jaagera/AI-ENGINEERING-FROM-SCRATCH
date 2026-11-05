> Convex problems have one valley. Neural networks have millions. Knowing the difference matters. 

* Understanding convexity does three things. First, it tells you when your problem is easy (convex) versus hard (non-convex). Second, it gives you faster tools like Newton's method for convex problems. Third, it explains concepts that appear throughout ML: regularization as a constraint, duality in SVMs, and why deep learning works despite violating every nice property convexity gives you.

> Examples of convex sets:

    A line, a plane, all of RnRn
    A ball (circle, sphere, hypersphere)
    A halfspace: {x:aTx≤b}{x:aTx≤b}
    The intersection of any number of convex sets

> Examples of non-convex sets:

    A donut (annulus)
    The union of two disjoint circles
    Any set with a "dent" or "hole"

* The Hessian matrix

The Hessian HH of a function f:Rn→Rf:Rn→R is the n×nn×n matrix of second partial derivatives

> The Hessian tells you about curvature:

    Eigenvalues all positive: the function curves upward in every direction (convex at that point)
    Eigenvalues all negative: curves downward in every direction (concave, a local max)
    Mixed signs: saddle point (curves up in some directions, down in others)
    Zero eigenvalue: flat in that direction (degenerate)

* KKT conditions

The Karush-Kuhn-Tucker conditions extend Lagrange multipliers to inequality constraints.

> Duality

Every constrained optimization problem (the primal) has a companion problem (the dual). For convex problems, the primal and dual have the same optimal value. This is strong duality.

> Why duality matters:

    The dual problem is sometimes easier to solve than the primal
    SVMs are solved in their dual form, where the problem depends on dot products between data points (enabling the kernel trick)
    The dual provides a lower bound on the primal optimum, useful for checking solution quality