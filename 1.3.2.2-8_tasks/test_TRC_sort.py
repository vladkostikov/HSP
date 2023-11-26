from unittest import TestCase
from TRC_sort import TRC_sort


class Test(TestCase):
    def test_trc_sort(self):
        self.assertEqual([0, 1, 2], TRC_sort([2, 1, 0]))
        self.assertEqual([0, 1, 2], TRC_sort([2, 1, 0]))
        self.assertEqual([0, 0, 1, 1, 2, 2], TRC_sort([0, 1, 2, 1, 0, 2]))
