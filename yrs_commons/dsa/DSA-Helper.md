# 🎯🎯🎯 15 Most Important LeetCode Patterns to Master

LeetCode is less about the number of problems you have solved and more about how many patterns you know. Learning patterns enables you to solve a wide variety of problems in lesser time and helps you quickly identify the right approach to a problem you have never seen before.

This guide covers the 15 most important patterns that will make your LeetCode journey significantly easier.

---

## 1. Prefix Sum

Prefix Sum involves preprocessing an array to create a new array where each element at index i represents the sum of the array from the start up to i. This allows for efficient sum queries on subarrays.

Use this pattern when you need to perform multiple sum queries on a subarray or need to calculate cumulative sums.

### Sample Problem:
Given an array nums, answer multiple queries about the sum of elements within a specific range [i, j].

**Example:**
- Input: `nums = [1, 2, 3, 4, 5, 6]`, `i = 1`, `j = 3`
- Output: `9`

**Explanation:**
Preprocess the array A to create a prefix sum array: `P = [1, 3, 6, 10, 15, 21]`.
To find the sum between indices i and j, use the formula: `P[j] - P[i-1]`.

### LeetCode Problems:
- Range Sum Query - Immutable [Leetcode #303](https://leetcode.com/problems/range-sum-query-immutable/) [Lintcode #943](https://www.lintcode.com/problem/943/)
- Contiguous Array [Leetcode #525](https://leetcode.com/problems/contiguous-array/) [Lintcode #994](https://www.lintcode.com/problem/994/)
- Subarray Sum Equals K [Leetcode #560](https://leetcode.com/problems/subarray-sum-equals-k/) [Lintcode #838](https://www.lintcode.com/problem/838/)

---

## 2. Two Pointers

The Two Pointers pattern involves using two pointers to iterate through an array or list, often used to find pairs or elements that meet specific criteria.

Use this pattern when dealing with sorted arrays or lists where you need to find pairs that satisfy a specific condition.

### Sample Problem:
Find two numbers in a sorted array that add up to a target value.

**Example:**
- Input: `nums = [1, 2, 3, 4, 6]`, `target = 6`
- Output: `[1, 3]`

**Explanation:**
Initialize two pointers, one at the start (left) and one at the end (right) of the array. Check the sum of the elements at the two pointers. If the sum equals the target, return the indices. If the sum is less than the target, move the left pointer to the right. If the sum is greater than the target, move the right pointer to the left.

### LeetCode Problems:
- Two Sum II - Input Array is Sorted [Leetcode #167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) [Lintcode #608](https://www.lintcode.com/problem/608/)
- 3Sum [Leetcode #15](https://leetcode.com/problems/3sum/) [Lintcode #57](https://www.lintcode.com/problem/57/)
- Container With Most Water [Leetcode #11](https://leetcode.com/problems/container-with-most-water/) [Lintcode #383](https://www.lintcode.com/problem/383/)

---

## 3. Sliding Window

The Sliding Window pattern is used to find a subarray or substring that satisfies a specific condition, optimizing the time complexity by maintaining a window of elements.

Use this pattern when dealing with problems involving contiguous subarrays or substrings.

### Sample Problem:
Find the maximum sum of a subarray of size k.

**Example:**
- Input: `nums = [2, 1, 5, 1, 3, 2]`, `k = 3`
- Output: `9`

**Explanation:**
Start with the sum of the first k elements. Slide the window one element at a time, subtracting the element that goes out of the window and adding the new element. Keep track of the maximum sum encountered.

### LeetCode Problems:
- Maximum Average Subarray I [Leetcode #643](https://leetcode.com/problems/maximum-average-subarray-i/) [Lintcode #](https://www.lintcode.com/problem//)
- Longest Substring Without Repeating Characters [Leetcode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) [Lintcode #](https://www.lintcode.com/problem//)
- Minimum Window Substring [Leetcode #76](https://leetcode.com/problems/minimum-window-substring/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 4. Fast & Slow Pointers

The Fast & Slow Pointers (Tortoise and Hare) pattern is used to detect cycles in linked lists and other similar structures.

### Sample Problem:
Detect if a linked list has a cycle.

**Explanation:**
Initialize two pointers, one moving one step at a time (slow) and the other moving two steps at a time (fast). If there is a cycle, the fast pointer will eventually meet the slow pointer. If the fast pointer reaches the end of the list, there is no cycle.

### LeetCode Problems:
- Linked List Cycle [Leetcode #141](https://leetcode.com/problems/linked-list-cycle/) [Lintcode #](https://www.lintcode.com/problem//)
- Happy Number [Leetcode #202](https://leetcode.com/problems/happy-number/) [Lintcode #](https://www.lintcode.com/problem//)
- Find the Duplicate Number [Leetcode #287](https://leetcode.com/problems/find-the-duplicate-number/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 5. LinkedList In-place Reversal

The In-place Reversal of a LinkedList pattern reverses parts of a linked list without using extra space.

Use this pattern when you need to reverse sections of a linked list.

### Sample Problem:
Reverse a sublist of a linked list from position m to n.

**Example:**
- Input: `head = [1, 2, 3, 4, 5]`, `m = 2`, `n = 4`
- Output: `[1, 4, 3, 2, 5]`

**Explanation:**
Identify the start and end of the sublist. Reverse the nodes in place by adjusting the pointers.

### LeetCode Problems:
- Reverse Linked List [Leetcode #206](https://leetcode.com/problems/reverse-linked-list/) [Lintcode #](https://www.lintcode.com/problem//)
- Reverse Linked List II [Leetcode #92](https://leetcode.com/problems/reverse-linked-list-ii/) [Lintcode #](https://www.lintcode.com/problem//)
- Swap Nodes in Pairs [Leetcode #24](https://leetcode.com/problems/swap-nodes-in-pairs/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 6. Monotonic Stack

The Monotonic Stack pattern uses a stack to maintain a sequence of elements in a specific order (increasing or decreasing).

Use this pattern for problems that require finding the next greater or smaller element.

### Sample Problem:
Find the next greater element for each element in an array. Output -1 if the greater element doesn't exist.

**Example:**
- Input: `nums = [2, 1, 2, 4, 3]`
- Output: `[4, 2, 4, -1, -1]`

**Explanation:**
Use a stack to keep track of elements for which we haven't found the next greater element yet. Iterate through the array, and for each element, pop elements from the stack until you find a greater element. If the stack is not empty, set the result for index at the top of the stack to current element. Push the current element onto the stack.

### LeetCode Problems:
- Next Greater Element I [Leetcode #496](https://leetcode.com/problems/next-greater-element-i/) [Lintcode #](https://www.lintcode.com/problem//)
- Daily Temperatures [Leetcode #739](https://leetcode.com/problems/daily-temperatures/) [Lintcode #](https://www.lintcode.com/problem//)
- Largest Rectangle in Histogram [Leetcode #84](https://leetcode.com/problems/largest-rectangle-in-histogram/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 7. Top 'K' Elements

The Top 'K' Elements pattern finds the top k largest or smallest elements in an array or stream of data using heaps or sorting.

### Sample Problem:
Find the k-th largest element in an unsorted array.

**Example:**
- Input: `nums = [3, 2, 1, 5, 6, 4]`, `k = 2`
- Output: `5`

**Explanation:**
Use a min-heap of size k to keep track of the k largest elements. Iterate through the array, adding elements to the heap. If the heap size exceeds k, remove the smallest element from the heap. The root of the heap will be the k-th largest element.

### LeetCode Problems:
- Kth Largest Element in an Array [Leetcode #215](https://leetcode.com/problems/kth-largest-element-in-an-array/) [Lintcode #](https://www.lintcode.com/problem//)
- Top K Frequent Elements [Leetcode #347](https://leetcode.com/problems/top-k-frequent-elements/) [Lintcode #](https://www.lintcode.com/problem//)
- Find K Pairs with Smallest Sums [Leetcode #373](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 8. Overlapping Intervals

The Overlapping Intervals pattern is used to merge or handle overlapping intervals in an array.

In an interval array sorted by start time, two intervals [a, b] and [c, d] overlap if b >= c (i.e., the end time of the first interval is greater than or equal to the start time of the second interval).

### Sample Problem:
Merge all overlapping intervals.

**Example:**
- Input: `intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]`
- Output: `[[1, 6], [8, 10], [15, 18]]`

**Explanation:**
Sort the intervals by their start time. Create an empty list called merged to store the merged intervals. Iterate through the intervals and check if it overlaps with the last interval in the merged list. If it overlaps, merge the intervals by updating the end time of the last interval in merged. If it does not overlap, simply add the current interval to the merged list.

### LeetCode Problems:
- Merge Intervals [Leetcode #56](https://leetcode.com/problems/merge-intervals/) [Lintcode #](https://www.lintcode.com/problem//)
- Insert Interval [Leetcode #57](https://leetcode.com/problems/insert-interval/) [Lintcode #](https://www.lintcode.com/problem//)
- Non-Overlapping Intervals [Leetcode #435](https://leetcode.com/problems/non-overlapping-intervals/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 9. Modified Binary Search

The Modified Binary Search pattern adapts binary search to solve a wider range of problems, such as finding elements in rotated sorted arrays.

Use this pattern for problems involving sorted or rotated arrays where you need to find a specific element.

### Sample Problem:
Find an element in a rotated sorted array.

**Example:**
- Input: `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`
- Output: `4`

**Explanation:**
Perform binary search with an additional check to determine which half of the array is sorted. We then check if the target is within the range of the sorted half. If it is, we search that half; otherwise, we search the other half.

### LeetCode Problems:
- Search in Rotated Sorted Array [Leetcode #33](https://leetcode.com/problems/search-in-rotated-sorted-array/) [Lintcode #](https://www.lintcode.com/problem//)
- Find Minimum in Rotated Sorted Array [Leetcode #153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) [Lintcode #](https://www.lintcode.com/problem//)
- Search a 2D Matrix II [Leetcode #240](https://leetcode.com/problems/search-a-2d-matrix-ii/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 10. Binary Tree Traversal

Binary Tree Traversal involves visiting all the nodes in a binary tree in a specific order.

- **PreOrder**: root → left → right
- **InOrder**: left → root → right
- **PostOrder**: left → right → root

### Sample Problem:
Perform inorder traversal of a binary tree.

**Example:**
- Input: `root = [1, null, 2, 3]`
- Output: `[1, 3, 2]`

**Explanation:**
Inorder traversal visits nodes in the order: left, root, right. Use recursion or a stack to traverse the tree in this order.

### LeetCode Problems:
- **PreOrder** → Binary Tree Paths [Leetcode #257](https://leetcode.com/problems/binary-tree-paths/) [Lintcode #](https://www.lintcode.com/problem//)
- **InOrder** → Kth Smallest Element in a BST [Leetcode #230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) [Lintcode #](https://www.lintcode.com/problem//)
- **PostOrder** → Binary Tree Maximum Path Sum [Leetcode #124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 11. Depth-First Search (DFS)

Depth-First Search (DFS) is a traversal technique that explores as far down a branch as possible before backtracking.

Use this pattern for exploring all paths or branches in graphs or trees.

### Sample Problem:
Find all paths from the root to leaves in a binary tree.

**Example:**
- Input: `root = [1, 2, 3, null, 5]`
- Output: `["1->2->5", "1->3"]`

**Explanation:**
Use recursion or a stack to traverse each path from the root to the leaves. Record each path as you traverse.

### LeetCode Problems:
- Clone Graph [Leetcode #133](https://leetcode.com/problems/clone-graph/) [Lintcode #](https://www.lintcode.com/problem//)
- Path Sum II [Leetcode #113](https://leetcode.com/problems/path-sum-ii/) [Lintcode #](https://www.lintcode.com/problem//)
- Course Schedule II [Leetcode #210](https://leetcode.com/problems/course-schedule-ii/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 12. Breadth-First Search (BFS)

Breadth-First Search (BFS) is a traversal technique that explores nodes level by level in a tree or graph.

Use this pattern for finding the shortest paths in unweighted graphs or level-order traversal in trees.

### Sample Problem:
Perform level-order traversal of a binary tree.

**Example:**
- Input: `root = [3, 9, 20, null, null, 15, 7]`
- Output: `[[3], [9, 20], [15, 7]]`

**Explanation:**
Use a queue to keep track of nodes at each level. Traverse each level and add the children of the current nodes to the queue.

### LeetCode Problems:
- Binary Tree Level Order Traversal [Leetcode #102](https://leetcode.com/problems/binary-tree-level-order-traversal/) [Lintcode #](https://www.lintcode.com/problem//)
- Rotting Oranges [Leetcode #994](https://leetcode.com/problems/rotting-oranges/) [Lintcode #](https://www.lintcode.com/problem//)
- Word Ladder [Leetcode #127](https://leetcode.com/problems/word-ladder/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 13. Matrix Traversal

Matrix Traversal involves traversing elements in a matrix using different techniques (DFS, BFS, etc.).

Use this pattern for problems involving traversing 2D grids or matrices horizontally, vertically or diagonally.

### Sample Problem:
Perform flood fill on a 2D grid. Change all the cells connected to the starting cell to new color.

**Example:**
- Input: `image = [[1,1,1],[1,1,0],[1,0,1]]`, `sr = 1`, `sc = 1`, `newColor = 2`
- Output: `[[2,2,2],[2,2,0],[2,0,1]]`

**Explanation:**
Use DFS or BFS to traverse the matrix starting from the given cell. Change the color of the connected cells to the new color.

### LeetCode Problems:
- Flood Fill [Leetcode #733](https://leetcode.com/problems/flood-fill/) [Lintcode #](https://www.lintcode.com/problem//)
- Number of Islands [Leetcode #200](https://leetcode.com/problems/number-of-islands/) [Lintcode #](https://www.lintcode.com/problem//)
- Surrounded Regions [Leetcode #130](https://leetcode.com/problems/surrounded-regions/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 14. Backtracking

Backtracking explores all possible solutions and backtracks when a solution path fails.

Use this pattern when you need to find all (or some) solutions to a problem that satisfies given constraints. For example: combinatorial problems, such as generating permutations, combinations, or subsets.

### Sample Problem:
Generate all permutations of a given list of numbers.

**Example:**
- Input: `nums = [1, 2, 3]`
- Output: `[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]`

**Explanation:**
Use recursion to generate permutations. For each element, include it in the current permutation and recursively generate the remaining permutations. Backtrack when all permutations for a given path are generated.

### LeetCode Problems:
- Permutations [Leetcode #46](https://leetcode.com/problems/permutations/) [Lintcode #](https://www.lintcode.com/problem//)
- Subsets [Leetcode #78](https://leetcode.com/problems/subsets/) [Lintcode #](https://www.lintcode.com/problem//)
- N-Queens [Leetcode #51](https://leetcode.com/problems/n-queens/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 15. Dynamic Programming Patterns

Dynamic Programming (DP) involves breaking down problems into smaller subproblems and solving them using a bottom-up or top-down approach.

Use this pattern for problems with overlapping subproblems and optimal substructure.

DP itself has multiple sub-patterns. Some of the most important ones are:
- Fibonacci Numbers
- 0/1 Knapsack
- Longest Common Subsequence (LCS)
- Longest Increasing Subsequence (LIS)
- Subset Sum
- Matrix Chain Multiplication

### Sample Problem:
Calculate the n-th Fibonacci number.

**Example:**
- Input: `n = 5`
- Output: `5` (The first five Fibonacci numbers are 0, 1, 1, 2, 3, 5)

**Explanation:**
Use a bottom-up approach to calculate the n-th Fibonacci number. Start with the first two numbers (0 and 1) and iterate to calculate the next numbers like `dp[i] = dp[i - 1] + dp[i - 2]`.

### LeetCode Problems:
- Climbing Stairs [Leetcode #70](https://leetcode.com/problems/climbing-stairs/) [Lintcode #](https://www.lintcode.com/problem//)
- House Robber [Leetcode #198](https://leetcode.com/problems/house-robber/) [Lintcode #](https://www.lintcode.com/problem//)
- Coin Change [Leetcode #322](https://leetcode.com/problems/coin-change/) [Lintcode #](https://www.lintcode.com/problem//)
- Longest Common Subsequence [Leetcode #1143](https://leetcode.com/problems/longest-common-subsequence/) [Lintcode #](https://www.lintcode.com/problem//)
- Longest Increasing Subsequence [Leetcode #300](https://leetcode.com/problems/longest-increasing-subsequence/) [Lintcode #](https://www.lintcode.com/problem//)
- Partition Equal Subset Sum [Leetcode #416](https://leetcode.com/problems/partition-equal-subset-sum/) [Lintcode #](https://www.lintcode.com/problem//)

---

*For more Dynamic Programming Patterns, check out: [20 Patterns to Master Dynamic Programming](https://blog.algomaster.io/p/20-patterns-to-master-dynamic-programming)*

# 🎯🎯🎯 20 Dynamic Programming Patterns to Master
# 20 Dynamic Programming Patterns to Master

Dynamic Programming (DP) is arguably the most difficult topic for coding interviews. But, like any other topic, the fastest way to learn it is by understanding different patterns that can help you solve a wide variety of problems.

This guide covers 20 patterns that will make learning DP much easier, listed from easy to hard with practice problems for each pattern.

---

## 1. Fibonacci Sequence

The Fibonacci sequence pattern is useful when the solution to a problem depends on the solutions of smaller instances of the same problem. There is a clear recursive relationship, often resembling the classic Fibonacci sequence F(n) = F(n-1) + F(n-2).

### LeetCode Problems:
- Climbing Stairs [Leetcode #70](https://leetcode.com/problems/climbing-stairs/) [Lintcode #](https://www.lintcode.com/problem//)
- Fibonacci Number [Leetcode #509](https://leetcode.com/problems/fibonacci-number/) [Lintcode #](https://www.lintcode.com/problem//)
- Min Cost Climbing Stairs [Leetcode #746](https://leetcode.com/problems/min-cost-climbing-stairs/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 2. Kadane's Algorithm

Kadane's Algorithm is primarily used for solving the Maximum Subarray Problem and its variations where the problem asks to optimize a contiguous subarray within a one-dimensional numeric array.

### LeetCode Problems:
- Maximum Subarray [Leetcode #53](https://leetcode.com/problems/maximum-subarray/) [Lintcode #](https://www.lintcode.com/problem//)
- Maximum Sum Circular Subarray [Leetcode #918](https://leetcode.com/problems/maximum-sum-circular-subarray/) [Lintcode #](https://www.lintcode.com/problem//)
- Maximum Product Subarray [Leetcode #152](https://leetcode.com/problems/maximum-product-subarray/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 3. 0/1 Knapsack

The 0/1 Knapsack pattern is useful when:
- You have a set of items, each with a weight and a value
- You need to select a subset of these items
- There's a constraint on the total weight (or some other resource) you can use
- You want to maximize (or minimize) the total value of the selected items
- Each item can be chosen only once (hence the "0/1" - you either take it or you don't)

### LeetCode Problems:
- Partition Equal Subset Sum [Leetcode #416](https://leetcode.com/problems/partition-equal-subset-sum/) [Lintcode #](https://www.lintcode.com/problem//)
- Target Sum [Leetcode #494](https://leetcode.com/problems/target-sum/) [Lintcode #](https://www.lintcode.com/problem//)
- Last Stone Weight II [Leetcode #1049](https://leetcode.com/problems/last-stone-weight-ii/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 4. Unbounded Knapsack

The Unbounded Knapsack pattern is useful when:
- You have a set of items, each with a weight and a value
- You need to select items to maximize total value
- There's a constraint on the total weight (or some other resource) you can use
- You can select each item multiple times (unlike 0/1 Knapsack where each item can be chosen only once)
- The supply of each item is considered infinite

### LeetCode Problems:
- Coin Change [Leetcode #322](https://leetcode.com/problems/coin-change/) [Lintcode #](https://www.lintcode.com/problem//)
- Coin Change 2 [Leetcode #518](https://leetcode.com/problems/coin-change-2/) [Lintcode #](https://www.lintcode.com/problem//)
- Perfect Squares [Leetcode #279](https://leetcode.com/problems/perfect-squares/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 5. Longest Common Subsequence (LCS)

The Longest Common Subsequence pattern is useful when you are given two sequences and need to find a subsequence that appears in the same order in both the given sequences.

### LeetCode Problems:
- Longest Common Subsequence [Leetcode #1143](https://leetcode.com/problems/longest-common-subsequence/) [Lintcode #](https://www.lintcode.com/problem//)
- Delete Operation for Two Strings [Leetcode #583](https://leetcode.com/problems/delete-operation-for-two-strings/) [Lintcode #](https://www.lintcode.com/problem//)
- Shortest Common Supersequence [Leetcode #1092](https://leetcode.com/problems/shortest-common-supersequence/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 6. Longest Increasing Subsequence (LIS)

The Longest Increasing Subsequence pattern is used to solve problems that involve finding the longest subsequence of elements in a sequence where the elements are in increasing order.

### LeetCode Problems:
- Longest Increasing Subsequence [Leetcode #300](https://leetcode.com/problems/longest-increasing-subsequence/) [Lintcode #](https://www.lintcode.com/problem//)
- Number of Longest Increasing Subsequence [Leetcode #673](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) [Lintcode #](https://www.lintcode.com/problem//)
- Russian Doll Envelopes [Leetcode #354](https://leetcode.com/problems/russian-doll-envelopes/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 7. Palindromic Subsequence

The Palindromic Subsequence pattern is used when solving problems that involve finding a subsequence within a sequence (usually a string) that reads the same forwards and backwards.

### LeetCode Problems:
- Longest Palindromic Subsequence [Leetcode #516](https://leetcode.com/problems/longest-palindromic-subsequence/) [Lintcode #](https://www.lintcode.com/problem//)
- Palindromic Substrings [Leetcode #647](https://leetcode.com/problems/palindromic-substrings/) [Lintcode #](https://www.lintcode.com/problem//)
- Minimum Insertion Steps to Make a String Palindrome [Leetcode #1312](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 8. Edit Distance

The Edit Distance pattern is used to solve problems that involve transforming one sequence (usually a string) into another sequence using a minimum number of operations. The allowed operations typically include insertion, deletion, and substitution.

### LeetCode Problems:
- Edit Distance [Leetcode #72](https://leetcode.com/problems/edit-distance/) [Lintcode #](https://www.lintcode.com/problem//)
- Delete Operation for Two Strings [Leetcode #583](https://leetcode.com/problems/delete-operation-for-two-strings/) [Lintcode #](https://www.lintcode.com/problem//)
- Minimum ASCII Delete Sum for Two Strings [Leetcode #712](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 9. Subset Sum

The Subset Sum pattern is used to solve problems where you need to determine whether a subset of elements from a given set can sum up to a specific target value.

### LeetCode Problems:
- Partition Equal Subset Sum [Leetcode #416](https://leetcode.com/problems/partition-equal-subset-sum/) [Lintcode #](https://www.lintcode.com/problem//)
- Target Sum [Leetcode #494](https://leetcode.com/problems/target-sum/) [Lintcode #](https://www.lintcode.com/problem//)
- Partition to K Equal Sum Subsets [Leetcode #698](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 10. String Partition

The String Partition pattern is used to solve problems that involve partitioning a string into smaller substrings that satisfy certain conditions.

It's useful when:
- You're working with problems involving strings or sequences
- The problem requires splitting the string into substrings or subsequences
- You need to optimize some property over these partitions (e.g., minimize cost, maximize value)
- The solution to the overall problem can be built from solutions to subproblems on smaller substrings
- There's a need to consider different ways of partitioning the string

### LeetCode Problems:
- Word Break [Leetcode #139](https://leetcode.com/problems/word-break/) [Lintcode #](https://www.lintcode.com/problem//)
- Palindrome Partitioning II [Leetcode #132](https://leetcode.com/problems/palindrome-partitioning-ii/) [Lintcode #](https://www.lintcode.com/problem//)
- Concatenated Words [Leetcode #472](https://leetcode.com/problems/concatenated-words/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 11. Catalan Numbers

The Catalan Number pattern is used to solve combinatorial problems that can be decomposed into smaller, similar subproblems.

Some of the use-cases of this pattern include:
- Counting the number of valid parentheses expressions of a given length
- Counting the number of distinct binary search trees that can be formed with n nodes
- Counting the number of ways to triangulate a polygon with n+2 sides

### LeetCode Problems:
- Unique Binary Search Trees [Leetcode #96](https://leetcode.com/problems/unique-binary-search-trees/) [Lintcode #](https://www.lintcode.com/problem//)
- Generate Parentheses [Leetcode #22](https://leetcode.com/problems/generate-parentheses/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 12. Matrix Chain Multiplication

This pattern is used to solve problems that involve determining the optimal order of operations to minimize the cost of performing a series of operations. It is based on the popular optimization problem: Matrix Chain Multiplication.

It's useful when:
- You're dealing with a sequence of elements that can be combined pairwise
- The cost of combining elements depends on the order of combination
- You need to find the optimal way to combine the elements
- The problem involves minimizing (or maximizing) the cost of operations of combining the elements

### LeetCode Problems:
- Minimum Score Triangulation of Polygon [Leetcode #1039](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/) [Lintcode #](https://www.lintcode.com/problem//)
- Burst Balloons [Leetcode #312](https://leetcode.com/problems/burst-balloons/) [Lintcode #](https://www.lintcode.com/problem//)
- Minimum Cost to Merge Stones [Leetcode #1000](https://leetcode.com/problems/minimum-cost-to-merge-stones/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 13. Count Distinct Ways

This pattern is useful when:
- You need to count the number of different ways to achieve a certain goal or reach a particular state
- The problem involves making a series of choices or steps to reach a target
- There are multiple valid paths or combinations to reach the solution
- The problem can be broken down into smaller subproblems with overlapping solutions
- You're dealing with combinatorial problems that ask "in how many ways" can something be done

### LeetCode Problems:
- Decode Ways [Leetcode #91](https://leetcode.com/problems/decode-ways/) [Lintcode #](https://www.lintcode.com/problem//)
- Count Number of Texts [Leetcode #2266](https://leetcode.com/problems/count-number-of-texts/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 14. DP on Grids

The DP on Grids pattern is used to solve problems that involve navigating or optimizing paths within a grid (2D array). For these problems, you need to consider multiple directions of movement (e.g., right, down, diagonal) and solution at each cell depends on the solutions of neighboring cells.

### LeetCode Problems:
- Unique Paths [Leetcode #62](https://leetcode.com/problems/unique-paths/) [Lintcode #](https://www.lintcode.com/problem//)
- Minimum Path Sum [Leetcode #64](https://leetcode.com/problems/minimum-path-sum/) [Lintcode #](https://www.lintcode.com/problem//)
- Longest Increasing Path in a Matrix [Leetcode #329](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 15. DP on Trees

The DP on Trees pattern is useful when:
- You're working with tree-structured data represented by nodes and edges
- The problem can be broken down into solutions of subproblems that are themselves tree problems
- The problem requires making decisions at each node that affect its children or parent
- You need to compute values for nodes based on their children or ancestors

### LeetCode Problems:
- House Robber III [Leetcode #337](https://leetcode.com/problems/house-robber-iii/) [Lintcode #](https://www.lintcode.com/problem//)
- Binary Tree Maximum Path Sum [Leetcode #124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) [Lintcode #](https://www.lintcode.com/problem//)
- Binary Tree Cameras [Leetcode #968](https://leetcode.com/problems/binary-tree-cameras/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 16. DP on Graphs

The DP on Graphs pattern is useful when:
- You're dealing with problems involving graph structures
- The problem requires finding optimal paths, longest paths, cycles, or other optimized properties on graphs
- You need to compute values for nodes or edges based on their neighbors or connected components
- The problem involves traversing a graph while maintaining some state

### LeetCode Problems:
- Cheapest Flights Within K Stops [Leetcode #787](https://leetcode.com/problems/cheapest-flights-within-k-stops/) [Lintcode #](https://www.lintcode.com/problem//)
- Find the City With the Smallest Number of Neighbors at a Threshold Distance [Leetcode #1334](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 17. Digit DP

The Digit DP Pattern is useful when:
- You're dealing with problems involving counting or summing over a range of numbers
- The problem requires considering the digits of numbers individually
- You need to find patterns or properties related to the digits of numbers within a range
- The range of numbers is large (often up to 10^18 or more), making brute force approaches infeasible
- The problem involves constraints on the digits

### LeetCode Problems:
- Count Numbers with Unique Digits [Leetcode #357](https://leetcode.com/problems/count-numbers-with-unique-digits/) [Lintcode #](https://www.lintcode.com/problem//)
- Number of Digit One [Leetcode #233](https://leetcode.com/problems/number-of-digit-one/) [Lintcode #](https://www.lintcode.com/problem//)
- Numbers At Most N Given Digit Set [Leetcode #902](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 18. Bitmasking DP

The Bitmasking DP pattern is used to solve problems that involve a large number of states or combinations, where each state can be efficiently represented using bits in an integer.

It's particularly useful when:
- You're dealing with problems involving subsets or combinations of elements
- The total number of elements is relatively small (typically <= 20-30)
- You need to efficiently represent and manipulate sets of elements
- The problem involves making decisions for each element (include/exclude) or tracking visited/unvisited states
- You want to optimize space usage in DP solutions

### LeetCode Problems:
- Minimum Number of Work Sessions to Finish the Tasks [Leetcode #1986](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/) [Lintcode #](https://www.lintcode.com/problem//)
- Fair Distribution of Cookies [Leetcode #2305](https://leetcode.com/problems/fair-distribution-of-cookies/) [Lintcode #](https://www.lintcode.com/problem//)
- Shortest Path Visiting All Nodes [Leetcode #847](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 19. Probability DP

This pattern is useful when:
- You're dealing with problems involving probability calculations
- The probability of a state depends on the probabilities of previous states
- You need to calculate the expected value of an outcome
- The problem involves random processes or games of chance

### LeetCode Problems:
- Knight Probability in Chessboard [Leetcode #688](https://leetcode.com/problems/knight-probability-in-chessboard/) [Lintcode #](https://www.lintcode.com/problem//)
- Soup Servings [Leetcode #808](https://leetcode.com/problems/soup-servings/) [Lintcode #](https://www.lintcode.com/problem//)
- New 21 Game [Leetcode #837](https://leetcode.com/problems/new-21-game/) [Lintcode #](https://www.lintcode.com/problem//)

---

## 20. State Machine DP

The State Machine DP Pattern is useful when:
- The problem can be modeled as a series of states and transitions between these states
- There are clear rules for moving from one state to another
- The optimal solution depends on making the best sequence of state transitions
- The problem involves making decisions that affect future states
- There's a finite number of possible states, and each state can be clearly defined

### LeetCode Problems:
- Best Time to Buy and Sell Stock with Cooldown [Leetcode #309](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) [Lintcode #](https://www.lintcode.com/problem//)
- Best Time to Buy and Sell Stock III [Leetcode #123](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) [Lintcode #](https://www.lintcode.com/problem//)

---

*Note: No images were referenced in the original document. Practice these patterns in order from easy to hard to build a solid foundation in Dynamic Programming.*

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

## Books
- https://github.com/Tippu1987/System-Design
- https://dokumen.pub/system-design-interview-an-insiders-guide-volume-2-1736049119-9781736049112.html
- https://blog.bytebytego.com/p/free-system-design-pdf-158-pages


## Links
- https://www.techinterviewhandbook.org/negotiation/
- https://www.codechef.com/roadmap/data-structures-and-algorithms
- https://shivangsnewsletter.com/
- https://learnsoftwarearchitecture.com/
- https://www.scaler.com/topics/bisect-python/
- https://blog.algomaster.io/p/15-leetcode-patterns
- https://blog.algomaster.io/p/20-patterns-to-master-dynamic-programming
- https://www.lintcode.com/problem/678/description?fromId=291&_from=collection
- https://bytebytego.com/courses/system-design-interview/back-of-the-envelope-estimation
- https://medium.com/@roopa.kushtagi/the-cap-theorem-why-cant-i-have-it-all-d98018b7101a 
- https://medium.com/@sentalkssane/a-beginners-guide-to-system-design-76d64689788b 
- https://github.com/donnemartin/system-design-primer
### [Reddit HLD](https://www.reddit.com/r/ExperiencedDevs/comments/1gz9ksj/my_senior_engineer_interview_experiences/?share_id=jzxGMYyKNsgB5ljrLQqHa&utm_content=2&utm_medium=android_app&utm_name=androidcss&utm_source=share&utm_term=1)
- https://www3.cs.stonybrook.edu/~skiena/373/videos/
- https://www.youtube.com/@TechPrepYT/shorts
