from unittest import TestCase
from linked_list import LinkedList


class Test(TestCase):
    def test_init(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.HEAD_NIL, linked_list.get_head_status())
        self.assertEqual(linked_list.TAIL_NIL, linked_list.get_tail_status())
        self.assertEqual(linked_list.RIGHT_NIL, linked_list.get_right_status())
        self.assertEqual(linked_list.GET_NIL, linked_list.get_get_status())
        self.assertEqual(linked_list.ADD_TO_EMPTY_NIL, linked_list.get_add_to_empty_status())
        self.assertEqual(linked_list.PUT_RIGHT_NIL, linked_list.get_put_right_status())
        self.assertEqual(linked_list.PUT_LEFT_NIL, linked_list.get_put_left_status())
        self.assertEqual(linked_list.REMOVE_NIL, linked_list.get_remove_status())
        self.assertEqual(linked_list.CLEAR_NIL, linked_list.get_clear_status())
        self.assertEqual(linked_list.ADD_TAIL_NIL, linked_list.get_add_tail_status())
        self.assertEqual(linked_list.REPLACE_NIL, linked_list.get_replace_status())
        self.assertEqual(linked_list.FIND_NIL, linked_list.get_find_status())
        self.assertEqual(linked_list.REMOVE_ALL_NIL, linked_list.get_remove_all_status())

    def test_head_with_empty_list(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.HEAD_NIL, linked_list.get_head_status())
        self.assertIsNone(linked_list.head())
        self.assertEqual(linked_list.HEAD_ERR, linked_list.get_head_status())

    def test_head_with_non_empty_list(self):
        linked_list = LinkedList()

        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertIsNone(linked_list.put_left(41))
        self.assertIsNone(linked_list.put_right(43))

        self.assertEqual(42, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

        self.assertEqual(linked_list.HEAD_NIL, linked_list.get_head_status())
        self.assertIsNone(linked_list.head())
        self.assertEqual(linked_list.HEAD_OK, linked_list.get_head_status())
        self.assertEqual(41, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

    def test_tail_with_empty_list(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.TAIL_NIL, linked_list.get_tail_status())
        self.assertIsNone(linked_list.tail())
        self.assertEqual(linked_list.TAIL_ERR, linked_list.get_head_status())

    def test_tail_with_non_empty_list(self):
        linked_list = LinkedList()

        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertIsNone(linked_list.put_left(41))
        self.assertIsNone(linked_list.put_right(43))

        self.assertEqual(42, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

        self.assertEqual(linked_list.TAIL_NIL, linked_list.get_tail_status())
        self.assertIsNone(linked_list.tail())
        self.assertEqual(linked_list.TAIL_OK, linked_list.get_head_status())
        self.assertEqual(43, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

    def test_right_with_empty_list(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.RIGHT_NIL, linked_list.get_right_status())
        self.assertIsNone(linked_list.right())
        self.assertEqual(linked_list.RIGHT_ERR, linked_list.get_right_status())

    def test_right_with_non_empty_list(self):
        linked_list = LinkedList()

        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertIsNone(linked_list.put_left(41))
        self.assertIsNone(linked_list.put_right(43))

        self.assertEqual(42, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

        self.assertIsNone(linked_list.right())
        self.assertEqual(43, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

        self.assertIsNone(linked_list.right())
        self.assertEqual(linked_list.RIGHT_ERR, linked_list.get_right_status())
        self.assertEqual(43, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

    def test_get(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.GET_NIL, linked_list.get_get_status())
        self.assertIsNone(linked_list.get())
        self.assertEqual(linked_list.GET_ERR, linked_list.get_get_status())

        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertEqual(42, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

        self.assertIsNone(linked_list.put_right(43))
        self.assertEqual(42, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())
        self.assertIsNone(linked_list.right())
        self.assertEqual(linked_list.RIGHT_OK, linked_list.get_right_status())
        self.assertEqual(43, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

        self.assertIsNone(linked_list.right())
        self.assertEqual(linked_list.RIGHT_ERR, linked_list.get_right_status())
        self.assertEqual(43, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

    def test_size_with_empty_list(self):
        linked_list = LinkedList()

        self.assertEqual(0, linked_list.size())

    def test_size_with_non_empty_list(self):
        linked_list = LinkedList()

        self.assertEqual(0, linked_list.size())
        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertEqual(1, linked_list.size())

        counter = 1
        for value in range(5):
            self.assertIsNone(linked_list.put_right(value))
            self.assertEqual(counter + 1, linked_list.size())
            counter += 1
        self.assertEqual(6, linked_list.size())

        self.assertIsNone(linked_list.clear())
        self.assertEqual(linked_list.CLEAR_OK, linked_list.get_clear_status())
        self.assertEqual(0, linked_list.size())

    def test_add_to_empty_with_empty_list(self):
        linked_list = LinkedList()

        self.assertEqual(0, linked_list.size())
        self.assertEqual(linked_list.ADD_TO_EMPTY_NIL, linked_list.get_add_to_empty_status())

        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertEqual(linked_list.ADD_TO_EMPTY_OK, linked_list.get_add_to_empty_status())

        self.assertEqual(1, linked_list.size())
        self.assertEqual(42, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

    def test_add_to_empty_with_non_empty_list(self):
        linked_list = LinkedList()

        self.assertEqual(0, linked_list.size())
        self.assertEqual(linked_list.ADD_TO_EMPTY_NIL, linked_list.get_add_to_empty_status())

        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertEqual(linked_list.ADD_TO_EMPTY_OK, linked_list.get_add_to_empty_status())

        self.assertEqual(1, linked_list.size())
        self.assertEqual(42, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

        self.assertIsNone(linked_list.add_to_empty(4242))
        self.assertEqual(linked_list.ADD_TO_EMPTY_ERR, linked_list.get_add_to_empty_status())

    def test_put_right_to_empty_list(self):
        linked_list = LinkedList()

        self.assertEqual(0, linked_list.size())
        self.assertEqual(linked_list.PUT_RIGHT_NIL, linked_list.get_put_right_status())

        self.assertIsNone(linked_list.put_right(42))
        self.assertEqual(linked_list.PUT_RIGHT_ERR, linked_list.get_put_right_status())
        self.assertEqual(0, linked_list.size())

    def test_put_right_to_non_empty_list(self):
        linked_list = LinkedList()

        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertEqual(1, linked_list.size())
        self.assertEqual(42, linked_list.get())

        self.assertEqual(linked_list.PUT_RIGHT_NIL, linked_list.get_put_right_status())
        self.assertIsNone(linked_list.put_right(43))
        self.assertEqual(linked_list.PUT_RIGHT_OK, linked_list.get_put_right_status())
        self.assertEqual(2, linked_list.size())
        self.assertEqual(42, linked_list.get())
        self.assertIsNone(linked_list.right())
        self.assertEqual(43, linked_list.get())

    def test_put_left_to_empty_list(self):
        linked_list = LinkedList()

        self.assertEqual(0, linked_list.size())
        self.assertEqual(linked_list.PUT_LEFT_NIL, linked_list.get_put_left_status())

        self.assertIsNone(linked_list.put_left(42))
        self.assertEqual(linked_list.PUT_LEFT_ERR, linked_list.get_put_left_status())
        self.assertEqual(0, linked_list.size())

    def test_put_left_to_non_empty_list(self):
        linked_list = LinkedList()

        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertEqual(1, linked_list.size())
        self.assertEqual(42, linked_list.get())
        self.assertEqual(linked_list.PUT_LEFT_NIL, linked_list.get_put_left_status())

        self.assertIsNone(linked_list.put_left(43))
        self.assertEqual(linked_list.PUT_LEFT_OK, linked_list.get_put_left_status())
        self.assertEqual(2, linked_list.size())
        self.assertEqual(42, linked_list.get())
        self.assertIsNone(linked_list.head())
        self.assertEqual(linked_list.HEAD_OK, linked_list.get_head_status())
        self.assertEqual(43, linked_list.get())

    def test_remove_from_empty_list(self):
        linked_list = LinkedList()
        self.assertEqual(0, linked_list.size())

        self.assertEqual(linked_list.REMOVE_NIL, linked_list.get_remove_status())
        self.assertIsNone(linked_list.remove())
        self.assertEqual(linked_list.REMOVE_ERR, linked_list.get_remove_status())

    def test_remove_from_list_with_1_node(self):
        linked_list = LinkedList()

        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertEqual(1, linked_list.size())
        self.assertEqual(42, linked_list.get())

        self.assertEqual(linked_list.REMOVE_NIL, linked_list.get_remove_status())
        self.assertIsNone(linked_list.remove())
        self.assertEqual(linked_list.REMOVE_OK, linked_list.get_remove_status())

        self.assertEqual(0, linked_list.size())
        self.assertIsNone(linked_list.get())
        self.assertEqual(linked_list.GET_ERR, linked_list.get_get_status())

    def test_remove_from_list_with_right_node(self):
        linked_list = LinkedList()

        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertIsNone(linked_list.put_right(43))
        self.assertEqual(2, linked_list.size())
        self.assertEqual(42, linked_list.get())

        self.assertEqual(linked_list.REMOVE_NIL, linked_list.get_remove_status())
        self.assertIsNone(linked_list.remove())
        self.assertEqual(linked_list.REMOVE_OK, linked_list.get_remove_status())

        self.assertEqual(1, linked_list.size())
        self.assertEqual(43, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

    def test_remove_from_list_with_left_node(self):
        linked_list = LinkedList()

        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertIsNone(linked_list.put_right(43))
        self.assertEqual(2, linked_list.size())
        self.assertEqual(42, linked_list.get())
        self.assertIsNone(linked_list.right())
        self.assertEqual(43, linked_list.get())

        self.assertEqual(linked_list.REMOVE_NIL, linked_list.get_remove_status())
        self.assertIsNone(linked_list.remove())
        self.assertEqual(linked_list.REMOVE_OK, linked_list.get_remove_status())

        self.assertEqual(1, linked_list.size())
        self.assertEqual(42, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

    def test_remove_from_list_with_left_and_right_node(self):
        linked_list = LinkedList()

        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertIsNone(linked_list.put_left(41))
        self.assertIsNone(linked_list.put_right(43))
        self.assertEqual(3, linked_list.size())
        self.assertEqual(42, linked_list.get())

        self.assertEqual(linked_list.REMOVE_NIL, linked_list.get_remove_status())
        self.assertIsNone(linked_list.remove())
        self.assertEqual(linked_list.REMOVE_OK, linked_list.get_remove_status())

        self.assertEqual(2, linked_list.size())
        self.assertEqual(43, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

    def test_clear_with_empty_list(self):
        linked_list = LinkedList()

        self.assertEqual(0, linked_list.size())
        self.assertEqual(linked_list.CLEAR_NIL, linked_list.get_clear_status())
        self.assertIsNone(linked_list.clear())
        self.assertEqual(linked_list.CLEAR_OK, linked_list.get_clear_status())
        self.assertEqual(0, linked_list.size())
        self.assertIsNone(linked_list.get())

    def test_clear_with_non_empty_list(self):
        linked_list = LinkedList()

        self.assertEqual(0, linked_list.size())
        self.assertIsNone(linked_list.add_to_empty(42))
        for value in range(5):
            self.assertIsNone(linked_list.put_right(value))
        self.assertEqual(6, linked_list.size())

        self.assertEqual(linked_list.CLEAR_NIL, linked_list.get_clear_status())
        self.assertIsNone(linked_list.clear())
        self.assertEqual(linked_list.CLEAR_OK, linked_list.get_clear_status())
        self.assertEqual(0, linked_list.size())
        self.assertIsNone(linked_list.get())

    def test_add_tail_to_empty_list(self):
        linked_list = LinkedList()

        self.assertEqual(0, linked_list.size())
        self.assertIsNone(linked_list.add_tail(42))
        self.assertEqual(linked_list.ADD_TAIL_ERR, linked_list.get_add_tail_status())

    def test_add_tail_to_non_empty_list(self):
        linked_list = LinkedList()

        self.assertEqual(0, linked_list.size())
        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertEqual(linked_list.ADD_TO_EMPTY_OK, linked_list.get_add_to_empty_status())
        self.assertEqual(1, linked_list.size())
        self.assertEqual(42, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

        self.assertIsNone(linked_list.add_tail(43))
        self.assertEqual(linked_list.ADD_TAIL_OK, linked_list.get_add_tail_status())
        self.assertEqual(2, linked_list.size())

        self.assertIsNone(linked_list.add_tail(44))
        self.assertEqual(linked_list.ADD_TAIL_OK, linked_list.get_add_tail_status())
        self.assertEqual(3, linked_list.size())

        self.assertIsNone(linked_list.right())
        self.assertEqual(linked_list.RIGHT_OK, linked_list.get_right_status())
        self.assertEqual(43, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

        self.assertIsNone(linked_list.right())
        self.assertEqual(linked_list.RIGHT_OK, linked_list.get_right_status())
        self.assertEqual(44, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

    def test_replace_with_empty_list(self):
        linked_list = LinkedList()

        self.assertEqual(0, linked_list.size())
        self.assertEqual(linked_list.REPLACE_NIL, linked_list.get_replace_status())
        self.assertIsNone(linked_list.replace(42))
        self.assertEqual(linked_list.REPLACE_ERR, linked_list.get_replace_status())
        self.assertEqual(0, linked_list.size())

    def test_replace_with_non_empty_list(self):
        linked_list = LinkedList()

        self.assertEqual(0, linked_list.size())
        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertEqual(linked_list.ADD_TO_EMPTY_OK, linked_list.get_add_to_empty_status())
        self.assertEqual(1, linked_list.size())
        self.assertEqual(42, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

        self.assertEqual(linked_list.REPLACE_NIL, linked_list.get_replace_status())
        self.assertIsNone(linked_list.replace(43))
        self.assertEqual(linked_list.REPLACE_OK, linked_list.get_replace_status())
        self.assertEqual(43, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())
        self.assertEqual(1, linked_list.size())

    def test_find_without_value_in_list(self):
        linked_list = LinkedList()

        self.assertEqual(0, linked_list.size())
        self.assertEqual(linked_list.FIND_NIL, linked_list.get_find_status())
        self.assertIsNone(linked_list.find(42))
        self.assertEqual(linked_list.FIND_ERR, linked_list.get_find_status())

        self.assertIsNone(linked_list.add_to_empty(40))
        self.assertIsNone(linked_list.add_tail(41))
        self.assertEqual(2, linked_list.size())
        self.assertEqual(40, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

        self.assertIsNone(linked_list.find(42))
        self.assertEqual(linked_list.FIND_ERR, linked_list.get_find_status())
        self.assertEqual(40, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

    def test_find_with_value_in_list(self):
        linked_list = LinkedList()

        self.assertIsNone(linked_list.add_to_empty(40))
        self.assertIsNone(linked_list.add_tail(41))
        self.assertIsNone(linked_list.add_tail(42))
        self.assertIsNone(linked_list.add_tail(43))
        self.assertIsNone(linked_list.add_tail(44))
        self.assertEqual(5, linked_list.size())
        self.assertEqual(40, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

        self.assertEqual(linked_list.FIND_NIL, linked_list.get_find_status())
        self.assertIsNone(linked_list.find(42))
        self.assertEqual(linked_list.FIND_OK, linked_list.get_find_status())
        self.assertEqual(42, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

        self.assertIsNone(linked_list.find(44))
        self.assertEqual(linked_list.FIND_OK, linked_list.get_find_status())
        self.assertEqual(44, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

        self.assertIsNone(linked_list.find(43))
        self.assertEqual(linked_list.FIND_ERR, linked_list.get_find_status())
        self.assertEqual(44, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

    def test_remove_all_with_empty_list(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.REMOVE_ALL_NIL, linked_list.get_remove_all_status())
        self.assertIsNone(linked_list.remove_all(42))
        self.assertEqual(linked_list.REMOVE_ALL_ERR, linked_list.get_remove_all_status())

    def test_remove_all_with_non_empty_list(self):
        linked_list = LinkedList()

        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertIsNone(linked_list.add_tail(43))
        self.assertIsNone(linked_list.add_tail(44))
        self.assertIsNone(linked_list.add_tail(43))
        self.assertIsNone(linked_list.add_tail(44))
        self.assertIsNone(linked_list.add_tail(45))
        self.assertEqual(6, linked_list.size())
        self.assertEqual(42, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())

        self.assertEqual(linked_list.REMOVE_ALL_NIL, linked_list.get_remove_all_status())
        self.assertIsNone(linked_list.remove_all(43))
        self.assertEqual(linked_list.REMOVE_ALL_OK, linked_list.get_remove_all_status())
        self.assertEqual(42, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())
        self.assertEqual(4, linked_list.size())

        self.assertIsNone(linked_list.remove_all(42))
        self.assertEqual(linked_list.REMOVE_ALL_OK, linked_list.get_remove_all_status())
        self.assertEqual(44, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())
        self.assertEqual(3, linked_list.size())

        self.assertIsNone(linked_list.remove_all(44))
        self.assertEqual(linked_list.REMOVE_ALL_OK, linked_list.get_remove_all_status())
        self.assertEqual(45, linked_list.get())
        self.assertEqual(linked_list.GET_OK, linked_list.get_get_status())
        self.assertEqual(1, linked_list.size())

        self.assertIsNone(linked_list.remove_all(45))
        self.assertEqual(linked_list.REMOVE_ALL_OK, linked_list.get_remove_all_status())
        self.assertIsNone(linked_list.get())
        self.assertEqual(linked_list.GET_ERR, linked_list.get_get_status())
        self.assertEqual(0, linked_list.size())

    def test_is_head(self):
        linked_list = LinkedList()

        self.assertFalse(linked_list.is_head())
        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertTrue(linked_list.is_head())
        self.assertIsNone(linked_list.put_right(43))
        self.assertTrue(linked_list.is_head())
        self.assertIsNone(linked_list.put_left(41))
        self.assertFalse(linked_list.is_head())

    def test_is_tail(self):
        linked_list = LinkedList()

        self.assertFalse(linked_list.is_tail())
        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertTrue(linked_list.is_tail())
        self.assertIsNone(linked_list.put_left(41))
        self.assertTrue(linked_list.is_tail())
        self.assertIsNone(linked_list.put_right(43))
        self.assertFalse(linked_list.is_tail())

    def test_is_value(self):
        linked_list = LinkedList()

        self.assertFalse(linked_list.is_value())
        self.assertIsNone(linked_list.add_to_empty(42))
        self.assertTrue(linked_list.is_value())
        self.assertIsNone(linked_list.put_left(41))
        self.assertTrue(linked_list.is_value())
        self.assertIsNone(linked_list.put_right(43))
        self.assertTrue(linked_list.is_value())

        self.assertIsNone(linked_list.clear())
        self.assertFalse(linked_list.is_value())
