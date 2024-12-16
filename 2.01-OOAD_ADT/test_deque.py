from unittest import TestCase
from deque import ParentQueue
from deque import Queue
from deque import Deque


class TestParentQueue(TestCase):
    def test_init(self):
        parent_queue = ParentQueue()
        self.assertEqual(parent_queue.REMOVE_FRONT_ERR, parent_queue.get_remove_front_status())
        self.assertEqual(parent_queue.GET_HEAD_ERR, parent_queue.get_get_head_status())
        self.assertEqual(0, parent_queue.size())

    def test_add_tail(self):
        parent_queue = ParentQueue()

        self.assertEqual(0, parent_queue.size())
        self.assertIsNone(parent_queue.add_tail(42))
        self.assertEqual(1, parent_queue.size())
        self.assertIsNone(parent_queue.add_tail(43))
        self.assertIsNone(parent_queue.add_tail(44))
        self.assertEqual(3, parent_queue.size())

    def test_get_head(self):
        parent_queue = ParentQueue()

        self.assertEqual(0, parent_queue.size())
        self.assertIsNone(parent_queue.get_head())
        self.assertEqual(parent_queue.GET_HEAD_ERR, parent_queue.get_get_head_status())

        self.assertIsNone(parent_queue.add_tail(42))
        self.assertEqual(1, parent_queue.size())
        self.assertEqual(42, parent_queue.get_head())
        self.assertEqual(parent_queue.GET_HEAD_OK, parent_queue.get_get_head_status())

        self.assertIsNone(parent_queue.add_tail(43))
        self.assertEqual(2, parent_queue.size())
        self.assertEqual(42, parent_queue.get_head())
        self.assertEqual(parent_queue.GET_HEAD_OK, parent_queue.get_get_head_status())

        self.assertIsNone(parent_queue.add_tail(44))
        self.assertEqual(3, parent_queue.size())
        self.assertEqual(42, parent_queue.get_head())
        self.assertEqual(parent_queue.GET_HEAD_OK, parent_queue.get_get_head_status())

    def test_remove_front(self):
        parent_queue = ParentQueue()

        self.assertEqual(0, parent_queue.size())
        self.assertIsNone(parent_queue.remove_front())
        self.assertEqual(parent_queue.REMOVE_FRONT_ERR, parent_queue.get_remove_front_status())

        self.assertIsNone(parent_queue.add_tail(42))
        self.assertIsNone(parent_queue.add_tail(43))
        self.assertIsNone(parent_queue.add_tail(44))
        self.assertEqual(3, parent_queue.size())

        self.assertEqual(42, parent_queue.get_head())
        self.assertEqual(parent_queue.GET_HEAD_OK, parent_queue.get_get_head_status())
        self.assertIsNone(parent_queue.remove_front())
        self.assertEqual(parent_queue.REMOVE_FRONT_OK, parent_queue.get_remove_front_status())
        self.assertEqual(2, parent_queue.size())

        self.assertEqual(43, parent_queue.get_head())
        self.assertEqual(parent_queue.GET_HEAD_OK, parent_queue.get_get_head_status())
        self.assertIsNone(parent_queue.remove_front())
        self.assertEqual(parent_queue.REMOVE_FRONT_OK, parent_queue.get_remove_front_status())
        self.assertEqual(1, parent_queue.size())

        self.assertEqual(44, parent_queue.get_head())
        self.assertEqual(parent_queue.GET_HEAD_OK, parent_queue.get_get_head_status())
        self.assertIsNone(parent_queue.remove_front())
        self.assertEqual(parent_queue.REMOVE_FRONT_OK, parent_queue.get_remove_front_status())
        self.assertEqual(0, parent_queue.size())

        self.assertIsNone(parent_queue.get_head())
        self.assertEqual(parent_queue.GET_HEAD_ERR, parent_queue.get_get_head_status())
        self.assertIsNone(parent_queue.remove_front())
        self.assertEqual(parent_queue.REMOVE_FRONT_ERR, parent_queue.get_remove_front_status())
        self.assertEqual(0, parent_queue.size())


class TestQueue(TestCase):
    def test_init(self):
        queue = Queue()
        self.assertTrue(issubclass(Queue, ParentQueue))
        self.assertEqual(queue.REMOVE_FRONT_ERR, queue.get_remove_front_status())
        self.assertEqual(queue.GET_HEAD_ERR, queue.get_get_status())
        self.assertEqual(0, queue.size())

    def test_get(self):
        queue = Queue()

        self.assertEqual(0, queue.size())
        self.assertIsNone(queue.get())
        self.assertEqual(queue.GET_HEAD_ERR, queue.get_get_status())

        self.assertIsNone(queue.add_tail(42))
        self.assertEqual(1, queue.size())
        self.assertEqual(42, queue.get())
        self.assertEqual(queue.GET_HEAD_OK, queue.get_get_status())

        self.assertIsNone(queue.add_tail(43))
        self.assertEqual(2, queue.size())
        self.assertEqual(42, queue.get())
        self.assertEqual(queue.GET_HEAD_OK, queue.get_get_status())

        self.assertIsNone(queue.add_tail(44))
        self.assertEqual(3, queue.size())
        self.assertEqual(42, queue.get())
        self.assertEqual(queue.GET_HEAD_OK, queue.get_get_status())


class TestDeque(TestCase):
    def test_init(self):
        deque = Deque()
        self.assertTrue(issubclass(Deque, ParentQueue))
        self.assertEqual(deque.REMOVE_FRONT_ERR, deque.get_remove_front_status())
        self.assertEqual(deque.GET_HEAD_ERR, deque.get_get_head_status())
        self.assertEqual(deque.REMOVE_TAIL_ERR, deque.get_remove_tail_status())
        self.assertEqual(deque.GET_TAIL_ERR, deque.get_get_tail_status())
        self.assertEqual(0, deque.size())

    def test_add_front(self):
        deque = Deque()

        self.assertIsNone(deque.add_front(42))
        self.assertEqual(42, deque.get_head())
        self.assertEqual(deque.GET_HEAD_OK, deque.get_get_head_status())
        self.assertEqual(1, deque.size())

        self.assertIsNone(deque.add_front(43))
        self.assertEqual(43, deque.get_head())
        self.assertEqual(deque.GET_HEAD_OK, deque.get_get_head_status())
        self.assertEqual(2, deque.size())

        self.assertIsNone(deque.add_front(44))
        self.assertEqual(44, deque.get_head())
        self.assertEqual(deque.GET_HEAD_OK, deque.get_get_head_status())
        self.assertEqual(3, deque.size())

    def test_get_tail(self):
        deque = Deque()

        self.assertEqual(0, deque.size())
        self.assertIsNone(deque.get_tail())
        self.assertEqual(deque.GET_TAIL_ERR, deque.get_get_tail_status())

        self.assertIsNone(deque.add_front(42))
        self.assertEqual(42, deque.get_tail())
        self.assertEqual(deque.GET_TAIL_OK, deque.get_get_tail_status())

        self.assertIsNone(deque.add_tail(43))
        self.assertEqual(43, deque.get_tail())
        self.assertEqual(deque.GET_TAIL_OK, deque.get_get_tail_status())

        self.assertIsNone(deque.add_tail(44))
        self.assertEqual(44, deque.get_tail())
        self.assertEqual(deque.GET_TAIL_OK, deque.get_get_tail_status())

    def test_remove_tail(self):
        deque = Deque()

        self.assertEqual(0, deque.size())
        self.assertIsNone(deque.remove_tail())
        self.assertEqual(deque.REMOVE_TAIL_ERR, deque.get_remove_tail_status())

        self.assertIsNone(deque.add_tail(42))
        self.assertIsNone(deque.add_front(43))
        self.assertIsNone(deque.add_front(44))
        self.assertEqual(42, deque.get_tail())
        self.assertEqual(deque.GET_TAIL_OK, deque.get_get_tail_status())
        self.assertEqual(44, deque.get_head())
        self.assertEqual(deque.GET_HEAD_OK, deque.get_get_head_status())
        self.assertEqual(3, deque.size())

        self.assertIsNone(deque.remove_tail())
        self.assertEqual(deque.REMOVE_TAIL_OK, deque.get_remove_tail_status())
        self.assertEqual(2, deque.size())

        self.assertIsNone(deque.remove_tail())
        self.assertEqual(deque.REMOVE_TAIL_OK, deque.get_remove_tail_status())
        self.assertEqual(1, deque.size())

        self.assertEqual(44, deque.get_head())
        self.assertEqual(deque.GET_HEAD_OK, deque.get_get_head_status())
        self.assertEqual(44, deque.get_tail())
        self.assertEqual(deque.GET_TAIL_OK, deque.get_get_tail_status())
