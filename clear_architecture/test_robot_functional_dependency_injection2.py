import unittest
from unittest import TestCase
from robot_functional_dependency_injection2 import api, fake_transfer, robot_handler, double_move_robot_handler
from pure_robot import RobotState, WATER, SOAP

class Test(TestCase):
    def setUp(self):
        api.cleaner_state = RobotState(0.0, 0.0, 0, WATER)

    def test_full_sequence(self):
        api.setup(robot_handler, fake_transfer)
        self.assertEqual(RobotState(x=0.0, y=0.0, angle=0, state=WATER), api.cleaner_state)
        self.assertEqual(RobotState(x=100.0, y=0.0, angle=0, state=WATER), api("move 100"))
        self.assertEqual(RobotState(x=100.0, y=0.0, angle=-90, state=WATER), api("turn -90"))
        self.assertEqual(RobotState(x=100.0, y=0.0, angle=-90, state=SOAP), api("set soap"))
        self.assertEqual(RobotState(x=100.0, y=0.0, angle=-90, state=SOAP), api("start"))
        self.assertEqual(RobotState(x=100.0, y=-50.0, angle=-90, state=SOAP), api("move 50"))
        self.assertEqual(RobotState(x=100.0, y=-50.0, angle=-90, state=SOAP), api("stop"))

    def test_double_move(self):
        api.setup(double_move_robot_handler, fake_transfer)
        self.assertEqual(RobotState(x=0.0, y=0.0, angle=0, state=WATER), api.cleaner_state)
        self.assertEqual(RobotState(x=200.0, y=0.0, angle=0, state=WATER), api("move 100"))

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(Test)
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
