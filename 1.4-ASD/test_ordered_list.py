from unittest import TestCase
from ordered_list import OrderedList


class TestOrderedList(TestCase):
    def test_compare(self):
        ordered_list = OrderedList(True)
        self.assertEqual(-1, ordered_list.compare(100, 200))
        self.assertEqual(1, ordered_list.compare(100, 50))
        self.assertEqual(0, ordered_list.compare(100, 100))

    def test_add(self):
        ordered_list = OrderedList(True)
        self.assertEqual(0, ordered_list.len())
        self.assertEqual(10, ordered_list.add(10))
        self.assertEqual(1, ordered_list.len())
        self.assertIsNone(ordered_list.head.prev)
        self.assertIsNone(ordered_list.tail.next)
        self.assertEqual(20, ordered_list.add(20))
        self.assertEqual(2, ordered_list.len())
        self.assertEqual(20, ordered_list.head.next.value)
        self.assertIsNone(ordered_list.head.prev)
        self.assertIsNone(ordered_list.tail.next)
        self.assertEqual(30, ordered_list.add(30))
        self.assertEqual(3, ordered_list.len())
        self.assertEqual(10, ordered_list.head.value)
        self.assertEqual(30, ordered_list.tail.value)

        ordered_list_desc = OrderedList(False)
        self.assertEqual(0, ordered_list_desc.len())
        self.assertEqual(10, ordered_list_desc.add(10))
        self.assertEqual(1, ordered_list_desc.len())
        self.assertIsNone(ordered_list_desc.head.prev)
        self.assertIsNone(ordered_list_desc.tail.next)
        self.assertEqual(20, ordered_list_desc.add(20))
        self.assertEqual(10, ordered_list_desc.head.next.value)
        self.assertIsNone(ordered_list_desc.head.prev)
        self.assertIsNone(ordered_list_desc.tail.next)
        self.assertEqual(2, ordered_list_desc.len())
        self.assertEqual(30, ordered_list_desc.add(30))
        self.assertEqual(3, ordered_list_desc.len())
        self.assertEqual(30, ordered_list_desc.head.value)
        self.assertEqual(10, ordered_list_desc.tail.value)

    def test_find(self):
        ordered_list = OrderedList(True)
        for i in range(100):
            ordered_list.add(i)
        self.assertIsNone(ordered_list.find(-10))
        self.assertIsNone(ordered_list.find(110))
        self.assertEqual(0, ordered_list.find(0).value)
        self.assertEqual(50, ordered_list.find(50).value)
        self.assertEqual(99, ordered_list.find(99).value)
        self.assertIsNone(ordered_list.find(100))

        ordered_list_desc = OrderedList(False)
        for i in range(100):
            ordered_list_desc.add(i)
        self.assertIsNone(ordered_list.find(-10))
        self.assertIsNone(ordered_list.find(110))
        self.assertEqual(0, ordered_list.find(0).value)
        self.assertEqual(50, ordered_list.find(50).value)
        self.assertEqual(99, ordered_list.find(99).value)
        self.assertIsNone(ordered_list.find(100))

    def test_delete(self):
        ordered_list = OrderedList(True)
        for i in range(100):
            ordered_list.add(i)
        self.assertIsNone(ordered_list.delete(-10))
        self.assertIsNone(ordered_list.delete(110))
        self.assertIsNone(ordered_list.delete(100))

        self.assertEqual(0, ordered_list.delete(0))
        self.assertIsNone(ordered_list.delete(0))
        self.assertEqual(99, ordered_list.delete(99))
        self.assertIsNone(ordered_list.delete(99))
        self.assertEqual(50, ordered_list.delete(50))
        self.assertIsNone(ordered_list.delete(50))

        self.assertEqual(50, ordered_list.add(50))
        self.assertEqual(50, ordered_list.add(50))
        self.assertEqual(50, ordered_list.delete(50))
        self.assertEqual(50, ordered_list.delete(50))
        self.assertIsNone(ordered_list.delete(50))

        for _i in range(ordered_list.len()):
            if _i == 96:
                None
            self.assertEqual(ordered_list.head.value, ordered_list.delete(ordered_list.head.value))
        self.assertEqual(0, ordered_list.len())
        self.assertIsNone(ordered_list.delete(10))

    def test_clean(self):
        ordered_list = OrderedList(True)
        for i in range(100):
            ordered_list.add(i)
        self.assertEqual(100, ordered_list.len())

        self.assertIsNone(ordered_list.clean(False))
        self.assertEqual(0, ordered_list.len())
        for i in range(100):
            ordered_list.add(i)
        self.assertEqual(99, ordered_list.head.value)
        self.assertEqual(0, ordered_list.tail.value)

    def test_len(self):
        ordered_list = OrderedList(True)
        self.assertEqual(0, ordered_list.len())
        for i in range(100):
            self.assertEqual(i, ordered_list.add(i))
            self.assertEqual(i + 1, ordered_list.len())

        ordered_list.clean(True)
        for i in range(100):
            self.assertEqual(i, ordered_list.add(i))
            self.assertEqual(i + 1, ordered_list.len())

    def test_get_all(self):
        ordered_list = OrderedList(True)
        self.assertEqual(0, ordered_list.len())
        self.assertEqual([], ordered_list.get_all())
        for i in range(100):
            ordered_list.add(i)
        self.assertEqual(list(range(100)), list(map(lambda node: node.value, ordered_list.get_all())))
        self.assertEqual(100, ordered_list.len())

        ordered_list_desc = OrderedList(False)
        self.assertEqual(0, ordered_list_desc.len())
        self.assertEqual([], ordered_list_desc.get_all())
        for i in range(100):
            ordered_list_desc.add(i)
        self.assertEqual(list(range(99, -1, -1)),
                         list(map(lambda node: node.value, ordered_list_desc.get_all())))
        self.assertEqual(100, ordered_list_desc.len())
