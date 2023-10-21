from unittest import TestCase
from sherlock_valid_string import SherlockValidString


class Test(TestCase):
    def test_sherlock_valid_string(self):
        self.assertEqual(SherlockValidString("xyz"), True)
        self.assertEqual(SherlockValidString("xyzaa"), True)
        self.assertEqual(SherlockValidString("xyzaaa"), False)
        self.assertEqual(SherlockValidString("xxyyz"), True)
        self.assertEqual(SherlockValidString("xyzzz"), False)
        self.assertEqual(SherlockValidString("xxyyza"), False)
        self.assertEqual(SherlockValidString("xxyyzabc"), False)
        self.assertEqual(SherlockValidString("ab"), True)
        self.assertEqual(SherlockValidString("aa"), True)
        self.assertEqual(SherlockValidString("aaaabbbbc"), True)
        self.assertEqual(SherlockValidString("xxxxxyyyyyyy"), False)
