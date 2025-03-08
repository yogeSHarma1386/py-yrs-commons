import unittest

import pytest

from yrs_commons.dsa import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    heap_sort,
    topological_sort,
)

# Define common test cases: each tuple is (input_list, expected_sorted_list)
test_cases = [
    ("Simple", [3, 1, 2], [1, 2, 3]),
    ("Simple", [5, 3, 8, 1, 2], [1, 2, 3, 5, 8]),
    ("Simple", [3, 3, 2, 1, 4], [1, 2, 3, 3, 4]),
    ("Simple", [10, -1, 2, 8, 0], [-1, 0, 2, 8, 10]),

    # Positive cases
    ("Positive cases", [4, 2, 1, 3], [1, 2, 3, 4]),
    ("Positive cases - Already sorted", [1, 2, 3, 4], [1, 2, 3, 4]),  # Already sorted
    ("Positive cases - Reverse sorted", [4, 3, 2, 1], [1, 2, 3, 4]),  # Reverse sorted

    # Boundary cases
    ("Boundary cases - Empty array", [], []),                       # Empty array
    ("Boundary cases - Single element", [1], [1]),                     # Single element
    ("Boundary cases - same elements", [2, 2, 2, 2], [2, 2, 2, 2]),  # All same elements

    # Negative cases
    ("Negative numbers", [-1, -5, -3, -2], [-5, -3, -2, -1]),  # Negative numbers
    ("Negative - Mixed numbers", [0, -1, 5, -10], [-10, -1, 0, 5]),    # Mixed numbers
]

@pytest.mark.unit
class TestSortingAlgorithms:

    @pytest.mark.unit
    def test_bubble_sort_types(self):
        with pytest.raises(TypeError):
            _ = bubble_sort({'a', 'b', 'c'})  # TypeError: 'set' object is not subscriptable
        with pytest.raises(TypeError):
            _ = bubble_sort([('b',), 'a', 'b', 'c'])  # TypeError: '>' not supported between instances of tuple and str
        with pytest.raises(AttributeError):
            bubble_sort(None)  # AttributeError: 'NoneType' object has no attribute 'copy'
        with pytest.raises(AttributeError):
            bubble_sort(42)  # Non-iterable input # AttributeError: 'NoneType' object has no attribute 'copy'

    @pytest.mark.parametrize("info, input_list, expected", test_cases)
    def test_bubble_sort(self, info, input_list, expected):
        assert bubble_sort(input_list) == expected

    @pytest.mark.parametrize("info, input_list, expected", test_cases)
    def test_selection_sort(self, info, input_list, expected):
        assert selection_sort(input_list) == expected

    @pytest.mark.parametrize("info, input_list, expected", test_cases)
    def test_insertion_sort(self, info, input_list, expected):
        assert insertion_sort(input_list) == expected

    @pytest.mark.parametrize("info, input_list, expected", test_cases)
    def test_merge_sort(self, info, input_list, expected):
        assert merge_sort(input_list) == expected

    @pytest.mark.parametrize("info, input_list, expected", test_cases)
    def test_quick_sort(self, info, input_list, expected):
        assert quick_sort(input_list) == expected

    @pytest.mark.parametrize("info, input_list, expected", test_cases)
    def test_heap_sort(self, info, input_list, expected):
        assert heap_sort(input_list) == expected


@pytest.mark.unit
class TestTopologicalSortAlgorithms:

    def test_basic_dag(self):
        number_of_nodes = 6
        edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
        result = topological_sort(number_of_nodes, edges)

        # Validate topological order using in-degree property
        index_map = {node: i for i, node in enumerate(result)}
        for source, destination in edges:
            assert index_map[source] < index_map[destination], "Invalid topological order"

    def test_graph_with_cycle(self):
        number_of_nodes = 3
        edges = [(0, 1), (1, 2), (2, 0)]  # Cycle: 0 → 1 → 2 → 0
        with pytest.raises(ValueError, match="The graph contains a cycle"):
            topological_sort(number_of_nodes, edges)

    def test_single_node(self):
        number_of_nodes = 1
        edges = []
        result = topological_sort(number_of_nodes, edges)
        assert result == [0], "Single node graph should return [0]"

    def test_multiple_independent_chains(self):
        number_of_nodes = 5
        edges = [(0, 2), (1, 3), (3, 4)]
        result = topological_sort(number_of_nodes, edges)

        # Ensure all nodes are present
        assert sorted(result) == list(range(number_of_nodes)), "Topological order missing nodes"

        # Validate order
        index_map = {node: i for i, node in enumerate(result)}
        for source, destination in edges:
            assert index_map[source] < index_map[destination], "Invalid topological order"

    def test_already_sorted_graph(self):
        number_of_nodes = 4
        edges = [(0, 1), (1, 2), (2, 3)]  # Already sorted order
        result = topological_sort(number_of_nodes, edges)
        assert result == [0, 1, 2, 3], "Graph with linear dependencies should return same order"


@pytest.mark.unit
class TestSortingFunctions(unittest.TestCase):
    def test_quicksort(self):
        # Test normal case
        arr = [64, 34, 25, 12, 22, 11, 90]
        self.assertEqual(quick_sort(arr), sorted(arr))

        # Test array with duplicates
        arr = [1, 4, 2, 4, 2, 4, 1, 2, 3]
        self.assertEqual(quick_sort(arr), sorted(arr))

        # Test empty array
        self.assertEqual(quick_sort([]), [])

        # Test single element array
        self.assertEqual(quick_sort([1]), [1])

        # Test already sorted array
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(quick_sort(arr), arr)

        # Test reverse sorted array
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(quick_sort(arr), [1, 2, 3, 4, 5])

    def test_merge_sort(self):
        # Test normal case
        arr = [64, 34, 25, 12, 22, 11, 90]
        self.assertEqual(merge_sort(arr), sorted(arr))

        # Test array with duplicates
        arr = [1, 4, 2, 4, 2, 4, 1, 2, 3]
        self.assertEqual(merge_sort(arr), sorted(arr))

        # Test empty array
        self.assertEqual(merge_sort([]), [])

        # Test single element array
        self.assertEqual(merge_sort([1]), [1])

        # Test already sorted array
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(merge_sort(arr), arr)

        # Test reverse sorted array
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(merge_sort(arr), [1, 2, 3, 4, 5])
