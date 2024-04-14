from unittest import TestCase
from insertion_sort import InsertionSort, InsertionSortStep


class Test(TestCase):
    def test_insertion_sort(self):
        array = [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual([1, 3, 2, 4, 6, 5, 7], InsertionSort(array, 3))

        array = [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], InsertionSort(array, 1))

    def test_insertion_sort_step(self):
        array = [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual([1, 6, 5, 4, 3, 2, 7], InsertionSortStep(array, 3, 0))

        array = [1, 6, 5, 4, 3, 2, 7]
        self.assertEqual([1, 3, 5, 4, 6, 2, 7], InsertionSortStep(array, 3, 1))
