from unittest import TestCase
from max_submatrix import max_submatrix


class Test(TestCase):
    def test_max_submatrix(self):
        self.assertEqual("1 1 2", max_submatrix(3, [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]))
        self.assertEqual("1 0 3", max_submatrix(4, [
            [1, 9, 2, 3],
            [4, 8, 5, 6],
            [0, 7, 1, 2],
            [0, 0, 0, 0]
        ]))
        self.assertEqual("1 1 3", max_submatrix(5, [
            [-5, -6, 3, 1, 0],
            [9, 7, 8, 3, 7],
            [-6, -2, -1, 2, -4],
            [-7, 5, 5, 2, -6],
            [3, 2, -9, -5, 1],
        ]))
        self.assertEqual("2 0 3", max_submatrix(5, [
            [-5, -6, 3, 1, 0],
            [9, -7, 8, 3, 7],
            [-6, -2, -1, 2, -4],
            [-7, 5, 5, 2, -6],
            [3, 2, -9, -5, 1],
        ]))
        self.assertEqual("0 1 4", max_submatrix(5, [
            [-5, -6, 3, 1, 0],
            [9, 7, 8, 3, 7],
            [-6, -2, -1, 2, -4],
            [-7, 5, 5, 2, -6],
            [3, 2, 9, -5, 1],
        ]))
        self.assertEqual("1 1 4", max_submatrix(6, [
            [-5, -6, 3, 1, 0, -10],
            [-9, 7, 8, 3, 7, -10],
            [-6, -2, -1, 2, -4, -10],
            [-7, 5, 5, 2, -6, -2],
            [-3, 2, 9, -5, 1, 0],
            [-10, -5, 0, -5, 1, 0],
        ]))
        self.assertEqual("1 1 5", max_submatrix(6, [
            [-5, -6, 3, 1, 0, -10],
            [-9, 7, 8, 3, 7, 10],
            [-6, -2, -1, 2, -4, 10],
            [-7, 5, 5, 2, -6, 2],
            [-3, 2, 9, -5, 1, 0],
            [-10, 5, 0, -5, 1, 0],
        ]))
