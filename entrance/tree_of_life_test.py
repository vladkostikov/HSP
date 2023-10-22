from unittest import TestCase
from tree_of_life import TreeOfLife


class Test(TestCase):
    def test_tree_of_life(self):
        self.assertEqual(TreeOfLife(3, 4, 1, [".+..", "..+.", ".+.."]), ["++++", "++++", "++++"])
        self.assertEqual(TreeOfLife(3, 4, 2, [".+..", "..+.", ".+.."]), ["...+", "+...", "...+"])
        self.assertEqual(TreeOfLife(3, 4, 3, [".+..", "..+.", ".+.."]), ["++++", "++++", "++++"])
        self.assertEqual(TreeOfLife(3, 4, 4, [".+..", "..+.", ".+.."]), [".+..", "..+.", ".+.."])
        self.assertEqual(TreeOfLife(1, 5, 1, ["+...."]), ["+++++"])
        self.assertEqual(TreeOfLife(1, 5, 2, ["+...."]), ["..+++"])
        self.assertEqual(TreeOfLife(1, 5, 3, ["+...."]), ["+++++"])
        self.assertEqual(TreeOfLife(1, 5, 4, ["+...."]), ["+...."])
