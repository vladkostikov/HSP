from unittest import TestCase
from quick_sort_tail_optimization import QuickSortTailOptimization
import random


class Test(TestCase):
    def test_quick_sort_tail_optimization(self):
        array = []
        QuickSortTailOptimization(array, 0, 0)
        self.assertEqual([], array)

        array = [0]
        QuickSortTailOptimization(array, 0, len(array) - 1)
        self.assertEqual([0], array)

        array = [1, 0]
        QuickSortTailOptimization(array, 0, len(array) - 1)
        self.assertEqual([0, 1], array)

        array = [1, 0, 2]
        QuickSortTailOptimization(array, 0, len(array) - 1)
        self.assertEqual([0, 1, 2], array)

        array = [1, 3, 0, 2]
        QuickSortTailOptimization(array, 0, len(array) - 1)
        self.assertEqual([0, 1, 2, 3], array)

        array = list(reversed([num for num in range(10)])) + [num for num in range(10, 20)]
        QuickSortTailOptimization(array, 0, len(array) - 1)
        self.assertEqual(list(sorted(array)), array)

        array = [num for num in range(1_000_000)]
        random.shuffle(array)
        QuickSortTailOptimization(array, 0, len(array) - 1)
        self.assertEqual(list(sorted(array)), array)
