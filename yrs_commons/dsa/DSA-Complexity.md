# Data Structures & Algorithms Pattern Recognition Framework

## Array & String Patterns

| Pattern | Keywords/Hints | Time Complexity | Space Complexity | Suitable Algorithms | Example Problems | When to Use |
|---------|---------------|-----------------|------------------|-------------------|------------------|-------------|
| Two Pointers | "sorted array", "target sum", "palindrome", "remove duplicates" | O(n) | O(1) | Two-pointer technique, Collision approach, Fast & slow pointers | Two Sum, 3Sum, Container With Most Water | When working with sorted arrays or searching for pairs |
| Sliding Window | "subarray", "substring", "consecutive", "longest", "shortest", "fixed size k" | O(n) | O(1) or O(k) | Fixed/variable size window, Expand-contract, Two pointers with window | Maximum Subarray Sum, Longest Substring Without Repeating | When looking for contiguous subarrays or substrings |
| Prefix Sum | "subarray sum", "range query", "cumulative", "between indices" | O(n) pre-computation, O(1) queries | O(n) | Cumulative sum array, Difference array, 2D prefix sum | Range Sum Query, Subarray Sum Equals K | For quick range sum computations |
| Dutch National Flag | "sort colors", "three-way partition", "pivot arrangement" | O(n) | O(1) | Three-way partitioning, Multi-pivot partitioning, Counting sort | Sort Colors, Partition Array | When partitioning array around one or more values |
| Kadane's Algorithm | "maximum subarray sum", "contiguous", "largest sum" | O(n) | O(1) | Dynamic programming (Kadane's), Running sum with reset | Maximum Subarray, Maximum Circular Subarray Sum | For maximum contiguous sum problems |
| Boyer-Moore Voting | "majority element", "more than n/2 times", "more than n/3 times" | O(n) | O(1) | Voting algorithm, Counter technique, Frequency tracking | Majority Element, Majority Element II | Finding elements that appear more than n/k times |
| Z-Algorithm/KMP | "string pattern", "substring search", "occurrences of pattern" | O(n+m) | O(n) | KMP, Z-algorithm, Rabin-Karp, Boyer-Moore | Implement strStr(), First Occurrence of Substring | When doing pattern matching in strings |

## Linked List Patterns

| Pattern | Keywords/Hints | Time Complexity | Space Complexity | Suitable Algorithms | Example Problems | When to Use |
|---------|---------------|-----------------|------------------|-------------------|------------------|-------------|
| Fast & Slow Pointers | "cycle detection", "middle of linked list", "nth from end" | O(n) | O(1) | Floyd's tortoise and hare, Runner technique, Two-pointer | Linked List Cycle, Find Middle of Linked List | Detecting cycles or finding middle elements |
| Sentinel Node | "head might change", "delete node", "before head" | O(n) | O(1) | Dummy head technique, Guarded linked list | Remove Linked List Elements | When operations might change the head node |
| Reverse Linked List | "reverse", "in-place reversal", "in groups" | O(n) | O(1) | Iterative reversal, Recursive reversal, Group reversal | Reverse Linked List, Reverse Nodes in k-Group | When needing to process list in reverse order |
| Merge Lists | "merge sorted lists", "merge k lists", "merge alternate" | O(n+m) or O(n log k) | O(1) or O(k) | Two-pointer merge, Priority queue merge, Divide and conquer | Merge Two Sorted Lists, Merge k Sorted Lists | When combining multiple sorted lists |
| Partition List | "partition around value", "smaller before larger" | O(n) | O(1) | Two-pointer partition, Multiple list building | Partition List | When rearranging nodes based on values |
| Deep Copy | "clone", "deep copy", "random pointer" | O(n) | O(n) | Hash map mapping, Interleaved copying | Copy List with Random Pointer | When making a deep copy with complex links |
| Intersection Detection | "intersection of two lists", "meeting point", "Y-shaped" | O(n+m) | O(1) | Two-pointer technique, Length difference, Hash set | Intersection of Two Linked Lists | For finding where two lists connect |

## Tree & Graph Patterns

| Pattern | Keywords/Hints | Time Complexity | Space Complexity | Suitable Algorithms | Example Problems | When to Use |
|---------|---------------|-----------------|------------------|-------------------|------------------|-------------|
| DFS (Depth-First Search) | "path exists", "connected components", "preorder", "inorder", "postorder" | O(V+E) | O(H) or O(V) | Recursive DFS, Iterative DFS with stack, Pre/In/Post-order traversal | Binary Tree Traversal, Path Sum, Number of Islands | Path finding, tree traversal, connected components |
| BFS (Breadth-First Search) | "shortest path", "level order", "minimum steps", "word ladder" | O(V+E) | O(V) | Queue-based BFS, Level-order traversal, Bidirectional BFS | Level Order Traversal, Shortest Path, Word Ladder | Finding shortest paths or level-wise processing |
| Topological Sort | "course schedule", "prerequisite", "build order", "dependency" | O(V+E) | O(V) | Kahn's algorithm, DFS with finish time sorting | Course Schedule, Alien Dictionary | Tasks with dependencies or directed acyclic graphs |
| Union Find | "connected components", "redundant connection", "number of islands", "groups" | O(α(n)) (almost O(1)) | O(n) | Disjoint Set Union (DSU), Path compression, Union by rank/size | Number of Connected Components, Redundant Connection | Dynamic connectivity problems |
| Minimum Spanning Tree | "minimum cost to connect", "network cables", "city connections" | O(E log E) or O(E log V) | O(V+E) | Kruskal's algorithm, Prim's algorithm | Minimum Spanning Tree, Network Connections | Minimizing total edge weight in connected graph |
| Shortest Path | "shortest distance", "network delay", "minimum cost path" | O(V log V + E) or O(V^2) | O(V) | Dijkstra's algorithm, Bellman-Ford, Floyd-Warshall | Network Delay Time, Cheapest Flights | Finding minimum distance paths |
| Backtracking on Trees | "all paths", "path sum II", "binary tree paths" | O(n) to O(2^n) | O(h) | DFS with path tracking, Recursive path building | All Paths from Root to Leaf, Path Sum II | Finding all possible paths or combinations |
| Tree Construction | "construct tree from", "preorder and inorder", "serialize deserialize" | O(n) | O(n) | Recursive construction, Hash map indexing, Queue-based construction | Construct Binary Tree from Inorder and Preorder | Recreating trees from traversal data |
| Lowest Common Ancestor | "LCA", "lowest common ancestor", "nearest common parent" | O(h) or O(n) | O(h) or O(n) | Binary lifting, Recursive LCA, Euler tour technique | Lowest Common Ancestor of a Binary Tree | Finding the closest shared ancestor |
| Trie (Prefix Tree) | "prefix", "word dictionary", "autocomplete", "word search" | O(L) (L = word length) | O(n*L) | Trie implementation, DFS on trie, Trie + backtracking | Implement Trie, Word Search II | Word dictionary problems, prefix matching |

## Dynamic Programming Patterns

| Pattern | Keywords/Hints | Time Complexity | Space Complexity | Suitable Algorithms | Example Problems | When to Use |
|---------|---------------|-----------------|------------------|-------------------|------------------|-------------|
| 1D DP | "maximum/minimum", "optimal", "ways to", "fibonacci", "climbing stairs" | O(n) to O(n^2) | O(n) or O(1) | Bottom-up tabulation, Top-down memoization, Sliding window DP | Climbing Stairs, Maximum Subarray | Linear sequence problems with optimal substructure |
| 2D DP | "matrix paths", "grid", "edit distance", "longest common" | O(n*m) | O(n*m) or O(min(n,m)) | Matrix filling, Space-optimized 2D DP, Prefix optimization | Unique Paths, Edit Distance, LCS | Problems involving 2D grids or two sequences |
| State Machine DP | "buy and sell stock", "state transitions", "with cooldown", "with fees" | O(n) | O(n) or O(1) | State transition DP, Multi-state tracking, Graph-based DP | Best Time to Buy and Sell Stock with Cooldown | Problems with distinct states and transitions |
| Interval DP | "burst balloons", "partition array", "optimal strategy game" | O(n^3) | O(n^2) | Gap-based DP, Range-based DP, Matrix chain multiplication | Burst Balloons, Merge Stones | Problems involving interval merging or partitioning |
| Decision Making | "rob houses", "include/exclude", "take or not take" | O(n) | O(n) or O(1) | Choose/not choose DP, Alternating selection DP | House Robber, Maximum Alternating Subsequence | When each element has clear take/not take choice |
| Knapsack | "knapsack", "target sum", "subset sum", "capacity" | O(n*W) | O(n*W) or O(W) | 0/1 Knapsack, Bounded knapsack, Unbounded knapsack, Subset sum | 0/1 Knapsack, Coin Change, Partition Equal Subset Sum | Resource allocation with constraints |
| Longest Increasing Subsequence | "longest increasing", "largest divisible subset", "Russian doll" | O(n^2) or O(n log n) | O(n) | Standard LIS, Binary search LIS, Patience sort | Longest Increasing Subsequence, Russian Doll Envelopes | Finding optimal ordered subsequences |
| String Matching | "palindrome", "edit distance", "wildcard", "regex" | O(n*m) | O(n*m) | Levenshtein distance, Needleman-Wunsch, Smith-Waterman | Longest Palindromic Substring, Regular Expression Matching | String comparison and pattern matching |

## Backtracking & Recursion Patterns

| Pattern | Keywords/Hints | Time Complexity | Space Complexity | Suitable Algorithms | Example Problems | When to Use |
|---------|---------------|-----------------|------------------|-------------------|------------------|-------------|
| Subset Generation | "all subsets", "combinations", "powerset" | O(2^n) | O(n) | Backtracking with inclusion/exclusion, Bitmask enumeration, Cascading | Subsets, Combinations | Finding all possible subsets of elements |
| Permutation Generation | "all permutations", "distinct permutations", "next permutation" | O(n!) | O(n) | Backtracking with swapping, Heap's algorithm, Lexicographic ordering | Permutations, Next Permutation | Generating all possible arrangements |
| Combination Sum | "target sum", "combination sum", "coin change" | O(2^n) to O(n^target) | O(target) | Backtracking with target reduction, DP with combinatorial counting | Combination Sum, Coin Change 2 | Finding combinations that add up to target |
| Palindrome Partitioning | "palindrome partitioning", "split into palindromes" | O(n*2^n) | O(n) | Backtracking with palindrome checking, DP + backtracking | Palindrome Partitioning | Splitting string into valid palindromes |
| Word Search | "word search", "boggle", "grid with words" | O(m*n*4^L) | O(L) | DFS with backtracking, Trie-based search, Marked visited exploration | Word Search, Word Search II | Finding words in a character grid |
| N-Queens | "n-queens", "chessboard arrangement", "non-attacking" | O(n!) | O(n) | Backtracking with constraint checking, Bitmask optimization | N-Queens | Problems with complex constraint satisfaction |
| Sudoku | "sudoku", "valid arrangement", "fill the board" | O(9^(n*n)) | O(n*n) | Backtracking with constraint propagation, Dancing Links (DLX) | Sudoku Solver | Grid-filling with strict constraints |
| Graph Coloring | "coloring", "bipartite", "no adjacent same" | O(m*n) | O(n) | Greedy coloring, BFS bipartite checking, Backtracking for k-coloring | Is Graph Bipartite? | Labeling nodes with constraints on neighbors |

## Heap & Priority Queue Patterns

| Pattern | Keywords/Hints | Time Complexity | Space Complexity | Suitable Algorithms | Example Problems | When to Use |
|---------|---------------|-----------------|------------------|-------------------|------------------|-------------|
| Top K Elements | "kth largest", "k most frequent", "k closest" | O(n log k) | O(k) | Min-heap of k elements, Quick select, Bucket sort | Top K Frequent Elements, Kth Largest Element | Finding k elements with extreme values |
| Merge K Sorted | "merge k sorted", "k-way merge" | O(n log k) | O(k) | Priority queue merge, Divide and conquer merge, Multi-way merge | Merge K Sorted Lists, Merge K Sorted Arrays | Combining multiple sorted collections |
| Sliding Window Maximum | "sliding window maximum", "maximum in window" | O(n log k) or O(n) | O(k) | Monotonic deque, Heap-based sliding window, Segment tree | Sliding Window Maximum | Tracking extremes in a moving window |
| Stream Median | "median of stream", "online median" | O(log n) per element | O(n) | Two heaps technique, Self-balancing BST, Order statistic tree | Find Median from Data Stream | Finding median in streaming data |
| Task Scheduler | "task scheduler", "CPU scheduling", "cooldown" | O(n log n) | O(n) | Greedy with max heap, Frequency counting + heap, Simulation | Task Scheduler | Optimizing task execution with constraints |
| Ugly Number | "ugly number", "super ugly", "nth smallest" | O(n log n) | O(n) | Min-heap with tracking, DP approach, Multi-source BFS | Ugly Number II, Super Ugly Number | Finding numbers with specific prime factors |
| Connect Ropes | "minimum cost", "connect ropes", "merge files" | O(n log n) | O(n) | Greedy with min heap, Huffman coding approach | Minimum Cost to Connect Ropes | Minimizing cost of sequential operations |

## Binary Search Patterns

| Pattern | Keywords/Hints | Time Complexity | Space Complexity | Suitable Algorithms | Example Problems | When to Use |
|---------|---------------|-----------------|------------------|-------------------|------------------|-------------|
| Classic Binary Search | "sorted array", "find target", "search" | O(log n) | O(1) | Standard binary search, Iterative/recursive binary search | Binary Search, Search Insert Position | Finding exact value in sorted collection |
| Boundary Binary Search | "first occurrence", "last position", "leftmost" | O(log n) | O(1) | Lower bound, Upper bound, Modified binary search | First and Last Position of Element | Finding boundary positions in sorted arrays |
| Search in Rotated Array | "rotated", "pivoted", "shifted" | O(log n) | O(1) | Two-phase binary search, Rotated array search, One-pass modified BS | Search in Rotated Sorted Array | Searching in partially sorted arrays |
| Matrix Binary Search | "sorted matrix", "row-column sorted" | O(log(n*m)) or O(n+m) | O(1) | Treat as 1D array, Binary search rows then columns, Diagonal search | Search a 2D Matrix, Search a 2D Matrix II | Searching in sorted 2D structures |
| Peak Finding | "peak element", "maximum", "local peak" | O(log n) | O(1) | Modified binary search, Gradient ascending search | Find Peak Element, Peak Index in Mountain Array | Finding extrema in partially sorted arrays |
| Kth Element | "kth smallest", "median of two sorted" | O(log n) or O(log(min(n,m))) | O(1) | Binary search on answer, Median finding algorithm, Quick select | Median of Two Sorted Arrays, Kth Smallest Element | Finding kth element without fully merging |
| Capacity Minimization | "minimize maximum", "maximize minimum", "capacity to" | O(n log range) | O(1) | Binary search on answer space, Feasibility checking | Split Array Largest Sum, Capacity To Ship | Minimizing maximum or maximizing minimum value |

## Bit Manipulation Patterns

| Pattern | Keywords/Hints | Time Complexity | Space Complexity | Suitable Algorithms | Example Problems | When to Use |
|---------|---------------|-----------------|------------------|-------------------|------------------|-------------|
| Basic Operations | "set bit", "clear bit", "count bits", "power of two" | O(1) to O(log n) | O(1) | Bit shifting, Bit masking, Brian Kernighan's algorithm | Counting Bits, Power of Two | Basic bit checking and manipulation |
| XOR Properties | "single number", "missing number", "find difference" | O(n) | O(1) | XOR cancellation, Bit frequency counting, Gauss sum with XOR | Single Number, Missing Number | Finding unique or missing elements |
| Bit Masking | "subset", "all possible", "combinations using bits" | O(2^n) | O(1) to O(n) | Bitmask enumeration, Gosper's hack, Bit iteration | Subsets, Generate Parentheses | Representing selection states compactly |
| Binary Addition | "add binary", "sum of two integers", "without +" | O(n) | O(1) | Half/full adder simulation, Bitwise operations for addition | Add Binary, Sum of Two Integers | Arithmetic without using operators |
| Binary Representation | "binary representation", "complement", "alternate bits" | O(log n) | O(log n) | Bit pattern checking, Mask creation, Bit manipulation tricks | Binary Number Alternating Bits | Checking patterns in binary representation |
| Bitwise AND of Range | "bitwise AND of range", "common prefix" | O(log n) | O(1) | Common prefix identification, Brian Kernighan's algorithm | Bitwise AND of Numbers Range | Finding common bit patterns in ranges |

## Advanced Data Structures

| Data Structure | Keywords/Hints | Time Complexity | Space Complexity | Suitable Algorithms | Example Problems | When to Use |
|----------------|---------------|-----------------|------------------|-------------------|------------------|-------------|
| Segment Tree | "range query", "range update", "sum/min/max over interval" | O(log n) query/update | O(n) | Array-based segment tree, Lazy propagation, Iterative segment tree | Range Sum Query - Mutable, Range Minimum Query | Dynamic range queries with updates |
| Fenwick Tree (BIT) | "range sum", "update values", "cumulative" | O(log n) query/update | O(n) | Binary Indexed Tree, LSB manipulation technique | Range Sum Query - Mutable | Prefix sum with efficient updates |
| Sparse Table | "range minimum/maximum", "static array", "RMQ" | O(1) query, O(n log n) build | O(n log n) | Dynamic programming sparse table, Segment min/max | Range Minimum Query | Fast static range queries |
| LRU Cache | "least recently used", "cache", "get/put" | O(1) | O(capacity) | Doubly linked list + hash map, STL containers (list + unordered_map) | LRU Cache | Caching with recency-based eviction |
| LFU Cache | "least frequently used", "frequency based" | O(1) | O(capacity) | Multi-layer hash maps, Min-heap with counters | LFU Cache | Caching with frequency-based eviction |
| Monotonic Stack/Queue | "next greater element", "largest rectangle", "temperatures" | O(n) | O(n) | Monotonic stack, Monotonic queue, Stack-based histogram algorithm | Next Greater Element, Largest Rectangle in Histogram | Finding next greater/smaller elements |
| Disjoint Set | "union find", "connected components", "friend circles" | O(α(n)) per operation | O(n) | Union by rank/size, Path compression, Quick union | Number of Connected Components, Redundant Connection | Dynamic connectivity problems |
| Suffix Array/Tree | "string searching", "longest common", "substring" | O(n log n) build, O(m) search | O(n) | Suffix array construction, LCP array, Ukkonen's algorithm | Longest Repeating Substring, Suffix Array | Advanced string pattern matching |
| Bloom Filter | "contains duplicate", "membership check", "space efficient" | O(k) | O(m) | Multiple hash functions, Bit array, Probabilistic data structure | Contains Duplicate, Web Crawler | Space-efficient approximate membership |

## Problem Complexity Selection Guide

| Time Constraint | Input Size (n) | Suitable Algorithm Complexity |
|-----------------|---------------|------------------------------|
| Tight Time Limit | n ≤ 10 | O(n!), O(n^n) |
| | n ≤ 15-18 | O(2^n) |
| | n ≤ 50 | O(n^4) |
| | n ≤ 500 | O(n^3) |
| | n ≤ 10,000 | O(n^2) |
| | n ≤ 1,000,000 | O(n log n) |
| | n ≤ 100,000,000 | O(n) |
| | n is very large | O(log n) or O(1) |
| Memory Constraint | Memory ≤ 8 MB | Avoid O(n) space if n > 10^6 |
| | Memory ≤ 80 MB | Avoid O(n^2) space if n > 10^4 |

# Algorithmic Complexity Constraint Analysis Framework

## Input Size Constraints & Acceptable Time Complexity

| Input Size (n) | Maximum Acceptable Time Complexity | Algorithms to Consider | Algorithms to Avoid | Example Problem Types |
|----------------|-----------------------------------|------------------------|---------------------|------------------------|
| n ≤ 10 | O(n!), O(n^n) | Brute force, Backtracking, Recursive exhaustive search | - | Permutations, Subset generation, TSP |
| n ≤ 15-20 | O(2^n) | Combinatorial, Bitmask DP, Meet in the middle | O(n!) | NP-hard problems, Power set, Subset sum |
| n ≤ 25-30 | O(3^n) | Meet in the middle, Pruned backtracking | O(n!) | TSP with pruning, Chess-related problems |
| n ≤ 50 | O(n^4) | DP with 3-4 states, Floyd-Warshall | O(2^n), O(n!) | All-pairs shortest path, Small matrix operations |
| n ≤ 100 | O(n^3) | 3-nested loops, Matrix chain multiplication | O(n^4+) | 3D DP, Small matrix multiplication |
| n ≤ 300-500 | O(n^2 log n) | Dijkstra all-pairs, Divide & Conquer | O(n^3+) | Small graph algorithms, Geometric algorithms |
| n ≤ 1,000 | O(n^2) | Quadratic algorithms, 2D DP | O(n^3+) | Pairwise computations, Small sorting, 2D grids |
| n ≤ 10,000 | O(n log^2 n) | Balanced BST operations, Divide & Conquer | O(n^2+) | Computational geometry, Range queries |
| n ≤ 100,000 | O(n log n) | Sorting, Heap operations, BST | O(n^2) | Sorting problems, Priority queue operations |
| n ≤ 1,000,000 | O(n) | Linear scanning, Hash tables, Two pointers | O(n log n+) | Array/string processing, Greedy algorithms |
| n ≤ 10,000,000 | O(n) | Optimized linear algorithms | O(n log n+) | Array traversal, Counting, Streaming algorithms |
| n ≤ 100,000,000 | O(√n) | Square root decomposition | O(n+) | Number theory, Prime factorization |
| n ≤ 10^9 | O(log n) | Binary search, GCD, Divide & Conquer | O(√n+) | Binary search on answer, GCD/LCM |
| n ≤ 10^18 | O(log n) | Binary exponentiation, Matrix exponentiation | O(√n+) | Modular arithmetic, Fibonacci numbers |

## Array/String Size Constraints

| Array/String Size | Acceptable Time Complexity | Acceptable Space Complexity | Likely Techniques | Example Problem Types |
|-------------------|----------------------------|----------------------------|-------------------|------------------------|
| n ≤ 100 | O(n^3) or better | O(n^2) | DP, Brute force | Subarray/substring problems, Matrix paths |
| n ≤ 1,000 | O(n^2) or better | O(n) | Two pointers, DP with optimization | Kadane's, Sliding window |
| n ≤ 10,000 | O(n log n) or better | O(n) | Merge sort, Binary search | Sorting-based problems, Range queries |
| n ≤ 100,000 | O(n) or better | O(n) | Linear scan, Hash table | Frequency counting, Two sum |
| n ≤ 1,000,000 | O(n) or better | O(1) or O(log n) | In-place algorithms, Stream processing | Constant extra space array manipulation |
| Multiple arrays with combined length n | O(n log n) or better | O(n) | Merge-based, Hash map | Intersection, Union, Common elements |

## Graph Constraints

| Graph Size (V = vertices, E = edges) | Acceptable Time Complexity | Acceptable Space Complexity | Likely Techniques | Example Problem Types |
|--------------------------------------|----------------------------|----------------------------|-------------------|------------------------|
| V ≤ 100, E ≤ 10,000 | O(V^3) or O(V^2 × E) | O(V^2) | Floyd-Warshall, Johnson's | All-pairs shortest paths |
| V ≤ 500, E ≤ 10,000 | O(V^2) or O(E log V) | O(V + E) | Dijkstra, MST algorithms | Single-source shortest paths |
| V ≤ 1,000, E ≤ 100,000 | O(E log V) | O(V + E) | Optimized graph algorithms | MST, Shortest paths with heap |
| V ≤ 10,000, E ≤ 100,000 | O(V + E) | O(V + E) | BFS, DFS, Union-Find | Connectivity, Topological sort |
| V ≤ 100,000, E ≤ 1,000,000 | O(V + E) | O(V + E) | Linear graph algorithms | Graph traversal, Connected components |
| V is large, graph is sparse (E ≈ V) | O(V) | O(V) | Specialized algorithms | Tree algorithms, Sparse graph traversal |
| V is large, graph is dense (E ≈ V^2) | O(V^2) | O(V^2) | Matrix representations | Complete graph problems |

## Tree Constraints

| Tree Size (n = nodes) | Acceptable Time Complexity | Acceptable Space Complexity | Likely Techniques | Example Problem Types |
|-----------------------|----------------------------|----------------------------|-------------------|------------------------|
| n ≤ 20 | O(2^n) | O(n) | Recursive tree traversal with combinatorial aspects | Tree DP with complex state |
| n ≤ 1,000 | O(n^2) | O(n) | Tree DP, Repeated DFS/BFS | Diameter, All-pairs LCA |
| n ≤ 100,000 | O(n) or O(n log n) | O(n) | DFS, BFS, Tree DP | Tree traversal, Path sum |
| n ≤ 1,000,000 | O(n) | O(n) or O(log n) | Efficient tree algorithms | Serialization, Iterative traversal |
| BST/AVL/RB Tree operations | O(log n) per operation | O(n) total, O(log n) per operation | Self-balancing tree operations | Insert, Delete, Find |
| LCA queries (q queries) | O(n + q log n) or O(n + q) | O(n log n) or O(n) | Sparse Table, Binary Lifting | Lowest Common Ancestor |

## Dynamic Programming Constraints

| DP State Space Size | Acceptable Time Complexity | Acceptable Space Complexity | Optimization Techniques | Example Problem Types |
|---------------------|----------------------------|----------------------------|-------------------------|------------------------|
| 1D DP, n ≤ 100,000 | O(n) | O(n) | Linear DP | Fibonacci, Climbing stairs |
| 1D DP, n ≤ 1,000,000 | O(n) | O(1) or O(k) | Space optimization, Sliding window | House robber, Best time to buy and sell stock |
| 2D DP, n,m ≤ 100 | O(n^2 × m^2) | O(n × m) | Matrix chain multiplication | 4-dimensional states |
| 2D DP, n,m ≤ 1,000 | O(n × m) | O(n × m) | 2D grid DP | Edit distance, Longest common subsequence |
| 2D DP, n,m ≤ 5,000 | O(n × m) | O(min(n, m)) | 1D space optimization | Knapsack, Edit distance (optimized) |
| 2D DP, n ≤ 10,000, m ≤ 100 | O(n × m) | O(m) | Small dimension space optimization | Bounded knapsack, Coin change |
| Bitmask DP, n ≤ 20 | O(2^n × n) | O(2^n) | State compression | Traveling salesman, Subset problems |
| Interval DP, n ≤ 1,000 | O(n^3) | O(n^2) | Bottom-up with increasing interval width | Matrix chain multiplication, Optimal BST |

## Number Theory & Math Constraints

| Value Range | Acceptable Time Complexity | Acceptable Space Complexity | Likely Techniques | Example Problem Types |
|-------------|----------------------------|----------------------------|-------------------|------------------------|
| n ≤ 10^9, operations ≤ 10^5 | O(log n) per operation | O(1) | Binary exponentiation, GCD | Modular arithmetic, GCD |
| n ≤ 10^18 | O(log n) | O(log n) | Logarithmic algorithms | Fast exponentiation, Divide & conquer |
| Prime checking, n ≤ 10^9 | O(√n) | O(1) | Primality test | Is prime, Prime factorization |
| Prime checking, n ≤ 10^18 | O(log^2 n) | O(1) | Miller-Rabin, deterministic for specific ranges | Primality test for large numbers |
| Sieve operations, n ≤ 10^6 | O(n log log n) build, O(1) query | O(n) | Sieve of Eratosthenes | Generate primes, Prime factors |
| Sieve operations, n ≤ 10^8 | O(n) build, O(1) query | O(n) | Linear sieve | Generate primes, Multiplicative functions |
| Factorials, n ≤ 10^6 | O(n) precomputation, O(1) query | O(n) | Precomputed factorials, modular inverse | Combinations, Permutations count |
| GCD of array, n ≤ 10^5 | O(n log max(arr)) | O(1) | Euclidean algorithm | GCD, LCM of multiple numbers |

## Query Processing Constraints

| Query Type & Count | Acceptable Time Complexity | Acceptable Space Complexity | Likely Data Structures | Example Problem Types |
|--------------------|----------------------------|----------------------------|------------------------|------------------------|
| q ≤ 10^5, array n ≤ 10^5 | O(q log n) or O(n log n + q) | O(n) | Segment tree, Fenwick tree, Sparse table | Range queries, Point updates |
| q ≤ 10^5, static range queries | O(n + q) | O(n) | Prefix sum, Sparse table | Range sum, RMQ (static) |
| q ≤ 10^5, range updates + queries | O(q log n) | O(n) | Segment tree with lazy propagation, Fenwick tree | Range updates, Range queries |
| q ≤ 10^5, balanced BST operations | O(q log n) | O(n) | Red-black tree, AVL tree, Treap | Order statistics, Range queries on dynamic set |
| q ≤ 10^5, LCA queries | O(n log n + q log n) or O(n + q) | O(n log n) or O(n) | Binary lifting, Sparse table | Lowest common ancestor |
| q ≤ 10^5, path queries on tree | O(n log n + q log n) | O(n log n) | Heavy-light decomposition, Euler tour | Path sum, Path min/max |
| q ≤ 10^9, n ≤ 10^5 (offline queries) | O((n+q) log (n+q)) | O(n+q) | Mo's algorithm, Square root decomposition | Range distinct elements, Frequency counting |

## Memory Constraints

| Available Memory | Maximum Data Structure Size | Techniques to Consider | Techniques to Avoid | Example Optimizations |
|------------------|-----------------------------|------------------------|---------------------|------------------------|
| 16 MB | Arrays ≤ 4×10^6 integers | In-place algorithms, Bit manipulation | Large auxiliary arrays, Recursive calls with large stack | Use `int8_t`/`char` instead of `int` when possible |
| 64 MB | Arrays ≤ 16×10^6 integers | Space-optimized DP, Stream processing | Deep recursion, Large 2D arrays | Rolling array technique for DP |
| 128 MB | Arrays ≤ 32×10^6 integers | Standard techniques | Quadratic space for n>5000 | Reuse temporary arrays |
| 256 MB | Arrays ≤ 64×10^6 integers | Most standard techniques | Cubic space for n>600 | Keep track of array bounds carefully |
| 512 MB | Arrays ≤ 128×10^6 integers | Less constrained operations | - | Consider chunking for very large inputs |

## Recursive Call Stack Depth

| Maximum Recursion Depth | Languages/Environments | Acceptable Algorithm Types | Techniques to Consider | Techniques to Avoid |
|-------------------------|------------------------|----------------------------|------------------------|---------------------|
| ~1,000 | Python default | Logarithmic depth algorithms | Tail recursion, Iterative solutions | DFS on large trees/graphs, Deep backtracking |
| ~10,000 | C++/Java default | Tree algorithms with bounded depth | Iterative DFS/BFS, Tail recursion | Deep combinatorial recursion |
| ~100,000 | Adjusted stack size | Standard recursive algorithms | Memoization to avoid redundant calls | Excessive stack variables |
| ~1,000,000 | Custom stack settings | Most recursive algorithms | Consider depth bounds | Exponential branching factors |

## Constraints Correlation Table (Input vs. Expected Complexity)

| Problem Element | Small Input (n≤100) | Medium Input (n≤10^4) | Large Input (n≤10^5) | Very Large Input (n≤10^6+) |
|-----------------|--------------------|-----------------------|----------------------|---------------------------|
| Array Operations | O(n^2) to O(n^3) | O(n log n) | O(n) | O(n) or better |
| String Processing | O(n^2) | O(n log n) | O(n) | O(n) |
| Sorting | O(n^2) | O(n log n) | O(n log n) | Radix/counting sort O(n) |
| Graph (V,E) | O(V^3) or O(V×E) | O(E log V) | O(V+E) | O(V+E) |
| DP States | O(n^3) or O(2^n) | O(n^2) | O(n) | 1D DP only O(n) |
| Tree Operations | O(n^2) | O(n log n) | O(n) | O(n) |
| Binary Search | O(log n) always acceptable at any input size, even for n≤10^18 |
| Number Theory | O(√n) | O(log n) | O(log n) | O(log n) |

## Special Case: Multiple Constraints Interaction

| Constraint Combination | Acceptable Time Complexity | Likely Algorithm Pattern | Example Problem Types |
|------------------------|----------------------------|--------------------------|------------------------|
| n ≤ 10^5, q ≤ 10^5 | O((n+q) log n) | Segment/Fenwick tree, balanced BST | Range queries with updates |
| n ≤ 10^5, m ≤ 10^5 | O(n+m) or O((n+m) log (n+m)) | Linear processing, Efficient sorting | Two array processing, Merging |
| V ≤ 10^5, E ≤ 10^5, q ≤ 10^5 | O((V+E+q) log V) | Dijkstra with priority queue, Offline queries | Shortest path queries |
| n ≤ 10^3, k ≤ 10^9 | O(n log k) | Binary exponentiation, Matrix exponentiation | Large power computations |
| n ≤ 10^6, queries involve prime factors | O(n log log n + q log n) | Sieve preprocessing + efficient queries | Number theory with queries |
| n ≤ 10^5, 2D grid with m ≤ 10^5 | O(n×m) | Grid traversal, 2D prefix sums | Grid path problems, 2D range queries |
| n ≤ 10^3, states ≤ 2^20 | O(n × 2^n) | Bitmask DP, Meet in the middle | Subset problems, TSP variants |
