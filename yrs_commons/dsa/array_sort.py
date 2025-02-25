import heapq


def binary_search(arr, target):  # O(log n)
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1


def bubble_sort(arr):
    """Bubble sort implementation (returns a sorted copy)."""
    result = arr.copy()
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def selection_sort(arr):
    """
    Given an array of N items and L = 0, Selection Sort will:

        - Find the position X of the smallest item in the range of [L...N−1],
        - Swap X-th item with the L-th item,
        - Increase the lower-bound L by 1 and repeat Step 1 until L = N-2.
    """
    result = arr.copy()
    n = len(result)

    for i in range(n):
        smallest = i

        for j in range(i + 1, n):
            if result[j] < result[smallest]:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]
    return result


def insertion_sort(arr):
    """
    Insertion sort is similar to how most people arrange a hand of poker cards.
        - Start with one card in your hand,
        - Pick the next card and insert it into its proper sorted order,
        - Repeat previous step for all cards.
    """
    result = arr.copy()
    for i in range(1, len(result)):
        current = result[i]
        prev_index = i - 1

        while prev_index >= 0 and result[prev_index] > current:
            result[prev_index + 1] = result[prev_index]
            prev_index -= 1
        result[prev_index + 1] = current
    return result


def merge_sort(arr):
    """Merge sort implementation (returns a sorted copy)."""
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return __merge(left, right)


def __merge(left, right):
    """Helper function for merge_sort to merge two sorted lists."""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    """Quick sort implementation (returns a sorted copy)."""
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def heap_sort(arr):
    """Heap sort implementation (returns a sorted copy)."""
    heap = arr.copy()
    heapq.heapify(heap)
    result = []
    while heap:
        result.append(heapq.heappop(heap))
    return result
