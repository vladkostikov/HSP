import unittest
from squirrel import squirrel

class MyTestCase(unittest.TestCase):
    def test_squirrel(self):
        self.assertEqual(squirrel(-100), 0)
        self.assertEqual(squirrel(0), 0)
        self.assertEqual(squirrel(1), 1)
        self.assertEqual(squirrel(2), 2)
        self.assertEqual(squirrel(3), 6)
        self.assertEqual(squirrel(4), 2)
        self.assertEqual(squirrel(5), 1)
        self.assertEqual(squirrel(10), 3)

if __name__ == '__main__':
    unittest.main()
