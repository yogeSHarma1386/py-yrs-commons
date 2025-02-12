from collections import deque
from numbers import Number
from typing import List, Tuple, Optional


# ============= Sliding Window: Real-World Examples =============
def max_sliding_window(nums: List[Number], k: Number) -> List[Number]:
    if not nums or k <= 0:
        return []

    result = []
    window = deque()  # Store indices

    for i, num in enumerate(nums):
        # Remove indices outside current window
        while window and window[0] < i - k + 1:
            window.popleft()

        # Remove smaller elements from back
        while window and nums[window[-1]] < num:
            window.pop()

        window.append(i)

        if i >= k - 1:
            result.append(nums[window[0]])

    return result


def monitor_cpu_usage(measurements: List[float], window_minutes: int) -> list[Number]:
    """Real-world example 1: CPU Usage Monitoring"""
    return max_sliding_window(measurements, window_minutes)


def track_stock_prices(prices: List[float], trading_window: int) -> list[Number]:
    """Real-world example 2: Stock Price Tracking"""
    return max_sliding_window(prices, trading_window)


# ============= Two Pointer: Real-World Examples =============
def find_meeting_time(
        person1_schedule: List[Tuple[int, int]],
        person2_schedule: List[Tuple[int, int]],
        meeting_duration: int,
) -> Optional[Tuple[int, int]]:
    """Real-world example 1: Meeting Schedule Finder"""
    # Convert schedules to free time blocks
    p1_free = [
        (s2[0] - s1[1]) for s1, s2 in zip(person1_schedule[:-1], person1_schedule[1:])
    ]
    p2_free = [
        (s2[0] - s1[1]) for s1, s2 in zip(person2_schedule[:-1], person2_schedule[1:])
    ]

    # Use two pointers to find overlapping free time
    i, j = 0, 0
    while i < len(p1_free) and j < len(p2_free):
        if min(p1_free[i], p2_free[j]) >= meeting_duration:
            return (
                max(person1_schedule[i][1], person2_schedule[j][1]),
                max(person1_schedule[i][1], person2_schedule[j][1]) + meeting_duration,
            )
        if p1_free[i] < p2_free[j]:
            i += 1
        else:
            j += 1
    return None


def find_restaurant_location(
        residential_areas: List[int], commercial_areas: List[int]
) -> int:
    """Real-world example 2: Optimal Restaurant Location"""
    # Find location that minimizes distance to both residential and commercial areas
    left, right = 0, len(residential_areas) - 1
    min_distance = float("inf")
    optimal_location = -1

    while left <= right:
        mid = (left + right) // 2
        res_dist = sum(abs(x - residential_areas[mid]) for x in residential_areas)
        com_dist = sum(abs(x - residential_areas[mid]) for x in commercial_areas)

        total_dist = res_dist + com_dist
        if total_dist < min_distance:
            min_distance = total_dist
            optimal_location = residential_areas[mid]

        if res_dist > com_dist:
            right = mid - 1
        else:
            left = mid + 1

    return optimal_location
