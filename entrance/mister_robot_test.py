from unittest import TestCase
from mister_robot import MisterRobot


class Test(TestCase):
    def test_mister_robot(self):
        self.assertEqual(MisterRobot(7, [1, 3, 4, 5, 6, 2, 7]), True)
        self.assertEqual(MisterRobot(9, [1, 9, 7, 3, 5, 4, 8, 6, 2]), False)
        self.assertEqual(MisterRobot(5, [3, 5, 2, 1, 4]), True)
        self.assertEqual(MisterRobot(5, [1, 4, 3, 5, 2]), True)
        self.assertEqual(MisterRobot(8, [8, 7, 6, 1, 4, 3, 5, 2]), True)
        self.assertEqual(MisterRobot(4, [4, 2, 1, 3]), True)
        self.assertEqual(MisterRobot(3, [3, 1, 2]), True)
        self.assertEqual(MisterRobot(3, [1, 3, 2]), False)
