from unittest import TestCase
from queue_from_stack import Queue


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
        self.assertIsNone(queue.dequeue())
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
        for element in range(100_000):
            queue.enqueue(element)
            self.assertEqual(element + 1, queue.size())
        for element in range(100_000):
            queue.dequeue()
            self.assertEqual(100_000 - element - 1, queue.size())
        for element in range(5):
            queue.dequeue()
            self.assertEqual(0, queue.size())

    def test_rotate(self):
        queue = Queue()
        for element in range(500):
            queue.enqueue(element)
        queue.rotate(queue.size())
        self.assertEqual(0, queue.dequeue())
        queue.rotate(5)
        self.assertEqual(6, queue.dequeue())
