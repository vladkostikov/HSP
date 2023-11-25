from unittest import TestCase
from massdriver import massdriver


class Test(TestCase):
    def test_massdriver(self):
        self.assertEqual(0, massdriver([1, 2, 3, 1, 2, 3, 4]))
        self.assertEqual(1, massdriver([1, 2, 3, 4, 3, 4, 2]))
        self.assertEqual(-1, massdriver([1, 2, 3, 4, 5, 6, 7]))
        self.assertEqual(0, massdriver([1, 2, 3, 4, 5, 2, 1]))
        self.assertEqual(1, massdriver([5, 4, 2, 2, 4]))
