from unittest import TestCase
from ksort import ksort

class Testksort(TestCase):
    def test_index(self):
        k_sort = ksort()
        self.assertEqual(0, k_sort.index("a00"))
        self.assertEqual(1, k_sort.index("a01"))
        self.assertEqual(2, k_sort.index("a02"))
        self.assertEqual(10, k_sort.index("a10"))
        self.assertEqual(11, k_sort.index("a11"))
        self.assertEqual(19, k_sort.index("a19"))
        self.assertEqual(100, k_sort.index("b00"))
        self.assertEqual(101, k_sort.index("b01"))
        self.assertEqual(110, k_sort.index("b10"))
        self.assertEqual(111, k_sort.index("b11"))
        self.assertEqual(700, k_sort.index("h00"))
        self.assertEqual(799, k_sort.index("h99"))
        self.assertEqual(-1, k_sort.index("i00"))
        self.assertEqual(-1, k_sort.index("i99"))
        self.assertEqual(-1, k_sort.index("a000"))
        self.assertEqual(-1, k_sort.index("a999"))

    def test_add(self):
        k_sort = ksort()
        self.assertTrue(k_sort.add("a00"))
        self.assertTrue(k_sort.add("a09"))
        self.assertTrue(k_sort.add("a10"))
        self.assertTrue(k_sort.add("a99"))
        self.assertTrue(k_sort.add("h00"))
        self.assertTrue(k_sort.add("h99"))
        self.assertFalse(k_sort.add("i00"))
        self.assertFalse(k_sort.add("i99"))
        self.assertFalse(k_sort.add("a000"))
        self.assertFalse(k_sort.add("a"))
        self.assertFalse(k_sort.add("a0"))
        self.assertFalse(k_sort.add("a9"))
        self.assertFalse(k_sort.add("h"))
        self.assertFalse(k_sort.add("i"))
