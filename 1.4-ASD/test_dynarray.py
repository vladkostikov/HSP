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

    def test_insert(self):
        dynarray = DynArray()
        dynarray.insert(0, 'first element')
        self.assertEqual('first element', dynarray[0])
        for element in range(25):
            dynarray.append(element)
        dynarray.insert(25, 'last but one element')
        self.assertEqual('last but one element', dynarray[25])
        dynarray.insert(26, 'second element')
        self.assertEqual('second element', dynarray[26])
        dynarray.insert(dynarray.count, 'third element')
        self.assertEqual('third element', dynarray[dynarray.count - 1])

    def test_insert_when_the_buffer_size_is_not_exceeded(self):
        dynarray = DynArray()
        dynarray.insert(0, 'first element')
        self.assertEqual('first element', dynarray[0])
        for element in range(25):
            dynarray.append(element)
        dynarray.insert(26, 'last element')
        self.assertEqual('last element', dynarray[26])
        self.assertEqual(32, dynarray.capacity)
        for element in range(5):
            dynarray.append(element)
        self.assertEqual(32, dynarray.capacity)
        self.assertEqual(32, dynarray.count)

    def test_insert_when_the_buffer_size_is_exceeded(self):
        dynarray = DynArray()
        dynarray.insert(0, 'first element')
        self.assertEqual('first element', dynarray[0])
        for element in range(25):
            dynarray.append(element)
        dynarray.insert(26, 'last element')
        self.assertEqual('last element', dynarray[26])
        self.assertEqual(32, dynarray.capacity)
        for element in range(25):
            dynarray.append(element)
        self.assertEqual(64, dynarray.capacity)
        for element in range(25):
            dynarray.append(element)
        self.assertEqual(128, dynarray.capacity)

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
