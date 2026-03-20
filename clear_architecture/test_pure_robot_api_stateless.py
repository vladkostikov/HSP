import unittest
from unittest import TestCase
from pure_robot_api_stateless import PureRobotAPIStateless, Result, WATER, SOAP, BRUSH

class Test(TestCase):
    def test_full_sequence(self):
        robot = PureRobotAPIStateless("test_robot")
        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 0.0, 'y': 0.0, 'angle': 0}, cleaning_state=WATER), robot.current_state())
        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 100.0, 'y': 0.0, 'angle': 0}, cleaning_state=WATER), robot.move(100))
        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 100.0, 'y': 0.0, 'angle': -90}, cleaning_state=WATER), robot.turn(-90))
        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 100.0, 'y': 0.0, 'angle': -90}, cleaning_state=SOAP), robot.set_cleaning_state("soap"))
        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 100.0, 'y': 0.0, 'angle': -90}, cleaning_state=SOAP), robot.start())
        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 100.0, 'y': -50.0, 'angle': -90}, cleaning_state=SOAP), robot.move(50))
        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 100.0, 'y': -50.0, 'angle': -90}, cleaning_state=SOAP), robot.stop())

    def test_many_robots(self):
        robot1 = PureRobotAPIStateless("test_robot1")
        robot2 = PureRobotAPIStateless("test_robot2")
        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 0.0, 'y': 0.0, 'angle': 0}, cleaning_state=WATER), robot1.current_state())
        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 0.0, 'y': 0.0, 'angle': 0}, cleaning_state=WATER), robot2.current_state())

        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 100.0, 'y': 0.0, 'angle': 0}, cleaning_state=WATER), robot1.move(100))
        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 100.0, 'y': 0.0, 'angle': 90}, cleaning_state=WATER), robot1.turn(90))
        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 100.0, 'y': 0.0, 'angle': 90}, cleaning_state=SOAP), robot1.set_cleaning_state("soap"))

        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 200.0, 'y': 0.0, 'angle': 0}, cleaning_state=WATER), robot2.move(200))
        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 200.0, 'y': 0.0, 'angle': -90}, cleaning_state=WATER), robot2.turn(-90))
        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 200.0, 'y': 0.0, 'angle': -90}, cleaning_state=BRUSH), robot2.set_cleaning_state("brush"))

        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 100.0, 'y': 0.0, 'angle': 90}, cleaning_state=SOAP), robot1.current_state())
        self.assertEqual(Result(ok=True, error=False, message="", position={'x': 200.0, 'y': 0.0, 'angle': -90}, cleaning_state=BRUSH), robot2.current_state())

    def test_invalid_inputs(self):
        robot = PureRobotAPIStateless("test_robot_invalid")
        self.assertEqual(Result(ok=False, error=True, message="Invalid distance value.", position={'x': 0.0, 'y': 0.0, 'angle': 0}, cleaning_state=WATER), robot.move("invalid_distance"))
        self.assertEqual(Result(ok=False, error=True, message="Invalid angle value.", position={'x': 0.0, 'y': 0.0, 'angle': 0}, cleaning_state=WATER), robot.turn("invalid_angle"))
        self.assertEqual(Result(ok=False, error=True, message="Invalid new cleaning state value.", position={'x': 0.0, 'y': 0.0, 'angle': 0}, cleaning_state=WATER), robot.set_cleaning_state("invalid_cleaning_state"))

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(Test)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
