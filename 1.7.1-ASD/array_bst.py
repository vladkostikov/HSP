class aBST:
    def __init__(self, depth: int):
        tree_size = self._calculate_tree_size(depth)
        self.Tree = [None] * tree_size

    def FindKeyIndex(self, key):
        index = 0
        while index < len(self.Tree):
            if key == self.Tree[index]:
                return index
            if self.Tree[index] is None:
                return -index
            if key < self.Tree[index]:
                index = self._find_left_child_index(index)
                continue
            if key > self.Tree[index]:
                index = self._find_right_child_index(index)

        return None

    def AddKey(self, key) -> int:
        index = self.FindKeyIndex(key)

        if index is None:
            return -1

        if index < 0:
            self.Tree[-index] = key
            return -index

        if index == 0 and self.Tree[index] is None:
            self.Tree[index] = key
            return index

        return index

    def _calculate_tree_size(self, depth: int) -> int:
        if depth < 0:
            return 0

        last_level = 2 ** depth
        previous_levels = last_level - 1
        return previous_levels + last_level

    def _find_parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2

    def _find_left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1

    def _find_right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2
