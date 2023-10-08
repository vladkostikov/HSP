import unittest
from big_minus import BigMinus


class MyTestCase(unittest.TestCase):
    def test_conquest_campaign(self):
        self.assertEqual(BigMinus("12345", "12346"), str(12346 - 12345))
        self.assertEqual(BigMinus("987", "1234"), str(1234 - 987))
        self.assertEqual(BigMinus("1234567891", "1"), str(1234567891 - 1))
        self.assertEqual(BigMinus("1", "321"), str(321 - 1))
        self.assertEqual(BigMinus("123", "123"), str(123 - 123))


if __name__ == '__main__':
    unittest.main()
