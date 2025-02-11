from .custom_nodes import *


class BinaryTree:
    def __init__(self):
        self.root = None
    
    # Tree Traversals
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

    # Height of the tree
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    
    # Check if tree is balanced
    def is_balanced(self, root):
        def check_height(node):
            if not node:
                return 0
            
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
                
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
                
            return 1 + max(left_height, right_height)
        
        return check_height(root) != -1


class BST(BinaryTree):
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


# Advanced Tree Node (for AVL Tree)
class AVLTree:
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
