from unittest import TestCase
from cleaning_robot_procedural_style import *
import unittest

class Test(TestCase):
    def setUp(self):
        self.robot = create_robot()

    def test_call_error_for_invalid_command(self):
        self.assertEqual("Error", call_robot(self.robot, "abcd"))

    def test_move_command(self):
        self.assertEqual("Error", call_robot(self.robot, "move abcd"))
        self.assertEqual("POS 0.0,0.0", call_robot(self.robot, "move -0"))
        self.assertEqual("POS 0.0,0.0", call_robot(self.robot, "move 0"))
        self.assertEqual("POS 100.0,0.0", call_robot(self.robot, "move 100"))
        self.assertEqual("POS -100.0,0.0", call_robot(self.robot, "move -200"))

    def test_turn_command(self):
        self.assertEqual("Error", call_robot(self.robot, "turn abcd"))
        self.assertEqual("ANGLE 0", call_robot(self.robot, "turn 0"))
        self.assertEqual("ANGLE 30", call_robot(self.robot, "turn 30"))
        self.assertEqual("ANGLE 0", call_robot(self.robot, "turn -30"))
        self.assertEqual("ANGLE 90", call_robot(self.robot, "turn 90"))
        self.assertEqual("ANGLE 270", call_robot(self.robot, "turn 180"))
        self.assertEqual("ANGLE 180", call_robot(self.robot, "turn -450"))

    def test_set_command(self):
        self.assertEqual("STATE water", call_robot(self.robot, "set water"))
        self.assertEqual("STATE soap", call_robot(self.robot, "set soap"))
        self.assertEqual("STATE brush", call_robot(self.robot, "set brush"))
        self.assertEqual("Error", call_robot(self.robot, "set invalid"))
        self.assertEqual("Error", call_robot(self.robot, "set brush soap"))
        self.assertEqual("Error", call_robot(self.robot, "set"))


    def test_start_stop_commands(self):
        self.assertEqual("STATE soap", call_robot(self.robot, "set soap"))
        self.assertEqual("START WITH soap", call_robot(self.robot, "start"))
        self.assertEqual("STOP", call_robot(self.robot, "stop"))

    def test_move_after_turn(self):
        call_robot(self.robot, "turn 90")
        self.assertEqual("POS 0.0,10.0", call_robot(self.robot, "move 10"))
        call_robot(self.robot, "turn 90")
        self.assertEqual("POS -20.0,10.0", call_robot(self.robot,   "move 20"))

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
                self.assertEqual(exp, call_robot(self.robot, cmd))

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(Test)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
