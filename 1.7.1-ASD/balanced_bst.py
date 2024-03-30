class BSTNode:
    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0

    def has_child(self) -> bool:
        return self.LeftChild is not None or self.RightChild is not None


class BalancedBST:
    def __init__(self):
        self.Root = None

    def GenerateTree(self, array: list):
        sorted_array = sorted(array)
        self._generate_tree(None, sorted_array)

    def IsBalanced(self, root_node: BSTNode) -> bool:
        if root_node.LeftChild is None and root_node.RightChild is None:
            return True

        if root_node.LeftChild is None and root_node.RightChild.has_child():
            return False
        if root_node.LeftChild is None and not root_node.RightChild.has_child():
            return True

        if root_node.RightChild is None and root_node.LeftChild.has_child():
            return False
        if root_node.RightChild is None and not root_node.LeftChild.has_child():
            return True

        return self.IsBalanced(root_node.LeftChild) and self.IsBalanced(root_node.RightChild)

    def _generate_tree(self, parent: BSTNode, sorted_array: list) -> BSTNode:
        center_index = len(sorted_array) // 2
        center_value = sorted_array[center_index]
        node = BSTNode(center_value, parent)

        if parent is None:
            self.Root = node
        if parent is not None:
            node.Level = node.Parent.Level + 1

        left_array = sorted_array[:center_index]
        if len(left_array) > 0:
            node.LeftChild = self._generate_tree(node, left_array)

        right_array = sorted_array[center_index + 1:]
        if len(right_array) > 0:
            node.RightChild = self._generate_tree(node, right_array)

        return node
