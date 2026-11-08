> Graphs are the data structure of relationships. If your data has connections, you need graph theory.

* Graph Neural Networks (GNNs) are the fastest-growing area in deep learning. They power drug discovery, social recommendation, fraud detection, and knowledge graph reasoning. Every GNN builds on the same foundation: basic graph theory.

You need four things:

    A way to represent graphs as matrices (so you can multiply them)
    Traversal algorithms to explore graph structure
    The Laplacian -- the single most important matrix in spectral graph theory
    Message passing -- the operation that makes GNNs work

> Directed vs undirected. In an undirected graph, edge (u,v)(u,v) means uu connects to vv AND vv connects to uu. In a directed graph (digraph), edge (u,v)(u,v) means uu points to vv, but not necessarily the reverse.

Weighted vs unweighted. In an unweighted graph, edges either exist or they don't. In a weighted graph, each edge has a numerical weight -- a distance, a cost, a strength.

> Graph type	                        Example
Undirected, unweighted	                Facebook friendship network
Directed, unweighted	                Twitter follow network
Undirected, weighted	                Road map (distances)
Directed, weighted	                    Web page links (PageRank scores)

* BFS and DFS

The two fundamental graph traversal algorithms. You need both.

Breadth-First Search (BFS): Explore all neighbors first, then neighbors' neighbors. Uses a queue (FIFO).

> Depth-First Search (DFS): Go as deep as possible before backtracking. Uses a stack (LIFO) or recursion.

* DFS is useful for:

    Finding connected components (run DFS from unvisited nodes)
    Cycle detection (back edges in DFS tree)
    Topological sorting (reverse DFS finish order)