from unittest import TestCase
from tree import SimpleTreeNode
from tree import SimpleTree

class TestSimpleTree(TestCase):
    def test_add_child(self):
        node1 = SimpleTreeNode(1, None)
        tree = SimpleTree(node1)
        node2 = SimpleTreeNode(2, None)
        tree.AddChild(node1, node2)
        self.assertIn(node2, node1.Children)

    def test_delete_node(self):
        node1 = SimpleTreeNode(1, None)
        tree = SimpleTree(node1)

        node2 = SimpleTreeNode(2, None)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode(3, None)
        tree.AddChild(node1, node3)

        node4 = SimpleTreeNode(4, None)
        node5 = SimpleTreeNode(5, None)
        tree.AddChild(node2, node4)
        tree.AddChild(node2, node5)

        node6 = SimpleTreeNode(6, None)
        tree.AddChild(node4, node6)

        tree.DeleteNode(node2)
        self.assertNotIn(node2, node1.Children)

    def test_get_all_nodes(self):
        node1 = SimpleTreeNode(1, None)
        tree = SimpleTree(node1)

        node2 = SimpleTreeNode(2, None)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode(3, None)
        tree.AddChild(node1, node3)

        node4 = SimpleTreeNode(4, None)
        node5 = SimpleTreeNode(5, None)
        tree.AddChild(node2, node4)
        tree.AddChild(node2, node5)

        node6 = SimpleTreeNode(6, None)
        tree.AddChild(node4, node6)

        all_nodes = tree.GetAllNodes()
        self.assertEqual(6, len(all_nodes))
        self.assertIn(node1, all_nodes)
        self.assertIn(node2, all_nodes)
        self.assertIn(node3, all_nodes)
        self.assertIn(node4, all_nodes)
        self.assertIn(node5, all_nodes)
        self.assertIn(node6, all_nodes)

    def test_find_nodes_by_value(self):
        node1 = SimpleTreeNode(1, None)
        tree = SimpleTree(node1)

        node2 = SimpleTreeNode(20, None)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode(3, None)
        tree.AddChild(node1, node3)

        node4 = SimpleTreeNode(20, None)
        node5 = SimpleTreeNode(5, None)
        tree.AddChild(node2, node4)
        tree.AddChild(node2, node5)

        node6 = SimpleTreeNode(20, None)
        tree.AddChild(node4, node6)

        found_nodes = tree.FindNodesByValue(20)
        self.assertEqual(3, len(found_nodes))
        self.assertIn(node2, found_nodes)
        self.assertIn(node4, found_nodes)
        self.assertIn(node6, found_nodes)

    def test_move_node(self):
        node1 = SimpleTreeNode(1, None)
        tree = SimpleTree(node1)

        node2 = SimpleTreeNode(2, None)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode(3, None)
        tree.AddChild(node1, node3)

        node4 = SimpleTreeNode(4, None)
        node5 = SimpleTreeNode(5, None)
        tree.AddChild(node2, node4)
        tree.AddChild(node2, node5)

        node6 = SimpleTreeNode(6, None)
        tree.AddChild(node4, node6)

        self.assertIn(node4, node2.Children)
        self.assertEqual(node2, node4.Parent)
        tree.MoveNode(node4, node3)
        self.assertEqual(node3, node4.Parent)
        self.assertNotIn(node4, node2.Children)
        self.assertIn(node4, node3.Children)

    def test_count(self):
        tree = SimpleTree(None)
        self.assertEqual(0, tree.Count())

        node1 = SimpleTreeNode(1, None)
        tree = SimpleTree(node1)
        self.assertEqual(1, tree.Count())

        node2 = SimpleTreeNode(2, None)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode(3, None)
        tree.AddChild(node1, node3)

        node4 = SimpleTreeNode(4, None)
        node5 = SimpleTreeNode(5, None)
        tree.AddChild(node2, node4)
        tree.AddChild(node2, node5)

        node6 = SimpleTreeNode(6, None)
        tree.AddChild(node4, node6)

        self.assertEqual(6, tree.Count())
        tree.DeleteNode(node4)
        self.assertEqual(4, tree.Count())


    def test_leaf_count(self):
        tree = SimpleTree(None)
        self.assertEqual(0, tree.LeafCount())

        node1 = SimpleTreeNode(1, None)
        tree = SimpleTree(node1)

        node2 = SimpleTreeNode(2, None)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode(3, None)
        tree.AddChild(node1, node3)

        node4 = SimpleTreeNode(4, None)
        node5 = SimpleTreeNode(5, None)
        tree.AddChild(node2, node4)
        tree.AddChild(node2, node5)

        node6 = SimpleTreeNode(6, None)
        tree.AddChild(node4, node6)

        self.assertEqual(3, tree.LeafCount())
        tree.DeleteNode(node4)
        self.assertEqual(2, tree.LeafCount())


    def test_add_level_to_nodes(self):
        node1 = SimpleTreeNode(1, None)
        tree = SimpleTree(node1)

        node2 = SimpleTreeNode(2, None)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode(3, None)
        tree.AddChild(node1, node3)

        node4 = SimpleTreeNode(4, None)
        node5 = SimpleTreeNode(5, None)
        tree.AddChild(node2, node4)
        tree.AddChild(node2, node5)

        node6 = SimpleTreeNode(6, None)
        tree.AddChild(node4, node6)

        tree.add_level_to_nodes()
        self.assertEqual(1, node1.Level)
        self.assertEqual(2, node2.Level)
        self.assertEqual(2, node3.Level)
        self.assertEqual(3, node4.Level)
        self.assertEqual(3, node5.Level)
        self.assertEqual(4, node6.Level)
