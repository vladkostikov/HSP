import unittest
from unittest import TestCase
from robot_concatenative_style import RobotAPI
from pure_robot import RobotState, WATER, SOAP

class Test(TestCase):
    def fake_transfer(self, state):
        return state

    def setUp(self):
        self.robot_api = RobotAPI(self.fake_transfer, RobotState(x=0.0, y=0.0, angle=0, state=WATER))

    def test_full_sequence_concatenative_style(self):
        self.assertEqual(RobotState(x=100.0, y=-50.0, angle=-90, state=SOAP), self.robot_api("100 move -90 turn soap set start 50 move stop"))

    def test_parser(self):
        self.assertEqual([('move', ['100', '50']), ('turn', ['-90', '50']), ('set', ['soap']), ('start', []), ('move', ['50']), ('stop', [])],
                        self.robot_api._parse_commands("50 100 move 50 -90 turn soap set start 50 move stop"))


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(Test)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
