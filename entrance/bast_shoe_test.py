from unittest import TestCase
from bast_shoe import BastShoe

class Test(TestCase):
    def test_bast_shoe(self):
        self.assertEqual(BastShoe("1 Привет"), "Привет")
        self.assertEqual(BastShoe("3 3"), "в")
        self.assertEqual(BastShoe("3 10"), "")
        self.assertEqual(BastShoe("3 -2"), "е")
        self.assertEqual(BastShoe("3 -10"), "")
        self.assertEqual(BastShoe("1 , Мир!"), "Привет, Мир!")
        self.assertEqual(BastShoe("1 ++"), "Привет, Мир!++")
        self.assertEqual(BastShoe("2 2"), "Привет, Мир!")
        self.assertEqual(BastShoe("4"), "Привет, Мир!++")
        self.assertEqual(BastShoe("4"), "Привет, Мир!")
        self.assertEqual(BastShoe("1 *"), "Привет, Мир!*")
        self.assertEqual(BastShoe("4"), "Привет, Мир!")
        self.assertEqual(BastShoe("4"), "Привет, Мир!")
        self.assertEqual(BastShoe("4"), "Привет, Мир!")
        self.assertEqual(BastShoe("3 6"), ",")
        self.assertEqual(BastShoe("2 100"), "")
        self.assertEqual(BastShoe("1 Привет"), "Привет")
        self.assertEqual(BastShoe("1 , Мир!"), "Привет, Мир!")
        self.assertEqual(BastShoe("1 ++"), "Привет, Мир!++")
        self.assertEqual(BastShoe("4"), "Привет, Мир!")
        self.assertEqual(BastShoe("4"), "Привет")
        self.assertEqual(BastShoe("5"), "Привет, Мир!")
        self.assertEqual(BastShoe("4"), "Привет")
        self.assertEqual(BastShoe("5"), "Привет, Мир!")
        self.assertEqual(BastShoe("5"), "Привет, Мир!++")
        self.assertEqual(BastShoe("5"), "Привет, Мир!++")
        self.assertEqual(BastShoe("5"), "Привет, Мир!++")
        self.assertEqual(BastShoe("4"), "Привет, Мир!")
        self.assertEqual(BastShoe("4"), "Привет")
        self.assertEqual(BastShoe("2 2"), "Прив")
        self.assertEqual(BastShoe("4"), "Привет")
        self.assertEqual(BastShoe("5"), "Прив")
        self.assertEqual(BastShoe("5"), "Прив")
        self.assertEqual(BastShoe("5"), "Прив")