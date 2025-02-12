from collections import deque
from typing import Optional, List

from ._nodes import NodeTree, TrieNode, NodeAVL
from ..utils.annotations import yrs_ignore_memorise


class BinaryTree:
    def __init__(self, val=None):
        self.root = None
        if val is not None:
            self.root = NodeTree(val)

    @property
    def val(self):
        return self.root.val

    @property
    def left(self):
        return self.root.left

    @left.setter
    def left(self, value):
        self.root.left = value

    @property
    def right(self):
        return self.root.right

    @right.setter
    def right(self, value):
        self.root.right = value

    # Tree Traversals
    # Level Order Traversal (BFS)
    def level_order(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
        return result

    def inorder(self, root):
        result = []
        if root:
            result.extend(self.inorder(root.left))
            result.append(root.val)
            result.extend(self.inorder(root.right))
        return result

    def preorder(self, root):
        result = []
        if root:
            result.append(root.val)
            result.extend(self.preorder(root.left))
            result.extend(self.preorder(root.right))
        return result

    def postorder(self, root):
        result = []
        if root:
            result.extend(self.postorder(root.left))
            result.extend(self.postorder(root.right))
            result.append(root.val)
        return result

    @classmethod
    def zigzag_order(cls, root: Optional[NodeTree]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not left_to_right:
                current_level.reverse()

            result.append(current_level)
            left_to_right = not left_to_right

        return result

    @classmethod
    def diameter(cls, root: Optional[NodeTree]) -> int:
        max_diameter = 0

        def __custom_depth(node: Optional[NodeTree]) -> int:
            nonlocal max_diameter
            if not node:
                return 0

            left_depth = __custom_depth(node.left)
            right_depth = __custom_depth(node.right)

            # Update max diameter if current path is longer
            max_diameter = max(max_diameter, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        __custom_depth(root)
        return max_diameter

    @classmethod
    def height(cls, root) -> int:
        if not root:
            return 0
        return 1 + max(cls.height(root.left), cls.height(root.right))

    edge_count = get_depth = height

    # """
    # # Check if tree is balanced
    # def is_balanced(self, root):
    #     def check_height(node):
    #         if not node:
    #             return 0
    #
    #         left_height = check_height(node.left)
    #         if left_height == -1:
    #             return -1
    #
    #         right_height = check_height(node.right)
    #         if right_height == -1:
    #             return -1
    #
    #         if abs(left_height - right_height) > 1:
    #             return -1
    #
    #         return 1 + max(left_height, right_height)
    #
    #     return check_height(root) != -1
    # """

    @classmethod
    def find_lca(cls, root: Optional[NodeTree], p: int, q: int) -> Optional[NodeTree]:
        if not root:
            return None

        if root.val == p or root.val == q:
            return root

        left = cls.find_lca(root.left, p, q)
        right = cls.find_lca(root.right, p, q)

        if left and right:
            return root
        return left if left else right

    @classmethod
    def is_balanced(cls, root: NodeTree) -> bool:
        if not root:
            return True

        def check_balance(node: NodeTree) -> tuple[bool, int]:
            if not node:
                return True, 0

            left_balanced, left_height = check_balance(node.left)
            right_balanced, right_height = check_balance(node.right)

            balanced = (
                left_balanced
                and right_balanced
                and abs(left_height - right_height) <= 1
            )

            return balanced, 1 + max(left_height, right_height)

        return check_balance(root)[0]

    @classmethod
    @yrs_ignore_memorise
    def display(
        cls, root: Optional[NodeTree], start_level=0
    ) -> str:  # pragma: no cover
        """
        Ignore memorising this.

        start_level, just like any other tree level starts from level: 0.
        """
        if not root:
            return "Tree is empty"

        def _to_level_printable(level_nodes, width):
            line = ["  " for _ in range(width)]
            for nde, posn in level_nodes:
                line[posn] = str(nde.val)
            return "".join(line)

        def navigate(depth, level, node, pos, queue):
            if node.left:
                queue.append((node.left, level + 1, pos - 2 ** (depth - level - 2)))
            if node.right:
                queue.append((node.right, level + 1, pos + 2 ** (depth - level - 2)))

        depth = cls.get_depth(root)
        max_width = 2**depth - 1  # Full width of the last level
        queue = deque([(root, 0, max_width // 2)])
        curr_level = 0
        level_nodes = []

        stacked_output = []
        while queue:
            node, level, pos = queue.popleft()
            if level < start_level:  # Skip levels until reaching start_level
                navigate(depth, level, node, pos, queue)
                continue

            if level != curr_level:
                stacked_output.append(_to_level_printable(level_nodes, max_width))
                level_nodes = []
                curr_level = level

            level_nodes.append((node, pos))
            navigate(depth, level, node, pos, queue)

        stacked_output.append(_to_level_printable(level_nodes, max_width))
        return "\n".join(stacked_output)

    @staticmethod
    def serialize(root: Optional[NodeTree]) -> str:
        if not root:
            return "null"

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        while result[-1] == "null":
            result.pop()

        return ",".join(result)

    @staticmethod
    def deserialize(data: str) -> Optional[NodeTree]:
        if data == "null":
            return None

        values = data.split(",")
        root = NodeTree(int(values[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            if i < len(values) and values[i] != "null":
                node.left = NodeTree(int(values[i]))
                queue.append(node.left)
            i += 1

            if i < len(values) and values[i] != "null":
                node.right = NodeTree(int(values[i]))
                queue.append(node.right)
            i += 1

        return root


class BST(BinaryTree):  # Binary Search Tree
    """
    A binary search tree (BST) is a data structure in computer science that stores data in a tree-like structure.
    It's also known as an ordered or sorted binary tree.

    Properties
    • Each node's left child has a smaller value than the node's value
    • Each node's right child has a larger value than the node's value
    • The left and right subtrees of a node are also binary search trees

    Advantages
    • BSTs are fast because they don't require shifting values in memory to perform operations like
            searching, inserting, and deleting
    • BSTs allow for efficient searching, insertion, and deletion

    Time complexity
    • The time complexity of operations on a BST is linear with respect to the height of the tree (O(h))

    Traversal
    • You can traverse a BST in inorder, preorder, or postorder
    """

    def insert(self, root, val):
        if not root:
            return NodeTree(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root

    def search(self, root, val):
        if not root or root.val == val:
            return root

        if val < root.val:
            return self.search(root.left, val)
        return self.search(root.right, val)

    def delete(self, root, val):
        if not root:
            return root

        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Node with two children
            # Get inorder successor (smallest in right subtree)
            temp = self.min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        return root

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current


class AVLTree:  # Advanced Tree Node (for AVL Tree)
    """
    AVL stands for Adelson-Velsky and Landis, the names of the inventors of the AVL tree.
    AVL trees are self-balancing binary search trees (BSTs).

    Explanation
    • AVL trees are used to organize information and perform efficient searches and retrievals.
    • AVL trees maintain balance by rotating automatically, even when data is inserted in an arbitrary order.
    • AVL trees are height-balanced, meaning the height difference between the left and right subtrees of any node
            is at most one.
    • AVL trees use a balance factor to determine the balance of a node. The balance factor is the difference
            between the heights of the left and right subtrees.
    • AVL trees are used to overcome the problem of unbalanced BSTs, which can lead to decreased performance.

    """

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, val):
        if not root:
            return NodeAVL(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and val < root.left.val:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and val > root.right.val:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and val > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and val < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


class BinaryIndexedTree:  # Fenwick Tree
    """
    A Binary Indexed Tree (also called a Fenwick Tree) is a data structure that allows for efficient calculation
    of prefix sums and updates on an array of values, enabling quick retrieval of the sum of elements within
    a specific range with a time complexity of O(log n) for both updates and queries; essentially, it's a way to
    store cumulative sums in an array using bit manipulation to navigate through relevant ranges quickly.

    Key points about Binary Indexed Trees:
    • Efficient range queries: You can quickly calculate the sum of elements within a specific range in
            logarithmic time.
    • Point updates: Individual element updates can also be done in logarithmic time. [1, 5, 6]
    • Bit manipulation: The structure leverages bit manipulation to determine which elements contribute to a
            specific range sum.
    • Applications: Useful in scenarios like calculating cumulative frequencies, finding the number of elements
            less than a certain value in a sorted array, and handling range updates in data analysis. [1, 4, 8]

    """

    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, val: int) -> None:
        index += 1
        while index <= self.size:
            self.tree[index] += val
            index += index & (-index)

    def get_sum(self, index: int) -> int:
        index += 1
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & (-index)
        return total


class Trie:  # Prefix Tree / Digital Tree
    """
    Trie is short for retrieval, and is a tree-based data structure used to store and retrieve strings.
    It's also known as a prefix tree or digital tree.

    How does it work?
    • A trie is a tree data structure that stores strings based on their prefixes.
    • The position of a node in the trie determines its associated key.
    • The connections between nodes are defined by individual characters.
    • A trie has a root node, internal nodes, leaf nodes, and edges.
    • The root node is the starting point of the trie.
    • Internal nodes represent characters within a word.
    • Leaf nodes represent the end of a word.
    • Edges are the connections between nodes that represent characters.

    What are the uses of a trie?
    • Tries are used in applications that require dynamic sets of strings, such as spell checkers and autocomplete.
    • They are also used in IP routing.

    What is the word trie pronounced as?
    • The word trie is usually pronounced "try" to distinguish it from other "tree" structures.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def longest_prefix_match(self, query):
        node = self.root
        longest_prefix = ""
        current_prefix = ""

        for char in query:
            if char not in node.children:
                break
            current_prefix += char
            node = node.children[char]
            if node.is_end:
                longest_prefix = current_prefix
        return longest_prefix
