import pytest

from yrs_commons.dsa.detailed.array_misc import max_sum_sliding_window, find_anagrams


@pytest.mark.unit
class TestAlgorithms:
    # Sliding Window Tests
    def test_sliding_window_sum_positive(self):
        arr = [1, 2, 3, 4, 5]
        assert max_sum_sliding_window(arr, 3) == [6, 9, 12]

        arr = [2, 4, 6, 8, 10]
        assert max_sum_sliding_window(arr, 2) == [6, 10, 14, 18]

    def test_sliding_window_sum_boundary(self):
        # Empty array
        assert max_sum_sliding_window([], 3) == []
        # Window size equals array length
        assert max_sum_sliding_window([1, 2, 3], 3) == [6]

    def test_sliding_window_anagrams_positive(self):
        assert find_anagrams("cbaebabacd", "abc") == [0, 6]
        assert find_anagrams("abab", "ab") == [0, 1, 2]

    def test_sliding_window_anagrams_boundary(self):
        # Empty strings
        assert find_anagrams("", "") == []
        # Pattern longer than string
        assert find_anagrams("abc", "abcd") == []
