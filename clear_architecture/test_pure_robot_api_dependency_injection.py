import unittest
from unittest import TestCase
from pure_robot_api_dependency_injection import PureRobotAPIDependencyInjection, PureRobotController, FakeOutputHandler, RobotState
from pure_robot import WATER, SOAP

class Test(TestCase):
    def setUp(self):
        self.robot = PureRobotAPIDependencyInjection(
            controller=PureRobotController(output_handler=FakeOutputHandler()),
            output_handler=FakeOutputHandler(),
            initial_state=RobotState(x=0.0, y=0.0, angle=0, state=WATER)
        )

    def test_full_sequence(self):
        self.robot.activate_cleaner(["move 100"])
        self.assertEqual(100.0, self.robot.get_x())
        self.robot.activate_cleaner(["turn -90"])
        self.assertEqual(-90, self.robot.get_angle())
        self.robot.activate_cleaner(["set soap"])
        self.assertEqual(SOAP, self.robot.get_cleaning_state())
        self.robot.activate_cleaner(["start"])
        self.assertEqual(SOAP, self.robot.get_cleaning_state())
        self.robot.activate_cleaner(["move 50"])
        self.assertEqual(-50.0, self.robot.get_y())
        self.robot.activate_cleaner(["stop"])
        self.assertEqual(SOAP, self.robot.get_cleaning_state())

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(Test)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
