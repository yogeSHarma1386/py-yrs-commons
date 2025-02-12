import heapq

from ._nodes import NodeLL, NodeDLL


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        import heapq

        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        if not self.is_empty():
            import heapq

            return heapq.heappop(self.heap)[1]
        raise IndexError("Priority Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.heap[0][1]
        raise IndexError("Priority Queue is empty")

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)


class LinkedList:  # Singly Linked List
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = NodeLL(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = NodeLL(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        elements = []
        current = self.head

        if self.is_cyclic():
            raise RecursionError(
                f"Detected cycle in {type(self.head).__name__}({self.head.data})"
            )

        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def is_cyclic(self):
        """Detects if a cycle exists in the linked list."""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = NodeDLL(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = NodeDLL(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def display_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def display_backward(self):
        elements = []
        current = self.tail
        while current:
            elements.append(current.data)
            current = current.prev
        return elements


class CircularQueue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.queue = [None] * maxsize
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Queue is full")

        self.rear = (self.rear + 1) % self.maxsize
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.maxsize
        self.size -= 1
        return item

    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.maxsize


class DeQueue:  # Double-ended Queue
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Deque is empty")

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Deque is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val: int) -> None:
        heapq.heappush(self.heap, val)

    def pop(self) -> int:
        if not self.heap:
            raise IndexError("Heap is empty")
        return heapq.heappop(self.heap)

    def peek(self) -> int:
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def size(self) -> int:
        return len(self.heap)
