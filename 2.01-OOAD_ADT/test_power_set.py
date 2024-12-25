from unittest import TestCase
from power_set import PowerSet


class Test(TestCase):
    def test_init(self):
        power_set = PowerSet(5)
        self.assertEqual(power_set.PUT_ERR, power_set.get_put_status())
        self.assertEqual(power_set.REMOVE_ERR, power_set.get_remove_status())
        self.assertEqual(0, power_set.size())

    def test_put(self):
        power_set = PowerSet(5)

        for i in range(5):
            self.assertIsNone(power_set.put(str(i)))
            self.assertEqual(power_set.PUT_OK, power_set.get_put_status())
            self.assertEqual(i + 1, power_set.size())
        self.assertEqual(5, power_set.size())

        self.assertIsNone(power_set.put("3"))
        self.assertEqual(power_set.PUT_EXIST, power_set.get_put_status())

        self.assertIsNone(power_set.put("10"))
        self.assertEqual(power_set.PUT_ERR, power_set.get_put_status())

    def test_remove(self):
        power_set = PowerSet(5)

        self.assertIsNone(power_set.remove("3"))
        self.assertEqual(power_set.REMOVE_ERR, power_set.get_remove_status())
        self.assertEqual(0, power_set.size())

        for i in range(5):
            self.assertIsNone(power_set.put(str(i)))
        self.assertEqual(5, power_set.size())

        self.assertIsNone(power_set.remove("3"))
        self.assertEqual(power_set.REMOVE_OK, power_set.get_remove_status())
        self.assertEqual(4, power_set.size())

        self.assertIsNone(power_set.remove("10"))
        self.assertEqual(power_set.REMOVE_ERR, power_set.get_remove_status())
        self.assertEqual(4, power_set.size())

    def test_intersection_with_intersection(self):
        power_set1 = PowerSet(10)
        for i in range(0, 10):
            self.assertIsNone(power_set1.put(str(i)))

        power_set2 = PowerSet(10)
        for i in range(5, 15):
            self.assertIsNone(power_set2.put(str(i)))

        intersection_set = power_set1.intersection(power_set2)
        self.assertEqual(5, intersection_set.size())
        for i in range(5, 10):
            self.assertTrue(intersection_set.get(str(i)))

    def test_intersection_without_intersection(self):
        power_set1 = PowerSet(10)
        for i in range(0, 10):
            self.assertIsNone(power_set1.put(str(i)))

        power_set2 = PowerSet(10)
        for i in range(15, 25):
            self.assertIsNone(power_set2.put(str(i)))

        intersection_set = power_set1.intersection(power_set2)
        self.assertEqual(0, intersection_set.size())

    def test_union_with_non_empty_sets_with_intersection(self):
        power_set1 = PowerSet(10)
        for i in range(0, 10):
            self.assertIsNone(power_set1.put(str(i)))

        power_set2 = PowerSet(10)
        for i in range(5, 15):
            self.assertIsNone(power_set2.put(str(i)))

        intersection_set = power_set1.union(power_set2)
        self.assertEqual(15, intersection_set.size())
        for i in range(0, 15):
            self.assertTrue(intersection_set.get(str(i)))

    def test_union_with_non_empty_sets_without_intersection(self):
        power_set1 = PowerSet(10)
        for i in range(0, 10):
            self.assertIsNone(power_set1.put(str(i)))

        power_set2 = PowerSet(20)
        for i in range(20, 35):
            self.assertIsNone(power_set2.put(str(i)))

        union_set = power_set1.union(power_set2)
        self.assertEqual(25, union_set.size())
        for i in range(0, 10):
            self.assertTrue(union_set.get(str(i)))
        for i in range(20, 35):
            self.assertTrue(union_set.get(str(i)))

    def test_union_with_empty_set(self):
        power_set1 = PowerSet(10)
        for i in range(0, 10):
            self.assertIsNone(power_set1.put(str(i)))

        power_set2 = PowerSet(20)

        union_set = power_set1.union(power_set2)
        self.assertEqual(10, union_set.size())
        for i in range(0, 10):
            self.assertTrue(union_set.get(str(i)))

    def test_union_with_empty_sets(self):
        power_set1 = PowerSet(10)
        power_set2 = PowerSet(20)

        union_set = power_set1.union(power_set2)
        self.assertEqual(0, union_set.size())

    def test_difference_with_empty_sets(self):
        power_set1 = PowerSet(10)
        power_set2 = PowerSet(20)

        difference_set = power_set1.difference(power_set2)
        self.assertEqual(0, difference_set.size())

    def test_difference_with_empty_first_set(self):
        power_set1 = PowerSet(10)
        power_set2 = PowerSet(20)
        for i in range(0, 10):
            self.assertIsNone(power_set2.put(str(i)))

        difference_set = power_set1.difference(power_set2)
        self.assertEqual(0, difference_set.size())

    def test_difference_with_empty_second_set(self):
        power_set1 = PowerSet(10)
        for i in range(0, 10):
            self.assertIsNone(power_set1.put(str(i)))

        power_set2 = PowerSet(20)

        difference_set = power_set1.difference(power_set2)
        self.assertEqual(10, difference_set.size())
        for i in range(0, 10):
            self.assertTrue(difference_set.get(str(i)))

    def test_difference_with_intersection_set(self):
        power_set1 = PowerSet(10)
        for i in range(0, 10):
            self.assertIsNone(power_set1.put(str(i)))

        power_set2 = PowerSet(20)
        for i in range(5, 20):
            self.assertIsNone(power_set2.put(str(i)))

        difference_set = power_set1.difference(power_set2)
        self.assertEqual(5, difference_set.size())
        for i in range(0, 5):
            self.assertTrue(difference_set.get(str(i)))

    def test_difference_with_full_intersection_set(self):
        power_set1 = PowerSet(10)
        for i in range(0, 10):
            self.assertIsNone(power_set1.put(str(i)))

        power_set2 = PowerSet(20)
        for i in range(-2, 12):
            self.assertIsNone(power_set2.put(str(i)))

        difference_set = power_set1.difference(power_set2)
        self.assertEqual(0, difference_set.size())

    def test_difference_without_intersection_set(self):
        power_set1 = PowerSet(10)
        for i in range(0, 10):
            self.assertIsNone(power_set1.put(str(i)))

        power_set2 = PowerSet(20)
        for i in range(20, 30):
            self.assertIsNone(power_set2.put(str(i)))

        difference_set = power_set1.difference(power_set2)
        self.assertEqual(10, difference_set.size())
        for i in range(0, 10):
            self.assertTrue(difference_set.get(str(i)))

    def test_issubset_with_subset(self):
        power_set1 = PowerSet(10)
        for i in range(0, 10):
            self.assertIsNone(power_set1.put(str(i)))

        power_set2 = PowerSet(20)
        for i in range(0, 5):
            self.assertIsNone(power_set2.put(str(i)))

        self.assertTrue(power_set1.issubset(power_set2))

    def test_issubset_when_current_set_is_subset_of_parameter_set(self):
        power_set1 = PowerSet(10)
        for i in range(0, 10):
            self.assertIsNone(power_set1.put(str(i)))

        power_set2 = PowerSet(20)
        for i in range(-2, 12):
            self.assertIsNone(power_set2.put(str(i)))

        self.assertFalse(power_set1.issubset(power_set2))

    def test_issubset_with_partial_subset(self):
        power_set1 = PowerSet(10)
        for i in range(0, 10):
            self.assertIsNone(power_set1.put(str(i)))

        power_set2 = PowerSet(20)
        for i in range(5, 15):
            self.assertIsNone(power_set2.put(str(i)))

        self.assertFalse(power_set1.issubset(power_set2))

    def test_equals(self):
        power_set1 = PowerSet(10)
        for i in range(0, 10):
            self.assertIsNone(power_set1.put(str(i)))

        power_set2 = PowerSet(20)
        self.assertFalse(power_set1.equals(power_set2))

        for i in range(0, 10):
            self.assertIsNone(power_set2.put(str(i)))
        self.assertTrue(power_set1.equals(power_set2))

        self.assertIsNone(power_set2.put("42"))
        self.assertFalse(power_set1.equals(power_set2))
