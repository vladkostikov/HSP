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
