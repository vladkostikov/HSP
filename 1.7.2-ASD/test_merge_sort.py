from unittest import TestCase
from merge_sort import MergeSort
from random import shuffle


class Test(TestCase):
    def test_merge_sort(self):
        self.assertEqual([1], MergeSort([1]))

        self.assertEqual([1, 2], MergeSort([1, 2]))
        self.assertEqual([1, 2], MergeSort([2, 1]))

        self.assertEqual([1, 2, 3], MergeSort([1, 2, 3]))
        self.assertEqual([1, 2, 3], MergeSort([1, 3, 2]))
        self.assertEqual([1, 2, 3], MergeSort([2, 1, 3]))
        self.assertEqual([1, 2, 3], MergeSort([2, 3, 1]))
        self.assertEqual([1, 2, 3], MergeSort([3, 1, 2]))
        self.assertEqual([1, 2, 3], MergeSort([3, 2, 1]))

        self.assertEqual([1, 2, 3, 4], MergeSort([3, 2, 4, 1]))
        self.assertEqual([1, 2, 3, 4], MergeSort([4, 2, 3, 1]))

        self.assertEqual([1, 2, 3, 4, 5], MergeSort([4, 2, 3, 1, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 5], MergeSort([4, 2, 5, 3, 1, 5]))

        array = [num for num in range(1_000)]
        self.assertEqual(sorted(array), MergeSort(array))

        array = [num for num in range(10_000)]
        self.assertEqual(sorted(array), MergeSort(array))

        array = [num for num in range(100_000)]
        self.assertEqual(sorted(array), MergeSort(array))

        array = [num for num in range(1_000_000)]
        self.assertEqual(sorted(array), MergeSort(array))
