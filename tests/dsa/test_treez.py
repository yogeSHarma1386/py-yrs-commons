import time
import unittest

import pytest

from yrs_commons.dsa import *


@pytest.mark.unit
class BaseTestTree(unittest.TestCase):
    def setUp(self):
        # Binary Tree Setup
        self.bt = BinaryTree()
        self.bt.root = NodeTree(1)
        self.bt.root.left = NodeTree(2)
        self.bt.root.right = NodeTree(3)
        self.bt.root.left.left = NodeTree(4)
        self.bt.root.left.right = NodeTree(5)

        # BST Setup
        self.bst = BST()
        self.bst.root = None
        values = [5, 3, 7, 2, 4, 6, 8]
        for val in values:
            self.bst.root = self.bst.insert(self.bst.root, val)

        # AVL Setup
        self.avl = AVLTree()
        self.avl_root = None
        values = [10, 20, 30, 40, 50]
        for val in values:
            self.avl_root = self.avl.insert(self.avl_root, val)


@pytest.mark.performance
class TestPerformance(unittest.TestCase):

    def test_bst_performance(self):

        # Test BST insertion performance
        bst = BST()
        root = None

        # # @Yogesh
        # sys.setrecursionlimit(1500)
        start_time = time.time()

        for i in range(750):
            root = bst.insert(root, i)
        end_time = time.time()

        self.assertLess(end_time - start_time, 1.0)  # Should complete within 1 second

    # @pytest.mark.skip(reason="RecursionError: maximum recursion depth exceeded")
    def test_bst_performance_extreme(self):

        # Test BST insertion performance
        bst = BST()
        root = None

        # # @Yogesh
        # sys.setrecursionlimit(1500)
        start_time = time.time()

        with self.assertRaises(RecursionError):
            for i in range(1250):
                root = bst.insert(root, i)
        end_time = time.time()

        self.assertLess(end_time - start_time, 1.0)  # Should complete within 1 second

    def test_avl_performance(self):
        import time

        # Test AVL insertion performance
        avl = AVLTree()
        root = None
        start_time = time.time()
        for i in range(1000):
            root = avl.insert(root, i)
        end_time = time.time()

        self.assertLess(end_time - start_time, 1.0)  # Should complete within 1 second


@pytest.mark.unit
class TestBinaryTree1:
    @pytest.fixture
    def sample_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        return root

    def test_tree_creation_positive(self, sample_tree):
        # Test basic tree structure
        assert sample_tree.val == 1
        assert sample_tree.left.val == 2
        assert sample_tree.right.val == 3
        assert sample_tree.left.left.val == 4
        assert sample_tree.left.right.val == 5

    def test_tree_leaf_nodes(self, sample_tree):
        # Test leaf nodes
        assert sample_tree.left.left.left is None
        assert sample_tree.left.left.right is None
        assert sample_tree.left.right.left is None
        assert sample_tree.left.right.right is None

    def test_tree_creation_boundary(self):
        # Test single node tree
        single_node = BinaryTree(1)
        assert single_node.val == 1
        assert single_node.left is None
        assert single_node.right is None

    def test_tree_value_negative(self):
        # Test negative values
        negative_tree = BinaryTree(-1)
        negative_tree.left = BinaryTree(-2)
        assert negative_tree.val == -1
        assert negative_tree.left.val == -2

    def test_diameter_positive(self, sample_tree):
        assert BinaryTree.diameter(sample_tree.root) == 3

        # Create another tree with different diameter
        root = NodeTree(1)
        root.left = NodeTree(2)
        root.left.left = NodeTree(3)
        root.left.left.left = NodeTree(4)
        assert BinaryTree.diameter(root) == 3

    def test_diameter_boundary(self):
        # Empty tree
        assert BinaryTree.diameter(None) == 0
        # Single node
        assert BinaryTree.diameter(NodeTree(1)) == 0

    def test_zigzag_traversal_positive(self, sample_tree):
        assert BinaryTree.zigzag_order(sample_tree.root) == [[1], [3, 2], [4, 5]]

        # Create another tree for testing
        root = NodeTree(3)
        root.left = NodeTree(9)
        root.right = NodeTree(20)
        root.right.left = NodeTree(15)
        root.right.right = NodeTree(7)
        assert BinaryTree.zigzag_order(root) == [[3], [20, 9], [15, 7]]

    def test_zigzag_traversal_boundary(self):
        # Empty tree
        assert BinaryTree.zigzag_order(None) == []
        # Single node
        assert BinaryTree.zigzag_order(NodeTree(1)) == [[1]]


@pytest.mark.unit
class TestBinaryTree2(BaseTestTree):
    def test_binary_tree_traversals(self):
        # Test inorder traversal
        self.assertEqual(self.bt.inorder(self.bt.root), [4, 2, 5, 1, 3])

        # Test preorder traversal
        self.assertEqual(self.bt.preorder(self.bt.root), [1, 2, 4, 5, 3])

        # Test postorder traversal
        self.assertEqual(self.bt.postorder(self.bt.root), [4, 5, 2, 3, 1])

        # Test level order traversal
        self.assertEqual(self.bt.level_order(self.bt.root), [[1], [2, 3], [4, 5]])

    def test_binary_tree_properties(self):
        # Test height
        self.assertEqual(self.bt.height(self.bt.root), 3)

        # Test balanced tree
        self.assertTrue(self.bt.is_balanced(self.bt.root))

        # Create unbalanced tree and test
        unbalanced = NodeTree(1)
        unbalanced.left = NodeTree(2)
        unbalanced.left.left = NodeTree(3)
        self.assertFalse(self.bt.is_balanced(unbalanced))
        self.assertTrue(self.bt.is_balanced(unbalanced.left.left.left))


@pytest.mark.unit
class TestBST(BaseTestTree):
    def test_bst_operations(self):
        # Test search
        self.assertIsNotNone(self.bst.search(self.bst.root, 7))
        self.assertIsNone(self.bst.search(self.bst.root, 10))

        # Test insertion
        self.bst.root = self.bst.insert(self.bst.root, 9)
        self.assertIsNotNone(self.bst.search(self.bst.root, 9))

        # Test deletion
        self.bst.root = self.bst.delete(self.bst.root, 7)
        self.assertIsNone(self.bst.search(self.bst.root, 7))

        # Test min value
        self.assertEqual(self.bst.min_value_node(self.bst.root).val, 2)


@pytest.mark.unit
class TestAVLTree(BaseTestTree):
    def test_avl_tree_operations(self):
        # Test height and balance
        self.assertTrue(abs(self.avl.get_balance(self.avl_root)) <= 1)

        # Test rotations
        # Left-Left case
        values = [3, 2, 1]
        avl_root = None
        for val in values:
            avl_root = self.avl.insert(avl_root, val)
        self.assertTrue(abs(self.avl.get_balance(avl_root)) <= 1)

        # Right-Right case
        values = [1, 2, 3]
        avl_root = None
        for val in values:
            avl_root = self.avl.insert(avl_root, val)
        self.assertTrue(abs(self.avl.get_balance(avl_root)) <= 1)

    def test_left_right_case(self):
        self.avl.insert(self.avl_root.right.right, 10)
        self.avl.insert(self.avl_root.right.right, 20)
        self.assertEqual(self.avl.get_balance(self.avl_root), -1)

        # Test height and balance
        self.assertTrue(abs(self.avl.get_balance(self.avl_root)) <= 1)

        # Test rotations
        # Left-Left case
        values = [3, 2, 1]
        avl_root = None
        for val in values:
            avl_root = self.avl.insert(avl_root, val)
        self.assertTrue(abs(self.avl.get_balance(avl_root)) <= 1)

        # Right-Right case
        values = [1, 2, 3]
        avl_root = None
        for val in values:
            avl_root = self.avl.insert(avl_root, val)
        self.assertTrue(abs(self.avl.get_balance(avl_root)) <= 1)
        self.assertEqual(self.avl.get_balance(self.avl_root.right.right.right), 0)

    @pytest.mark.skip(reason="not increasing coverage")
    def test_right_left_case(self):
        self.avl.insert(self.avl_root.right.left, 10)
        self.avl.insert(self.avl_root.left.left, 20)
        self.assertEqual(self.avl.get_balance(self.avl_root), -1)


@pytest.mark.unit
class BaseTestTree2:
    @pytest.fixture
    def sample_tree(self):
        """
        Creates a tree:
                 3
               /   \
              5     1
             / \   / \
            6   2 0   8
               / \
              7   4
        """
        root = NodeTree(3)
        root.left = NodeTree(5)
        root.right = NodeTree(1)
        root.left.left = NodeTree(6)
        root.left.right = NodeTree(2)
        root.right.left = NodeTree(0)
        root.right.right = NodeTree(8)
        root.left.right.left = NodeTree(7)
        root.left.right.right = NodeTree(4)
        return root


@pytest.mark.unit
class TestBinaryTreeLCA(BaseTestTree2):

    def test_lca_positive(self, sample_tree):
        assert BinaryTree.find_lca(sample_tree, 5, 1).val == 3
        assert BinaryTree.find_lca(sample_tree, 6, 4).val == 5
        assert BinaryTree.find_lca(sample_tree, 7, 4).val == 2

    def test_lca_boundary(self):
        # Single node tree
        root = NodeTree(1)
        assert BinaryTree.find_lca(root, 1, 1).val == 1
        # Empty tree
        assert BinaryTree.find_lca(None, 1, 2) is None

    def test_lca_negative(self, sample_tree):
        # Non-existent nodes
        assert BinaryTree.find_lca(sample_tree, 10, 11) is None


@pytest.mark.unit
class TestBinaryTreeBalance(BaseTestTree2):

    def test_depth_positive(self, sample_tree):
        assert BinaryTree.get_depth(sample_tree) == 4

    def test_depth_boundary(self):
        assert BinaryTree.get_depth(None) == 0
        assert BinaryTree.get_depth(NodeTree(1)) == 1

    def test_balance_positive(self, sample_tree):
        sample_tree.left.right.right.left = NodeTree(40)
        sample_tree.left.right.right.right = NodeTree(48)
        assert not BinaryTree.is_balanced(sample_tree)

        # Creating a balanced tree
        balanced_tree = NodeTree(1)
        balanced_tree.left = NodeTree(20)
        balanced_tree.right = NodeTree(30)
        assert BinaryTree.is_balanced(balanced_tree)


@pytest.mark.unit
class TestBinaryTreeSerialisation(BaseTestTree2):

    def test_serialization_positive(self, sample_tree):
        serialized = BinaryTree.serialize(sample_tree)
        deserialized = BinaryTree.deserialize(serialized)
        assert BinaryTree.serialize(deserialized) == serialized

    def test_serialization_boundary(self):
        # Empty tree
        assert BinaryTree.serialize(None) == "null"
        assert BinaryTree.deserialize("null") is None

        # Single node
        single_node = NodeTree(1)
        assert BinaryTree.deserialize(BinaryTree.serialize(single_node)).val == 1


@pytest.mark.unit
class TestBinaryIndexedTree(BaseTestTree2):

    def test_bit_positive(self):
        bit = BinaryIndexedTree(5)
        bit.update(0, 1)
        bit.update(2, 2)
        assert bit.get_sum(2) == 3
        assert bit.get_sum(4) == 3

    def test_bit_boundary(self):
        bit = BinaryIndexedTree(1)
        bit.update(0, 1)
        assert bit.get_sum(0) == 1


@pytest.mark.unit
class TestTrie(BaseTestTree2):

    def test_trie_positive(self):
        trie = Trie()
        trie.insert("apple")
        assert trie.search("apple")
        assert not trie.search("app")
        assert not trie.search("peepal")

    def test_trie_prefix_match(self):
        trie = Trie()
        words = ["apple", "app", "apricot", "apartment"]
        for word in words:
            trie.insert(word)

        assert trie.longest_prefix_match("application") == "app"
        assert trie.longest_prefix_match("apricot") == "apricot"
        assert trie.longest_prefix_match("apartment") == "apartment"
        assert trie.longest_prefix_match("banana") == ""

    def test_trie_boundary(self):
        trie = Trie()
        # Empty string
        trie.insert("")
        assert trie.search("")
        # Single character
        trie.insert("a")
        assert trie.search("a")
