import unittest
from mad_max import MadMax

class MyTestCase(unittest.TestCase):
    def test_mad_max(self):
        self.assertEqual(MadMax(7,[1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 7, 6, 5, 4])
        self.assertEqual(MadMax(0,[1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 7, 6, 5, 4])
        self.assertEqual(MadMax(3,[2, 1, 3]), [1, 3, 2])
        self.assertEqual(MadMax(1,[5]), [5])
        self.assertEqual(MadMax(1,[5]), [5])
if __name__ == '__main__':
    unittest.main()
