class Vertex:
    def __init__(self, value: int):
        self.Value = value


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

    def _find_free_index(self):
        try:
            return self.vertex.index(None)
        except:
            return None
