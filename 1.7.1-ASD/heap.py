class Heap:
    def __init__(self):
        self.HeapArray = []

    def MakeHeap(self, array: list, depth: int):
        self.HeapArray = [None] * self._calculate_depth(depth)
        for key in array:
            self.Add(key)

    def GetMax(self):
        node_index = self._find_free_place() - 1

        if node_index == - 1:
            return -1

        max = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[node_index]
        self.HeapArray[node_index] = None

        node_index = 0
        maximum_child_index = self._find_maximum_child_index(node_index)
        while maximum_child_index is not None and self.HeapArray[node_index] < self.HeapArray[maximum_child_index]:
            self._swap(node_index, maximum_child_index)
            node_index = maximum_child_index
            maximum_child_index = self._find_maximum_child_index(node_index)

        return max

    def Add(self, key: int) -> bool:
        node_index = self._find_free_place()
        if node_index is None:
            return False

        self.HeapArray[node_index] = key

        if node_index == 0:
            return True

        parent_index = self._find_parent_index(node_index)
        while parent_index >= 0 and self.HeapArray[node_index] > self.HeapArray[parent_index]:
            self._swap(node_index, parent_index)
            node_index = parent_index
            parent_index = self._find_parent_index(node_index)

        return True

    def _find_parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2

    def _find_left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1

    def _find_right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2

    def _calculate_depth(self, depth: int) -> int:
        return 2 ** (depth + 1) - 1

    def _find_free_place(self):
        try:
            return self.HeapArray.index(None)
        except:
            return None

    def _swap(self, first_index: int, second_index: int):
        self.HeapArray[first_index], self.HeapArray[second_index] = (
            self.HeapArray[second_index], self.HeapArray[first_index])

    def _find_maximum_child_index(self, parent_index: int):
        left_child_index = self._find_left_child_index(parent_index)
        left_child = self.HeapArray[left_child_index]

        right_child_index = self._find_right_child_index(parent_index)
        right_child = self.HeapArray[right_child_index]

        if left_child is not None and right_child is not None:
            if left_child > right_child:
                return left_child_index
            return right_child_index

        if left_child is not None and right_child is None:
            return left_child_index

        if left_child is None and right_child is not None:
            return right_child_index

        return None
