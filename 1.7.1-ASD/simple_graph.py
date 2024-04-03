class Vertex:
    def __init__(self, value: int):
        self.Value = value
        self.Hit = False


class SimpleGraph:

    def __init__(self, size: int):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v: int):
        index = self._find_free_index()

        if index is None:
            return

        self.vertex[index] = Vertex(v)

    def RemoveVertex(self, v: int):
        for vertex_index, edge in enumerate(self.m_adjacency[v]):
            if edge == 1:
                self.RemoveEdge(v, vertex_index)

        self.vertex[v] = None

    def IsEdge(self, v1: int, v2: int) -> bool:
        return self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1

    def AddEdge(self, v1: int, v2: int):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1: int, v2: int):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, VFrom: int, VTo: int) -> list:
        for vertex in self.vertex:
            if type(vertex) is Vertex:
                vertex.Hit = False

        return self._depth_first_search([], VFrom, VTo)

    def _depth_first_search(self, stack: list, VFrom: int, VTo: int) -> list:
        current_vertex = self.vertex[VFrom]
        current_vertex.Hit = True
        stack.append(current_vertex)

        found = self.IsEdge(VFrom, VTo)
        if found:
            stack.append(self.vertex[VTo])
            return stack

        for vertex_index, edge in enumerate(self.m_adjacency[VFrom]):
            if edge and self.vertex[vertex_index].Hit is False:
                result_stack = self._depth_first_search(stack, vertex_index, VTo)
                if len(result_stack) == 0 or result_stack[-1] is self.vertex[VTo]:
                    return result_stack

        stack.pop()
        return stack

    def _find_free_index(self):
        try:
            return self.vertex.index(None)
        except:
            return None
