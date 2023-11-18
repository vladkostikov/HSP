from unittest import TestCase
from generate_balanced_brackets import generate_balanced_brackets


class Test(TestCase):
    def test_generate_balanced_brackets(self):
        self.assertEqual(0, len(generate_balanced_brackets(-2)))
        self.assertEqual(0, len(generate_balanced_brackets(-1)))
        self.assertEqual(0, len(generate_balanced_brackets(0)))
        self.assertEqual(1, len(generate_balanced_brackets(1)))
        self.assertIn("()", generate_balanced_brackets(1))
        self.assertEqual(2, len(generate_balanced_brackets(2)))
        self.assertIn("(())", generate_balanced_brackets(2))
        self.assertIn("()()", generate_balanced_brackets(2))
        self.assertEqual(5, len(generate_balanced_brackets(3)))
        self.assertIn("((()))", generate_balanced_brackets(3))
        self.assertIn("(()())", generate_balanced_brackets(3))
        self.assertIn("(())()", generate_balanced_brackets(3))
        self.assertIn("()(())", generate_balanced_brackets(3))
        self.assertIn("()()()", generate_balanced_brackets(3))
        self.assertEqual(14, len(generate_balanced_brackets(4)))
        self.assertIn("(((())))", generate_balanced_brackets(4))
        self.assertIn("()()()()", generate_balanced_brackets(4))
