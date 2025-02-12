import pytest

from yrs_commons.dsa.detailed.recursion import fibonacci, power


class TestRecursion:
    # Recursion Tests
    def test_fibonacci_positive(self):
        assert fibonacci(5) == 5
        assert fibonacci(7) == 13

    def test_fibonacci_boundary(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1

    def test_fibonacci_negative(self):
        with pytest.raises(ValueError):
            fibonacci(-1)

    def test_power_positive(self):
        assert power(2, 3) == 8
        assert power(3, 4) == 81

    def test_power_boundary(self):
        assert power(5, 0) == 1
        assert power(5, 1) == 5
