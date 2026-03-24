import unittest
from unittest import TestCase
from robot_functional_dependency_injection import PureRobot
from pure_robot import RobotState, WATER, SOAP

class Test(TestCase):
    def fake_transfer(self, state):
        return state

    def setUp(self):
        self.robot = PureRobot(self.fake_transfer)

    def test_full_sequence(self):
        self.assertEqual(RobotState(x=0.0, y=0.0, angle=0, state=WATER), self.robot.set_cleaning_state("water"))
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
