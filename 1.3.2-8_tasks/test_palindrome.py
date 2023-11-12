from unittest import TestCase
from palindrome import palindrome


class Test(TestCase):
    def test_palindrome(self):
        self.assertEqual(palindrome(""), True)
        self.assertEqual(palindrome("1"), True)
        self.assertEqual(palindrome("11"), True)
        self.assertEqual(palindrome("12"), False)
        self.assertEqual(palindrome("112"), False)
        self.assertEqual(palindrome("212"), True)
        self.assertEqual(palindrome("2123"), False)
        self.assertEqual(palindrome("32123"), True)
        self.assertEqual(palindrome("321 23"), False)
        self.assertEqual(palindrome("34123"), False)
        self.assertEqual(palindrome("34 23"), False)
        self.assertEqual(palindrome("32 23"), True)
