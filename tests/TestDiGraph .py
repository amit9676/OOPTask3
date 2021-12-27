from unittest import TestCase

from src.DiGraph import DiGraph


# noinspection DuplicatedCode
class TestDiGraph(TestCase):
    def test_v_size(self):
        g = DiGraph()
        self.assertEqual(g.v_size(), 0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(10)
        self.assertEqual(g.v_size(), 3)

    def test_e_size(self):
        g = DiGraph()
        g.add_node(node_id=1)
        g.add_node(node_id=2)
        self.assertEqual(0, g.e_size())
        g.add_edge(id1=1, id2=2, weight=4)
        self.assertEqual(1, g.e_size())

    def test_get_all_v(self):
        g = DiGraph()
        g.add_node(node_id=1)
        g.add_node(node_id=2)
        g.add_node(node_id=3)
        self.assertEqual({1, 2, 3}, g.get_all_v().keys())

    def test_all_in_edges_of_node(self):
        g1 = DiGraph()
        g1.add_node(node_id=1)
        g1.add_node(node_id=2)
        g1.add_node(node_id=3)
        g1.add_edge(2, 1, 6)
        g1.add_edge(1, 3, 4)
        g1.add_edge(3, 2, 7)
        self.assertEqual(6, g1.all_in_edges_of_node(1).get(2))
        self.assertEqual(7, g1.all_in_edges_of_node(2).get(3))
        self.assertEqual(4, g1.all_in_edges_of_node(3).get(1))

        g2 = DiGraph()
        g2.add_node(node_id=1)
        g2.add_node(node_id=2)
        g2.add_node(node_id=3)
        g2.add_node(node_id=4)
        g2.add_node(node_id=5)
        g2.add_edge(1, 2, 1)
        g2.add_edge(1, 3, 2)
        g2.add_edge(1, 4, 3)
        g2.add_edge(1, 5, 4)
        self.assertEqual({}, g2.all_in_edges_of_node(1))
        self.assertEqual(1, g2.all_in_edges_of_node(2).get(1))
        self.assertEqual(2, g2.all_in_edges_of_node(3).get(1))
        self.assertEqual(3, g2.all_in_edges_of_node(4).get(1))
        self.assertEqual(4, g2.all_in_edges_of_node(5).get(1))

    def test_all_out_edges_of_node(self):
        g3 = DiGraph()
        g3.add_node(node_id=1)
        g3.add_node(node_id=2)
        g3.add_node(node_id=3)
        g3.add_edge(1, 2, 6)
        g3.add_edge(1, 3, 7)
        self.assertEqual(6, g3.all_out_edges_of_node(1).get(2))
        self.assertEqual(7, g3.all_out_edges_of_node(1).get(3))

        g4 = DiGraph()
        g4.add_node(node_id=1)
        g4.add_node(node_id=2)
        g4.add_node(node_id=3)
        g4.add_node(node_id=4)
        g4.add_node(node_id=5)
        g4.add_edge(1, 2, 1)
        g4.add_edge(1, 3, 2)
        g4.add_edge(1, 4, 3)
        g4.add_edge(1, 5, 4)
        self.assertEqual(1, g4.all_in_edges_of_node(2).get(1))
        self.assertEqual(2, g4.all_in_edges_of_node(3).get(1))
        self.assertEqual(3, g4.all_in_edges_of_node(4).get(1))
        self.assertEqual(4, g4.all_in_edges_of_node(5).get(1))

    def test_get_mc(self):
        g = DiGraph()
        g.add_node(1, (1, 2, 0))
        g.add_node(2, (1, 5, 0))
        g.add_node(3, (5, 1, 0))
        g.add_edge(1, 2, 6)
        g.add_edge(1, 3, 7)
        g.add_edge(2, 3, 1.33)
        self.assertEqual(g.get_mc(), 6)

    def test_add_edge(self):
        g5 = DiGraph()
        g5.add_node(node_id=1)
        g5.add_node(node_id=2)
        g5.add_node(node_id=3)
        g5.add_edge(1, 2, 6)
        g5.add_edge(1, 3, 7)

        numin = 0
        print(g5.neighborsIn)
        print(g5.neighborsIn.values())
        for di in g5.neighborsIn:
            numin += len(g5.neighborsIn[di])
        self.assertEqual(2, numin)

        num_out = 0
        for di in g5.neighborsOut:
            num_out += len(g5.neighborsOut[di])
        self.assertEqual(2, num_out)

        g6 = DiGraph()
        g6.add_edge(0, 1, 1.33)
        self.assertEqual(g6.e_size(), 0)
        g6.add_node(0)
        g6.add_node(1, (1, 2, 0))
        g6.add_edge(0, 1, 12)
        g6.add_edge(0, 1, 12)
        g6.add_edge(1, 0, 12)
        g6.add_edge(1, 20, 12)
        self.assertEqual(g6.e_size(), 2)

    def test_add_node(self):
        g = DiGraph()
        self.assertEqual(g.v_size(), 0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(10)
        self.assertFalse(g.add_node(10))
        self.assertEqual(g.v_size(), 3)
        self.assertEqual(1, g.vertices.get(1).get_key())

    def test_remove_node(self):
        g8 = DiGraph()
        g8.add_node(node_id=1)
        g8.add_node(node_id=2)
        g8.add_node(node_id=3)
        g8.add_node(node_id=4)
        g8.add_node(node_id=5)
        g8.add_node(node_id=6)
        self.assertEqual(6, g8.v_size())
        g8.remove_node(1)
        g8.remove_node(3)
        g8.remove_node(5)
        self.assertEqual(3, g8.v_size())

    def test_remove_edge(self):
        g9 = DiGraph()
        g9.add_node(node_id=1)
        g9.add_node(node_id=2)
        g9.add_node(node_id=3)
        g9.add_node(node_id=4)
        g9.add_edge(1, 2, 32)
        g9.add_edge(2, 3, 32)
        g9.add_edge(3, 4, 32)
        self.assertEqual(3, g9.e_size())

        g9.remove_edge(3, 4)
        g9.remove_edge(2, 3)
        self.assertEqual(1, g9.e_size())
