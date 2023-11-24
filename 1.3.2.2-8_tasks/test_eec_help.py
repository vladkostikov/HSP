from unittest import TestCase
from eec_help import EEC_help


class Test(TestCase):
    def test_eec_help(self):
        self.assertEqual(False, EEC_help([1, 2, 3], [1, 2, 3, 4]))
        self.assertEqual(True, EEC_help([1, 2, 3], [1, 2, 3]))
        self.assertEqual(True, EEC_help([1, 3, 2], [1, 2, 3]))
        self.assertEqual(False, EEC_help([1, 3, 2, 3], [1, 2, 2, 3]))
        self.assertEqual(True, EEC_help([1, 1], [1, 1]))
        self.assertEqual(False, EEC_help([1, 2, 2, 2, 4], [1, 2, 2, 2, 1]))
