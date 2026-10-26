> You cannot build AI systems without being fluent in matrix operations the same way you cannot write code without understanding variables.

# Key Terms
Term	        What people say	                What it actually means
Vector	        "An arrow"	                    An ordered list of numbers. In AI: a point in high-dimensional space.
Matrix	        "A table of numbers"	        A linear transformation. It maps vectors from one space to another.
Matrix multiply	"Just multiply the numbers"	    Dot products between every row of the first matrix and every column of the second. Order matters.
Transpose	    "Flip it"	                    Swap rows and columns. Turns an m×nm×n matrix into n×mn×m. Critical in backpropagation.
Determinant	    "Some number from the matrix"	Measures how much the matrix scales area (2D) or volume (3D). Zero means the transformation crushes a dimension.
Inverse	        "Undo the matrix"	            The matrix that reverses the transformation. Only exists when the determinant is not zero.
Identity matrix	"The boring matrix"	            The matrix equivalent of multiplying by 1. Used in residual connections (ResNets).
Broadcasting	"Magic shape fixing"	        Stretching a smaller array to match a larger one by repeating along missing dimensions.
Element-wise	"Regular multiplication"	    Multiply matching positions. Both arrays must have the same shape (or be broadcastable).

* ReLU (Rectified Linear Unit) is the most popular activation function in deep learning that outputs positive numbers directly and turns negative numbers into zero.
