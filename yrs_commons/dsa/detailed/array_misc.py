from typing import List


# ============= Sliding Window Implementation =============
def max_sum_sliding_window(arr: List[int], k: int) -> List[int]:
    if not arr or k <= 0 or k > len(arr):
        return []

    result = []
    window_sum = sum(arr[:k])
    result.append(window_sum)

    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        result.append(window_sum)

    return result


def find_anagrams(s: str, p: str) -> List[int]:
    if len(p) > len(s):
        return []

    p_count = {}
    window_count = {}
    for char in p:
        p_count[char] = p_count.get(char, 0) + 1

    result = []
    for i in range(len(s)):
        # Add new character to window
        window_count[s[i]] = window_count.get(s[i], 0) + 1

        # Remove character from window if window size > p
        if i >= len(p):
            char = s[i - len(p)]
            window_count[char] -= 1
            if window_count[char] == 0:
                del window_count[char]

        # Check if current window is an anagram
        if i >= len(p) - 1 and window_count == p_count:
            result.append(i - len(p) + 1)

    return result


# ============= Two Pointer Implementation =============
def find_pair_sum(arr: List[int], target: int) -> tuple[int, int]:
    if len(arr) < 2:
        return -1, -1

    arr.sort()
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return left, right
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return -1, -1


def remove_duplicates(arr: List[int]) -> int:
    if not arr:
        return 0

    write_ptr = 1
    for read_ptr in range(1, len(arr)):
        if arr[read_ptr] != arr[read_ptr - 1]:
            arr[write_ptr] = arr[read_ptr]
            write_ptr += 1

    return write_ptr
