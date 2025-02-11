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


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2):
        self.adjacency_list[v1].append(v2)
