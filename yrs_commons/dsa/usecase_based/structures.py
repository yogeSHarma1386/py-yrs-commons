import heapq
from datetime import datetime
from typing import Optional, Tuple


class TaskScheduler:
    """
    Real-world example MinHeap: Priority Task Scheduler
    """

    def __init__(self):
        self.tasks = []  # [(priority, task_name, deadline)]

    def add_task(self, task_name: str, priority: int, deadline: datetime) -> None:
        heapq.heappush(self.tasks, (priority, task_name, deadline))

    def get_next_task(self) -> Optional[Tuple[str, datetime]]:
        if not self.tasks:
            return None
        priority, task_name, deadline = heapq.heappop(self.tasks)
        return task_name, deadline


class NetworkPacketProcessor:
    """
    Real-world example MinHeap: Network Packet Priority Queue
    """

    def __init__(self):
        self.packets = []  # [(priority, packet_size, destination)]

    def add_packet(self, priority: int, packet_size: int, destination: str) -> None:
        heapq.heappush(self.packets, (priority, packet_size, destination))

    def process_next_packet(self) -> Optional[Tuple[int, str]]:
        if not self.packets:
            return None
        priority, size, dest = heapq.heappop(self.packets)
        return size, dest
