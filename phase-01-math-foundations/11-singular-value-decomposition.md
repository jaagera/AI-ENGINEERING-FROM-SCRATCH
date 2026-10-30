> SVD(Singular Value Decomposition) is the Swiss Army knife of linear algebra. Every matrix has one. Every data scientist needs one.

* U are called left singular vectors; The i-th left singular vector is the direction in output space where the i-th right singular vector lands (after scaling).

* V are called right singular vectors; Think of them as the natural coordinate system for the domain.

* Singular values: A singular value of zero means the matrix crushes that direction entirely.

* The diagonal entries of ΣΣ are called singular values. They are always non-negative and conventionally sorted in decreasing order.

> Noisy data has signal concentrated in the top singular values and noise spread across all singular values. Truncating removes the noise floor.