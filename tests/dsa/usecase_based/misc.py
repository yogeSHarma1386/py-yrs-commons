import unittest

import pytest

from yrs_commons.dsa.usecase_based.array_misc import (
    find_meeting_time,
    find_restaurant_location,
    track_stock_prices,
    monitor_cpu_usage,
)
from yrs_commons.dsa.usecase_based.recursion import (
    calculate_compound_interest,
    calculate_directory_size,
)


@pytest.mark.unit
class TestRealWorldArray(unittest.TestCase):

    ### # ============= Two Pointer: Real-World Examples ============= # ###
    def test_meeting_schedule_positive(self):
        person1_schedule = [(9, 10), (11, 12), (14, 16)]
        person2_schedule = [(9, 11), (13, 14), (15, 16)]
        meeting_duration = 1

        meeting_time = find_meeting_time(
            person1_schedule, person2_schedule, meeting_duration
        )
        assert meeting_time is not None

    def test_restaurant_location_positive(self):
        residential = [1, 3, 5, 7, 9]
        commercial = [2, 4, 6, 8]
        location = find_restaurant_location(residential, commercial)
        assert 1 <= location <= 9

    ### # ============= Sliding Window: Real-World Examples ============= # ###
    def test_cpu_monitoring_positive(self):
        measurements = [45.2, 52.1, 49.8, 47.5, 53.2, 50.1, 49.9]
        window = 3
        max_usage = monitor_cpu_usage(measurements, window)
        assert len(max_usage) == len(measurements) - window + 1
        assert all(x <= 53.2 for x in max_usage)

    def test_stock_tracking_positive(self):
        prices = [100.0, 102.5, 101.8, 103.2, 102.9, 105.1]
        window = 3
        max_prices = track_stock_prices(prices, window)
        assert len(max_prices) == len(prices) - window + 1


@pytest.mark.unit
class TestRealWorldRecursion(unittest.TestCase):
    def test_compound_interest_positive(self):
        principal = 1000.0
        rate = 0.05
        years = 3
        final_amount = calculate_compound_interest(principal, rate, years)
        assert final_amount > principal

    def test_directory_size_positive(self):
        directory = {
            "documents": {"text.txt": 100, "image.jpg": 2048},
            "downloads": {"video.mp4": 10240},
        }
        total_size = calculate_directory_size(directory)
        assert total_size == 12388
