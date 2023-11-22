from unittest import TestCase
from digital_rain import digital_rain


class Test(TestCase):
    def test_digital_rain(self):
        self.assertEqual("111000", digital_rain("1111000"))
        self.assertEqual("11101000", digital_rain("11101000"))
        self.assertEqual("10", digital_rain("011111110"))
        self.assertEqual("", digital_rain("11111111"))
        self.assertEqual("1100", digital_rain("000011000"))
