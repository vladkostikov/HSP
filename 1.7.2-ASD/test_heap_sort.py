from unittest import TestCase
from heap_sort import HeapSort


class TestHeapSort(TestCase):
    def test_init(self):
        array = []
        heap_sort = HeapSort(array)
        self.assertEqual([None, None, None], heap_sort.HeapObject.HeapArray)

        array = [0]
        heap_sort = HeapSort(array)
        self.assertEqual([0, None, None, None, None, None, None], heap_sort.HeapObject.HeapArray)

        array = [1, 2, 3, 4, 5]
        heap_sort = HeapSort(array)
        self.assertEqual([5, 4, 2, 1, 3, None, None], heap_sort.HeapObject.HeapArray)
        self.assertGreaterEqual(len(heap_sort.HeapObject.HeapArray), 5)

        array = [num for num in range(1000)]
        heap_sort = HeapSort(array)
        self.assertEqual([999, 765, 998], heap_sort.HeapObject.HeapArray[:3])
        self.assertGreaterEqual(len(heap_sort.HeapObject.HeapArray), 1000)

    def test_get_next_max(self):
        array = [1, 2, 3, 4, 5]
        heap_sort = HeapSort(array)
        self.assertEqual(5, heap_sort.GetNextMax())
        self.assertEqual(4, heap_sort.HeapObject.HeapArray[0])

        self.assertEqual(4, heap_sort.GetNextMax())
        self.assertEqual(3, heap_sort.HeapObject.HeapArray[0])

        self.assertEqual(3, heap_sort.GetNextMax())
        self.assertEqual(2, heap_sort.HeapObject.HeapArray[0])

        self.assertEqual(2, heap_sort.GetNextMax())
        self.assertEqual(1, heap_sort.HeapObject.HeapArray[0])

        self.assertEqual(1, heap_sort.GetNextMax())
        self.assertEqual(None, heap_sort.HeapObject.HeapArray[0])

        self.assertEqual(-1, heap_sort.GetNextMax())
        self.assertEqual(None, heap_sort.HeapObject.HeapArray[0])

        array = [num for num in range(1000)]
        heap_sort = HeapSort(array)
        self.assertEqual(999, heap_sort.GetNextMax())
        self.assertEqual(998, heap_sort.GetNextMax())
        self.assertEqual(997, heap_sort.GetNextMax())
