from unittest import TestCase
from sum_of_digits import sum_of_digits


class Test(TestCase):
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(5), 5)
        self.assertEqual(sum_of_digits(52), 7)
        self.assertEqual(sum_of_digits(522), 9)
        self.assertEqual(sum_of_digits(846), 18)
        self.assertEqual(sum_of_digits(9457), 25)
