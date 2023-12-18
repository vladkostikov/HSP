import ctypes
from unittest import TestCase
from dynarray import DynArray


class TestDynArray(TestCase):
    def test_init(self):
        dynarray = DynArray()
        for element in range(100, 150):
            dynarray.append(element)
        self.assertEqual(50, dynarray.count)
        self.assertEqual(64, dynarray.capacity)

    def test_len(self):
        dynarray = DynArray()
        for element in range(100, 150):
            dynarray.append(element)
        self.assertEqual(50, len(dynarray))
        self.assertEqual(dynarray.count, len(dynarray))

    def test_make_array(self):
        dynarray = DynArray()
        self.assertIsInstance(dynarray.array, ctypes.Array)

    def test_resize(self):
        dynarray = DynArray()
        for element in range(100, 150):
            dynarray.append(element)
        self.assertEqual(64, dynarray.capacity)

        for element in range(1000, 1050):
            dynarray.append(element)
        self.assertEqual(128, dynarray.capacity)

    def test_append(self):
        dynarray = DynArray()
        for element in range(100, 150):
            dynarray.append(element)
        self.assertEqual([el for el in range(100, 150)], list(dynarray.array._objects.values()))

    def test_insert_when_the_buffer_size_is_not_exceeded(self):
        dynarray = DynArray()
        for index in range(25):
            dynarray.insert(index, index)

        dynarray.insert(0, 'first element')
        self.assertEqual('first element', dynarray[0])
        self.assertEqual(0, dynarray[1])

        dynarray.insert(26, 'last element')
        self.assertEqual('last element', dynarray[26])
        self.assertEqual(32, dynarray.capacity)

        dynarray.insert(20, 'element instead 20 index with value 19')
        self.assertEqual('element instead 20 index with value 19', dynarray[20])
        self.assertEqual(19, dynarray[21])
        self.assertEqual(20, dynarray[22])
        self.assertEqual(32, dynarray.capacity)
        self.assertEqual(28, dynarray.count)

    def test_insert_when_the_buffer_size_is_exceeded(self):
        dynarray = DynArray()
        dynarray.insert(0, 'first element')
        self.assertEqual('first element', dynarray[0])

        for element in range(25):
            dynarray.append(element)
        dynarray.insert(len(dynarray), 'last element')
        self.assertEqual('last element', dynarray[len(dynarray) - 1])
        self.assertEqual(32, dynarray.capacity)

        for element in range(27, 35):
            dynarray.insert(len(dynarray) - 1, element)
        self.assertEqual(64, dynarray.capacity)

        for index_element in range(35, 80):
            dynarray.insert(len(dynarray) - 1, index_element)
        self.assertEqual(128, dynarray.capacity)
        self.assertEqual(80, dynarray.count)

    def test_insert_into_invalid_position(self):
        dynarray = DynArray()
        for element in range(25):
            dynarray.append(element)
        with self.assertRaises(IndexError):
            dynarray.insert(30, 'invalid position')

    def test_delete(self):
        dynarray = DynArray()
        for element in range(100, 135):
            dynarray.append(element)
        self.assertEqual(64, dynarray.capacity)
        self.assertEqual(100, dynarray[0])
        dynarray.delete(0)
        self.assertEqual(101, dynarray[0])
        dynarray.delete(33)
        self.assertEqual(133, dynarray[32])
        self.assertEqual(64, dynarray.capacity)
        dynarray.delete(32)
        self.assertEqual(132, dynarray[31])
        self.assertEqual(64, dynarray.capacity)
        dynarray.delete(31)
        self.assertEqual(131, dynarray[30])
        self.assertEqual(42, dynarray.capacity)

        dynarray = DynArray()
        for element in range(18):
            dynarray.append(element)
        self.assertEqual(32, dynarray.capacity)
        dynarray.delete(0)
        dynarray.delete(0)
        self.assertEqual(32, dynarray.capacity)
        dynarray.delete(0)
        self.assertEqual(21, dynarray.capacity)
        dynarray.delete(0)
        dynarray.delete(0)
        dynarray.delete(0)
        dynarray.delete(0)
        self.assertEqual(21, dynarray.capacity)
        dynarray.delete(0)
        self.assertEqual(16, dynarray.capacity)
        dynarray.delete(0)
        dynarray.delete(0)
        dynarray.delete(0)
        dynarray.delete(0)
        dynarray.delete(0)
        dynarray.delete(0)
        dynarray.delete(0)
        dynarray.delete(0)
        dynarray.delete(0)
        dynarray.delete(0)
        self.assertEqual(0, dynarray.count)
        self.assertEqual(16, dynarray.capacity)

    def test_delete_when_the_buffer_size_not_change(self):
        dynarray = DynArray()
        for element in range(100, 135):
            dynarray.append(element)
        self.assertEqual(64, dynarray.capacity)
        dynarray.delete(34)
        dynarray.delete(33)
        dynarray.delete(32)
        self.assertEqual(64, dynarray.capacity)

    def test_delete_when_the_buffer_size_change(self):
        dynarray = DynArray()
        for element in range(100, 135):
            dynarray.append(element)
        self.assertEqual(64, dynarray.capacity)
        dynarray.delete(34)
        dynarray.delete(33)
        dynarray.delete(32)
        self.assertEqual(64, dynarray.capacity)
        dynarray.delete(31)
        self.assertEqual(42, dynarray.capacity)

    def test_delete_in_invalid_position(self):
        dynarray = DynArray()
        for element in range(100, 135):
            dynarray.append(element)
        with self.assertRaises(IndexError):
            dynarray.delete(35)
