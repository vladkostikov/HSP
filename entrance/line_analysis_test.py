from unittest import TestCase
from line_analysis import LineAnalysis


class Test(TestCase):
    def test_line_analysis(self):
        self.assertEqual(LineAnalysis("*..*..*..*..*..*..*"), True)
        self.assertEqual(LineAnalysis("*..*...*..*..*..*..*"), False)
        self.assertEqual(LineAnalysis("*..*..*..*..*..**..*"), False)
        self.assertEqual(LineAnalysis("*"), True)
        self.assertEqual(LineAnalysis("***"), True)
        self.assertEqual(LineAnalysis("*.......*.......*"), True)
        self.assertEqual(LineAnalysis("**"), True)
        self.assertEqual(LineAnalysis("*.*"), True)
        self.assertEqual(LineAnalysis("*.**"), False)
        self.assertEqual(LineAnalysis("**..**..**"), True)
        self.assertEqual(LineAnalysis("***....***....***"), True)
        self.assertEqual(LineAnalysis(""), True)
