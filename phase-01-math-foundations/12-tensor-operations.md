> Tensors are the common language between data and deep learning. Every image, every sentence, every gradient flows through them.

* What a tensor is

A tensor is a multi-dimensional array of numbers with a uniform data type. The number of dimensions is the rank (or order). Each dimension is an axis. The shape is a tuple listing the size along each axis. *** 

> A tensor is a multi-dimensional grid of numbers. Rank is the number of axes, and shape is the size of each axis.

* Shape errors are the most common bug in deep learning code. They are not hard conceptually -- each operation has a shape contract -- but they multiply fast. A transformer has dozens of reshapes, transposes, and broadcasts chained together. One wrong axis and the error cascades. Worse, some shape mistakes do not throw errors at all. They silently produce garbage by broadcasting along the wrong dimension or summing over the wrong axis.