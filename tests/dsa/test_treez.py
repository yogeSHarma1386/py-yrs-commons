import unittest
import time
import pytest
import sys

from yrs_commons.dsa import *

# DSA Tests
class TreeTestNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


@pytest.mark.unit
class TestDSA(unittest.TestCase):
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


# Performance Tests
@pytest.mark.performance
class TestPerformance(unittest.TestCase):

    # @pytest.mark.skip
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
