from unittest import TestCase, TestLoader, TextTestRunner
from cleaning_robot import CleaningRobot
import unittest

class Test(TestCase):
    def setUp(self):
        self.robot = CleaningRobot()
    
    def test_call_error_for_invalid_command(self):
        self.assertEqual("Error", self.robot.call("abcd"))

    def test_move_command(self):
        self.assertEqual("POS 0,0", self.robot.call("move -0"))
        self.assertEqual("POS 0,0", self.robot.call("move 0"))
        self.assertEqual("POS 0,100", self.robot.call("move 100"))
        self.assertEqual("POS 0,-100", self.robot.call("move -200"))

    def test_turn_command(self):
        self.assertEqual("AngleError", self.robot.call("turn 45"))
        self.assertEqual("ANGLE 90", self.robot.call("turn 90"))
        self.assertEqual("ANGLE 270", self.robot.call("turn 180"))
        self.assertEqual("ANGLE 180", self.robot.call("turn -450"))

    def test_set_command(self):
        self.assertEqual("STATE water", self.robot.call("set water"))
        self.assertEqual("STATE soap", self.robot.call("set soap"))
        self.assertEqual("STATE brush", self.robot.call("set brush"))
        self.assertEqual("Error", self.robot.call("set invalid"))
        self.assertEqual("Error", self.robot.call("set brush soap"))
        self.assertEqual("Error", self.robot.call("set"))


    def test_start_stop_commands(self):
        self.robot.call("set soap")
        self.assertEqual("START WITH soap", self.robot.call("start"))
        self.assertEqual("STOP", self.robot.call("stop"))

    def test_move_after_turn(self):
        self.robot.call("turn 90")
        self.assertEqual("POS 10,0", self.robot.call("move 10"))
        self.robot.call("turn 90")
        self.assertEqual("POS 10,-20", self.robot.call("move 20"))

    def test_full_sequence(self):
        commands = [
            'move 100',
            'turn -90',
            'set soap',
            'start',
            'move 50',
            'stop'
        ]
        expected = [
            "POS 0,100",
            "ANGLE 270",
            "STATE soap",
            "START WITH soap",
            "POS -50,100",
            "STOP"
        ]
        for cmd, exp in zip(commands, expected):
            with self.subTest(command=cmd):
                self.assertEqual(exp, self.robot.call(cmd))

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(Test)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
