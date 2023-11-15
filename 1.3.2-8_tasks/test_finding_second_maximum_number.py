from unittest import TestCase
from find_second_maximum_number import find_second_maximum_number


class Test(TestCase):
    def test_finding_second_maximum_number(self):
        self.assertEqual(find_second_maximum_number([2, 5, 4, 3, 5]), 5)
        self.assertEqual(find_second_maximum_number([2, 3, 5, 4]), 4)
        self.assertEqual(find_second_maximum_number([1, 2]), 1)
        self.assertEqual(find_second_maximum_number([2, 1]), 1)
        self.assertEqual(find_second_maximum_number([1, 2, 3]), 2)
        self.assertEqual(find_second_maximum_number([1, 2, 3, 4]), 3)
        self.assertEqual(find_second_maximum_number([0, 1, 2, 2]), 2)
        self.assertEqual(find_second_maximum_number([0, 1, 2, 2, 3]), 2)
        self.assertEqual(find_second_maximum_number([2, 1, 1, 1]), 1)
        self.assertEqual(find_second_maximum_number([5, 6, 4, 2]), 5)
        self.assertEqual(find_second_maximum_number([6, 5, 4, 2]), 5)
