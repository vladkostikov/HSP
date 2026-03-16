from unittest import TestCase
from cleaning_robot_modular_style import CleaningRobot, CleaningRobotTransfer
import unittest

class Test(TestCase):
    def setUp(self):
        transfer = CleaningRobotTransfer()
        self.robot = CleaningRobot(transfer)

    def test_call_error_for_invalid_command(self):
        self.assertEqual("Error: no argument", self.robot.call("abcd"))

    def test_move_command(self):
        self.assertEqual("Error", self.robot.call("move abcd"))
        self.assertEqual("POS 0.0,0.0", self.robot.call("move -0"))
        self.assertEqual("POS 0.0,0.0", self.robot.call("move 0"))
        self.assertEqual("POS 100.0,0.0", self.robot.call("move 100"))
        self.assertEqual("POS -100.0,0.0", self.robot.call("move -200"))

    def test_turn_command(self):
        self.assertEqual("Error", self.robot.call("turn abcd"))
        self.assertEqual("ANGLE 0", self.robot.call("turn 0"))
        self.assertEqual("ANGLE 30", self.robot.call("turn 30"))
        self.assertEqual("ANGLE 0", self.robot.call("turn -30"))
        self.assertEqual("ANGLE 90", self.robot.call("turn 90"))
        self.assertEqual("ANGLE 270", self.robot.call("turn 180"))
        self.assertEqual("ANGLE 180", self.robot.call("turn -450"))

    def test_set_command(self):
        self.assertEqual("STATE water", self.robot.call("set water"))
        self.assertEqual("STATE soap", self.robot.call("set soap"))
        self.assertEqual("STATE brush", self.robot.call("set brush"))
        self.assertEqual("STATE brush", self.robot.call("set brush soap"))
        self.assertEqual("Error: no argument", self.robot.call("set"))
        self.assertEqual("Error: invalid cleaning state", self.robot.call("set invalid"))


    def test_start_stop_commands(self):
        self.assertEqual("STATE soap", self.robot.call("set soap"))
        self.assertEqual("START WITH soap", self.robot.call("start"))
        self.assertEqual("STOP", self.robot.call("stop"))

    def test_move_after_turn(self):
        self.robot.call("turn 90")
        self.assertEqual("POS 0.0,10.0", self.robot.call("move 10"))
        self.robot.call("turn 90")
        self.assertEqual("POS -20.0,10.0", self.robot.call("move 20"))

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
            "POS 100.0,0.0",
            "ANGLE 270",
            "STATE soap",
            "START WITH soap",
            "POS 100.0,-50.0",
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
