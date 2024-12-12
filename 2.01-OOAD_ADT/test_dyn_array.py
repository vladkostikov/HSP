from unittest import TestCase
from dyn_array import DynArray


class Test(TestCase):
    def test_init(self):
        dyn_array = DynArray()

        self.assertEqual(0, dyn_array.size())
        self.assertEqual(16, dyn_array.capacity())
        self.assertEqual(dyn_array.INSERT_ERR, dyn_array.get_insert_status())
        self.assertEqual(dyn_array.REMOVE_ERR, dyn_array.get_remove_status())
        self.assertEqual(dyn_array.GET_ERR, dyn_array.get_get_status())
        self.assertEqual(dyn_array.INDEX_ERR, dyn_array.get_index_status())

    def test_append(self):
        dyn_array = DynArray()
        self.assertEqual(0, dyn_array.size())
        self.assertEqual(16, dyn_array.capacity())

        for num in range(20):
            self.assertIsNone(dyn_array.append(num))
            self.assertEqual(num + 1, dyn_array.size())
        self.assertEqual(20, dyn_array.size())
        self.assertEqual(32, dyn_array.capacity())

    def test_insert_with_incorrect_index(self):
        dyn_array = DynArray()

        self.assertEqual(0, dyn_array.size())
        self.assertEqual(dyn_array.INSERT_ERR, dyn_array.get_insert_status())
        self.assertIsNone(dyn_array.insert(10, 42))
        self.assertEqual(dyn_array.INSERT_ERR, dyn_array.get_insert_status())
        self.assertEqual(0, dyn_array.size())

    def test_insert_with_correct_index_without_offset(self):
        dyn_array = DynArray()

        self.assertEqual(0, dyn_array.size())
        self.assertEqual(dyn_array.INSERT_ERR, dyn_array.get_insert_status())

        for index in range(20):
            self.assertIsNone(dyn_array.insert(index, index + 100))
            self.assertEqual(dyn_array.INSERT_OK, dyn_array.get_insert_status())
            self.assertEqual(index + 1, dyn_array.size())

        self.assertEqual(20, dyn_array.size())

    def test_insert_with_correct_index_with_offset(self):
        dyn_array = DynArray()

        self.assertEqual(0, dyn_array.size())
        self.assertEqual(16, dyn_array.capacity())
        self.assertEqual(dyn_array.INSERT_ERR, dyn_array.get_insert_status())

        for index in range(16):
            self.assertIsNone(dyn_array.insert(index, index + 100))
            self.assertEqual(dyn_array.INSERT_OK, dyn_array.get_insert_status())
            self.assertEqual(index + 1, dyn_array.size())
            self.assertEqual(16, dyn_array.capacity())

        self.assertEqual(16, dyn_array.size())
        self.assertEqual(16, dyn_array.capacity())

        self.assertIsNone(dyn_array.insert(10, 42))
        self.assertEqual(dyn_array.INSERT_OK, dyn_array.get_insert_status())
        self.assertEqual(17, dyn_array.size())
        self.assertEqual(32, dyn_array.capacity())

    def test_remove_with_incorrect_index(self):
        dyn_array = DynArray()

        self.assertEqual(0, dyn_array.size())
        self.assertEqual(16, dyn_array.capacity())
        self.assertEqual(dyn_array.REMOVE_ERR, dyn_array.get_remove_status())

        self.assertIsNone(dyn_array.remove(-5))
        self.assertEqual(dyn_array.REMOVE_ERR, dyn_array.get_remove_status())
        self.assertIsNone(dyn_array.remove(-1))
        self.assertEqual(dyn_array.REMOVE_ERR, dyn_array.get_remove_status())
        self.assertIsNone(dyn_array.remove(0))
        self.assertEqual(dyn_array.REMOVE_ERR, dyn_array.get_remove_status())
        self.assertIsNone(dyn_array.remove(1))
        self.assertEqual(dyn_array.REMOVE_ERR, dyn_array.get_remove_status())
        self.assertIsNone(dyn_array.remove(5))
        self.assertEqual(dyn_array.REMOVE_ERR, dyn_array.get_remove_status())

        self.assertEqual(0, dyn_array.size())
        self.assertEqual(16, dyn_array.capacity())

        for num in range(5):
            self.assertIsNone(dyn_array.append(num))
        self.assertEqual(5, dyn_array.size())
        self.assertEqual(16, dyn_array.capacity())

        self.assertIsNone(dyn_array.remove(-5))
        self.assertEqual(dyn_array.REMOVE_ERR, dyn_array.get_remove_status())
        self.assertIsNone(dyn_array.remove(-1))
        self.assertEqual(dyn_array.REMOVE_ERR, dyn_array.get_remove_status())
        self.assertIsNone(dyn_array.remove(5))
        self.assertEqual(dyn_array.REMOVE_ERR, dyn_array.get_remove_status())

        self.assertEqual(5, dyn_array.size())
        self.assertEqual(16, dyn_array.capacity())

    def test_remove_with_correct_index(self):
        dyn_array = DynArray()

        self.assertEqual(0, dyn_array.size())
        self.assertEqual(16, dyn_array.capacity())

        for num in range(20):
            self.assertIsNone(dyn_array.append(num))
        self.assertEqual(20, dyn_array.size())
        self.assertEqual(32, dyn_array.capacity())

        self.assertIsNone(dyn_array.remove(19))
        self.assertEqual(dyn_array.REMOVE_OK, dyn_array.get_remove_status())
        self.assertEqual(19, dyn_array.size())
        self.assertIsNone(dyn_array.remove(10))
        self.assertEqual(dyn_array.REMOVE_OK, dyn_array.get_remove_status())
        self.assertEqual(18, dyn_array.size())
        self.assertIsNone(dyn_array.remove(0))
        self.assertEqual(dyn_array.REMOVE_OK, dyn_array.get_remove_status())
        self.assertEqual(17, dyn_array.size())

    def test_remove_with_decrease(self):
        dyn_array = DynArray()

        self.assertEqual(0, dyn_array.size())
        self.assertEqual(16, dyn_array.capacity())

        for num in range(20):
            self.assertIsNone(dyn_array.append(num))
        self.assertEqual(20, dyn_array.size())
        self.assertEqual(32, dyn_array.capacity())

        for num in range(4):
            self.assertIsNone(dyn_array.remove(num))
        self.assertEqual(16, dyn_array.size())
        self.assertEqual(32, dyn_array.capacity())

        self.assertIsNone(dyn_array.remove(0))
        self.assertEqual(15, dyn_array.size())
        self.assertEqual(21, dyn_array.capacity())

        for num in range(4):
            self.assertIsNone(dyn_array.remove(num))
        self.assertEqual(11, dyn_array.size())
        self.assertEqual(21, dyn_array.capacity())

        self.assertIsNone(dyn_array.remove(0))
        self.assertEqual(10, dyn_array.size())
        self.assertEqual(16, dyn_array.capacity())

    def test_clear(self):
        dyn_array = DynArray()

        self.assertEqual(0, dyn_array.size())
        self.assertEqual(16, dyn_array.capacity())

        for num in range(20):
            self.assertIsNone(dyn_array.append(num))
        self.assertEqual(20, dyn_array.size())
        self.assertEqual(32, dyn_array.capacity())

        self.assertIsNone(dyn_array.clear(100))
        self.assertEqual(0, dyn_array.size())
        self.assertEqual(100, dyn_array.capacity())

        self.assertIsNone(dyn_array.clear())
        self.assertEqual(0, dyn_array.size())
        self.assertEqual(16, dyn_array.capacity())

    def test_get(self):
        dyn_array = DynArray()
        self.assertEqual(dyn_array.GET_ERR, dyn_array.get_get_status())

        for num in range(20):
            self.assertIsNone(dyn_array.append(num + 100))
        self.assertEqual(20, dyn_array.size())
        self.assertEqual(32, dyn_array.capacity())

        for index in range(20):
            self.assertEqual(index + 100, dyn_array.get(index))
            self.assertEqual(dyn_array.GET_OK, dyn_array.get_get_status())

        self.assertIsNone(dyn_array.get(-1))
        self.assertEqual(dyn_array.GET_ERR, dyn_array.get_get_status())
        self.assertIsNone(dyn_array.get(20))
        self.assertEqual(dyn_array.GET_ERR, dyn_array.get_get_status())
        self.assertEqual(119, dyn_array.get(19))
        self.assertEqual(dyn_array.GET_OK, dyn_array.get_get_status())

    def test_index(self):
        dyn_array = DynArray()
        self.assertEqual(dyn_array.INDEX_ERR, dyn_array.get_index_status())

        for num in range(20):
            self.assertIsNone(dyn_array.append(num + 100))

        self.assertEqual(0, dyn_array.index(-1))
        self.assertEqual(dyn_array.INDEX_ERR, dyn_array.get_index_status())
        self.assertEqual(0, dyn_array.index(0))
        self.assertEqual(dyn_array.INDEX_ERR, dyn_array.get_index_status())
        self.assertEqual(0, dyn_array.index(1))
        self.assertEqual(dyn_array.INDEX_ERR, dyn_array.get_index_status())

        for num in range(20):
            self.assertEqual(num, dyn_array.index(num + 100))
            self.assertEqual(dyn_array.INDEX_OK, dyn_array.get_index_status())

        self.assertEqual(10, dyn_array.index(110))
        self.assertEqual(dyn_array.INDEX_OK, dyn_array.get_index_status())

        self.assertIsNone(dyn_array.insert(5, 110))
        self.assertEqual(dyn_array.INSERT_OK, dyn_array.get_insert_status())
        self.assertEqual(5, dyn_array.index(110))
        self.assertEqual(dyn_array.INDEX_OK, dyn_array.get_index_status())
