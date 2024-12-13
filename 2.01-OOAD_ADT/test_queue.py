from unittest import TestCase
from queue import Queue


class Test(TestCase):
    def test_init(self):
        queue = Queue()
        self.assertEqual(queue.DEQUEUE_ERR, queue.get_dequeue_status())
        self.assertEqual(queue.HEAD_ERR, queue.get_head_status())
        self.assertEqual(0, queue.size())

    def test_enqueue(self):
        queue = Queue()

        self.assertEqual(queue.enqueue, queue.enq)

        self.assertEqual(0, queue.size())
        self.assertIsNone(queue.enq(42))
        self.assertEqual(1, queue.size())
        self.assertIsNone(queue.enq(43))
        self.assertEqual(2, queue.size())
        self.assertIsNone(queue.enq(44))
        self.assertEqual(3, queue.size())

    def test_dequeue(self):
        queue = Queue()

        self.assertEqual(queue.dequeue, queue.deq)

        self.assertIsNone(queue.enq(42))
        self.assertIsNone(queue.enq(43))
        self.assertIsNone(queue.enq(44))
        self.assertEqual(3, queue.size())

        self.assertEqual(queue.DEQUEUE_ERR, queue.get_dequeue_status())
        self.assertIsNone(queue.deq())
        self.assertEqual(queue.DEQUEUE_OK, queue.get_dequeue_status())
        self.assertEqual(2, queue.size())

        self.assertIsNone(queue.deq())
        self.assertEqual(queue.DEQUEUE_OK, queue.get_dequeue_status())
        self.assertEqual(1, queue.size())

        self.assertIsNone(queue.deq())
        self.assertEqual(queue.DEQUEUE_OK, queue.get_dequeue_status())
        self.assertEqual(0, queue.size())

        self.assertIsNone(queue.deq())
        self.assertEqual(queue.DEQUEUE_ERR, queue.get_dequeue_status())
        self.assertEqual(0, queue.size())

    def test_clear(self):
        queue = Queue()

        self.assertIsNone(queue.enq(42))
        self.assertIsNone(queue.enq(43))
        self.assertIsNone(queue.enq(44))
        self.assertEqual(3, queue.size())

        self.assertIsNone(queue.clear())
        self.assertEqual(0, queue.size())

    def test_head(self):
        queue = Queue()

        self.assertEqual(0, queue.size())
        self.assertIsNone(queue.head())
        self.assertEqual(queue.HEAD_ERR, queue.get_head_status())

        self.assertIsNone(queue.enq(42))
        self.assertIsNone(queue.enq(43))
        self.assertIsNone(queue.enq(44))
        self.assertEqual(3, queue.size())

        self.assertEqual(42, queue.head())
        self.assertEqual(queue.HEAD_OK, queue.get_head_status())

        self.assertIsNone(queue.deq())
        self.assertEqual(43, queue.head())
        self.assertEqual(queue.HEAD_OK, queue.get_head_status())

        self.assertIsNone(queue.deq())
        self.assertEqual(44, queue.head())
        self.assertEqual(queue.HEAD_OK, queue.get_head_status())

        self.assertIsNone(queue.deq())
        self.assertIsNone(queue.head())
        self.assertEqual(queue.HEAD_ERR, queue.get_head_status())

    def test_size(self):
        queue = Queue()

        for num in range(20):
            self.assertIsNone(queue.enq(num))
            self.assertEqual(num + 1, queue.size())

        self.assertEqual(20, queue.size())
