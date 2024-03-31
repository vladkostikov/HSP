from unittest import TestCase
from heap import Heap

class TestHeap(TestCase):
    def test_make_heap(self):
        heap = Heap()
        self.assertEqual([], heap.HeapArray)

        heap.MakeHeap([10, 20, 30], 1)
        self.assertEqual([30, 10, 20], heap.HeapArray)

        heap.MakeHeap([10, 20, 30, 25], 2)
        self.assertEqual([30, 25, 20, 10, None, None, None], heap.HeapArray)

        heap.MakeHeap([10, 20, 30, 25, 35], 2)
        self.assertEqual([35, 30, 20, 10, 25, None, None], heap.HeapArray)

    def test_get_max(self):
        heap = Heap()

        self.assertEqual([], heap.HeapArray)
        self.assertEqual(-1, heap.GetMax())

        heap.MakeHeap([10, 20, 30, 25, 35, 40, 45], 2)
        self.assertEqual(45, heap.GetMax())

        heap.MakeHeap([10, 20, 30, 25, 35], 2)
        self.assertEqual([35, 30, 20, 10, 25, None, None], heap.HeapArray)

        self.assertEqual(35, heap.GetMax())
        self.assertEqual([30, 25, 20, 10, None, None, None], heap.HeapArray)

        self.assertEqual(30, heap.GetMax())
        self.assertEqual([25, 10, 20, None, None, None, None], heap.HeapArray)

        self.assertEqual(25, heap.GetMax())
        self.assertEqual([20, 10, None, None, None, None, None], heap.HeapArray)

        self.assertEqual(20, heap.GetMax())
        self.assertEqual([10, None, None, None, None, None, None], heap.HeapArray)

        self.assertEqual(10, heap.GetMax())
        self.assertEqual([None, None, None, None, None, None, None], heap.HeapArray)

        self.assertEqual(-1, heap.GetMax())
        self.assertEqual([None, None, None, None, None, None, None], heap.HeapArray)


    def test_add(self):
        heap = Heap()
        self.assertEqual([], heap.HeapArray)

        heap.MakeHeap([10, 20, 30, 25, 35], 2)
        self.assertEqual([35, 30, 20, 10, 25, None, None], heap.HeapArray)

        self.assertTrue(heap.Add(18))
        self.assertEqual([35, 30, 20, 10, 25, 18, None], heap.HeapArray)

        self.assertTrue(heap.Add(22))
        self.assertEqual([35, 30, 22, 10, 25, 18, 20], heap.HeapArray)
