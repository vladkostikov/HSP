from unittest import TestCase
from list_length_with_pop import list_length_with_pop


class Test(TestCase):
    def test_list_length_with_pop(self):
        self.assertEqual(list_length_with_pop([]), 0)
        self.assertEqual(list_length_with_pop([1]), 1)
        self.assertEqual(list_length_with_pop([1, 2]), 2)
        self.assertEqual(list_length_with_pop([1, 2, 3]), 3)
        self.assertEqual(list_length_with_pop([1, 2, 3, 4]), 4)
        self.assertEqual(list_length_with_pop([1, 2, 3, 4, 5]), 5)
