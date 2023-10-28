from unittest import TestCase
from keymaker import Keymaker


class Test(TestCase):
    def test_keymaker(self):
        self.assertEqual(Keymaker(0), "")
        self.assertEqual(Keymaker(1), "1")
        self.assertEqual(Keymaker(2), "10")
        self.assertEqual(Keymaker(3), "100")
        self.assertEqual(Keymaker(4), "1001")
        self.assertEqual(Keymaker(5), "10010")
        self.assertEqual(Keymaker(6), "100100")
        self.assertEqual(Keymaker(7), "1001000")
        self.assertEqual(Keymaker(8), "10010000")
        self.assertEqual(Keymaker(9), "100100001")
        self.assertEqual(Keymaker(10), "1001000010")
        self.assertEqual(Keymaker(17), "10010000100000010")
        self.assertEqual(Keymaker(26), "10010000100000010000000010")
        self.assertEqual(Keymaker(37), "1001000010000001000000001000000000010")
