> The chain rule is the engine behind every neural network that learns.

> Forward Mode vs Reverse Mode
There are two ways to apply the chain rule through a graph.
Forward mode starts at the inputs and pushes derivatives forward. It computes dx/dx=1dx/dx=1 and propagates through each operation. Good when you have few inputs and many outputs.

Reverse mode starts at the output and pulls gradients backward. It computes dy/dy=1dy/dy=1 and propagates through each operation in reverse. Good when you have many inputs and few outputs.

> Building an Autograd Engine

An autograd engine needs three things:

    01. Value wrapping. Wrap every number in an object that stores its value and gradient.
    02. Graph recording. Every operation records its inputs and the local gradient function.
    03. Backward pass. Topological sort the graph, then walk it in reverse, applying the chain rule at each node. 
## Tagline: “The chain rule is the engine behind every neural network that learns.”
