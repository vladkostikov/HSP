class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None

    def is_leaf(self) -> bool:
        return self.LeftChild is None and self.RightChild is None

    def has_child(self) -> bool:
        return (self.LeftChild is not None and self.RightChild is None) or (
                    self.LeftChild is None and self.RightChild is not None)

    def has_two_child(self) -> bool:
        return self.LeftChild is not None and self.RightChild is not None

    def delete_child(self, node_to_delete) -> bool:
        if self.LeftChild is node_to_delete:
            self.LeftChild = None
            return True
        if self.RightChild is node_to_delete:
            self.RightChild = None
            return True
        return False


class BSTFind:
    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:
    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key) -> BSTFind:
        found = BSTFind()
        if self.Root is None:
            return found

        node = self.Root
        while node.NodeKey != key:
            if key < node.NodeKey and node.LeftChild is not None:
                node = node.LeftChild
            elif key > node.NodeKey and node.RightChild is not None:
                node = node.RightChild
            else:
                break

        found.Node = node
        if node.NodeKey == key:
            found.NodeHasKey = True
        elif key < node.NodeKey:
            found.ToLeft = True

        return found

    def AddKeyValue(self, key, val) -> bool:
        found = self.FindNodeByKey(key)

        if found.NodeHasKey:
            return False  # если ключ уже есть

        if found.Node is None:
            self.Root = BSTNode(key, val, None)
            return True

        parent = found.Node
        if found.ToLeft:
            parent.LeftChild = BSTNode(key, val, parent)
        else:
            parent.RightChild = BSTNode(key, val, parent)
        return True

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool) -> BSTNode:
        if FindMax:
            return self._find_max(FromNode)
        return self._find_min(FromNode)

    def DeleteNodeByKey(self, key) -> bool:
        found_node_to_delete = self.FindNodeByKey(key)
        if not found_node_to_delete.NodeHasKey:
            return False

        node_to_delete = found_node_to_delete.Node

        # Удаление узла без потомков.
        if node_to_delete.is_leaf():
            return self._delete_leaf(node_to_delete)

        # Удаление узла с одним потомком.
        if node_to_delete.has_child():
            return self._delete_node_with_one_child(node_to_delete)

        # Удаление узла с двумя потомками.
        if node_to_delete.has_two_child():
            return self._delete_node_with_two_child(node_to_delete)

        return False

    def Count(self) -> int:
        return self._count(self.Root)

    def _count(self, node) -> int:
        if node is None:
            return 0
        return 1 + self._count(node.LeftChild) + self._count(node.RightChild)

    def _find_min(self, FromNode: BSTNode) -> BSTNode:
        node = FromNode
        while node.LeftChild is not None:
            node = node.LeftChild
        return node

    def _find_max(self, FromNode: BSTNode) -> BSTNode:
        node = FromNode
        while node.RightChild is not None:
            node = node.RightChild
        return node

    def _delete_leaf(self, node: BSTNode) -> bool:
        parent = node.Parent
        return parent.delete_child(node)

    def _delete_node_with_one_child(self, node: BSTNode) -> bool:
        if node.LeftChild is not None:
            successor_node = node.LeftChild
        else:
            successor_node = node.RightChild

        parent = node.Parent
        if node is parent.LeftChild:
            parent.LeftChild = successor_node
            successor_node.Parent = parent.LeftChild
        else:
            parent.RightChild = successor_node
            successor_node.Parent = parent.RightChild
        return True

    def _delete_node_with_two_child(self, node: BSTNode) -> bool:
        successor_node = self.FinMinMax(node.RightChild, False)
        parent = node.Parent
        if successor_node.is_leaf():
            successor_node.Parent.LeftChild = None
            successor_node.Parent = parent

        if not successor_node.is_leaf():
            successor_node.Parent.LeftChild = successor_node.RightChild
            successor_node.Parent = parent
            successor_node.RightChild.Parent = successor_node.Parent

        successor_node.LeftChild = node.LeftChild
        successor_node.LeftChild.Parent = successor_node
        successor_node.RightChild = node.RightChild
        successor_node.RightChild.Parent = successor_node
        if node is parent.LeftChild:
            parent.LeftChild = successor_node
        if node is parent.RightChild:
            parent.RightChild = successor_node
        return True
