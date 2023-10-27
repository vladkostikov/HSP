from unittest import TestCase
from white_walkers import white_walkers


class Test(TestCase):
    def test_white_walkers(self):
        self.assertEqual(white_walkers("axxb6===4xaf5===eee5"), True)
        self.assertEqual(white_walkers("5==ooooooo=5=5"), False)
        self.assertEqual(white_walkers("abc=7==hdjs=3gg1=======5"), True)
        self.assertEqual(white_walkers("aaS=8"), False)
        self.assertEqual(white_walkers("9===1===9===1===9"), True)
        self.assertEqual(white_walkers(""), False)
        self.assertEqual(white_walkers("1==8====2"), False)
        self.assertEqual(white_walkers("1==8===2"), True)
