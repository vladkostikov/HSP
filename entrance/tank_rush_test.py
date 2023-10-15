import unittest
from tank_rush import TankRush


class MyTestCase(unittest.TestCase):
    def test_tank_rush(self):
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 2, "34 98"), True)
        self.assertEqual(TankRush(3, 4, "0000 0220 3030", 2, 1, "2 3"), True)
        self.assertEqual(TankRush(3, 4, "0010 0111 0011", 2, 2, "11 11"), True)
        self.assertEqual(TankRush(6, 6, "011110 001111 001111 222222 003333 333333", 3, 4, "1111 2222 3333"), True)
        self.assertEqual(TankRush(6, 6, "011110 001111 001111 222222 003333 333333", 3, 4, "1111 2222 4444"), False)
        self.assertEqual(TankRush(2, 2, "0000 0001", 1, 1, "1"), True)
        self.assertEqual(TankRush(2, 2, "0000 0012", 1, 2, "12"), True)
        self.assertEqual(TankRush(2, 2, "0001 0002", 1, 2, "12"), False)


if __name__ == '__main__':
    unittest.main()
