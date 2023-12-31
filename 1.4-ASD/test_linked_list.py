from unittest import TestCase
from linked_list import LinkedList
from linked_list import Node


class TestLinkedList(TestCase):
    def test_init(self):
        linked_list = LinkedList()
        self.assertEqual(0, linked_list.len())

    def test_add_in_tail(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(2))
        linked_list.add_in_tail(Node(4))
        linked_list.add_in_tail(Node(8))
        self.assertEqual(1, linked_list.head.value)
        self.assertEqual(8, linked_list.tail.value)
        self.assertEqual(4, linked_list.len())

    def test_find(self):
        node = Node(5)
        linked_list = LinkedList()
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(node)
        linked_list.add_in_tail(Node(5))
        self.assertIs(node, linked_list.find(node.value))

    def test_find_all(self):
        node1 = Node(1)
        node5_1 = Node(5)
        node5_2 = Node(5)
        node5_3 = Node(5)
        node8 = Node(8)
        linked_list = LinkedList()
        linked_list.add_in_tail(node1)
        linked_list.add_in_tail(node5_1)
        linked_list.add_in_tail(node5_2)
        linked_list.add_in_tail(node5_3)
        linked_list.add_in_tail(node8)
        self.assertEqual([node1], linked_list.find_all(1))
        self.assertEqual([node5_1, node5_2, node5_3], linked_list.find_all(5))
        self.assertEqual([], linked_list.find_all(10))

    def test_delete(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(2))
        linked_list.add_in_tail(Node(4))
        linked_list.add_in_tail(Node(4))
        linked_list.add_in_tail(Node(4))
        linked_list.add_in_tail(Node(6))
        linked_list.add_in_tail(Node(4))
        linked_list.add_in_tail(Node(8))
        linked_list.add_in_tail(Node(8))
        linked_list.add_in_tail(Node(10))
        self.assertEqual(10, linked_list.len())
        linked_list.delete(2)
        self.assertEqual(9, linked_list.len())
        linked_list.delete(1)
        self.assertEqual(8, linked_list.len())
        linked_list.delete(10)
        self.assertEqual(7, linked_list.len())
        linked_list.delete(4, True)
        self.assertEqual(3, linked_list.len())
        linked_list.delete(8, True)
        self.assertEqual(1, linked_list.len())
        linked_list.delete(6, True)
        self.assertEqual(0, linked_list.len())
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

    def test_clean(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(2))
        linked_list.add_in_tail(Node(4))
        linked_list.add_in_tail(Node(8))
        self.assertEqual(4, linked_list.len())
        linked_list.clean()
        self.assertEqual(0, linked_list.len())
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

    def test_len(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(2))
        linked_list.add_in_tail(Node(4))
        linked_list.add_in_tail(Node(8))
        self.assertEqual(4, linked_list.len())

    def test_insert(self):
        node4 = Node(4)
        node42 = Node(42)
        node50 = Node(50)
        linked_list = LinkedList()
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(2))
        linked_list.add_in_tail(node4)
        linked_list.add_in_tail(Node(8))
        self.assertEqual(4, linked_list.len())
        linked_list.insert(None, node42)
        self.assertEqual(42, linked_list.head.value)
        self.assertEqual(5, linked_list.len())
        linked_list.insert(node4, node50)
        self.assertEqual(node50, node4.next)
        self.assertEqual(6, linked_list.len())

        node22 = Node(22)
        linked_list = LinkedList()
        linked_list.insert(None, node22)
        self.assertEqual(1, linked_list.len())
        self.assertEqual(node22, linked_list.head)
        self.assertEqual(node22, linked_list.tail)
    def test_sum_of_two_linked_lists(self):
        first_list = LinkedList()
        second_list = LinkedList()
        third_list = LinkedList()
        self.assertEqual([], first_list.sum_of_two_linked_lists(second_list))

        first_list.add_in_tail(Node(1))
        first_list.add_in_tail(Node(2))
        first_list.add_in_tail(Node(4))
        first_list.add_in_tail(Node(8))

        second_list.add_in_tail(Node(1))
        second_list.add_in_tail(Node(2))
        second_list.add_in_tail(Node(3))
        second_list.add_in_tail(Node(4))

        third_list = LinkedList()
        third_list.add_in_tail(Node(1))
        third_list.add_in_tail(Node(2))
        third_list.add_in_tail(Node(3))

        self.assertEqual([2, 4, 7, 12], first_list.sum_of_two_linked_lists(second_list))
        self.assertEqual(None, first_list.sum_of_two_linked_lists(third_list))
        self.assertEqual(None, third_list.sum_of_two_linked_lists(first_list))
