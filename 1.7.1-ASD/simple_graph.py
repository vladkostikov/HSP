class Queue:
    def __init__(self):
        self.data = LinkedList()

    def enqueue(self, item):
        self.data.add_in_tail(Node(item))
        return self.data.last().value

    def dequeue(self):
        node = self.data.delete_from_head()
        if node is None:
            return None
        return node.value

    def size(self) -> int:
        return self.data.len()


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
        self._reset_vertex_visits()
        return self._depth_first_search([], VFrom, VTo)

    def BreadthFirstSearch(self, VFrom: int, VTo: int) -> list:
        self._reset_vertex_visits()

        current_vertex = self.vertex[VFrom]
        current_vertex.Hit = True
        levels = {}
        self._add_vertex_to_levels(levels, 0, current_vertex)

        queue = Queue()
        self._breadth_first_search(queue, levels, 1, VFrom, VTo)

        shortest_way = self._find_shortest_way(levels)
        return shortest_way

    def _breadth_first_search(self, queue: Queue, levels: dict, level: int, VFrom: int, VTo: int) -> list:
        for vertex_index, edge in enumerate(self.m_adjacency[VFrom]):
            if edge and self.vertex[vertex_index].Hit is False:
                current_vertex = self.vertex[vertex_index]
                queue.enqueue(current_vertex)
                self._add_vertex_to_levels(levels, level, current_vertex)
                if vertex_index == VTo:
                    return queue

                current_vertex.Hit = True

        if queue.size() == 0:
            return queue

        current_vertex = queue.dequeue()
        current_vertex_index = self._find_vertex_index(current_vertex)
        new_level = self._find_vertex_level(levels, current_vertex) + 1
        self._breadth_first_search(queue, levels, new_level, current_vertex_index, VTo)

    def _reset_vertex_visits(self):
        for vertex in self.vertex:
            if type(vertex) is Vertex:
                vertex.Hit = False

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
        except ValueError:
            return None

    def _find_vertex_index(self, vertex: Vertex) -> int:
        return self.vertex.index(vertex)

    def _add_vertex_to_levels(self, levels: dict, level: int, vertex: Vertex):
        if level not in levels:
            levels[level] = []
        levels[level].append(vertex)

    def _find_vertex_level(self, levels: dict, vertex: Vertex):
        for level in levels:
            if vertex in levels[level]:
                return level
        return None

    def _find_shortest_way(self, levels: dict) -> list:
        level_keys = list(reversed(levels.keys()))
        shortest_way_indexes = [self._find_vertex_index(vertex) for vertex in levels[level_keys[0]] if vertex.Hit is False]

        if len(shortest_way_indexes) != 1:
            return []

        for level in level_keys[1:]:
            for vertex in levels[level]:
                vertex_index = self._find_vertex_index(vertex)
                if self.IsEdge(vertex_index, shortest_way_indexes[-1]):
                    shortest_way_indexes.append(vertex_index)
                    break

        shortest_way = list(reversed([self.vertex[vertex_index] for vertex_index in shortest_way_indexes]))
        return shortest_way


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class DummyNode(Node):
    def __init__(self):
        super().__init__(None)


class LinkedList:
    def __init__(self):
        self.head = DummyNode()
        self.tail = self.head
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def add_in_tail(self, item):
        self.tail.prev.next = item
        item.prev = self.tail.prev
        item.next = self.tail
        self.tail.prev = item
        self.length += 1
        return None

    def delete_from_head(self):
        node = self.head.next
        if type(node) is Node:
            self.head.next = node.next
            node.next.prev = self.head
            self.length -= 1
            return node
        return None

    def len(self) -> int:
        return self.length

    def last(self):
        node = self.tail.prev
        if type(node) is Node:
            return node
        return None
