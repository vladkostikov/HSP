from unittest import TestCase
from bigger_greater import BiggerGreater


class Test(TestCase):
    def test_bigger_greater(self):
        self.assertEqual(BiggerGreater("ая"), "яа")
        self.assertEqual(BiggerGreater("fff"), "")
        self.assertEqual(BiggerGreater("нклм"), "нкмл")
        self.assertEqual(BiggerGreater("вибк"), "викб")
        self.assertEqual(BiggerGreater("вкиб"), "ибвк")
        self.assertEqual(BiggerGreater("шааа"), "")
        self.assertEqual(BiggerGreater("tt"), "")
        self.assertEqual(BiggerGreater("boo"), "obo")
