import pytest

from yrs_commons.dsa.detailed.array_misc import find_pair_sum, remove_duplicates


@pytest.mark.unit
class TestTwoPointer:
    def test_pair_sum_positive(self):
        assert find_pair_sum([2, 7, 11, 15], 9) == (0, 1)
        assert find_pair_sum([3, 2, 4], 6) == (0, 2)

    def test_pair_sum_boundary(self):
        # Empty array
        assert find_pair_sum([], 5) == (-1, -1)
        # Single element
        assert find_pair_sum([1], 5) == (-1, -1)

    def test_remove_duplicates_positive(self):
        arr1 = [1, 1, 2]
        assert remove_duplicates(arr1) == 2

        arr2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        assert remove_duplicates(arr2) == 5

    def test_remove_duplicates_boundary(self):
        # Empty array
        assert remove_duplicates([]) == 0
        # No duplicates
        arr = [1, 2, 3]
        assert remove_duplicates(arr) == 3
