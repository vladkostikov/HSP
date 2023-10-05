import unittest
from sum_of_the import SumOfThe


class MyTestCase(unittest.TestCase):
    def test_sum_of_the(self):
        self.assertEqual(SumOfThe(7, [100, -50, 10, -25, 90, -35, 90]), 90)
        self.assertEqual(SumOfThe(5, [5, -25, 10, -35, -45]), -45)
        self.assertEqual(SumOfThe(5, [360, 10, -50, 100, 300]), 360)
        self.assertEqual(SumOfThe(2, [10, 10]), 10)
        self.assertEqual(SumOfThe(3, [100, -150, -250]), -150)


if __name__ == '__main__':
    unittest.main()
