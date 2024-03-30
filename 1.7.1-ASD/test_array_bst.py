from unittest import TestCase
from array_bst import aBST


class TestaBST(TestCase):
    def test_find_key_index(self):
        bst = aBST(-5)
        self.assertEqual([], bst.Tree)
        self.assertIsNone(bst.FindKeyIndex(-100))
        self.assertIsNone(bst.FindKeyIndex(0))
        self.assertIsNone(bst.FindKeyIndex(100))

        bst = aBST(0)
        self.assertEqual(0, bst.FindKeyIndex(-100))
        self.assertEqual(0, bst.FindKeyIndex(0))
        self.assertEqual(0, bst.FindKeyIndex(100))

        bst = aBST(1)
        self.assertEqual(0, bst.FindKeyIndex(-100))
        self.assertEqual(0, bst.FindKeyIndex(0))
        self.assertEqual(0, bst.FindKeyIndex(100))

        bst.AddKey(100)
        self.assertEqual(0, bst.FindKeyIndex(100))
        self.assertEqual(-1, bst.FindKeyIndex(50))
        self.assertEqual(-2, bst.FindKeyIndex(200))

        bst = aBST(2)
        bst.AddKey(100)
        bst.AddKey(50)
        bst.AddKey(200)
        self.assertEqual(0, bst.FindKeyIndex(100))
        self.assertEqual(1, bst.FindKeyIndex(50))
        self.assertEqual(2, bst.FindKeyIndex(200))
        self.assertEqual(-3, bst.FindKeyIndex(25))
        self.assertEqual(-4, bst.FindKeyIndex(75))
        self.assertEqual(-5, bst.FindKeyIndex(150))
        self.assertEqual(-6, bst.FindKeyIndex(250))

    def test_add_key(self):
        bst = aBST(-5)
        self.assertEqual([], bst.Tree)
        self.assertEqual(-1, bst.AddKey(100))

        bst = aBST(0)
        self.assertEqual([None], bst.Tree)
        self.assertEqual(0, bst.AddKey(100))

        bst = aBST(1)
        self.assertEqual([None, None, None], bst.Tree)
        self.assertEqual(0, bst.AddKey(100))
        self.assertEqual(2, bst.AddKey(200))
        self.assertEqual(1, bst.AddKey(50))

        self.assertEqual(0, bst.AddKey(100))
        self.assertEqual(2, bst.AddKey(200))
        self.assertEqual(1, bst.AddKey(50))

        self.assertEqual(-1, bst.AddKey(25))
        self.assertEqual(-1, bst.AddKey(75))
        self.assertEqual(-1, bst.AddKey(150))
        self.assertEqual(-1, bst.AddKey(250))

    def test_calculate_tree_size(self):
        self.assertEqual(0, aBST._calculate_tree_size(None, -100))
        self.assertEqual(0, aBST._calculate_tree_size(None, -1))
        self.assertEqual(1, aBST._calculate_tree_size(None, 0))
        self.assertEqual(3, aBST._calculate_tree_size(None, 1))
        self.assertEqual(7, aBST._calculate_tree_size(None, 2))
        self.assertEqual(15, aBST._calculate_tree_size(None, 3))
        self.assertEqual(31, aBST._calculate_tree_size(None, 4))
