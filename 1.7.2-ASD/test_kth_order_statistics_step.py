from unittest import TestCase
from kth_order_statistics_step import KthOrderStatisticsStep, KthOrderStatistics
from random import shuffle


class Test(TestCase):
    def test_kth_order_statistics_step(self):
        self.assertEqual([0, 0], KthOrderStatisticsStep([3, 5, 2, 4, 1], 0, 4, 0))
        self.assertEqual([1, 1], KthOrderStatisticsStep([3, 5, 2, 4, 1], 0, 4, 1))
        self.assertEqual([2, 4], KthOrderStatisticsStep([3, 5, 2, 4, 1], 0, 4, 2))
        self.assertEqual([2, 4], KthOrderStatisticsStep([3, 5, 2, 4, 1], 0, 4, 3))
        self.assertEqual([2, 4], KthOrderStatisticsStep([3, 5, 2, 4, 1], 0, 4, 4))
        self.assertEqual([1, 4], KthOrderStatisticsStep([3, 5, 0, 4, 1], 0, 4, 4))
        self.assertEqual([4, 4], KthOrderStatisticsStep([3, 5, 6, 4, 1], 0, 4, 4))

    def test_kth_order_statistics(self):
        self.assertEqual(1, KthOrderStatistics([3, 5, 2, 4, 1], 0, 4, 0))
        self.assertEqual(2, KthOrderStatistics([3, 5, 2, 4, 1], 0, 4, 1))
        self.assertEqual(3, KthOrderStatistics([3, 5, 2, 4, 1], 0, 4, 2))
        self.assertEqual(4, KthOrderStatistics([3, 5, 2, 4, 1], 0, 4, 3))
        self.assertEqual(5, KthOrderStatistics([3, 5, 2, 4, 1], 0, 4, 4))

        self.assertEqual(5, KthOrderStatistics([3, 5, 0, 4, 1], 0, 4, 4))
        self.assertEqual(6, KthOrderStatistics([3, 5, 6, 4, 1], 0, 4, 4))

        array = [num for num in range(100)]
        shuffle(array)
        self.assertEqual(90, KthOrderStatistics(array, 0, len(array) - 1, 90))

        array = [num for num in range(1_000)]
        shuffle(array)
        self.assertEqual(900, KthOrderStatistics(array, 0, len(array) - 1, 900))

        array = [num for num in range(10_000)]
        shuffle(array)
        self.assertEqual(9000, KthOrderStatistics(array, 0, len(array) - 1, 9000))

        array = [num for num in range(100_000)]
        shuffle(array)
        self.assertEqual(90000, KthOrderStatistics(array, 0, len(array) - 1, 90000))

        array = [num for num in range(1_000_000)]
        shuffle(array)
        self.assertEqual(900000, KthOrderStatistics(array, 0, len(array) - 1, 900000))
