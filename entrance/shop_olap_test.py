from unittest import TestCase
from shop_olap import ShopOLAP


class Test(TestCase):
    def test_shop_olap(self):
        self.assertEqual(ShopOLAP(5, ["платье1 5", "сумка32 2", "платье1 1", "сумка23 2", "сумка128 4"]), ["платье1 6", "сумка128 4", "сумка23 2", "сумка32 2"])
        self.assertEqual(ShopOLAP(4, ["товар1 4", "товар3 9", "товар2 5", "товар2 4"]), ["товар2 9", "товар3 9", "товар1 4"])
        self.assertEqual(ShopOLAP(4, ["товар1 4"]), ["товар1 4"])
