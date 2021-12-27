from unittest import TestCase

from src.NodeData import NodeData

g1 = NodeData(0, "not visited!", 0, (1, -1, 0), 0)
g2 = NodeData(1, "not visited!", 0, (1, 1, 0), 0)
g3 = NodeData(2, "not visited!", 0, (-1, -1, 0), 0)
g4 = NodeData(3, "not visited!", 0, (-1, 1, 0), 0)
list_node1 = [g1, g2, g3, g4]
list_node2 = [g1, g2, g3, g4]


# noinspection DuplicatedCode
class TestNodeData(TestCase):
    def test_set_key(self):
        list_node1[0].set_key(5)
        list_node1[1].set_key(4)
        list_node1[2].set_key(3)
        list_node1[3].set_key(2)
        self.assertEqual(5, list_node1[0].get_key())
        self.assertEqual(4, list_node1[1].get_key())
        self.assertEqual(3, list_node1[2].get_key())
        self.assertEqual(2, list_node1[3].get_key())
        list_node1[0].set_key(0)
        list_node1[1].set_key(1)
        list_node1[2].set_key(2)
        list_node1[3].set_key(3)
        self.assertEqual(0, list_node1[0].get_key())
        self.assertEqual(1, list_node1[1].get_key())
        self.assertEqual(2, list_node1[2].get_key())
        self.assertEqual(3, list_node1[3].get_key())

    def test_get_key(self):
        self.assertEqual(0, list_node2[0].get_key())
        self.assertEqual(1, list_node2[1].get_key())
        self.assertEqual(2, list_node2[2].get_key())
        self.assertEqual(3, list_node2[3].get_key())

    def test_set_info(self):
        list_node1[0].set_info("visited!")
        list_node1[1].set_info("visited!")
        list_node1[2].set_info("visited!")
        list_node1[3].set_info("visited!")
        self.assertEqual("visited!", list_node1[0].get_info())
        self.assertEqual("visited!", list_node1[1].get_info())
        self.assertEqual("visited!", list_node1[2].get_info())
        self.assertEqual("visited!", list_node1[3].get_info())
        list_node1[0].set_info("not visited!")
        list_node1[1].set_info("not visited!")
        list_node1[2].set_info("not visited!")
        list_node1[3].set_info("not visited!")
        self.assertEqual("not visited!", list_node1[0].get_info())
        self.assertEqual("not visited!", list_node1[1].get_info())
        self.assertEqual("not visited!", list_node1[2].get_info())
        self.assertEqual("not visited!", list_node1[3].get_info())

    def test_get_info(self):
        self.assertEqual("not visited!", list_node1[0].get_info())
        self.assertEqual("not visited!", list_node1[1].get_info())
        self.assertEqual("not visited!", list_node1[2].get_info())
        self.assertEqual("not visited!", list_node1[3].get_info())

    def test_set_tag(self):
        list_node1[0].set_tag(1)
        list_node1[1].set_tag(1)
        list_node1[2].set_tag(1)
        list_node1[3].set_tag(1)
        self.assertEqual(1, list_node1[0].get_tag())
        self.assertEqual(1, list_node1[1].get_tag())
        self.assertEqual(1, list_node1[2].get_tag())
        self.assertEqual(1, list_node1[3].get_tag())
        list_node1[0].set_tag(0)
        list_node1[1].set_tag(0)
        list_node1[2].set_tag(0)
        list_node1[3].set_tag(0)
        self.assertEqual(0, list_node1[0].get_tag())
        self.assertEqual(0, list_node1[1].get_tag())
        self.assertEqual(0, list_node1[2].get_tag())
        self.assertEqual(0, list_node1[3].get_tag())

    def test_get_tag(self):
        self.assertEqual(0, list_node1[0].get_tag())
        self.assertEqual(0, list_node1[1].get_tag())
        self.assertEqual(0, list_node1[2].get_tag())
        self.assertEqual(0, list_node1[3].get_tag())

    def test_set_location(self):
        list_node1[0].set_location((1, 1, 0))
        list_node1[1].set_location((2, 2, 0))
        list_node1[2].set_location((3, 3, 0))
        list_node1[3].set_location((4, 4, 0))
        self.assertEqual((1, 1, 0), list_node1[0].get_location())
        self.assertEqual((2, 2, 0), list_node1[1].get_location())
        self.assertEqual((3, 3, 0), list_node1[2].get_location())
        self.assertEqual((4, 4, 0), list_node1[3].get_location())
        list_node1[0].set_location((0, 0, 0))
        list_node1[1].set_location((0, 0, 0))
        list_node1[2].set_location((0, 0, 0))
        list_node1[3].set_location((0, 0, 0))
        self.assertEqual((0, 0, 0), list_node1[0].get_location())
        self.assertEqual((0, 0, 0), list_node1[1].get_location())
        self.assertEqual((0, 0, 0), list_node1[2].get_location())
        self.assertEqual((0, 0, 0), list_node1[3].get_location())

    def test_get_location(self):
        self.assertEqual((1, -1, 0), list_node1[0].get_location())
        self.assertEqual((1, 1, 0), list_node1[1].get_location())
        self.assertEqual((-1, -1, 0), list_node1[2].get_location())
        self.assertEqual((-1, 1, 0), list_node1[3].get_location())

    def test_set_weight(self):
        list_node1[0].set_weight(1)
        list_node1[1].set_weight(2)
        list_node1[2].set_weight(3)
        list_node1[3].set_weight(4)
        self.assertEqual(1, list_node1[0].get_weight())
        self.assertEqual(2, list_node1[1].get_weight())
        self.assertEqual(3, list_node1[2].get_weight())
        self.assertEqual(4, list_node1[3].get_weight())
        list_node1[0].set_weight(0)
        list_node1[1].set_weight(0)
        list_node1[2].set_weight(0)
        list_node1[3].set_weight(0)
        self.assertEqual(0, list_node1[0].get_weight())
        self.assertEqual(0, list_node1[1].get_weight())
        self.assertEqual(0, list_node1[2].get_weight())
        self.assertEqual(0, list_node1[3].get_weight())

    def test_get_weight(self):
        self.assertEqual(0, list_node1[0].get_weight())
        self.assertEqual(0, list_node1[1].get_weight())
        self.assertEqual(0, list_node1[2].get_weight())
        self.assertEqual(0, list_node1[3].get_weight())
