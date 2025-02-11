import pytest
from yrs_commons.dsa import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    heap_sort,
)

# Define common test cases: each tuple is (input_list, expected_sorted_list)
test_cases = [
    ([], []),
    ([1], [1]),
    ([3, 1, 2], [1, 2, 3]),
    ([5, 3, 8, 1, 2], [1, 2, 3, 5, 8]),
    ([3, 3, 2, 1, 4], [1, 2, 3, 3, 4]),
    ([10, -1, 2, 8, 0], [-1, 0, 2, 8, 10]),
]

@pytest.mark.unit
class TestSortingAlgorithms:

    @pytest.mark.parametrize("input_list, expected", test_cases)
    def test_bubble_sort(self, input_list, expected):
        assert bubble_sort(input_list) == expected

    @pytest.mark.parametrize("input_list, expected", test_cases)
    def test_selection_sort(self, input_list, expected):
        assert selection_sort(input_list) == expected

    @pytest.mark.parametrize("input_list, expected", test_cases)
    def test_insertion_sort(self, input_list, expected):
        assert insertion_sort(input_list) == expected

    @pytest.mark.parametrize("input_list, expected", test_cases)
    def test_merge_sort(self, input_list, expected):
        assert merge_sort(input_list) == expected

    @pytest.mark.parametrize("input_list, expected", test_cases)
    def test_quick_sort(self, input_list, expected):
        assert quick_sort(input_list) == expected

    @pytest.mark.parametrize("input_list, expected", test_cases)
    def test_heap_sort(self, input_list, expected):
        assert heap_sort(input_list) == expected
