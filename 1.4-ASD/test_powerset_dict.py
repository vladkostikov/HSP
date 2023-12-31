from unittest import TestCase
from powerset_dict import PowerSet


class TestPowerSet(TestCase):
    def test_size(self):
        powerset = PowerSet()
        self.assertEqual(0, powerset.size())
        self.assertFalse(powerset.remove(10))
        self.assertEqual(0, powerset.size())

        self.assertEqual(10, powerset.put(10))
        self.assertEqual(1, powerset.size())

        self.assertEqual(20, powerset.put(20))
        self.assertEqual(2, powerset.size())

        self.assertEqual(30, powerset.put(30))
        self.assertEqual(3, powerset.size())

        self.assertTrue(powerset.remove(20))
        self.assertEqual(2, powerset.size())

    def test_put(self):
        powerset = PowerSet()
        self.assertEqual(0, powerset.size())
        self.assertEqual(10, powerset.put(10))
        self.assertEqual(20, powerset.put(20))
        self.assertEqual(30, powerset.put(30))
        self.assertEqual(3, powerset.size())

        self.assertEqual(10, powerset.put(10))
        self.assertEqual(20, powerset.put(20))
        self.assertEqual(3, powerset.size())

        self.assertEqual(40, powerset.put(40))
        self.assertEqual(4, powerset.size())

    def test_get(self):
        powerset = PowerSet()
        self.assertFalse(powerset.get(10))
        self.assertFalse(powerset.get(20))
        self.assertFalse(powerset.get(30))

        self.assertEqual(10, powerset.put(10))
        self.assertTrue(powerset.get(10))
        self.assertFalse(powerset.get(20))
        self.assertFalse(powerset.get(30))

        self.assertEqual(20, powerset.put(20))
        self.assertEqual(30, powerset.put(30))
        self.assertTrue(powerset.get(10))
        self.assertTrue(powerset.get(20))
        self.assertTrue(powerset.get(30))

    def test_remove(self):
        powerset = PowerSet()
        self.assertEqual(0, powerset.size())
        self.assertFalse(powerset.remove(10))
        self.assertEqual(0, powerset.size())

        self.assertEqual(10, powerset.put(10))
        self.assertEqual(1, powerset.size())

        self.assertEqual(20, powerset.put(20))
        self.assertEqual(2, powerset.size())

        self.assertTrue(powerset.remove(10))
        self.assertEqual(1, powerset.size())
        self.assertFalse(powerset.get(10))
        self.assertTrue(powerset.get(20))

    def test_intersection(self):
        set1 = PowerSet()
        for number in [10, 20, 30, 40, 50]:
            set1.put(number)

        set2 = PowerSet()
        for number in [30, 40, 50, 60, 70]:
            set2.put(number)

        set3 = PowerSet()
        for number in [60, 70, 80]:
            set3.put(number)

        intersection_set = set1.intersection(set2)
        self.assertEqual(3, intersection_set.size())
        self.assertFalse(intersection_set.get(10))
        self.assertFalse(intersection_set.get(20))
        self.assertTrue(intersection_set.get(30))
        self.assertTrue(intersection_set.get(40))
        self.assertTrue(intersection_set.get(50))
        self.assertFalse(intersection_set.get(60))
        self.assertFalse(intersection_set.get(70))

        self.assertEqual(0, set1.intersection(set3).size())
        self.assertEqual(2, set2.intersection(set3).size())

    def test_union(self):
        set1 = PowerSet()
        for number in [10, 20, 30, 40, 50]:
            set1.put(number)

        set2 = PowerSet()
        for number in [30, 40, 50, 60, 70]:
            set2.put(number)

        union_set = set1.union(set2)
        self.assertEqual(7, union_set.size())
        self.assertTrue(union_set.get(10))
        self.assertTrue(union_set.get(20))
        self.assertTrue(union_set.get(30))
        self.assertTrue(union_set.get(40))
        self.assertTrue(union_set.get(50))
        self.assertTrue(union_set.get(60))
        self.assertTrue(union_set.get(70))

        self.assertEqual(5, set1.union(PowerSet()).size())

    def test_difference(self):
        set1 = PowerSet()
        for number in [10, 20, 30, 40, 50]:
            set1.put(number)

        set2 = PowerSet()
        for number in [30, 40, 50, 60, 70]:
            set2.put(number)

        set3 = PowerSet()
        for number in [0, 10, 20, 30, 40, 50, 60]:
            set3.put(number)

        difference_set = set1.difference(set2)
        self.assertEqual(2, difference_set.size())
        self.assertTrue(difference_set.get(10))
        self.assertTrue(difference_set.get(20))

        self.assertEqual(0, set1.difference(set3).size())
        self.assertEqual(1, set2.difference(set3).size())

    def test_issubset(self):
        set1 = PowerSet()
        for number in [10, 20, 30, 40, 50]:
            set1.put(number)
        self.assertTrue(set1.issubset(PowerSet()))

        set2 = PowerSet()
        for number in [30, 40, 50, 60, 70]:
            set2.put(number)
        self.assertFalse(set1.issubset(set2))

        set3 = PowerSet()
        for number in [30, 40, 50, 60]:
            set3.put(number)
        self.assertFalse(set1.issubset(set3))
        self.assertTrue(set2.issubset(set3))

        set4 = PowerSet()
        for number in [10, 20, 30, 40, 50, 60, 70]:
            set4.put(number)
        self.assertFalse(set1.issubset(set4))

    def test_with_20_000_elements(self):
        powerset = PowerSet()
        for number in range(20000):
            self.assertEqual(number, powerset.put(number))

        for number in range(10000, 11000):
            self.assertTrue(powerset.get(number))
            self.assertTrue(powerset.remove(number))

        set2 = PowerSet()
        for number in range(25000, 30000):
            set2.put(number)
        self.assertEqual(24000, powerset.union(set2).size())
