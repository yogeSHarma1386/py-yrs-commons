# Basic Tree Node
class NodeTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Advanced Tree Node (for AVL Tree)
class NodeAVL(NodeTree):
    def __init__(self, val=0):
        super().__init__(val)
        self.height = 1


# Doubly Linked List Node
class NodeDLL:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Linked List Node
class NodeLL:
    def __init__(self, data):
        self.data = data
        self.next = None
