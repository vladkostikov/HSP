from unittest import TestCase
from find_second_maximum_number_imperative import find_second_maximum_number_imperative


class Test(TestCase):
    def test_find_second_maximum_number_imperative(self):
        self.assertEqual(find_second_maximum_number_imperative([2, 5, 4, 3, 5]), 5)
        self.assertEqual(find_second_maximum_number_imperative([2, 3, 5, 4]), 4)
        self.assertEqual(find_second_maximum_number_imperative([1, 2]), 1)
        self.assertEqual(find_second_maximum_number_imperative([2, 1]), 1)
        self.assertEqual(find_second_maximum_number_imperative([1, 2, 3]), 2)
        self.assertEqual(find_second_maximum_number_imperative([1, 2, 3, 4]), 3)
        self.assertEqual(find_second_maximum_number_imperative([0, 1, 2, 2]), 2)
        self.assertEqual(find_second_maximum_number_imperative([0, 1, 2, 2, 3]), 2)
        self.assertEqual(find_second_maximum_number_imperative([2, 1, 1, 1]), 1)
        self.assertEqual(find_second_maximum_number_imperative([5, 6, 4, 2]), 5)
        self.assertEqual(find_second_maximum_number_imperative([6, 5, 4, 2]), 5)

