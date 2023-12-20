from unittest import TestCase
from postfix import postfix


class Test(TestCase):
    def test_postfix(self):
        self.assertEqual(5, postfix("3 2 + ="))
        self.assertEqual(5, postfix("3 2 +"))
        self.assertEqual(6, postfix("3 2 *"))
        self.assertEqual(150, postfix("5 30 *"))
        self.assertEqual(170, postfix("5 30 * 20 +"))
        self.assertEqual(195, postfix("15 180 +"))
        self.assertEqual(9, postfix("1 2 + 3 *"))
        self.assertEqual(258, postfix("8 20 30 + 5 * +"))
        self.assertEqual(59, postfix("8 2 + 5 * 9 + ="))

        # Не совсем корректные записи.
        self.assertIsNone(postfix(""))
        self.assertEqual(3, postfix("3 = 2"))
        self.assertEqual(3, postfix("3 = 2 +"))
        self.assertEqual(2, postfix("3 2 ="))
        self.assertEqual(2, postfix("3 + 2 ="))
        self.assertEqual(11, postfix("3 4 5 6 +"))
        self.assertEqual(10, postfix("8 2 + = 5 * 9 +"))
        self.assertEqual(59, postfix("8 2 + 5 * 9 + = 25 25 +"))
