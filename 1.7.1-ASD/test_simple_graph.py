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

    def test_depth_first_search(self):
        graph = SimpleGraph(10)
        a = 0
        b = 1
        c = 2
        d = 3
        e = 4
        graph.AddVertex(a)
        graph.AddVertex(b)
        graph.AddVertex(c)
        graph.AddVertex(d)
        graph.AddVertex(e)

        graph.AddEdge(a, b)
        graph.AddEdge(a, c)
        graph.AddEdge(a, d)
        graph.AddEdge(b, d)
        graph.AddEdge(b, e)
        graph.AddEdge(d, e)

        self.assertEqual([graph.vertex[a], graph.vertex[b]], graph.DepthFirstSearch(a, b))
        self.assertEqual([graph.vertex[a], graph.vertex[c]], graph.DepthFirstSearch(a, c))
        self.assertEqual([graph.vertex[a], graph.vertex[d]], graph.DepthFirstSearch(a, d))
        self.assertEqual([graph.vertex[a], graph.vertex[b], graph.vertex[e]], graph.DepthFirstSearch(a, e))

        f = 5
        graph.AddVertex(f)
        graph.AddEdge(d, f)
        self.assertEqual([graph.vertex[a], graph.vertex[b], graph.vertex[d], graph.vertex[f]],
                         graph.DepthFirstSearch(a, f))

        g = 6
        graph.AddVertex(g)
        self.assertEqual([], graph.DepthFirstSearch(a, g))

        graph.AddEdge(c, g)
        self.assertEqual([graph.vertex[a], graph.vertex[c], graph.vertex[g]], graph.DepthFirstSearch(a, g))

    def test_breadth_first_search(self):
        graph = SimpleGraph(10)

        a = 0
        b = 1
        c = 2
        d = 3
        e = 4
        graph.AddVertex(a)
        graph.AddVertex(b)
        graph.AddVertex(c)
        graph.AddVertex(d)
        graph.AddVertex(e)

        graph.AddEdge(a, b)
        graph.AddEdge(a, c)
        graph.AddEdge(a, d)
        graph.AddEdge(b, d)
        graph.AddEdge(d, e)

        self.assertEqual([graph.vertex[a], graph.vertex[b]], graph.BreadthFirstSearch(a, b))
        self.assertEqual([graph.vertex[a], graph.vertex[c]], graph.BreadthFirstSearch(a, c))
        self.assertEqual([graph.vertex[a], graph.vertex[d]], graph.BreadthFirstSearch(a, d))
        self.assertEqual([graph.vertex[a], graph.vertex[d], graph.vertex[e]], graph.BreadthFirstSearch(a, e))

        f = 5
        graph.AddVertex(f)
        graph.AddEdge(d, f)
        self.assertEqual([graph.vertex[a], graph.vertex[d], graph.vertex[f]], graph.BreadthFirstSearch(a, f))

        g = 6
        graph.AddVertex(g)
        self.assertEqual([], graph.BreadthFirstSearch(a, g))

        graph.AddEdge(c, g)
        self.assertEqual([graph.vertex[a], graph.vertex[c], graph.vertex[g]], graph.BreadthFirstSearch(a, g))

    def test_weak_vertices(self):
        graph = SimpleGraph(10)

        a1 = 0
        a2 = 1
        a3 = 2
        a4 = 3
        a5 = 4
        a6 = 5
        a7 = 6
        a8 = 7
        a0 = 8

        self.assertEqual([], graph.WeakVertices())
        graph.AddVertex(a1)
        self.assertEqual([graph.vertex[a1]], graph.WeakVertices())
        graph.AddVertex(a2)
        self.assertEqual([graph.vertex[a1], graph.vertex[a2]], graph.WeakVertices())
        graph.AddEdge(a1, a2)
        self.assertEqual([graph.vertex[a1], graph.vertex[a2]], graph.WeakVertices())
        graph.AddVertex(a3)
        graph.AddEdge(a1, a3)
        self.assertEqual([graph.vertex[a1], graph.vertex[a2], graph.vertex[a3]], graph.WeakVertices())
        graph.AddEdge(a2, a3)
        self.assertEqual([], graph.WeakVertices())
        graph.AddVertex(a4)
        graph.AddEdge(a2, a4)
        self.assertEqual([graph.vertex[a4]], graph.WeakVertices())
        graph.AddEdge(a3, a4)
        self.assertEqual([], graph.WeakVertices())
        graph.AddVertex(a5)
        graph.AddEdge(a1, a5)
        self.assertEqual([graph.vertex[a5]], graph.WeakVertices())
        graph.AddVertex(a6)
        graph.AddEdge(a3, a6)
        self.assertEqual([graph.vertex[a5], graph.vertex[a6]], graph.WeakVertices())
        graph.AddEdge(a5, a6)
        self.assertEqual([graph.vertex[a5], graph.vertex[a6]], graph.WeakVertices())
        graph.AddVertex(a7)
        graph.AddEdge(a6, a7)
        self.assertEqual([graph.vertex[a5], graph.vertex[a6], graph.vertex[a7]], graph.WeakVertices())
        graph.AddVertex(a8)
        graph.AddEdge(a6, a8)
        self.assertEqual([graph.vertex[a5], graph.vertex[a6], graph.vertex[a7], graph.vertex[a8]], graph.WeakVertices())
        graph.AddEdge(a7, a8)
        self.assertEqual([graph.vertex[a5]], graph.WeakVertices())
        graph.AddVertex(a0)
        graph.AddEdge(a8, a0)
        self.assertEqual([graph.vertex[a5], graph.vertex[a0]], graph.WeakVertices())
