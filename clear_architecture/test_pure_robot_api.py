import unittest
from unittest import TestCase
from pure_robot_api import PureRobotAPI, RobotState, WATER, SOAP

class Test(TestCase):
    def setUp(self):
        self.robot = PureRobotAPI("test_robot")

    def test_full_sequence(self):
        self.assertEqual(RobotState(x=0.0, y=0.0, angle=0, state=WATER), self.robot.current_state())
        self.assertEqual(RobotState(x=100.0, y=0.0, angle=0, state=WATER), self.robot.move(100))
        self.assertEqual(RobotState(x=100.0, y=0.0, angle=-90, state=WATER), self.robot.turn(-90))
        self.assertEqual(RobotState(x=100.0, y=0.0, angle=-90, state=SOAP), self.robot.set_cleaning_state("soap"))
        self.assertEqual(RobotState(x=100.0, y=0.0, angle=-90, state=SOAP), self.robot.start())
        self.assertEqual(RobotState(x=100.0, y=-50.0, angle=-90, state=SOAP), self.robot.move(50))
        self.assertEqual(RobotState(x=100.0, y=-50.0, angle=-90, state=SOAP), self.robot.stop())

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(Test)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
