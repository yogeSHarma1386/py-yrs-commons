# Algorithmic Patterns by Engineering Level

## Table 1: Fundamental Patterns (SDE1-SDE2)

| #      | Pattern Name                     | Key Concepts                            | Typical Use Cases                             |
|--------|----------------------------------|-----------------------------------------|-----------------------------------------------|
| **1**  | **Prefix Sum**                   | Cumulative sums, Range queries          | Subarray problems, Range sum queries          |
| **2**  | **Two Pointers**                 | Left/right pointers, Fast/slow          | Array problems, Palindromes, Sorted arrays    |
| **3**  | **Sliding Window**               | Fixed/variable window, Deque            | Substring problems, Maximum/minimum in ranges |
| **4**  | **Fast & Slow Pointers**         | Floyd's cycle detection                 | Linked list cycles, Finding middle element    |
| **5**  | **LinkedList In-place Reversal** | Pointer manipulation                    | Reversing linked lists, Reordering            |
| **6**  | **Monotonic Stack**              | Maintaining order, Next greater/smaller | Daily temperatures, Histogram problems        |
| **7**  | **Top 'K' Elements**             | Heaps, QuickSelect                      | Finding kth largest, Top k frequent           |
| **8**  | **Overlapping Intervals**        | Sorting, Merging intervals              | Meeting rooms, Calendar scheduling            |
| **9**  | **Modified Binary Search**       | Search space reduction                  | Rotated arrays, Peak finding                  |
| **10** | **Binary Tree Traversal**        | DFS, BFS, Inorder/Preorder/Postorder    | Tree problems, Path finding                   |
| **11** | **Depth-First Search (DFS)**     | Recursion, Backtracking                 | Graph traversal, Connected components         |
| **12** | **Breadth-First Search (BFS)**   | Queue, Level-order traversal            | Shortest path, Level-order problems           |
| **13** | **Matrix Traversal**             | 2D DFS/BFS, Directions array            | Island problems, Path finding in grid         |
| **14** | **Backtracking**                 | State space search, Pruning             | N-Queens, Sudoku, Permutations                |
| **15** | **Basic Dynamic Programming**    | Memoization, Tabulation                 | Fibonacci, Climbing stairs, Basic DP          |

## Table 2: Advanced Patterns (SDE3-Staff Engineer)

| #      | Pattern Name                        | Key Concepts                            | Typical Use Cases                            |
|--------|-------------------------------------|-----------------------------------------|----------------------------------------------|
| **16** | **Advanced Dynamic Programming**    | Complex state transitions, Optimization | Knapsack variants, LCS, Edit distance        |
| **17** | **Union-Find (Disjoint Set Union)** | Path compression, Union by rank         | Connected components, Kruskal's MST          |
| **18** | **Trie (Prefix Tree)**              | String prefix matching, Autocomplete    | Word search, IP routing, Autocomplete        |
| **19** | **Segment Trees**                   | Range queries, Lazy propagation         | Range sum/min/max updates, Interval problems |
| **20** | **Fenwick Trees (BIT)**             | Binary indexed tree, Prefix sums        | Dynamic range queries, Order statistics      |
| **21** | **String Algorithms**               | KMP, Z-algorithm, Rolling hash          | Pattern matching, String processing          |
| **22** | **Advanced Graph Algorithms**       | SCC, MST, Shortest paths                | Network analysis, Social graphs              |
| **23** | **Lowest Common Ancestor (LCA)**    | Binary lifting, Euler tour              | Tree queries, Genealogy systems              |
| **24** | **Mathematical Algorithms**         | Number theory, Modular arithmetic       | Cryptography, Mathematical computations      |
| **25** | **Game Theory**                     | Minimax, Alpha-beta pruning             | Decision making, AI systems                  |
| **26** | **Geometric Algorithms**            | Convex hull, Line intersection          | Computer graphics, Computational geometry    |
| **27** | **System Design Algorithms**        | Consistent hashing, Bloom filters       | Distributed systems, Caching strategies      |
| **28** | **Network Flow**                    | Max flow, Min cost flow                 | Resource allocation, Matching problems       |
| **29** | **Advanced Bit Manipulation**       | XOR basis, Bit operations               | Cryptography, Optimization tricks            |
| **30** | **Randomized Algorithms**           | Reservoir sampling, Monte Carlo         | Sampling, Approximation algorithms           |

## Table 3: Expert Patterns (Staff-Senior Staff Engineer)

| #      | Pattern Name                    | Key Concepts                            | Typical Use Cases                           |
|--------|---------------------------------|-----------------------------------------|---------------------------------------------|
| **31** | **Heavy-Light Decomposition**   | Path decomposition, Tree queries        | Complex tree path queries, Network routing  |
| **32** | **Convex Hull Optimization**    | DP optimization, Slope trick            | Advanced DP optimization, Scheduling        |
| **33** | **Suffix Arrays/Trees**         | String suffix processing                | DNA sequencing, Text compression, Search    |
| **34** | **Matrix Algorithms**           | Matrix exponentiation, Linear algebra   | Graphics, Machine learning, Transformations |
| **35** | **Advanced Optimization**       | Linear programming, Hungarian algorithm | Resource allocation, Assignment problems    |
| **36** | **Parallel Algorithms**         | MapReduce, Parallel sorting             | Big data processing, Distributed computing  |
| **37** | **Approximation Algorithms**    | FPTAS, Approximation ratios             | NP-hard problems, Performance guarantees    |
| **38** | **Online Algorithms**           | Competitive analysis, Streaming         | Real-time processing, Limited memory        |
| **39** | **Quantum Algorithms**          | Quantum computing principles            | Cryptography, Optimization (emerging)       |
| **40** | **Machine Learning Algorithms** | Gradient descent, Neural networks       | AI systems, Data science applications       |
| **41** | **Cryptographic Algorithms**    | RSA, AES, Hash functions                | Security systems, Blockchain                |
| **42** | **Compiler Algorithms**         | Parsing, Optimization                   | Language processing, Code generation        |
| **43** | **Database Algorithms**         | B-trees, Query optimization             | Database systems, Indexing strategies       |
| **44** | **Distributed Algorithms**      | Consensus, Byzantine fault tolerance    | Distributed systems, Blockchain             |
| **45** | **Bioinformatics Algorithms**   | Sequence alignment, Phylogenetics       | DNA analysis, Computational biology         |

## Mastery Expectations

- **SDE1-SDE2**: Master Table 1 patterns (1-15)
- **SDE3**: Master Table 1 + Most of Table 2 (1-25)
- **Staff Engineer**: Master Tables 1-2 + Familiar with Table 3 (1-35)
  - Check few code examples [here](/yrs_commons/dsa/detailed/java/senior-backend-dsa-guide.md)
- **Senior Staff**: Master all patterns, can design novel algorithms (1-45)

## Key Differentiators by Level

**Junior → Mid**: Pattern recognition and implementation <br/>
**Mid → Senior**: Optimization and adaptation of patterns <br/>
**Senior → Staff**: System-level pattern application <br/>
**Staff → Senior Staff**: Novel algorithm design and research-level problems


# DSA Helper Functions Complexities

Here's a table of common data structure and algorithm helper functions with their time and space complexities; Where
- n = number of elements in the data structure
- h = height of the tree/structure (for tree-based structures)
- m = length of string/pattern
- V = number of vertices in a graph
- E = number of edges in a graph
- k = number of elements in a heap/priority queue
- d = number of digits/characters in RadixSort
- z = number of matches in prefix search

| Function                          | Time Complexity (Best)    | Time Complexity (Worst) | Space Complexity | Description              |
|-----------------------------------|---------------------------|-------------------------|------------------|--------------------------|
| --------------------------------- | **Array/List Operations** |
| Push/Append                       | O(1)                      | O(1)                    | O(1)             | Add element to end       |
| Pop                               | O(1)                      | O(1)                    | O(1)             | Remove from end          |
| Insert                            | O(1) (at end)             | O(n) (at beginning)     | O(1)             | Add at specific index    |
| Delete                            | O(1) (at end)             | O(n) (at beginning)     | O(1)             | Remove at specific index |
| Search                            | O(1) (if index known)     | O(n) (linear search)    | O(1)             | Find element             |
| Binary Search                     | O(1) (lucky guess)        | O(log n)                | O(1)             | Find in sorted array     |

| Function                          | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description      |
|-----------------------------------|------------------------|-------------------------|------------------|------------------|
| --------------------------------- | **Stack Operations**   |
| Push                              | O(1)                   | O(1)                    | O(1)             | Add to top       |
| Pop                               | O(1)                   | O(1)                    | O(1)             | Remove from top  |
| Peek/Top                          | O(1)                   | O(1)                    | O(1)             | View top element |

| Function                          | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description        |
|-----------------------------------|------------------------|-------------------------|------------------|--------------------|
| --------------------------------- | **Queue Operations**   |
| Enqueue                           | O(1)                   | O(1)                    | O(1)             | Add to rear        |
| Dequeue                           | O(1)                   | O(1)                    | O(1)             | Remove from front  |
| Front                             | O(1)                   | O(1)                    | O(1)             | View front element |

| Function                          | Time Complexity (Best)     | Time Complexity (Worst) | Space Complexity | Description  |
|-----------------------------------|----------------------------|-------------------------|------------------|--------------|
| --------------------------------- | **Linked List Operations** |
| Insert                            | O(1) (at head/tail)        | O(n) (at middle)        | O(1)             | Add new node |
| Delete                            | O(1) (at head)             | O(n) (at middle/tail)   | O(1)             | Remove node  |
| Search                            | O(1) (at head)             | O(n) (at tail)          | O(1)             | Find element |

| Function                          | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description             |
|-----------------------------------|------------------------|-------------------------|------------------|-------------------------|
| --------------------------------- | **Heap Operations**    |
| Insert                            | O(1) (lucky case)      | O(log k)                | O(1)             | Add element             |
| Extract Min/Max                   | O(log k)               | O(log k)                | O(1)             | Remove root             |
| Heapify                           | O(k)                   | O(k)                    | O(1)             | Build heap              |
| Peek/Find Min/Max                 | O(1)                   | O(1)                    | O(1)             | View root element       |
| Decrease/Increase Key             | O(1) (lucky case)      | O(log k)                | O(1)             | Update priority         |
| Delete                            | O(log k)               | O(log k)                | O(1)             | Remove specific element |
| Merge Heaps                       | O(k)                   | O(k)                    | O(k)             | Combine two heaps       |

| Function                          | Time Complexity (Best)    | Time Complexity (Worst) | Space Complexity | Description           |
|-----------------------------------|---------------------------|-------------------------|------------------|-----------------------|
| --------------------------------- | **Hash Table Operations** |
| Insert                            | O(1) (no collision)       | O(n) (many collisions)  | O(1)             | Add key-value pair    |
| Delete                            | O(1) (no collision)       | O(n) (many collisions)  | O(1)             | Remove key-value pair |
| Search                            | O(1) (no collision)       | O(n) (many collisions)  | O(1)             | Find by key           |
| Rehash                            | O(n)                      | O(n)                    | O(n)             | Resize table          |

| Function                          | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description                |
|-----------------------------------|------------------------|-------------------------|------------------|----------------------------|
| --------------------------------- | **Sorting Algorithms** |
| QuickSort                         | O(n log n)             | O(n²)                   | O(log n)         | Divide and conquer sorting |
| MergeSort                         | O(n log n)             | O(n log n)              | O(n)             | Divide and conquer sorting |
| HeapSort                          | O(n log n)             | O(n log n)              | O(1)             | Heap-based sorting         |
| BubbleSort                        | O(n) (already sorted)  | O(n²)                   | O(1)             | Simple comparison sort     |
| InsertionSort                     | O(n) (already sorted)  | O(n²)                   | O(1)             | Simple comparison sort     |
| SelectionSort                     | O(n²)                  | O(n²)                   | O(1)             | Simple comparison sort     |
| CountingSort                      | O(n+k)                 | O(n+k)                  | O(k)             | Integer sorting            |
| RadixSort                         | O(d(n+k))              | O(d(n+k))               | O(n+k)           | Integer sorting            |

| Function                          | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description                   |
|-----------------------------------|------------------------|-------------------------|------------------|-------------------------------|
| --------------------------------- | **String Operations**  |
| KMP Search                        | O(n+m)                 | O(n+m)                  | O(m)             | Pattern matching              |
| Rabin-Karp                        | O(n+m)                 | O(n·m)                  | O(1)             | Pattern matching with hashing |
| Z-Algorithm                       | O(n+m)                 | O(n+m)                  | O(n+m)           | Pattern matching              |
| Suffix Array                      | O(n)                   | O(n log² n)             | O(n)             | Suffix sorting                |
| Longest Common Prefix             | O(m)                   | O(m)                    | O(1)             | Find common prefix            |

| Function                          | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description                  |
|-----------------------------------|------------------------|-------------------------|------------------|------------------------------|
| --------------------------------- | **Trie Operations**    |
| Insert                            | O(m)                   | O(m)                    | O(m)             | Add string to trie           |
| Search                            | O(m)                   | O(m)                    | O(1)             | Find string in trie          |
| Delete                            | O(m)                   | O(m)                    | O(1)             | Remove string from trie      |
| Prefix Search                     | O(m+z)                 | O(m+z)                  | O(z)             | Find all strings with prefix |

| Function                          | Time Complexity (Best)     | Time Complexity (Worst) | Space Complexity | Description         |
|-----------------------------------|----------------------------|-------------------------|------------------|---------------------|
| --------------------------------- | **Union-Find**             |
| MakeSet                           | O(1)                       | O(1)                    | O(1)             | Create new set      |
| Find                              | O(1) (path compression)    | O(log n) (worst case)   | O(1)             | Find representative |
| Union                             | O(1) (rank/size heuristic) | O(log n) (worst case)   | O(1)             | Merge two sets      |

| Function                          | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description     |
|-----------------------------------|------------------------|-------------------------|------------------|-----------------|
| --------------------------------- | **Binary Search Tree** |
| Insert                            | O(log n) (balanced)    | O(n) (unbalanced)       | O(1)             | Add new node    |
| Delete                            | O(log n) (balanced)    | O(n) (unbalanced)       | O(1)             | Remove node     |
| Search                            | O(log n) (balanced)    | O(n) (unbalanced)       | O(1)             | Find element    |
| Height                            | O(1) (stored)          | O(n) (compute)          | O(1)             | Tree height     |
| Traversal                         | O(n)                   | O(n)                    | O(h)             | Visit all nodes |

| Function                          | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description  |
|-----------------------------------|------------------------|-------------------------|------------------|--------------|
| --------------------------------- | **BST (height-based)** |
| Insert                            | O(h)                   | O(h)                    | O(1)             | Add new node |
| Delete                            | O(h)                   | O(h)                    | O(1)             | Remove node  |
| Search                            | O(h)                   | O(h)                    | O(1)             | Find element |

| Function                          | Time Complexity (Best)             | Time Complexity (Worst)       | Space Complexity | Description     |
|-----------------------------------|------------------------------------|-------------------------------|------------------|-----------------|
| --------------------------------- | **Balanced Tree (AVL, Red-Black)** |
| Insert                            | O(log n)                           | O(log n)                      | O(1)             | Add new node    |
| Delete                            | O(log n)                           | O(log n)                      | O(1)             | Remove node     |
| Search                            | O(log n)                           | O(log n)                      | O(1)             | Find element    |
| Rebalance                         | O(1) (single rotation)             | O(log n) (multiple rotations) | O(1)             | Restore balance |

| Function                           | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description                       |
|------------------------------------|------------------------|-------------------------|------------------|-----------------------------------|
| ---------------------------------- | **Graph Operations**   |
| BFS                                | O(V+E)                 | O(V+E)                  | O(V)             | Breadth-First Search              |
| DFS                                | O(V+E)                 | O(V+E)                  | O(V)             | Depth-First Search                |
| Dijkstra                           | O(E + V log V)         | O(E + V log V)          | O(V)             | Shortest path                     |
| Bellman-Ford                       | O(V·E)                 | O(V·E)                  | O(V)             | Shortest path with negative edges |
| Floyd-Warshall                     | O(V³)                  | O(V³)                   | O(V²)            | All-pairs shortest path           |
| Prim's                             | O(E log V)             | O(E log V)              | O(V)             | Minimum Spanning Tree             |
| Kruskal's                          | O(E log E)             | O(E log E)              | O(V)             | Minimum Spanning Tree             |
| Topological Sort                   | O(V+E)                 | O(V+E)                  | O(V)             | DAG ordering                      |
