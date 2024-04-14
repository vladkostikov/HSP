from unittest import TestCase
from sorting import SelectionSortStep, BubbleSortStep


class Test(TestCase):
    def test_selection_sort_step(self):
        array = []
        self.assertEqual(array, SelectionSortStep(array, 0))
        self.assertEqual(array, SelectionSortStep(array, 1))

        array = [4]
        self.assertEqual(array, SelectionSortStep(array, 0))
        self.assertEqual(array, SelectionSortStep(array, 1))

        array = [4, 3]
        self.assertEqual([3, 4], SelectionSortStep(array, 0))
        self.assertEqual(array, SelectionSortStep(array, 1))
        self.assertEqual(array, SelectionSortStep(array, 2))

        array = [4, 3, 1]
        self.assertEqual([1, 3, 4], SelectionSortStep(array, 0))
        self.assertEqual([4, 1, 3], SelectionSortStep(array, 1))
        self.assertEqual(array, SelectionSortStep(array, 2))
        self.assertEqual(array, SelectionSortStep(array, 3))

        array = [4, 3, 1, 2]
        self.assertEqual([1, 3, 4, 2], SelectionSortStep(array, 0))
        self.assertEqual([4, 1, 3, 2], SelectionSortStep(array, 1))
        self.assertEqual(array, SelectionSortStep(array, 2))
        self.assertEqual(array, SelectionSortStep(array, 3))
        self.assertEqual(array, SelectionSortStep(array, 4))

    def test_bubble_sort_step(self):
        array = []
        self.assertTrue(BubbleSortStep(array))

        array = [4]
        self.assertTrue(BubbleSortStep(array))

        array = [1, 4]
        self.assertTrue(BubbleSortStep(array))

        array = [1, 2, 3, 4]
        self.assertTrue(BubbleSortStep(array))

        array = [1, 2, 4, 3]
        self.assertFalse(BubbleSortStep(array))

        array = [4, 3]
        self.assertFalse(BubbleSortStep(array))

        array = [4, 3, 1]
        self.assertFalse(BubbleSortStep(array))

        array = [4, 3, 1, 2]
        self.assertFalse(BubbleSortStep(array))
