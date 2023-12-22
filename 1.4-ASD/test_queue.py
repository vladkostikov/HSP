from unittest import TestCase
from queue import Queue


class TestQueue(TestCase):
    def test_enqueue(self):
        queue = Queue()
        self.assertEqual(10, queue.enqueue(10))
        self.assertEqual(20, queue.enqueue(20))
        self.assertEqual(30, queue.enqueue(30))
        self.assertEqual(3, queue.size())
        self.assertEqual(10, queue.enqueue(10))
        self.assertEqual(4, queue.size())

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        self.assertEqual(10, queue.dequeue())
        self.assertEqual(20, queue.dequeue())
        self.assertEqual(30, queue.dequeue())
        self.assertEqual(None, queue.dequeue())

    def test_size(self):
        queue = Queue()
        self.assertEqual(0, queue.size())
        queue.enqueue(10)
        self.assertEqual(1, queue.size())
        queue.enqueue(20)
        queue.enqueue(30)
        self.assertEqual(3, queue.size())
        queue.dequeue()
        self.assertEqual(2, queue.size())
        queue.dequeue()
        self.assertEqual(1, queue.size())
        queue.dequeue()
        self.assertEqual(0, queue.size())
        queue.dequeue()
        self.assertEqual(0, queue.size())

    def test_queue_with_100_000_elements(self):
        queue = Queue()
        for element in range(10000):
            queue.enqueue(element)
            self.assertEqual(element + 1, queue.size())
        for element in range(10000):
            queue.dequeue()
            self.assertEqual(10000 - element - 1, queue.size())
        for element in range(5):
            queue.dequeue()
            self.assertEqual(0, queue.size())
