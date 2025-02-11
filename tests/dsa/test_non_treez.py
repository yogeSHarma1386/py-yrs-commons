import random
import time
import unittest
import pytest
from collections import defaultdict
import heapq

# Import the functions we want to test
from yrs_commons.dsa import (
    binary_search, quick_sort, merge_sort, GraphAlgo,
    lcs, Graph
)

@pytest.mark.unit
class TestDSAFunctions(unittest.TestCase):
    def test_binary_search(self):
        # Test normal cases
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(binary_search(arr, 1), 0)  # First element
        self.assertEqual(binary_search(arr, 9), 8)  # Last element
        self.assertEqual(binary_search(arr, 5), 4)  # Middle element
        
        # Test element not present
        self.assertEqual(binary_search(arr, 10), -1)
        
        # Test empty array
        self.assertEqual(binary_search([], 1), -1)
        
        # Test single element array
        self.assertEqual(binary_search([1], 1), 0)
        self.assertEqual(binary_search([1], 2), -1)

@pytest.mark.unit
class TestGraphAlgos(unittest.TestCase):
    def test_bfs(self):
        # Create a sample graph
        graph = {
            0: [1, 2],
            1: [2],
            2: [0, 3],
            3: [3]
        }
        
        visited_nodes = set()
        def test_bfs_visitor(vertex):
            visited_nodes.add(vertex)
        
        # Test BFS traversal
        GraphAlgo.bfs(graph, 2, visited_nodes)  # Starting from vertex 2
        self.assertEqual(visited_nodes, {0, 1, 2, 3})
        
        # Test isolated vertex
        graph_isolated = {0: [], 1: []}
        visited_nodes.clear()
        GraphAlgo.bfs(graph_isolated, 0, visited_nodes)
        self.assertEqual(visited_nodes, {0})

    def test_dfs(self):
        # Create a sample graph
        graph = {
            0: [1, 2],
            1: [2],
            2: [0, 3],
            3: [3]
        }
        
        visited_nodes = set()
        GraphAlgo.dfs(graph, 2, visited_nodes)  # Starting from vertex 2
        self.assertEqual(visited_nodes, {0, 1, 2, 3})
        
        # Test isolated vertex
        graph_isolated = {0: [], 1: []}
        visited_nodes.clear()
        GraphAlgo.dfs(graph_isolated, 0, visited_nodes)
        self.assertEqual(visited_nodes, {0})

    def test_has_cycle(self):
        # Test cyclic graph
        graph_cyclic = {
            0: [1],
            1: [2],
            2: [3],
            3: [1]  # Creates cycle 1->2->3->1
        }
        self.assertTrue(GraphAlgo.has_cycle(graph_cyclic))
        
        # Test acyclic graph
        graph_acyclic = {
            0: [1, 2],
            1: [3],
            2: [3],
            3: []
        }
        self.assertFalse(GraphAlgo.has_cycle(graph_acyclic))
        
        # Test empty graph
        self.assertFalse(GraphAlgo.has_cycle({}))
        
        # Test single node with self-loop
        self.assertTrue(GraphAlgo.has_cycle({0: [0]}))

    def test_lcs(self):
        # Test normal cases
        self.assertEqual(lcs("ABCDGH", "AEDFHR"), 3)  # LCS is "ADH"
        self.assertEqual(lcs("AGGTAB", "GXTXAYB"), 4)  # LCS is "GTAB"
        
        # Test empty strings
        self.assertEqual(lcs("", "ABC"), 0)
        self.assertEqual(lcs("ABC", ""), 0)
        self.assertEqual(lcs("", ""), 0)
        
        # Test identical strings
        self.assertEqual(lcs("ABCD", "ABCD"), 4)
        
        # Test no common subsequence
        self.assertEqual(lcs("ABC", "DEF"), 0)
        
        # Test single character strings
        self.assertEqual(lcs("A", "A"), 1)
        self.assertEqual(lcs("A", "B"), 0)

    def test_dijkstra(self):
        # Test normal graph
        graph = {
            'A': {'B': 4, 'C': 2},
            'B': {'A': 4, 'C': 1, 'D': 5},
            'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
            'D': {'B': 5, 'C': 8, 'E': 2},
            'E': {'C': 10, 'D': 2}
        }
        distances = GraphAlgo.dijkstra(graph, 'A')
        self.assertEqual(distances['A'], 0)
        self.assertEqual(distances['B'], 3)  # A->C->B
        self.assertEqual(distances['C'], 2)  # A->C
        self.assertEqual(distances['D'], 8)  # A->C->B->D
        self.assertEqual(distances['E'], 10) # A->C->B->D->E
        
        # Test disconnected graph
        graph_disconnected = {
            'A': {'B': 1},
            'B': {'A': 1},
            'C': {}
        }
        distances = GraphAlgo.dijkstra(graph_disconnected, 'A')
        self.assertEqual(distances['A'], 0)
        self.assertEqual(distances['B'], 1)
        self.assertEqual(distances['C'], float('infinity'))
        
        # Test single node graph
        graph_single = {'A': {}}
        distances = GraphAlgo.dijkstra(graph_single, 'A')
        self.assertEqual(distances['A'], 0)

    def test_edge_cases(self):
        # Test binary search with repeated elements
        arr = [1, 2, 2, 2, 3, 4, 5]
        self.assertIn(binary_search(arr, 2), [1, 2, 3])  # Should find any occurrence of 2
        
        # Test sorting with negative numbers
        arr = [-5, 3, -2, 1, -8, 4]
        self.assertEqual(quick_sort(arr), sorted(arr))
        self.assertEqual(merge_sort(arr), sorted(arr))
        
        # Test LCS with special characters
        self.assertEqual(lcs("A#B$C", "A#B#C"), 4)  # LCS is "A#BC"
        
        # Test cycle detection with multiple cycles
        graph_multiple_cycles = {
            0: [1, 2],
            1: [3],
            2: [3],
            3: [4, 5],
            4: [2],  # Creates cycle
            5: [5]   # Self loop
        }
        self.assertTrue(GraphAlgo.has_cycle(graph_multiple_cycles))

@pytest.mark.performance
class TestPerformance(unittest.TestCase):
    def test_sorting_performance(self):
        import random
        import time
        
        # Generate large random array
        arr = [random.randint(-1000, 1000) for _ in range(1000)]
        
        # Test quicksort performance
        start_time = time.time()
        quick_sort(arr.copy())
        quick_time = time.time() - start_time
        
        # Test merge sort performance
        start_time = time.time()
        merge_sort(arr.copy())
        merge_time = time.time() - start_time
        
        # Both should complete within reasonable time
        self.assertLess(quick_time, 1.0)
        self.assertLess(merge_time, 1.0)

    def test_graph_algorithm_performance(self):
        # Generate large graph
        large_graph = {i: {j: random.randint(1, 10) 
                         for j in range(max(0, i-5), min(100, i+5))}
                      for i in range(100)}
        
        start_time = time.time()
        GraphAlgo.dijkstra(large_graph, 0)
        self.assertLess(time.time() - start_time, 1.0)

@pytest.mark.unit
class TestGraph:
    @pytest.fixture
    def sample_graph(self):
        graph = Graph()
        vertices = [1, 2, 3, 4, 5]
        for vertex in vertices:
            graph.add_vertex(vertex)
        edges = [(1, 2), (1, 3), (2, 4), (3, 5)]
        for v1, v2 in edges:
            graph.add_edge(v1, v2)
        return graph

    def test_graph_creation_positive(self, sample_graph):
        # Test vertex existence
        assert set(sample_graph.adjacency_list.keys()) == {1, 2, 3, 4, 5}
        # Test edge existence
        assert sample_graph.adjacency_list[1] == [2, 3]
        assert sample_graph.adjacency_list[2] == [4]
        assert sample_graph.adjacency_list[3] == [5]

    def test_graph_empty_boundary(self):
        # Test empty graph
        graph = Graph()
        assert len(graph.adjacency_list) == 0

    def test_graph_single_vertex_boundary(self):
        # Test single vertex graph
        graph = Graph()
        graph.add_vertex(1)
        assert len(graph.adjacency_list) == 1
        assert graph.adjacency_list[1] == []

    def test_graph_cycle(self):
        # Test graph with cycle
        graph = Graph()
        for i in range(1, 4):
            graph.add_vertex(i)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 1)
        assert graph.adjacency_list[1] == [2]
        assert graph.adjacency_list[2] == [3]
        assert graph.adjacency_list[3] == [1]

    def test_graph_isolated_vertices(self):
        # Test graph with isolated vertices
        graph = Graph()
        vertices = [1, 2, 3]
        for vertex in vertices:
            graph.add_vertex(vertex)
        assert all(len(neighbors) == 0 for neighbors in graph.adjacency_list.values())
