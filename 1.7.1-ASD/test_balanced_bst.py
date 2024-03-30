from unittest import TestCase
from balanced_bst import BalancedBST
from balanced_bst import BSTNode


class TestBalancedBST(TestCase):
    def test_generate_tree(self):
        bst = BalancedBST()
        self.assertIsNone(bst.Root)

        bst.GenerateTree([100, 50, 200])
        self.assertEqual(100, bst.Root.NodeKey)
        self.assertEqual(0, bst.Root.Level)
        self.assertEqual(50, bst.Root.LeftChild.NodeKey)
        self.assertEqual(1, bst.Root.LeftChild.Level)
        self.assertEqual(200, bst.Root.RightChild.NodeKey)
        self.assertEqual(1, bst.Root.RightChild.Level)
        self.assertIsNone(bst.Root.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild)
        self.assertIsNone(bst.Root.RightChild.RightChild)

        bst = BalancedBST()
        bst.GenerateTree([100, 50, 200, 25, 75, 150, 250])
        self.assertEqual(100, bst.Root.NodeKey)
        self.assertEqual(50, bst.Root.LeftChild.NodeKey)
        self.assertEqual(200, bst.Root.RightChild.NodeKey)
        self.assertEqual(25, bst.Root.LeftChild.LeftChild.NodeKey)
        self.assertEqual(2, bst.Root.LeftChild.LeftChild.Level)
        self.assertEqual(75, bst.Root.LeftChild.RightChild.NodeKey)
        self.assertEqual(2, bst.Root.LeftChild.RightChild.Level)
        self.assertEqual(150, bst.Root.RightChild.LeftChild.NodeKey)
        self.assertEqual(2, bst.Root.RightChild.LeftChild.Level)
        self.assertEqual(250, bst.Root.RightChild.RightChild.NodeKey)
        self.assertEqual(2, bst.Root.RightChild.RightChild.Level)

    def test_is_balanced(self):
        bst = BalancedBST()
        bst.GenerateTree([100, 50, 200])
        self.assertTrue(bst.IsBalanced(bst.Root))

        bst = BalancedBST()
        bst.GenerateTree([100, 50, 200, 25, 75, 150, 250])
        self.assertTrue(bst.IsBalanced(bst.Root))

        bst = BalancedBST()
        bst.GenerateTree([100, 50, 200, 25, 75, 150, 250, 20, 30, 70, 80, 140, 160, 240, 260])
        self.assertTrue(bst.IsBalanced(bst.Root))

        bst = BalancedBST()
        bst.GenerateTree([100, 50, 200, 25, 75])
        self.assertTrue(bst.IsBalanced(bst.Root))

        node25 = bst.Root.LeftChild.LeftChild
        node25.LeftChild = BSTNode(20, node25)
        self.assertFalse(bst.IsBalanced(bst.Root))

        node25.RightChild = BSTNode(30, node25)
        self.assertFalse(bst.IsBalanced(bst.Root))
