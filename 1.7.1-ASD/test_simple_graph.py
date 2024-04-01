from unittest import TestCase
from simple_graph import SimpleGraph
from simple_graph import Vertex


class TestSimpleGraph(TestCase):
    def test_add_vertex(self):
        graph = SimpleGraph(10)
        self.assertEqual(10, graph.max_vertex)
        self.assertEqual(10, len(graph.vertex))
        self.assertEqual(10, len(graph.m_adjacency))

        graph.AddVertex(100)
        self.assertTrue(type(graph.vertex[0]) is Vertex)
        self.assertEqual(100, graph.vertex[0].Value)
        self.assertTrue(1 not in graph.m_adjacency[0])

        graph.AddVertex(200)
        self.assertTrue(type(graph.vertex[1]) is Vertex)
        self.assertEqual(200, graph.vertex[1].Value)
        self.assertTrue(1 not in graph.m_adjacency[1])

    def test_remove_vertex(self):
        graph = SimpleGraph(10)
        graph.AddVertex(100)
        graph.AddVertex(200)
        graph.AddVertex(300)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        self.assertTrue(graph.IsEdge(0, 1))
        self.assertTrue(graph.IsEdge(0, 2))

        graph.RemoveVertex(0)
        self.assertIsNone(graph.vertex[0])
        self.assertFalse(graph.IsEdge(0, 1))
        self.assertFalse(graph.IsEdge(0, 2))
        self.assertEqual(0, graph.m_adjacency[0][1])
        self.assertEqual(0, graph.m_adjacency[0][2])
        self.assertEqual(0, graph.m_adjacency[1][0])
        self.assertEqual(0, graph.m_adjacency[2][0])

    def test_is_edge(self):
        graph = SimpleGraph(10)
        graph.AddVertex(100)
        graph.AddVertex(200)
        graph.AddVertex(300)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)

        self.assertTrue(graph.IsEdge(0, 1))
        self.assertTrue(graph.IsEdge(1, 0))

        self.assertTrue(graph.IsEdge(0, 2))
        self.assertTrue(graph.IsEdge(2, 0))

        self.assertFalse(graph.IsEdge(1, 2))
        self.assertFalse(graph.IsEdge(2, 1))

        self.assertFalse(graph.IsEdge(0, 3))
        self.assertFalse(graph.IsEdge(3, 0))

        self.assertFalse(graph.IsEdge(3, 4))
        self.assertFalse(graph.IsEdge(4, 3))

    def test_add_edge(self):
        graph = SimpleGraph(10)
        graph.AddVertex(100)
        graph.AddVertex(200)
        graph.AddVertex(300)

        graph.AddEdge(0, 1)
        self.assertEqual(1, graph.m_adjacency[0][1])
        self.assertEqual(1, graph.m_adjacency[1][0])

        graph.AddEdge(0, 1)
        self.assertEqual(1, graph.m_adjacency[0][1])
        self.assertEqual(1, graph.m_adjacency[1][0])

        graph.AddEdge(0, 2)
        self.assertEqual(1, graph.m_adjacency[0][2])
        self.assertEqual(1, graph.m_adjacency[2][0])

        graph.AddEdge(1, 2)
        self.assertEqual(1, graph.m_adjacency[1][2])
        self.assertEqual(1, graph.m_adjacency[2][1])

    def test_remove_edge(self):
        graph = SimpleGraph(10)
        graph.AddVertex(100)
        graph.AddVertex(200)
        graph.AddVertex(300)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(1, 2)

        graph.RemoveEdge(0, 1)
        self.assertEqual(0, graph.m_adjacency[0][1])
        self.assertEqual(0, graph.m_adjacency[1][0])

        graph.RemoveEdge(0, 2)
        self.assertEqual(0, graph.m_adjacency[0][2])
        self.assertEqual(0, graph.m_adjacency[2][0])

        graph.RemoveEdge(1, 2)
        self.assertEqual(0, graph.m_adjacency[1][2])
        self.assertEqual(0, graph.m_adjacency[2][1])
