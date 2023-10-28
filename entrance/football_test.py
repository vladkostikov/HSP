from unittest import TestCase
from football import Football


class Test(TestCase):
    def test_football(self):
        self.assertEqual(Football([1, 3, 2], 3), True)
        self.assertEqual(Football([3, 2, 1], 3), True)
        self.assertEqual(Football([1, 7, 5, 3, 9], 5), True)
        self.assertEqual(Football([9, 5, 3, 7, 1], 5), False)
        self.assertEqual(Football([1, 4, 3, 2, 5], 5), True)
        self.assertEqual(Football([1, 5, 4, 3, 2, 6], 6), True)
        self.assertEqual(Football([1, 6, 4, 3, 2, 5], 6), False)
        self.assertEqual(Football([2, 4, 3, 1], 4), False)
