import unittest
from unmanned import Unmanned


class MyTestCase(unittest.TestCase):
    def test_unmanned(self):
        self.assertEqual(Unmanned(0, 0, []), 0)
        self.assertEqual(Unmanned(5, 1, [[2, 15, 5]]), 18)
        self.assertEqual(Unmanned(10, 0, []), 10)
        self.assertEqual(Unmanned(10, 2, [[3, 5, 5], [5, 2, 2]]), 12)
        self.assertEqual(Unmanned(10, 3, [[3, 5, 5], [5, 2, 2], [8, 8, 2]]), 20)
        self.assertEqual(Unmanned(10, 3, [[1, 10, 2], [5, 10, 2], [9, 10, 2]]), 35)
        self.assertEqual(Unmanned(15, 4, [[2, 1, 1], [4, 1, 1], [6, 1, 1], [8, 1, 1]]), 16)
        self.assertEqual(Unmanned(20, 4, [[0, 10, 1], [4, 0, 1], [6, 0, 1], [8, 0, 1]]), 30)


if __name__ == '__main__':
    unittest.main()
