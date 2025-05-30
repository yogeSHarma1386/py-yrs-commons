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

| Function | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description |
|----------|---------------------------------|-------------------------|------------------|-------------|
|---------------------------------| **Array/List Operations** |
| Push/Append | O(1) | O(1) | O(1) | Add element to end |
| Pop | O(1) | O(1) | O(1) | Remove from end |
| Insert | O(1) (at end) | O(n) (at beginning) | O(1) | Add at specific index |
| Delete | O(1) (at end) | O(n) (at beginning) | O(1) | Remove at specific index |
| Search | O(1) (if index known) | O(n) (linear search) | O(1) | Find element |
| Binary Search | O(1) (lucky guess) | O(log n) | O(1) | Find in sorted array |

| Function | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description |
|----------|---------------------------------|-------------------------|------------------|-------------|
|---------------------------------| **Stack Operations** |
| Push | O(1) | O(1) | O(1) | Add to top |
| Pop | O(1) | O(1) | O(1) | Remove from top |
| Peek/Top | O(1) | O(1) | O(1) | View top element |

| Function | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description |
|----------|---------------------------------|-------------------------|------------------|-------------|
|---------------------------------| **Queue Operations** |
| Enqueue | O(1) | O(1) | O(1) | Add to rear |
| Dequeue | O(1) | O(1) | O(1) | Remove from front |
| Front | O(1) | O(1) | O(1) | View front element |

| Function | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description |
|----------|---------------------------------|-------------------------|------------------|-------------|
|---------------------------------| **Linked List Operations** |
| Insert | O(1) (at head/tail) | O(n) (at middle) | O(1) | Add new node |
| Delete | O(1) (at head) | O(n) (at middle/tail) | O(1) | Remove node |
| Search | O(1) (at head) | O(n) (at tail) | O(1) | Find element |

| Function | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description |
|----------|---------------------------------|-------------------------|------------------|-------------|
|---------------------------------| **Heap Operations** |
| Insert | O(1) (lucky case) | O(log k) | O(1) | Add element |
| Extract Min/Max | O(log k) | O(log k) | O(1) | Remove root |
| Heapify | O(k) | O(k) | O(1) | Build heap |
| Peek/Find Min/Max | O(1) | O(1) | O(1) | View root element |
| Decrease/Increase Key | O(1) (lucky case) | O(log k) | O(1) | Update priority |
| Delete | O(log k) | O(log k) | O(1) | Remove specific element |
| Merge Heaps | O(k) | O(k) | O(k) | Combine two heaps |

| Function | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description |
|----------|---------------------------------|-------------------------|------------------|-------------|
|---------------------------------| **Hash Table Operations** |
| Insert | O(1) (no collision) | O(n) (many collisions) | O(1) | Add key-value pair |
| Delete | O(1) (no collision) | O(n) (many collisions) | O(1) | Remove key-value pair |
| Search | O(1) (no collision) | O(n) (many collisions) | O(1) | Find by key |
| Rehash | O(n) | O(n) | O(n) | Resize table |

| Function                           | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description |
|------------------------------------|---------------------------------|-------------------------|------------------|-------------|
| ---------------------------------  | **Sorting Algorithms** |
| QuickSort                          | O(n log n) | O(n²) | O(log n) | Divide and conquer sorting |
| MergeSort                          | O(n log n) | O(n log n) | O(n) | Divide and conquer sorting |
| HeapSort                           | O(n log n) | O(n log n) | O(1) | Heap-based sorting |
| BubbleSort                         | O(n) (already sorted) | O(n²) | O(1) | Simple comparison sort |
| InsertionSort                      | O(n) (already sorted) | O(n²) | O(1) | Simple comparison sort |
| SelectionSort                      | O(n²) | O(n²) | O(1) | Simple comparison sort |
| CountingSort                       | O(n+k) | O(n+k) | O(k) | Integer sorting |
| RadixSort                          | O(d(n+k)) | O(d(n+k)) | O(n+k) | Integer sorting |

| Function                          | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description |
|-----------------------------------|---------------------------------|-------------------------|------------------|-------------|
| --------------------------------- | **String Operations** |
| KMP Search                        | O(n+m) | O(n+m) | O(m) | Pattern matching |
| Rabin-Karp                        | O(n+m) | O(n·m) | O(1) | Pattern matching with hashing |
| Z-Algorithm                       | O(n+m) | O(n+m) | O(n+m) | Pattern matching |
| Suffix Array                      | O(n) | O(n log² n) | O(n) | Suffix sorting |
| Longest Common Prefix             | O(m) | O(m) | O(1) | Find common prefix |

| Function | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description |
|----------|---------------------------------|-------------------------|------------------|-------------|
|---------------------------------| **Trie Operations** |
| Insert | O(m) | O(m) | O(m) | Add string to trie |
| Search | O(m) | O(m) | O(1) | Find string in trie |
| Delete | O(m) | O(m) | O(1) | Remove string from trie |
| Prefix Search | O(m+z) | O(m+z) | O(z) | Find all strings with prefix |

| Function | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description |
|----------|---------------------------------|-------------------------|------------------|-------------|
|---------------------------------| **Union-Find** |
| MakeSet | O(1) | O(1) | O(1) | Create new set |
| Find | O(1) (path compression) | O(log n) (worst case) | O(1) | Find representative |
| Union | O(1) (rank/size heuristic) | O(log n) (worst case) | O(1) | Merge two sets |

| Function | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description |
|----------|---------------------------------|-------------------------|------------------|-------------|
|---------------------------------| **Binary Search Tree** |
| Insert | O(log n) (balanced) | O(n) (unbalanced) | O(1) | Add new node |
| Delete | O(log n) (balanced) | O(n) (unbalanced) | O(1) | Remove node |
| Search | O(log n) (balanced) | O(n) (unbalanced) | O(1) | Find element |
| Height | O(1) (stored) | O(n) (compute) | O(1) | Tree height |
| Traversal | O(n) | O(n) | O(h) | Visit all nodes |

| Function | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description |
|----------|---------------------------------|-------------------------|------------------|-------------|
|---------------------------------| **BST (height-based)** |
| Insert | O(h)                   | O(h) | O(1) | Add new node |
| Delete | O(h)                   | O(h) | O(1) | Remove node |
| Search | O(h)                   | O(h) | O(1) | Find element |

| Function | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description |
|----------|---------------------------------|-------------------------|------------------|-------------|
|---------------------------------| **Balanced Tree (AVL, Red-Black)** |
| Insert | O(log n) | O(log n) | O(1) | Add new node |
| Delete | O(log n) | O(log n) | O(1) | Remove node |
| Search | O(log n) | O(log n) | O(1) | Find element |
| Rebalance | O(1) (single rotation) | O(log n) (multiple rotations) | O(1) | Restore balance |

| Function                           | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Description |
|------------------------------------|---------------------------------|-------------------------|------------------|-------------|
| ---------------------------------- | **Graph Operations** |
| BFS                                | O(V+E) | O(V+E) | O(V) | Breadth-First Search |
| DFS                                | O(V+E) | O(V+E) | O(V) | Depth-First Search |
| Dijkstra                           | O(E + V log V) | O(E + V log V) | O(V) | Shortest path |
| Bellman-Ford                       | O(V·E) | O(V·E) | O(V) | Shortest path with negative edges |
| Floyd-Warshall                     | O(V³) | O(V³) | O(V²) | All-pairs shortest path |
| Prim's                             | O(E log V) | O(E log V) | O(V) | Minimum Spanning Tree |
| Kruskal's                          | O(E log E) | O(E log E) | O(V) | Minimum Spanning Tree |
| Topological Sort                   | O(V+E) | O(V+E) | O(V) | DAG ordering |
