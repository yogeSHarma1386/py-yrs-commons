# Advanced DSA for 10+ Year Backend Engineers: Python Edition

## Table of Contents
- [Introduction](#introduction)
- [Advanced Data Structures](#advanced-data-structures)
  - [Specialized Trees](#specialized-trees)
  - [Concurrent Data Structures](#concurrent-data-structures)
  - [Probabilistic Data Structures](#probabilistic-data-structures)
  - [Custom Cache Implementations](#custom-cache-implementations)
- [Algorithm Deep Dives](#algorithm-deep-dives)
  - [Graph Algorithms at Scale](#graph-algorithms-at-scale)
  - [Distributed Algorithms](#distributed-algorithms)
  - [Optimization Algorithms](#optimization-algorithms)
  - [String and Text Processing](#string-and-text-processing)
- [Real-World DSA Patterns](#real-world-dsa-patterns)
  - [Rate Limiting & Throttling](#rate-limiting--throttling)
  - [Consistent Hashing](#consistent-hashing)
  - [Write-Ahead Logging](#write-ahead-logging)
  - [Backpressure Mechanisms](#backpressure-mechanisms)
- [Performance Optimization](#performance-optimization)
  - [Memory Access Patterns](#memory-access-patterns)
  - [Thread-Safe Programming](#thread-safe-programming)
  - [Data-Oriented Design](#data-oriented-design)
- [System Design with DSA](#system-design-with-dsa)
  - [Partitioning Strategies](#partitioning-strategies)
  - [Replication Algorithms](#replication-algorithms)
  - [Consensus Protocols](#consensus-protocols)
- [Problem-Solving Techniques](#problem-solving-techniques)
- [Interview Preparation](#interview-preparation)

## Introduction

After 10+ years as a backend engineer, you're expected to have mastered not just basic data structures and algorithms, but also their advanced applications, trade-offs, and real-world optimizations. This guide expands beyond HelloInterview.com's content to cover the deep DSA knowledge senior backend engineers should possess, with a focus on Python implementations.

## Advanced Data Structures

### Specialized Trees

#### B-Trees and B+ Trees

B-trees and B+ trees form the backbone of databases and file systems. As a senior engineer, you need a deep understanding of their implementation:

```python
class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t  # Minimum degree

    def search(self, k, node=None):
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1

        if i < len(node.keys) and k == node.keys[i]:
            return (node, i)

        if node.leaf:
            return None

        return self.search(k, node.children[i])

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            # Root is full, create new root
            new_root = BTreeNode(False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(new_root, k)
        else:
            self._insert_non_full(root, k)

    def _split_child(self, parent, index):
        t = self.t
        child = parent.children[index]
        new_child = BTreeNode(child.leaf)

        # Move keys and children
        parent.keys.insert(index, child.keys[t-1])
        parent.children.insert(index + 1, new_child)

        new_child.keys = child.keys[t:]
        child.keys = child.keys[:t-1]

        if not child.leaf:
            new_child.children = child.children[t:]
            child.children = child.children[:t]

    def _insert_non_full(self, node, k):
        i = len(node.keys) - 1

        if node.leaf:
            # Insert into leaf
            while i >= 0 and k < node.keys[i]:
                i -= 1
            node.keys.insert(i + 1, k)
        else:
            # Insert into internal node
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1

            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i)
                if k > node.keys[i]:
                    i += 1

            self._insert_non_full(node.children[i], k)
```

#### Segment Trees

Segment trees enable efficient range queries and updates in logarithmic time:

```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        # 4n is a safe size for the segment tree
        self.tree = [0] * (4 * self.n)
        self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        """
        Build the segment tree recursively
        """
        if start == end:
            # Leaf node
            self.tree[node] = arr[start]
            return

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        # Recursively build left and right subtrees
        self._build(arr, left_child, start, mid)
        self._build(arr, right_child, mid + 1, end)

        # Internal node stores the sum of its children
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, index, value):
        """
        Update the value at the given index
        """
        self._update(0, 0, self.n - 1, index, value)

    def _update(self, node, start, end, index, value):
        if start == end:
            # Leaf node: update the value
            self.tree[node] = value
            return

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        if index <= mid:
            # Index is in the left subtree
            self._update(left_child, start, mid, index, value)
        else:
            # Index is in the right subtree
            self._update(right_child, mid + 1, end, index, value)

        # Update the internal node
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, left, right):
        """
        Query the sum in the range [left, right]
        """
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        # No overlap
        if right < start or end < left:
            return 0

        # Complete overlap
        if left <= start and end <= right:
            return self.tree[node]

        # Partial overlap: query both children
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        left_sum = self._query(left_child, start, mid, left, right)
        right_sum = self._query(right_child, mid + 1, end, left, right)

        return left_sum + right_sum
```

#### Advanced Trie Implementations

Tries with path compression (Radix Trees) optimize space usage:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """Search for a word in the trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """Check if any word starts with the given prefix"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

class RadixTreeNode:
    def __init__(self):
        self.children = {}  # {edge_label: node}
        self.is_end_of_word = False

class RadixTree:
    """A space-optimized trie with path compression"""
    def __init__(self):
        self.root = RadixTreeNode()

    def insert(self, word):
        self._insert(self.root, word)

    def _insert(self, node, word):
        if not word:
            node.is_end_of_word = True
            return

        # Find matching prefix with existing edges
        for edge, child in node.children.items():
            i = 0
            while i < len(edge) and i < len(word) and edge[i] == word[i]:
                i += 1

            if i > 0:
                # Common prefix found
                if i == len(edge):
                    # Edge fully matched, continue with remaining word
                    self._insert(child, word[i:])
                else:
                    # Edge partially matched, split the edge
                    new_node = RadixTreeNode()
                    new_edge = edge[i:]
                    node.children[edge[:i]] = new_node
                    new_node.children[new_edge] = child
                    del node.children[edge]

                    if i == len(word):
                        # Word fully consumed
                        new_node.is_end_of_word = True
                    else:
                        # Insert remaining word
                        new_node.children[word[i:]] = RadixTreeNode()
                        new_node.children[word[i:]].is_end_of_word = True
                return

        # No matching prefix, add new edge
        node.children[word] = RadixTreeNode()
        node.children[word].is_end_of_word = True

    def search(self, word):
        return self._search(self.root, word)

    def _search(self, node, word):
        if not word:
            return node.is_end_of_word

        for edge, child in node.children.items():
            if word.startswith(edge):
                return self._search(child, word[len(edge):])

        return False
```

### Probabilistic Data Structures

Space-efficient structures that trade accuracy for performance:

#### Bloom Filters

```python
import math
import mmh3  # MurmurHash3 library

class BloomFilter:
    def __init__(self, capacity, error_rate=0.001):
        """
        Initialize a Bloom Filter

        capacity: Expected number of elements
        error_rate: Acceptable false positive rate
        """
        self.capacity = capacity
        self.error_rate = error_rate

        # Calculate optimal size and number of hash functions
        self.size = self._get_size(capacity, error_rate)
        self.hash_count = self._get_hash_count(self.size, capacity)

        # Initialize bit array
        self.bit_array = [0] * self.size

    def _get_size(self, n, p):
        """Calculate optimal bit array size"""
        return int(-(n * math.log(p)) / (math.log(2) ** 2))

    def _get_hash_count(self, m, n):
        """Calculate optimal number of hash functions"""
        return int((m / n) * math.log(2))

    def _get_hash_values(self, item):
        """Generate hash values for an item"""
        # Use two hash functions to simulate k hash functions
        h1 = mmh3.hash(str(item), 0)
        h2 = mmh3.hash(str(item), 1)

        return [(h1 + i * h2) % self.size for i in range(self.hash_count)]

    def add(self, item):
        """Add an item to the filter"""
        for index in self._get_hash_values(item):
            self.bit_array[index] = 1

    def contains(self, item):
        """Check if an item might be in the filter"""
        for index in self._get_hash_values(item):
            if self.bit_array[index] == 0:
                return False
        return True

    def __len__(self):
        """Estimate the number of elements in the filter"""
        # Count the number of bits set to 1
        X = sum(self.bit_array)

        # Estimate cardinality using the formula
        # n = -m/k * ln(1 - X/m) where m is size, k is hash count
        if X == 0:
            return 0
        return int(-(self.size / self.hash_count) * math.log(1 - X / self.size))
```

#### HyperLogLog for Cardinality Estimation

```python
import math
import mmh3

class HyperLogLog:
    def __init__(self, precision=10):
        """
        Initialize HyperLogLog for cardinality estimation

        precision: Determines the number of registers (2^precision)
        """
        self.precision = precision
        self.m = 1 << precision  # Number of registers
        self.registers = [0] * self.m
        self.alpha = self._get_alpha(self.m)

    def _get_alpha(self, m):
        """Get the bias correction factor alpha"""
        if m == 16:
            return 0.673
        elif m == 32:
            return 0.697
        elif m == 64:
            return 0.709
        else:
            return 0.7213 / (1 + 1.079 / m)

    def add(self, item):
        """Add an item to the estimator"""
        # Hash the item
        item_hash = mmh3.hash(str(item), 0)

        # Get the first precision bits to determine the register
        register_idx = item_hash & (self.m - 1)

        # Count the number of leading zeros in the remaining bits
        # plus 1 (to avoid log(0))
        bit_pattern = item_hash >> self.precision
        leading_zeros = min(32, self._count_leading_zeros(bit_pattern) + 1)

        # Update the register if the new value is larger
        self.registers[register_idx] = max(self.registers[register_idx], leading_zeros)

    def _count_leading_zeros(self, value):
        """Count the number of leading zeros in a 32-bit integer"""
        if value == 0:
            return 32

        return 31 - value.bit_length()

    def cardinality(self):
        """Estimate the cardinality (number of unique items)"""
        # Calculate the harmonic mean of register values
        sum_inv = sum(math.pow(2, -register) for register in self.registers)
        estimate = self.alpha * (self.m ** 2) / sum_inv

        # Apply corrections for small and large cardinalities
        if estimate <= 2.5 * self.m:  # Small range correction
            zeros = self.registers.count(0)
            if zeros > 0:
                estimate = self.m * math.log(self.m / zeros)

        if estimate > (1 << 32) / 30:  # Large range correction
            estimate = -1 * (1 << 32) * math.log(1 - estimate / (1 << 32))

        return int(estimate)
```

#### Count-Min Sketch for Frequency Estimation

```python
import mmh3
import numpy as np

class CountMinSketch:
    def __init__(self, width=2000, depth=5):
        """
        Initialize Count-Min Sketch for frequency estimation

        width: Number of columns (counters per hash function)
        depth: Number of rows (hash functions)
        """
        self.width = width
        self.depth = depth
        self.table = np.zeros((depth, width), dtype=np.int32)
        self.seeds = np.arange(depth)  # Seeds for hash functions

    def add(self, item, count=1):
        """Add an item with the given count"""
        for i in range(self.depth):
            j = mmh3.hash(str(item), self.seeds[i]) % self.width
            self.table[i, j] += count

    def estimate(self, item):
        """Estimate the frequency of an item"""
        # Find the minimum value across all hash functions
        min_val = float('inf')
        for i in range(self.depth):
            j = mmh3.hash(str(item), self.seeds[i]) % self.width
            min_val = min(min_val, self.table[i, j])

        return min_val

    def merge(self, other):
        """Merge with another Count-Min Sketch"""
        if self.width != other.width or self.depth != other.depth:
            raise ValueError("Dimensions must match")

        result = CountMinSketch(self.width, self.depth)
        result.table = self.table + other.table
        return result

    def heavy_hitters(self, threshold):
        """
        This method is not directly possible with Count-Min Sketch
        without additional data structures or storing all items.
        In practice, we would use this with a stream of items and
        keep track of potential heavy hitters separately.
        """
        pass
```

### Custom Cache Implementations

#### LRU Cache with O(1) Operations

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Maps key to node

        # Create dummy head and tail nodes
        self.head = Node(0, 0)  # Most recently used
        self.tail = Node(0, 0)  # Least recently used
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """Add node right after head (most recently used)"""
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Remove a node from the doubly linked list"""
        prev = node.prev
        next_node = node.next

        prev.next = next_node
        next_node.prev = prev

    def _move_to_head(self, node):
        """Move an existing node to the head (mark as most recently used)"""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """Remove and return the least recently used node"""
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key):
        """Get value by key and mark as recently used"""
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        """Add or update a key-value pair"""
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
            return

        # Add new key
        node = Node(key, value)
        self.cache[key] = node
        self._add_node(node)

        # Check capacity
        if len(self.cache) > self.capacity:
            # Remove least recently used
            lru = self._pop_tail()
            del self.cache[lru.key]
```

#### SLRU (Segmented LRU) Cache

```python
class SLRUCache:
    def __init__(self, protected_size, probationary_size):
        """
        Initialize Segmented LRU Cache

        protected_size: Size of the protected segment
        probationary_size: Size of the probationary segment
        """
        self.protected = LRUCache(protected_size)
        self.probationary = LRUCache(probationary_size)

    def get(self, key):
        """Get value by key and update segments"""
        # Check protected segment first
        value = self.protected.get(key)
        if value != -1:
            # Already in protected
            return value

        # Check probationary segment
        value = self.probationary.get(key)
        if value != -1:
            # Promote to protected segment
            self.probationary._pop_tail()  # This isn't accurate but simplifies
            self.protected.put(key, value)
            return value

        return -1

    def put(self, key, value):
        """Add or update a key-value pair"""
        # Check if already in protected
        if self.protected.get(key) != -1:
            self.protected.put(key, value)
            return

        # Check if in probationary
        if self.probationary.get(key) != -1:
            # Promote to protected
            self.probationary._pop_tail()  # This isn't accurate but simplifies
            self.protected.put(key, value)
            return

        # New item goes to probationary
        if len(self.probationary.cache) >= self.probationary.capacity:
            # If probationary is full
            lru = self.probationary._pop_tail()
            del self.probationary.cache[lru.key]

        self.probationary.put(key, value)
```

## Algorithm Deep Dives

### Graph Algorithms at Scale

#### Parallel Breadth-First Search

```python
import threading
from collections import deque
import queue

def parallel_bfs(graph, start, num_threads=4):
    """
    Parallel implementation of BFS using threads

    graph: Adjacency list representation of the graph
    start: Starting vertex
    num_threads: Number of worker threads to use
    """
    n = len(graph)
    distances = [-1] * n  # -1 means not visited
    distances[start] = 0

    # Queue of nodes to process
    frontier = queue.Queue()
    frontier.put(start)

    # Set of nodes to visit in next level
    next_frontier = queue.Queue()

    # Synchronization barriers
    level_complete = threading.Barrier(num_threads + 1)  # +1 for main thread

    # Lock for next_frontier
    next_lock = threading.Lock()

    # Thread-safe visited set
    visited_lock = threading.Lock()
    visited = {start}

    def worker():
        while True:
            # Get nodes to process for this level
            local_nodes = []
            while not frontier.empty():
                try:
                    local_nodes.append(frontier.get_nowait())
                except queue.Empty:
                    break

            if not local_nodes:
                # No more nodes at this level
                level_complete.wait()

                # Check if we're done completely
                if next_frontier.empty():
                    return

                # Move to next level
                with next_lock:
                    while not next_frontier.empty():
                        try:
                            frontier.put(next_frontier.get_nowait())
                        except queue.Empty:
                            break

                level_complete.wait()
                continue

            # Process nodes at current level
            for node in local_nodes:
                current_dist = distances[node]

                # Add unvisited neighbors to next level
                for neighbor in graph[node]:
                    with visited_lock:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            distances[neighbor] = current_dist + 1
                            next_frontier.put(neighbor)

            # Wait for all threads to finish current level
            level_complete.wait()

            # Check if we're done
            if next_frontier.empty():
                return

            # Move to next level
            with next_lock:
                while not next_frontier.empty():
                    try:
                        frontier.put(next_frontier.get_nowait())
                    except queue.Empty:
                        break

            level_complete.wait()

    # Start worker threads
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    # Wait for all threads to complete
    for t in threads:
        t.join()

    return distances
```

#### A* Pathfinding with Optimizations

```python
import heapq
import math

def a_star(graph, start, goal, heuristic):
    """
    A* pathfinding algorithm with optimizations

    graph: Weighted adjacency list {node: [(neighbor, cost), ...]}
    start: Starting node
    goal: Goal node
    heuristic: Function that estimates distance from node to goal
    """
    # Priority queue of (f_score, node)
    open_set = [(heuristic(start, goal), 0, start)]  # (f_score, g_score, node)

    # For node n, came_from[n] is the node preceding it on the path
    came_from = {}

    # For node n, g_score[n] is the cost from start to n
    g_score = {start: 0}

    # For node n, f_score[n] = g_score[n] + heuristic(n, goal)
    f_score = {start: heuristic(start, goal)}

    # Set of visited nodes for O(1) lookup
    visited = set()

    while open_set:
        # Get node with lowest f_score
        _, current_g, current = heapq.heappop(open_set)

        # Check if already processed this node with a better path
        if current in visited and current_g > g_score[current]:
            continue

        visited.add(current)

        # If goal reached, reconstruct and return path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        # Explore neighbors
        for neighbor, cost in graph[current]:
            # Calculate tentative g_score
            tentative_g = g_score[current] + cost

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                # This path is better than any previous one
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                f_score[neighbor] = f

                # Add to open set if not visited
                if neighbor not in visited:
                    heapq.heappush(open_set, (f, tentative_g, neighbor))

    # No path found
    return None
```

### Distributed Algorithms

#### Distributed Consistent Hashing

```python
import hashlib
import bisect

class ConsistentHash:
    def __init__(self, nodes=None, replicas=100):
        """
        Initialize consistent hashing ring

        nodes: Initial set of nodes
        replicas: Number of virtual nodes per physical node
        """
        self.replicas = replicas
        self.ring = {}  # Map of hash values to nodes
        self.sorted_keys = []  # Sorted list of hash values

        if nodes:
            for node in nodes:
                self.add_node(node)

    def _hash(self, key):
        """Generate a hash value for a key"""
        key_bytes = str(key).encode('utf-8')
        return int(hashlib.md5(key_bytes).hexdigest(), 16)

    def add_node(self, node):
        """Add a node to the hash ring"""
        for i in range(self.replicas):
            # Create virtual node
            virtual_node_key = f"{node}:{i}"
            hash_value = self._hash(virtual_node_key)

            # Add to ring
            self.ring[hash_value] = node

            # Add to sorted keys
            bisect.insort(self.sorted_keys, hash_value)

    def remove_node(self, node):
        """Remove a node from the hash ring"""
        for i in range(self.replicas):
            virtual_node_key = f"{node}:{i}"
            hash_value = self._hash(virtual_node_key)

            if hash_value in self.ring:
                del self.ring[hash_value]
                self.sorted_keys.remove(hash_value)

    def get_node(self, key):
        """Get the node responsible for a key"""
        if not self.ring:
            return None

        # Generate hash for the key
        hash_value = self._hash(key)

        # Find the first node with hash >= key's hash
        idx = bisect.bisect(self.sorted_keys, hash_value)

        # Wrap around to the first node if past the end
        if idx == len(self.sorted_keys):
            idx = 0

        # Return the corresponding node
        return self.ring[self.sorted_keys[idx]]

    def get_nodes(self, key, count=1):
        """Get multiple nodes for a key (for replication)"""
        if len(self.ring) < count:
            return self.get_all_nodes()

        nodes = []
        for i in range(count):
            node = self.get_node(f"{key}:{i}")
            while node in nodes:
                # Avoid duplicates
                node = self.get_node(f"{key}:{i}:{len(nodes)}")
            nodes.append(node)

        return nodes

    def get_all_nodes(self):
        """Get all unique nodes in the ring"""
        return set(self.ring.values())