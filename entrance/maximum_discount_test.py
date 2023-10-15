import unittest
from maximum_discount import MaximumDiscount


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(MaximumDiscount(3, [400, 300, 250]), 250)
        self.assertEqual(MaximumDiscount(7, [400, 350, 300, 250, 200, 150, 100]), sum([300, 150]))
        self.assertEqual(MaximumDiscount(1, [100]), 0)
        self.assertEqual(MaximumDiscount(2, [100, 200]), 0)
        self.assertEqual(MaximumDiscount(3, [25, 100, 200]), 25)


if __name__ == '__main__':
    unittest.main()
