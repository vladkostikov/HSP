from unittest import TestCase
from two_way_list import ParentList
from two_way_list import LinkedList
from two_way_list import TwoWayList


class Test(TestCase):
    def test_init(self):
        parent_list = ParentList()

        self.assertEqual(parent_list.HEAD_ERR, parent_list.get_head_status())
        self.assertEqual(parent_list.RIGHT_ERR, parent_list.get_right_status())
        self.assertEqual(parent_list.GET_ERR, parent_list.get_get_status())
        self.assertEqual(parent_list.ADD_TO_EMPTY_NIL, parent_list.get_add_to_empty_status())
        self.assertEqual(parent_list.PUT_RIGHT_ERR, parent_list.get_put_right_status())
        self.assertEqual(parent_list.PUT_LEFT_ERR, parent_list.get_put_left_status())
        self.assertEqual(parent_list.REMOVE_ERR, parent_list.get_remove_status())
        self.assertEqual(parent_list.REPLACE_ERR, parent_list.get_replace_status())
        self.assertEqual(parent_list.FIND_ERR, parent_list.get_find_status())
        self.assertEqual(parent_list.REMOVE_ALL_ERR, parent_list.get_remove_all_status())

    def test_head_with_empty_list(self):
        parent_list = ParentList()

        self.assertIsNone(parent_list.head())
        self.assertEqual(parent_list.HEAD_ERR, parent_list.get_head_status())

    def test_head_with_non_empty_list(self):
        parent_list = ParentList()

        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertIsNone(parent_list.put_left(41))
        self.assertIsNone(parent_list.put_right(43))

        self.assertEqual(42, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

        self.assertIsNone(parent_list.head())
        self.assertEqual(parent_list.HEAD_OK, parent_list.get_head_status())
        self.assertEqual(41, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

    def test_tail_with_empty_list(self):
        parent_list = ParentList()

        self.assertIsNone(parent_list.tail())
        self.assertEqual(parent_list.TAIL_ERR, parent_list.get_head_status())

    def test_tail_with_non_empty_list(self):
        parent_list = ParentList()

        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertIsNone(parent_list.put_left(41))
        self.assertIsNone(parent_list.put_right(43))

        self.assertEqual(42, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

        self.assertIsNone(parent_list.tail())
        self.assertEqual(parent_list.TAIL_OK, parent_list.get_head_status())
        self.assertEqual(43, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

    def test_right_with_empty_list(self):
        parent_list = ParentList()

        self.assertIsNone(parent_list.right())
        self.assertEqual(parent_list.RIGHT_ERR, parent_list.get_right_status())

    def test_right_with_non_empty_list(self):
        parent_list = ParentList()

        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertIsNone(parent_list.put_left(41))
        self.assertIsNone(parent_list.put_right(43))

        self.assertEqual(42, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

        self.assertIsNone(parent_list.right())
        self.assertEqual(43, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

        self.assertIsNone(parent_list.right())
        self.assertEqual(parent_list.RIGHT_ERR, parent_list.get_right_status())
        self.assertEqual(43, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

    def test_get(self):
        parent_list = ParentList()

        self.assertIsNone(parent_list.get())
        self.assertEqual(parent_list.GET_ERR, parent_list.get_get_status())

        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertEqual(42, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

        self.assertIsNone(parent_list.put_right(43))
        self.assertEqual(42, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())
        self.assertIsNone(parent_list.right())
        self.assertEqual(parent_list.RIGHT_OK, parent_list.get_right_status())
        self.assertEqual(43, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

        self.assertIsNone(parent_list.right())
        self.assertEqual(parent_list.RIGHT_ERR, parent_list.get_right_status())
        self.assertEqual(43, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

    def test_size_with_empty_list(self):
        parent_list = ParentList()

        self.assertEqual(0, parent_list.size())

    def test_size_with_non_empty_list(self):
        parent_list = ParentList()

        self.assertEqual(0, parent_list.size())
        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertEqual(1, parent_list.size())

        counter = 1
        for value in range(5):
            self.assertIsNone(parent_list.put_right(value))
            self.assertEqual(counter + 1, parent_list.size())
            counter += 1
        self.assertEqual(6, parent_list.size())

        self.assertIsNone(parent_list.clear())
        self.assertEqual(0, parent_list.size())

    def test_add_to_empty_with_empty_list(self):
        parent_list = ParentList()

        self.assertEqual(0, parent_list.size())
        self.assertEqual(parent_list.ADD_TO_EMPTY_NIL, parent_list.get_add_to_empty_status())

        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertEqual(parent_list.ADD_TO_EMPTY_OK, parent_list.get_add_to_empty_status())

        self.assertEqual(1, parent_list.size())
        self.assertEqual(42, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

    def test_add_to_empty_with_non_empty_list(self):
        parent_list = ParentList()

        self.assertEqual(0, parent_list.size())
        self.assertEqual(parent_list.ADD_TO_EMPTY_NIL, parent_list.get_add_to_empty_status())

        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertEqual(parent_list.ADD_TO_EMPTY_OK, parent_list.get_add_to_empty_status())

        self.assertEqual(1, parent_list.size())
        self.assertEqual(42, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

        self.assertIsNone(parent_list.add_to_empty(4242))
        self.assertEqual(parent_list.ADD_TO_EMPTY_ERR, parent_list.get_add_to_empty_status())

    def test_put_right_to_empty_list(self):
        parent_list = ParentList()

        self.assertEqual(0, parent_list.size())

        self.assertIsNone(parent_list.put_right(42))
        self.assertEqual(parent_list.PUT_RIGHT_ERR, parent_list.get_put_right_status())
        self.assertEqual(0, parent_list.size())

    def test_put_right_to_non_empty_list(self):
        parent_list = ParentList()

        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertEqual(1, parent_list.size())
        self.assertEqual(42, parent_list.get())

        self.assertIsNone(parent_list.put_right(43))
        self.assertEqual(parent_list.PUT_RIGHT_OK, parent_list.get_put_right_status())
        self.assertEqual(2, parent_list.size())
        self.assertEqual(42, parent_list.get())
        self.assertIsNone(parent_list.right())
        self.assertEqual(43, parent_list.get())

    def test_put_left_to_empty_list(self):
        parent_list = ParentList()

        self.assertEqual(0, parent_list.size())

        self.assertIsNone(parent_list.put_left(42))
        self.assertEqual(parent_list.PUT_LEFT_ERR, parent_list.get_put_left_status())
        self.assertEqual(0, parent_list.size())

    def test_put_left_to_non_empty_list(self):
        parent_list = ParentList()

        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertEqual(1, parent_list.size())
        self.assertEqual(42, parent_list.get())

        self.assertIsNone(parent_list.put_left(43))
        self.assertEqual(parent_list.PUT_LEFT_OK, parent_list.get_put_left_status())
        self.assertEqual(2, parent_list.size())
        self.assertEqual(42, parent_list.get())
        self.assertIsNone(parent_list.head())
        self.assertEqual(parent_list.HEAD_OK, parent_list.get_head_status())
        self.assertEqual(43, parent_list.get())

    def test_remove_from_empty_list(self):
        parent_list = ParentList()
        self.assertEqual(0, parent_list.size())

        self.assertIsNone(parent_list.remove())
        self.assertEqual(parent_list.REMOVE_ERR, parent_list.get_remove_status())

    def test_remove_from_list_with_1_node(self):
        parent_list = ParentList()

        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertEqual(1, parent_list.size())
        self.assertEqual(42, parent_list.get())

        self.assertIsNone(parent_list.remove())
        self.assertEqual(parent_list.REMOVE_OK, parent_list.get_remove_status())

        self.assertEqual(0, parent_list.size())
        self.assertIsNone(parent_list.get())
        self.assertEqual(parent_list.GET_ERR, parent_list.get_get_status())

    def test_remove_from_list_with_right_node(self):
        parent_list = ParentList()

        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertIsNone(parent_list.put_right(43))
        self.assertEqual(2, parent_list.size())
        self.assertEqual(42, parent_list.get())

        self.assertIsNone(parent_list.remove())
        self.assertEqual(parent_list.REMOVE_OK, parent_list.get_remove_status())

        self.assertEqual(1, parent_list.size())
        self.assertEqual(43, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

    def test_remove_from_list_with_left_node(self):
        parent_list = ParentList()

        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertIsNone(parent_list.put_right(43))
        self.assertEqual(2, parent_list.size())
        self.assertEqual(42, parent_list.get())
        self.assertIsNone(parent_list.right())
        self.assertEqual(43, parent_list.get())

        self.assertIsNone(parent_list.remove())
        self.assertEqual(parent_list.REMOVE_OK, parent_list.get_remove_status())

        self.assertEqual(1, parent_list.size())
        self.assertEqual(42, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

    def test_remove_from_list_with_left_and_right_node(self):
        parent_list = ParentList()

        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertIsNone(parent_list.put_left(41))
        self.assertIsNone(parent_list.put_right(43))
        self.assertEqual(3, parent_list.size())
        self.assertEqual(42, parent_list.get())

        self.assertIsNone(parent_list.remove())
        self.assertEqual(parent_list.REMOVE_OK, parent_list.get_remove_status())

        self.assertEqual(2, parent_list.size())
        self.assertEqual(43, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

    def test_clear_with_empty_list(self):
        parent_list = ParentList()

        self.assertEqual(0, parent_list.size())
        self.assertEqual(0, parent_list.size())
        self.assertIsNone(parent_list.get())

    def test_clear_with_non_empty_list(self):
        parent_list = ParentList()

        self.assertEqual(0, parent_list.size())
        self.assertIsNone(parent_list.add_to_empty(42))
        for value in range(5):
            self.assertIsNone(parent_list.put_right(value))
        self.assertEqual(6, parent_list.size())

        self.assertIsNone(parent_list.clear())
        self.assertEqual(0, parent_list.size())
        self.assertIsNone(parent_list.get())

    def test_add_tail_to_empty_list(self):
        parent_list = ParentList()

        self.assertEqual(0, parent_list.size())
        self.assertIsNone(parent_list.add_tail(42))
        self.assertIsNone(parent_list.get())
        self.assertIsNone(parent_list.tail())
        self.assertEqual(42, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

    def test_add_tail_to_non_empty_list(self):
        parent_list = ParentList()

        self.assertEqual(0, parent_list.size())
        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertEqual(parent_list.ADD_TO_EMPTY_OK, parent_list.get_add_to_empty_status())
        self.assertEqual(1, parent_list.size())
        self.assertEqual(42, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

        self.assertIsNone(parent_list.add_tail(43))
        self.assertEqual(2, parent_list.size())

        self.assertIsNone(parent_list.add_tail(44))
        self.assertEqual(3, parent_list.size())

        self.assertIsNone(parent_list.right())
        self.assertEqual(parent_list.RIGHT_OK, parent_list.get_right_status())
        self.assertEqual(43, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

        self.assertIsNone(parent_list.right())
        self.assertEqual(parent_list.RIGHT_OK, parent_list.get_right_status())
        self.assertEqual(44, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

    def test_replace_with_empty_list(self):
        parent_list = ParentList()

        self.assertEqual(0, parent_list.size())
        self.assertIsNone(parent_list.replace(42))
        self.assertEqual(parent_list.REPLACE_ERR, parent_list.get_replace_status())
        self.assertEqual(0, parent_list.size())

    def test_replace_with_non_empty_list(self):
        parent_list = ParentList()

        self.assertEqual(0, parent_list.size())
        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertEqual(parent_list.ADD_TO_EMPTY_OK, parent_list.get_add_to_empty_status())
        self.assertEqual(1, parent_list.size())
        self.assertEqual(42, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

        self.assertIsNone(parent_list.replace(43))
        self.assertEqual(parent_list.REPLACE_OK, parent_list.get_replace_status())
        self.assertEqual(43, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())
        self.assertEqual(1, parent_list.size())

    def test_find_without_value_in_list(self):
        parent_list = ParentList()

        self.assertEqual(0, parent_list.size())
        self.assertIsNone(parent_list.find(42))
        self.assertEqual(parent_list.FIND_EMPTY, parent_list.get_find_status())

        self.assertIsNone(parent_list.add_to_empty(40))
        self.assertIsNone(parent_list.add_tail(41))
        self.assertEqual(2, parent_list.size())
        self.assertEqual(40, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

        self.assertIsNone(parent_list.find(42))
        self.assertEqual(parent_list.FIND_ERR, parent_list.get_find_status())
        self.assertEqual(40, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

    def test_find_with_value_in_list(self):
        parent_list = ParentList()

        self.assertIsNone(parent_list.find(42))
        self.assertEqual(parent_list.FIND_EMPTY, parent_list.get_find_status())

        self.assertIsNone(parent_list.add_to_empty(40))
        self.assertIsNone(parent_list.add_tail(41))
        self.assertIsNone(parent_list.add_tail(42))
        self.assertIsNone(parent_list.add_tail(43))
        self.assertIsNone(parent_list.add_tail(44))
        self.assertEqual(5, parent_list.size())
        self.assertEqual(40, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

        self.assertIsNone(parent_list.find(42))
        self.assertEqual(parent_list.FIND_OK, parent_list.get_find_status())
        self.assertEqual(42, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

        self.assertIsNone(parent_list.find(44))
        self.assertEqual(parent_list.FIND_OK, parent_list.get_find_status())
        self.assertEqual(44, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

        self.assertIsNone(parent_list.find(43))
        self.assertEqual(parent_list.FIND_ERR, parent_list.get_find_status())
        self.assertEqual(44, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

    def test_remove_all_with_empty_list(self):
        parent_list = ParentList()

        self.assertIsNone(parent_list.remove_all(42))
        self.assertEqual(parent_list.REMOVE_ALL_ERR, parent_list.get_remove_all_status())

    def test_remove_all_with_non_empty_list(self):
        parent_list = ParentList()

        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertIsNone(parent_list.add_tail(43))
        self.assertIsNone(parent_list.add_tail(44))
        self.assertIsNone(parent_list.add_tail(43))
        self.assertIsNone(parent_list.add_tail(44))
        self.assertIsNone(parent_list.add_tail(45))
        self.assertEqual(6, parent_list.size())
        self.assertEqual(42, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())

        self.assertIsNone(parent_list.remove_all(43))
        self.assertEqual(parent_list.REMOVE_ALL_OK, parent_list.get_remove_all_status())
        self.assertEqual(42, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())
        self.assertEqual(4, parent_list.size())

        self.assertIsNone(parent_list.remove_all(42))
        self.assertEqual(parent_list.REMOVE_ALL_OK, parent_list.get_remove_all_status())
        self.assertEqual(44, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())
        self.assertEqual(3, parent_list.size())

        self.assertIsNone(parent_list.remove_all(44))
        self.assertEqual(parent_list.REMOVE_ALL_OK, parent_list.get_remove_all_status())
        self.assertEqual(45, parent_list.get())
        self.assertEqual(parent_list.GET_OK, parent_list.get_get_status())
        self.assertEqual(1, parent_list.size())

        self.assertIsNone(parent_list.remove_all(45))
        self.assertEqual(parent_list.REMOVE_ALL_OK, parent_list.get_remove_all_status())
        self.assertIsNone(parent_list.get())
        self.assertEqual(parent_list.GET_ERR, parent_list.get_get_status())
        self.assertEqual(0, parent_list.size())

    def test_is_head(self):
        parent_list = ParentList()

        self.assertFalse(parent_list.is_head())
        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertTrue(parent_list.is_head())
        self.assertIsNone(parent_list.put_right(43))
        self.assertTrue(parent_list.is_head())
        self.assertIsNone(parent_list.put_left(41))
        self.assertFalse(parent_list.is_head())

    def test_is_tail(self):
        parent_list = ParentList()

        self.assertFalse(parent_list.is_tail())
        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertTrue(parent_list.is_tail())
        self.assertIsNone(parent_list.put_left(41))
        self.assertTrue(parent_list.is_tail())
        self.assertIsNone(parent_list.put_right(43))
        self.assertFalse(parent_list.is_tail())

    def test_is_value(self):
        parent_list = ParentList()

        self.assertFalse(parent_list.is_value())
        self.assertIsNone(parent_list.add_to_empty(42))
        self.assertTrue(parent_list.is_value())
        self.assertIsNone(parent_list.put_left(41))
        self.assertTrue(parent_list.is_value())
        self.assertIsNone(parent_list.put_right(43))
        self.assertTrue(parent_list.is_value())

        self.assertIsNone(parent_list.clear())
        self.assertFalse(parent_list.is_value())

    def test_linked_list_init(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.HEAD_ERR, linked_list.get_head_status())
        self.assertEqual(linked_list.RIGHT_ERR, linked_list.get_right_status())
        self.assertEqual(linked_list.GET_ERR, linked_list.get_get_status())
        self.assertEqual(linked_list.ADD_TO_EMPTY_NIL, linked_list.get_add_to_empty_status())
        self.assertEqual(linked_list.PUT_RIGHT_ERR, linked_list.get_put_right_status())
        self.assertEqual(linked_list.PUT_LEFT_ERR, linked_list.get_put_left_status())
        self.assertEqual(linked_list.REMOVE_ERR, linked_list.get_remove_status())
        self.assertEqual(linked_list.REPLACE_ERR, linked_list.get_replace_status())
        self.assertEqual(linked_list.FIND_ERR, linked_list.get_find_status())
        self.assertEqual(linked_list.REMOVE_ALL_ERR, linked_list.get_remove_all_status())

    def test_two_way_list_init(self):
        two_way_list = TwoWayList()

        self.assertEqual(two_way_list.HEAD_ERR, two_way_list.get_head_status())
        self.assertEqual(two_way_list.RIGHT_ERR, two_way_list.get_right_status())
        self.assertEqual(two_way_list.GET_ERR, two_way_list.get_get_status())
        self.assertEqual(two_way_list.ADD_TO_EMPTY_NIL, two_way_list.get_add_to_empty_status())
        self.assertEqual(two_way_list.PUT_RIGHT_ERR, two_way_list.get_put_right_status())
        self.assertEqual(two_way_list.PUT_LEFT_ERR, two_way_list.get_put_left_status())
        self.assertEqual(two_way_list.REMOVE_ERR, two_way_list.get_remove_status())
        self.assertEqual(two_way_list.REPLACE_ERR, two_way_list.get_replace_status())
        self.assertEqual(two_way_list.FIND_ERR, two_way_list.get_find_status())
        self.assertEqual(two_way_list.REMOVE_ALL_ERR, two_way_list.get_remove_all_status())
        self.assertEqual(two_way_list.LEFT_ERR, two_way_list.get_right_status())

    def test_two_way_list_left(self):
        two_way_list = TwoWayList()

        self.assertEqual(0, two_way_list.size())
        self.assertIsNone(two_way_list.left())
        self.assertEqual(two_way_list.LEFT_ERR, two_way_list.get_left_status())

        self.assertIsNone(two_way_list.add_to_empty(42))
        self.assertIsNone(two_way_list.left())
        self.assertEqual(two_way_list.LEFT_ERR, two_way_list.get_left_status())

        self.assertIsNone(two_way_list.add_tail(43))
        self.assertIsNone(two_way_list.add_tail(44))
        self.assertEqual(3, two_way_list.size())
        self.assertIsNone(two_way_list.tail())
        self.assertEqual(44, two_way_list.get())
        self.assertEqual(two_way_list.GET_OK, two_way_list.get_get_status())

        self.assertIsNone(two_way_list.left())
        self.assertEqual(two_way_list.LEFT_OK, two_way_list.get_left_status())
        self.assertEqual(43, two_way_list.get())
        self.assertEqual(two_way_list.GET_OK, two_way_list.get_get_status())

        self.assertIsNone(two_way_list.left())
        self.assertEqual(two_way_list.LEFT_OK, two_way_list.get_left_status())
        self.assertEqual(42, two_way_list.get())
        self.assertEqual(two_way_list.GET_OK, two_way_list.get_get_status())

        self.assertIsNone(two_way_list.left())
        self.assertEqual(two_way_list.LEFT_ERR, two_way_list.get_left_status())
        self.assertEqual(42, two_way_list.get())
        self.assertEqual(two_way_list.GET_OK, two_way_list.get_get_status())
