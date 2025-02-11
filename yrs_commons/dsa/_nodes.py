from typing import Dict


class NodeLL:  # Linked List Node
    def __init__(self, data):
        self.data = data
        self.next = None


class NodeDLL:  # Doubly Linked List Node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class NodeTree:  # Basic Tree Node
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end = False


class NodeAVL(NodeTree):  # Advanced Tree Node (for AVL Tree)
    def __init__(self, val=0):
        super().__init__(val)
        self.height = 1


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2):
        self.adjacency_list[v1].append(v2)
