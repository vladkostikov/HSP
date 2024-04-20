from unittest import TestCase
from quick_sort import QuickSort


class Test(TestCase):
    def test_quick_sort(self):
        array = []
        QuickSort(array, 0, len(array) - 1)
        self.assertEqual([], array)

        array = [0]
        QuickSort(array, 0, len(array) - 1)
        self.assertEqual([0], array)

        array = [1, 0]
        QuickSort(array, 0, len(array) - 1)
        self.assertEqual([0, 1], array)

        array = [1, 0, 2]
        QuickSort(array, 0, len(array) - 1)
        self.assertEqual([0, 1, 2], array)

        array = [1, 3, 0, 2]
        QuickSort(array, 0, len(array) - 1)
        self.assertEqual([0, 1, 2, 3], array)

        array = list(reversed([num for num in range(10)])) + [num for num in range(10, 20)]
        QuickSort(array, 0, len(array) - 1)
        self.assertEqual(list(sorted(array)), array)
