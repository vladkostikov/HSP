from unittest import TestCase
from exponentiation import exponentiation


class Test(TestCase):
    def test_exponentiation(self):
        self.assertEqual(exponentiation(2, 0), 1)
        self.assertEqual(exponentiation(2, 1), 2)
        self.assertEqual(exponentiation(2, 2), 4)
        self.assertEqual(exponentiation(2, 3), 8)
        self.assertEqual(exponentiation(2, 4), 16)
        self.assertEqual(exponentiation(2, 5), 32)
        self.assertEqual(exponentiation(3, 2), 9)
        self.assertEqual(exponentiation(3, 3), 27)
        self.assertEqual(exponentiation(3, 3), 27)
        self.assertEqual(exponentiation(4, 2), 16)
        self.assertEqual(exponentiation(4, 3), 64)

    def test_exponentiation_of_a_negative_number(self):
        self.assertEqual(exponentiation(-2, 0), 1)
        self.assertEqual(exponentiation(-2, 1), -2)
        self.assertEqual(exponentiation(-2, 2), 4)
        self.assertEqual(exponentiation(-2, 3), -8)
        self.assertEqual(exponentiation(-2, 4), 16)
