from unittest import TestCase
from binary_search_tree import BST, BSTNode, BSTFind


class TestBST(TestCase):
    def test_find_node_by_key(self):
        bst = BST(None)

        # Проверяем отсутствие корневого узла.
        self.assertIsNone(bst.FindNodeByKey(100).Node)

        # Проверяем корневой узел.
        root = BSTNode(100, 100, None)
        bst.Root = root
        found_node = bst.FindNodeByKey(100)
        self.assertEqual(bst.Root.NodeKey, found_node.Node.NodeKey)
        self.assertTrue(found_node.NodeHasKey)
        self.assertFalse(found_node.ToLeft)

        # Проверяем поиск при добавлении в левую ветку.
        found_node = bst.FindNodeByKey(50)
        self.assertEqual(bst.Root.NodeKey, found_node.Node.NodeKey)
        self.assertFalse(found_node.NodeHasKey)
        self.assertTrue(found_node.ToLeft)

        # Проверяем поиск при добавлении в правую ветку.
        found_node = bst.FindNodeByKey(200)
        self.assertEqual(bst.Root.NodeKey, found_node.Node.NodeKey)
        self.assertFalse(found_node.NodeHasKey)
        self.assertFalse(found_node.ToLeft)

    def test_add_key_value(self):
        bst = BST(BSTNode(100, 100, None))

        # Проверяем корневой узел.
        self.assertIsNotNone(bst.FindNodeByKey(100).Node)

        # Проверяем добавление в левую ветку.
        self.assertFalse(bst.FindNodeByKey(50).NodeHasKey)
        self.assertTrue(bst.AddKeyValue(50, 50))
        self.assertTrue(bst.FindNodeByKey(50).NodeHasKey)
        self.assertEqual(50, bst.Root.LeftChild.NodeKey)

        # Проверяем повторное добавление присутствующего ключа.
        self.assertFalse(bst.AddKeyValue(50, 50))
        self.assertIsNone(bst.Root.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild)
        self.assertIsNone(bst.Root.RightChild)

        # Проверяем добавление в правую ветку.
        self.assertFalse(bst.FindNodeByKey(200).NodeHasKey)
        self.assertTrue(bst.AddKeyValue(200, 200))
        self.assertTrue(bst.FindNodeByKey(200).NodeHasKey)
        self.assertEqual(200, bst.Root.RightChild.NodeKey)

        # Проверяем добавление в левую ветку двух листов.
        self.assertTrue(bst.AddKeyValue(30, 30))
        self.assertEqual(30, bst.Root.LeftChild.LeftChild.NodeKey)
        self.assertTrue(bst.AddKeyValue(40, 40))
        self.assertEqual(40, bst.Root.LeftChild.LeftChild.RightChild.NodeKey)

        # Проверяем добавление в правую ветку двух листов.
        self.assertTrue(bst.AddKeyValue(150, 150))
        self.assertEqual(150, bst.Root.RightChild.LeftChild.NodeKey)
        self.assertTrue(bst.AddKeyValue(250, 250))
        self.assertEqual(250, bst.Root.RightChild.RightChild.NodeKey)

    def test_fin_min_max(self):
        bst = BST(BSTNode(100, 100, None))
        self.assertEqual(100, bst.FinMinMax(bst.Root, False).NodeKey)
        self.assertEqual(100, bst.FinMinMax(bst.Root, True).NodeKey)

        bst.AddKeyValue(50, 50)
        self.assertEqual(50, bst.FinMinMax(bst.Root, False).NodeKey)

        bst.AddKeyValue(40, 40)
        self.assertEqual(40, bst.FinMinMax(bst.Root, False).NodeKey)

        bst.AddKeyValue(60, 60)
        self.assertEqual(40, bst.FinMinMax(bst.Root, False).NodeKey)

        bst.AddKeyValue(30, 30)
        self.assertEqual(30, bst.FinMinMax(bst.Root, False).NodeKey)

        bst.AddKeyValue(35, 35)
        self.assertEqual(30, bst.FinMinMax(bst.Root, False).NodeKey)

        bst.AddKeyValue(200, 200)
        self.assertEqual(200, bst.FinMinMax(bst.Root, True).NodeKey)
        self.assertEqual(30, bst.FinMinMax(bst.Root, False).NodeKey)

        bst.AddKeyValue(150, 150)
        self.assertEqual(200, bst.FinMinMax(bst.Root, True).NodeKey)
        self.assertEqual(30, bst.FinMinMax(bst.Root, False).NodeKey)
        self.assertEqual(200, bst.FinMinMax(bst.Root.RightChild, True).NodeKey)
        self.assertEqual(150, bst.FinMinMax(bst.Root.RightChild, False).NodeKey)

        bst.AddKeyValue(250, 250)
        self.assertEqual(250, bst.FinMinMax(bst.Root, True).NodeKey)
        self.assertEqual(30, bst.FinMinMax(bst.Root, False).NodeKey)

        self.assertEqual(150, bst.FinMinMax(bst.Root.RightChild.LeftChild, True).NodeKey)
        self.assertEqual(150, bst.FinMinMax(bst.Root.RightChild.LeftChild, False).NodeKey)

    def test_delete_node_by_key(self):
        bst = BST(BSTNode(100, 100, None))
        bst.AddKeyValue(50, 50)
        bst.AddKeyValue(40, 40)
        bst.AddKeyValue(60, 60)
        bst.AddKeyValue(30, 30)

        # Проверяем удаление несуществующего ключа.
        self.assertFalse(bst.FindNodeByKey(45).NodeHasKey)
        self.assertFalse(bst.DeleteNodeByKey(45))

        # Проверяем удаление левого листа.
        node_to_delete = bst.FindNodeByKey(30).Node
        parent = node_to_delete.Parent
        self.assertEqual(30, parent.LeftChild.NodeKey)
        self.assertTrue(bst.DeleteNodeByKey(30))
        self.assertIsNone(parent.LeftChild)

        # Проверяем удаление правого листа.
        node_to_delete = bst.FindNodeByKey(60).Node
        parent = node_to_delete.Parent
        self.assertEqual(60, parent.RightChild.NodeKey)
        self.assertTrue(bst.DeleteNodeByKey(60))
        self.assertIsNone(parent.RightChild)

        # Проверяем удаление узла с одним потомком.
        node_to_delete = bst.FindNodeByKey(50).Node
        parent = node_to_delete.Parent
        self.assertEqual(50, parent.LeftChild.NodeKey)
        self.assertTrue(bst.DeleteNodeByKey(50))
        self.assertEqual(40, parent.LeftChild.NodeKey)

        bst.AddKeyValue(200, 200)
        bst.AddKeyValue(150, 150)
        bst.AddKeyValue(250, 250)
        bst.AddKeyValue(225, 225)
        bst.AddKeyValue(220, 220)
        bst.AddKeyValue(230, 230)
        bst.AddKeyValue(235, 235)
        bst.AddKeyValue(275, 275)
        bst.AddKeyValue(270, 270)
        bst.AddKeyValue(280, 280)

        # Проверяем удаление узла с двумя потомками, минимальный потомок - лист.
        node_to_delete = bst.FindNodeByKey(200).Node
        parent = node_to_delete.Parent
        self.assertEqual(200, parent.RightChild.NodeKey)
        self.assertTrue(bst.DeleteNodeByKey(200))
        self.assertEqual(220, parent.RightChild.NodeKey)

        # Проверяем удаление узла с двумя потомками, минимальный потомок - узел с правым потомком.
        node_to_delete = bst.FindNodeByKey(220).Node
        parent = node_to_delete.Parent
        self.assertEqual(220, parent.RightChild.NodeKey)
        self.assertTrue(bst.DeleteNodeByKey(220))
        self.assertEqual(225, parent.RightChild.NodeKey)
        self.assertEqual(230, parent.RightChild.RightChild.LeftChild.NodeKey)
        self.assertEqual(235, parent.RightChild.RightChild.LeftChild.RightChild.NodeKey)

    def test_delete_root_node_by_key(self):
        bst = BST(BSTNode(100, 100, None))

        # Проверяем удаление корневого узла без потомков.
        node_to_delete = bst.FindNodeByKey(100).Node
        self.assertIsNone(node_to_delete.Parent)
        self.assertIsNone(node_to_delete.Parent)
        self.assertIsNone(node_to_delete.LeftChild)
        self.assertIsNone(node_to_delete.RightChild)
        self.assertTrue(bst.DeleteNodeByKey(100))
        self.assertIsNone(bst.Root)

        # Проверяем удаление корневого узла с одним потомком.
        bst = BST(BSTNode(100, 100, None))
        bst.AddKeyValue(50, 50)
        bst.AddKeyValue(40, 40)
        bst.AddKeyValue(60, 60)
        bst.AddKeyValue(30, 30)
        node_to_delete = bst.FindNodeByKey(100).Node
        self.assertIsNone(node_to_delete.Parent)
        self.assertIsNone(node_to_delete.Parent)
        self.assertIsNotNone(node_to_delete.LeftChild)
        self.assertIsNone(node_to_delete.RightChild)
        self.assertTrue(bst.DeleteNodeByKey(100))
        self.assertEqual(50, bst.Root.NodeKey)
        self.assertIsNone(bst.Root.Parent)
        self.assertEqual(40, bst.Root.LeftChild.NodeKey)
        self.assertEqual(60, bst.Root.RightChild.NodeKey)

        # Проверяем удаление корневого узла с двумя потомками.
        bst = BST(BSTNode(100, 100, None))
        bst.AddKeyValue(50, 50)
        bst.AddKeyValue(40, 40)
        bst.AddKeyValue(60, 60)
        bst.AddKeyValue(30, 30)
        bst.AddKeyValue(200, 200)
        bst.AddKeyValue(150, 150)
        bst.AddKeyValue(180, 180)
        bst.AddKeyValue(175, 175)
        bst.AddKeyValue(185, 185)
        bst.AddKeyValue(250, 250)
        node_to_delete = bst.FindNodeByKey(100).Node
        self.assertIsNone(node_to_delete.Parent)
        self.assertIsNone(node_to_delete.Parent)
        self.assertTrue(bst.DeleteNodeByKey(100))
        self.assertEqual(150, bst.Root.NodeKey)
        self.assertIsNone(bst.Root.Parent)
        self.assertEqual(50, bst.Root.LeftChild.NodeKey)
        self.assertEqual(200, bst.Root.RightChild.NodeKey)
        self.assertEqual(180, bst.Root.RightChild.LeftChild.NodeKey)
        self.assertEqual(200, bst.Root.RightChild.LeftChild.Parent.NodeKey)
        self.assertEqual(250, bst.Root.RightChild.RightChild.NodeKey)

    def test_count(self):
        bst = BST(None)
        self.assertEqual(0, bst.Count())
        root = BSTNode(100, 100, None)
        bst.Root = root
        self.assertEqual(1, bst.Count())
        bst.AddKeyValue(50, 50)
        self.assertEqual(2, bst.Count())
        bst.AddKeyValue(40, 40)
        self.assertEqual(3, bst.Count())
        bst.AddKeyValue(60, 60)
        self.assertEqual(4, bst.Count())
        bst.AddKeyValue(30, 30)
        self.assertEqual(5, bst.Count())
        bst.AddKeyValue(200, 200)
        self.assertEqual(6, bst.Count())
        bst.AddKeyValue(150, 150)
        self.assertEqual(7, bst.Count())
        bst.AddKeyValue(250, 250)
        self.assertEqual(8, bst.Count())

        self.assertTrue(bst.DeleteNodeByKey(30))
        self.assertEqual(7, bst.Count())
        self.assertTrue(bst.DeleteNodeByKey(150))
        self.assertEqual(6, bst.Count())
        self.assertTrue(bst.DeleteNodeByKey(60))
        self.assertEqual(5, bst.Count())

        self.assertFalse(bst.DeleteNodeByKey(1000))
        self.assertEqual(5, bst.Count())

    def test_wide_all_nodes(self):
        bst = BST(None)
        self.assertEqual((), tuple(map(lambda node: node.NodeKey, bst.WideAllNodes())))

        bst = BST(BSTNode(100, 100, None))
        self.assertEqual((100,), tuple(map(lambda node: node.NodeKey, bst.WideAllNodes())))
        bst.AddKeyValue(50, 50)
        bst.AddKeyValue(40, 40)
        bst.AddKeyValue(60, 60)
        self.assertEqual((100, 50, 40, 60), tuple(map(lambda node: node.NodeKey, bst.WideAllNodes())))

        bst.AddKeyValue(30, 30)
        bst.AddKeyValue(200, 200)
        self.assertEqual((100, 50, 200, 40, 60, 30), tuple(map(lambda node: node.NodeKey, bst.WideAllNodes())))

        bst.AddKeyValue(150, 150)
        bst.AddKeyValue(250, 250)
        self.assertEqual((100, 50, 200, 40, 60, 150, 250, 30), tuple(map(lambda node: node.NodeKey, bst.WideAllNodes())))

        bst.AddKeyValue(180, 180)
        bst.AddKeyValue(175, 175)
        bst.AddKeyValue(185, 185)
        self.assertEqual((100, 50, 200, 40, 60, 150, 250, 30, 180, 175, 185), tuple(map(lambda node: node.NodeKey, bst.WideAllNodes())))

    def test_deep_all_nodes(self):
        bst = BST(None)
        self.assertEqual((), tuple(map(lambda node: node.NodeKey, bst.DeepAllNodes(0))))
        self.assertEqual((), tuple(map(lambda node: node.NodeKey, bst.DeepAllNodes(1))))
        self.assertEqual((), tuple(map(lambda node: node.NodeKey, bst.DeepAllNodes(2))))

        bst = BST(BSTNode(100, 100, None))
        self.assertEqual((100,), tuple(map(lambda node: node.NodeKey, bst.DeepAllNodes(0))))
        self.assertEqual((100,), tuple(map(lambda node: node.NodeKey, bst.DeepAllNodes(1))))
        self.assertEqual((100,), tuple(map(lambda node: node.NodeKey, bst.DeepAllNodes(2))))

        bst.AddKeyValue(50, 50)
        bst.AddKeyValue(40, 40)
        bst.AddKeyValue(60, 60)
        self.assertEqual((40, 50, 60, 100), tuple(map(lambda node: node.NodeKey, bst.DeepAllNodes(0))))
        self.assertEqual((40, 60, 50, 100), tuple(map(lambda node: node.NodeKey, bst.DeepAllNodes(1))))
        self.assertEqual((100, 50, 40, 60), tuple(map(lambda node: node.NodeKey, bst.DeepAllNodes(2))))

        bst.AddKeyValue(30, 30)
        bst.AddKeyValue(200, 200)
        self.assertEqual((30, 40, 50, 60, 100, 200), tuple(map(lambda node: node.NodeKey, bst.DeepAllNodes(0))))
        self.assertEqual((30, 40, 60, 50, 200, 100), tuple(map(lambda node: node.NodeKey, bst.DeepAllNodes(1))))
        self.assertEqual((100, 50, 40, 30, 60, 200), tuple(map(lambda node: node.NodeKey, bst.DeepAllNodes(2))))

        bst.AddKeyValue(150, 150)
        bst.AddKeyValue(250, 250)
        self.assertEqual((30, 40, 50, 60, 100, 150, 200, 250), tuple(map(lambda node: node.NodeKey, bst.DeepAllNodes(0))))
        self.assertEqual((30, 40, 60, 50, 150, 250, 200, 100), tuple(map(lambda node: node.NodeKey, bst.DeepAllNodes(1))))
        self.assertEqual((100, 50, 40, 30, 60, 200, 150, 250), tuple(map(lambda node: node.NodeKey, bst.DeepAllNodes(2))))
