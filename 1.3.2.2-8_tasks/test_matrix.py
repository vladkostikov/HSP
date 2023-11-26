from unittest import TestCase
from matrix import matrix


class Test(TestCase):
    def test_matrix(self):
        self.assertEqual([1], matrix(1, 1, [[1]]))
        self.assertEqual([1, 2, 4, 3], matrix(2, 2, [[1, 2], [3, 4]]))
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        self.assertEqual([1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],
                         matrix(4, 4, [
                             [1, 2, 3, 4],
                             [5, 6, 7, 8],
                             [9, 10, 11, 12],
                             [13, 14, 15, 16]]))
        self.assertEqual([1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13],
                         matrix(5, 5, [
                             [1, 2, 3, 4, 5],
                             [6, 7, 8, 9, 10],
                             [11, 12, 13, 14, 15],
                             [16, 17, 18, 19, 20],
                             [21, 22, 23, 24, 25]]))
