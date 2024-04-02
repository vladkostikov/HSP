class SimpleTreeNode:

    def __init__(self, value, parent):
        self.NodeValue = value
        self.Parent = parent
        self.Children = []


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        NodeToDelete.Parent.Children.remove(NodeToDelete)

    def GetAllNodes(self) -> list:
        return self._get_all_nodes(self.Root)

    def FindNodesByValue(self, value) -> list:
        return list(filter(lambda node: node.NodeValue is value, self.GetAllNodes()))

    def MoveNode(self, OriginalNode, NewParent):
        OriginalNode.Parent.Children.remove(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        return len(list(filter(lambda node: len(node.Children) == 0, self.GetAllNodes())))

    def EvenTrees(self) -> list:
        leaves = list(filter(lambda node: len(node.Children) == 0, self.GetAllNodes()))

        separated_pairs = []
        for node in leaves:
            separated = self._separate_even(node)
            separated_pairs.extend(separated)

        unique_separated_pairs = []
        for pair in separated_pairs:
            if pair in unique_separated_pairs:
                continue
            unique_separated_pairs.append(pair)

        unique_separated_nodes = []
        for pair in unique_separated_pairs:
            unique_separated_nodes.extend(pair)

        return unique_separated_nodes

    def _separate_even(self, node: SimpleTreeNode) -> list:
        sepatated = []

        parent = node.Parent
        if parent is None:
            return sepatated

        childs = self._get_all_nodes(node)
        if len(childs) > 0 and len(childs) % 2 == 1:
            sepatated.append([parent, node])
        sepatated.extend(self._separate_even(parent))

        return sepatated

    def _get_all_nodes(self, node) -> list:
        if node is None:
            return []

        nodes = node.Children[:]
        for children in nodes[:]:
            sub_children = self._get_all_nodes(children)
            nodes.extend(sub_children)

        if node is self.Root:
            nodes.append(node)
        return nodes

    def add_level_to_nodes(self):
        self._add_level_to_nodes(self.Root, 1)

    def _add_level_to_nodes(self, node, level):
        if node is self.Root:
            node.Level = level

        for children in node.Children[:]:
            children.Level = level + 1
            self._add_level_to_nodes(children, level + 1)
