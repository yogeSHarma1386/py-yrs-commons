import unittest

import pytest

from yrs_commons.dsa import (
    Stack,
    Queue,
    PriorityQueue,
    LinkedList,
    DoublyLinkedList,
    CircularQueue,
    DeQueue,
    MinHeap,
)


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    # Positive Tests
    def test_push_pop(self):
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)

    def test_multiple_push_pop(self):
        items = [1, 2, 3, 4, 5]
        for item in items:
            self.stack.push(item)

        for item in reversed(items):
            self.assertEqual(self.stack.pop(), item)

    def test_peek(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.assertEqual(self.stack.size(), 1)  # Peek shouldn't remove item

    # Negative Tests
    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_empty(self):
        with self.assertRaises(IndexError):
            self.stack.peek()

    # Boundary Tests
    def test_push_large_number(self):
        self.stack.push(10 ** 6)
        self.assertEqual(self.stack.pop(), 10 ** 6)

    def test_push_none(self):
        self.stack.push(None)
        self.assertEqual(self.stack.pop(), None)


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    # Positive Tests
    def test_enqueue_dequeue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.dequeue(), 1)

    def test_multiple_enqueue_dequeue(self):
        items = [1, 2, 3, 4, 5]
        for item in items:
            self.queue.enqueue(item)

        for item in items:
            self.assertEqual(self.queue.dequeue(), item)

    def test_front(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.front(), 1)
        self.assertEqual(self.queue.size(), 1)  # Front shouldn't remove item

    # Negative Tests
    def test_dequeue_empty(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_front_empty(self):
        with self.assertRaises(IndexError):
            self.queue.front()

    # Boundary Tests
    def test_enqueue_large_number(self):
        self.queue.enqueue(10 ** 6)
        self.assertEqual(self.queue.dequeue(), 10 ** 6)

    def test_enqueue_none(self):
        self.queue.enqueue(None)
        self.assertEqual(self.queue.dequeue(), None)


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()

    # Positive Tests
    def test_push_pop(self):
        self.pq.push("task1", 1)
        self.assertEqual(self.pq.pop(), "task1")

    def test_priority_order(self):
        items = [("task3", 3), ("task1", 1), ("task2", 2)]
        for item, priority in items:
            self.pq.push(item, priority)

        self.assertEqual(self.pq.pop(), "task1")
        self.assertEqual(self.pq.pop(), "task2")
        self.assertEqual(self.pq.pop(), "task3")

    # Negative Tests
    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.pq.pop()

    # Boundary Tests
    def test_same_priority(self):
        self.pq.push("task1", 1)
        self.pq.push("task2", 1)
        self.assertEqual(len(self.pq.heap), 2)

    def test_extreme_priority(self):
        self.pq.push("task1", -float("inf"))
        self.pq.push("task2", float("inf"))
        self.assertEqual(self.pq.pop(), "task1")


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    # Positive Tests
    def test_append(self):
        self.ll.append(1)
        self.assertEqual(self.ll.display(), [1])

    def test_prepend(self):
        self.ll.prepend(1)
        self.ll.prepend(2)
        self.assertEqual(self.ll.display(), [2, 1])

    def test_delete(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.delete(1)
        self.assertEqual(self.ll.display(), [2])

    # Negative Tests
    def test_delete_empty(self):
        self.ll.delete(1)  # Should not raise error
        self.assertEqual(self.ll.display(), [])

    def test_delete_nonexistent(self):
        self.ll.append(1)
        self.ll.delete(2)  # Should not raise error
        self.assertEqual(self.ll.display(), [1])

    # Boundary Tests
    def test_large_list(self):
        for i in range(1000):
            self.ll.append(i)
        self.assertEqual(len(self.ll.display()), 1000)

    # @pytest.mark.skip(reason="RecursionError: Detected cycle in NodeLL(1)")
    def test_cycle_detection(self):
        # Create a cycle and test if display() handles it
        self.ll.append(1)
        self.ll.append(2)
        current = self.ll.head
        while current.next:
            current = current.next
        current.next = self.ll.head
        with self.assertRaises(RecursionError):  # Should detect cycle
            self.ll.display()


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

    # Positive Tests
    def test_append(self):
        self.dll.append(1)
        self.assertEqual(self.dll.display_forward(), [1])
        self.assertEqual(self.dll.display_backward(), [1])

    def test_prepend(self):
        self.dll.prepend(1)
        self.dll.prepend(2)
        self.assertEqual(self.dll.display_forward(), [2, 1])
        self.assertEqual(self.dll.display_backward(), [1, 2])

    def test_delete(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.delete(1)
        self.assertEqual(self.dll.display_forward(), [2])

    # Negative Tests
    def test_delete_empty(self):
        self.dll.delete(1)  # Should not raise error
        self.assertEqual(self.dll.display_forward(), [])

    # Boundary Tests
    def test_bidirectional_traversal(self):
        items = list(range(100))
        for item in items:
            self.dll.append(item)
        self.assertEqual(self.dll.display_forward(), items)
        self.assertEqual(self.dll.display_backward(), list(reversed(items)))


class TestCircularQueue(unittest.TestCase):
    def setUp(self):
        self.cq = CircularQueue(3)

    # Positive Tests
    def test_enqueue_dequeue(self):
        self.cq.enqueue(1)
        self.assertEqual(self.cq.dequeue(), 1)

    def test_circular_behavior(self):
        self.cq.enqueue(1)
        self.cq.enqueue(2)
        self.cq.enqueue(3)
        self.assertEqual(self.cq.dequeue(), 1)
        self.cq.enqueue(4)  # Should wrap around
        self.assertEqual(self.cq.dequeue(), 2)

    # Negative Tests
    def test_enqueue_full(self):
        self.cq.enqueue(1)
        self.cq.enqueue(2)
        self.cq.enqueue(3)
        with self.assertRaises(IndexError):
            self.cq.enqueue(4)

    def test_dequeue_empty(self):
        with self.assertRaises(IndexError):
            self.cq.dequeue()

    # Boundary Tests
    def test_full_cycle(self):
        for i in range(self.cq.maxsize * 2):
            try:
                self.cq.enqueue(i)
                self.cq.dequeue()
            except IndexError:
                self.fail("Should handle full cycle without errors")


class TestDeque(unittest.TestCase):
    def setUp(self):
        self.deque = DeQueue()

    # Positive Tests
    def test_add_remove_front(self):
        self.deque.add_front(1)
        self.assertEqual(self.deque.remove_front(), 1)

    def test_add_remove_rear(self):
        self.deque.add_rear(1)
        self.assertEqual(self.deque.remove_rear(), 1)

    def test_mixed_operations(self):
        self.deque.add_front(1)
        self.deque.add_rear(2)
        self.assertEqual(self.deque.remove_front(), 1)
        self.assertEqual(self.deque.remove_rear(), 2)

    # Negative Tests
    def test_remove_front_empty(self):
        with self.assertRaises(IndexError):
            self.deque.remove_front()

    def test_remove_rear_empty(self):
        with self.assertRaises(IndexError):
            self.deque.remove_rear()

    # Boundary Tests
    def test_alternating_operations(self):
        operations = 100
        for i in range(operations):
            if i % 2 == 0:
                self.deque.add_front(i)
            else:
                self.deque.add_rear(i)
        self.assertEqual(self.deque.size(), operations)


class TestPerformance(unittest.TestCase):
    def test_large_stack_operations(self):
        import time

        stack = Stack()
        start_time = time.time()
        for i in range(10 ** 5):
            stack.push(i)
        for i in range(10 ** 5):
            stack.pop()
        duration = time.time() - start_time
        self.assertLess(duration, 1.0)  # Should complete within 1 second

    def test_large_queue_operations(self):
        import time

        queue = Queue()
        start_time = time.time()
        for i in range(10 ** 5):
            queue.enqueue(i)
        for i in range(10 ** 5):
            queue.dequeue()
        duration = time.time() - start_time
        self.assertLess(duration, 1.0)


class TestHeap:
    def test_heap_positive(self):  # Positive numbers
        heap = MinHeap()
        numbers = [4, 1, 7, 3, 8, 5]
        for num in numbers:
            heap.push(num)

        assert heap.peek() == 1
        assert [heap.pop() for _ in range(heap.size())] == [1, 3, 4, 5, 7, 8]

    def test_heap_boundary(self):
        heap = MinHeap()
        # Single element
        heap.push(1)
        assert heap.peek() == 1
        assert heap.pop() == 1

        # Empty heap
        with pytest.raises(IndexError):
            heap.peek()

    def test_heap_negative(self):  # Mixed positive and negative numbers
        heap = MinHeap()
        numbers = [-4, 1, -7, 3, -8, 5]
        for num in numbers:
            heap.push(num)
        assert heap.peek() == -8


if __name__ == "__main__":
    unittest.main()
