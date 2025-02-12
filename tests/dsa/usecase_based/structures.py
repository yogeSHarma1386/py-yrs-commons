from datetime import timedelta, datetime

from yrs_commons.dsa.usecase_based.structures import (
    TaskScheduler,
    NetworkPacketProcessor,
)


class TestRealWorldExamples:
    # ===== Task Scheduler Tests =====
    def test_task_scheduler_positive(self):
        scheduler = TaskScheduler()
        now = datetime.now()

        scheduler.add_task("Urgent Bug Fix", 1, now + timedelta(hours=1))
        scheduler.add_task("Feature Development", 2, now + timedelta(hours=4))
        scheduler.add_task("Code Review", 3, now + timedelta(hours=2))

        next_task, _ = scheduler.get_next_task()
        assert next_task == "Urgent Bug Fix"

    def test_task_scheduler_boundary(self):
        scheduler = TaskScheduler()
        assert scheduler.get_next_task() is None

    # ===== Network Packet Processor Tests =====
    def test_packet_processor_positive(self):
        processor = NetworkPacketProcessor()
        processor.add_packet(1, 1024, "Server A")
        processor.add_packet(2, 512, "Server B")

        size, dest = processor.process_next_packet()
        assert size == 1024
        assert dest == "Server A"
