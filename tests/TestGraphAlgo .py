import math
from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class MyTestCase(TestCase):

    def graph1(self) -> DiGraph:
        g1 = DiGraph()  # creates an empty directed graph
        for n in range(3):
            g1.add_node(n)

        g1.add_edge(0, 1, 3)
        g1.add_edge(1, 2, 4)
        g1.add_edge(2, 0, 5)

        return g1

    def graph2(self):
        g2 = DiGraph()  # creates an empty directed graph
        for n in range(8):
            g2.add_node(n)

        g2.add_edge(0, 1, 10)
        g2.add_edge(1, 5, 8)
        g2.add_edge(2, 1, 2)
        g2.add_edge(3, 2, 2)
        g2.add_edge(3, 1, 5)
        g2.add_edge(4, 0, 11)
        g2.add_edge(1, 4, 4)
        g2.add_edge(7, 4, 4)
        g2.add_edge(5, 6, 9)

        return g2

    def graph3(self):
        g3 = DiGraph()  # creates an empty directed graph
        for n in range(14):
            g3.add_node(n)

        g3.add_edge(0, 3, 4)
        g3.add_edge(1, 0, 6)
        g3.add_edge(1, 5, 20)
        g3.add_edge(1, 8, 19)
        g3.add_edge(1, 11, 25)
        g3.add_edge(2, 13, 11)
        g3.add_edge(3, 1, 11)
        #
        g3.add_edge(3, 10, 17)
        #
        g3.add_edge(4, 1, 20)
        g3.add_edge(4, 5, 6)
        g3.add_edge(5, 4, 4)
        #
        g3.add_edge(6, 1, 5)
        #
        g3.add_edge(6, 7, 8)
        g3.add_edge(7, 6, 8)
        #
        g3.add_edge(8, 7, 15)
        #
        g3.add_edge(9, 11, 10)
        g3.add_edge(9, 12, 7)
        g3.add_edge(10, 6, 5)
        g3.add_edge(10, 9, 6)
        g3.add_edge(11, 13, 23)
        g3.add_edge(12, 2, 10)
        g3.add_edge(13, 8, 29)

        return g3

    def test_short_path(self):

        g = GraphAlgo(self.graph1())
        self.assertEqual(g.shortest_path(0, 2), (7, [0, 1, 2]))
        self.assertEqual(g.shortest_path(1, 2), (4, [1, 2]))
        self.assertEqual(g.shortest_path(2, 2), (0, [2]))
        self.assertEqual(g.shortest_path(0, 1), (3, [0, 1]))
        self.assertEqual(g.shortest_path(1, 1), (0, [1]))
        self.assertEqual(g.shortest_path(2, 1), (8, [2, 0, 1]))
        self.assertEqual(g.shortest_path(0, 0), (0, [0]))
        self.assertEqual(g.shortest_path(1, 0), (9, [1, 2, 0]))
        self.assertEqual(g.shortest_path(2, 0), (5, [2, 0]))

        g = GraphAlgo(self.graph2())
        self.assertEqual(g.shortest_path(0, 4), (14, [0, 1, 4]))
        self.assertEqual(g.shortest_path(1, 6), (17, [1, 5, 6]))
        self.assertEqual(g.shortest_path(5, 2), (math.inf, []))
        self.assertEqual(g.shortest_path(3, 4), (8, [3, 2, 1, 4]))
        self.assertEqual(g.shortest_path(2, 5), (10, [2, 1, 5]))
        self.assertEqual(g.shortest_path(6, 4), (math.inf, []))

        g = GraphAlgo(self.graph3())
        self.assertEqual(g.shortest_path(0, 7), (34, [0, 3, 10, 6, 7]))
        self.assertEqual(g.shortest_path(7, 12), (53, [7, 6, 1, 0, 3, 10, 9, 12]))
        self.assertEqual(g.shortest_path(13, 6), (52, [13, 8, 7, 6]))
        self.assertEqual(g.shortest_path(4, 5), (6, [4, 5]))
        self.assertEqual(g.shortest_path(2, 0), (74, [2, 13, 8, 7, 6, 1, 0]))
        self.assertEqual(g.shortest_path(9, 10), (112, [9, 12, 2, 13, 8, 7, 6, 1, 0, 3, 10]))
        self.assertEqual(g.shortest_path(10, 4), (34, [10, 6, 1, 5, 4]))

    def test_center(self):
        g = GraphAlgo(self.graph1())
        self.assertEqual(g.centerPoint(), (0, 7))
        g = GraphAlgo(self.graph2())
        self.assertEqual(g.centerPoint(), (None, float("inf")))
        g = GraphAlgo(self.graph3())
        self.assertEqual(g.centerPoint(), (10, 34))

    def test_tsp(self):
        g = GraphAlgo(self.graph1())
        self.assertEqual(g.TSP([0, 2]), ([2, 0], 5))
        g = GraphAlgo(self.graph2())
        self.assertEqual(g.TSP([0, 2]), ([2, 1, 4, 0], 17))
        self.assertEqual(g.TSP([1, 3, 6, 2]), ([3, 2, 1, 5, 6], 21))
        g = GraphAlgo(self.graph3())
        self.assertEqual(g.TSP([9, 7, 11, 5]), ([7, 6, 1, 5, 4, 1, 0, 3, 10, 9, 11], 100))
        self.assertEqual(g.TSP([0, 1, 10, 2, 8, 4]), ([10, 6, 1, 5, 4, 1, 0, 3, 10, 9, 12, 2, 13, 8], 144))

    def test_connect(self):
        g = GraphAlgo(self.graph1())
        self.assertEqual(g.is_connected(), True)
        g = GraphAlgo(self.graph2())
        self.assertEqual(g.is_connected(), False)
        g = GraphAlgo(self.graph3())
        self.assertEqual(g.is_connected(), True)

