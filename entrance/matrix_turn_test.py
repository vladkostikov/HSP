from unittest import TestCase
from matrix_turn import MatrixTurn


class Test(TestCase):
    def test_matrix_turn_4_6_1(self):
        matrix_before_changes = ["123456", "234567", "345678", "456789"]
        expected_matrix = ["212345", "343456", "456767", "567898"]
        MatrixTurn(matrix_before_changes, 4, 6, 1)
        self.assertEqual(matrix_before_changes, expected_matrix)

    def test_matrix_turn_4_6_2(self):
        matrix_before_changes = ["123456", "234567", "345678", "456789"]
        expected_matrix = ["321234", "454345", "567656", "678987"]
        MatrixTurn(matrix_before_changes, 4, 6, 2)
        self.assertEqual(matrix_before_changes, expected_matrix)

    def test_matrix_turn_2_3_1(self):
        matrix_before_changes = ["123", "456"]
        expected_matrix = ["412", "563"]
        MatrixTurn(matrix_before_changes, 2, 3, 1)
        self.assertEqual(matrix_before_changes, expected_matrix)

    def test_matrix_turn_2_2_1(self):
        matrix_before_changes = ["12", "34"]
        expected_matrix = ["31", "42"]
        MatrixTurn(matrix_before_changes, 2, 2, 1)
        self.assertEqual(matrix_before_changes, expected_matrix)

    def test_matrix_turn_5_5_1(self):
        matrix_before_changes = ["11111", "22222", "33833", "44444", "55555"]
        expected_matrix = ['21111', '33221', '44822', '54433', '55554']
        MatrixTurn(matrix_before_changes, 5, 5, 1)
        self.assertEqual(matrix_before_changes, expected_matrix)
