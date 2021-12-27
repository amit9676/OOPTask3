import random
import matplotlib.pyplot as plt
from src import NodeData
from src.DiGraph import DiGraph


class Show_graph:
    WIDTH, HEIGHT = 800, 600

    def __init__(self, graph: DiGraph):
        self.pr_graph = graph

    def have_pos(self):
        """
        Checks if there is a vertex that does not have a pos
        :return: true or false
        """
        for v in self.pr_graph.vertices.values():
            if v.get_location() is None:
                self.random_pos(v)

    def random_pos(self, v: NodeData):
        """
        Grid numbers in a given area for the position of points in the graph
        """
        x = random.randint(31, 36)
        y = random.randint(31, 36)
        z = 0.0
        v.set_location((x, y, z))

    def paint(self):
        """
         This method draws the graph.
        """

        for src in self.pr_graph.vertices.values():
            pos = src.get_location()
            x = pos[0]
            y = pos[1]
            plt.plot(x, y, markersize=10, marker="o", color="blue")
            plt.text(x, y, str(src.get_key()), color="red", fontsize=12)
            for dest in self.pr_graph.all_out_edges_of_node(src.get_key()):
                pos_dest = self.pr_graph.vertices[dest].get_location()
                his_x = pos_dest[0]
                his_y = pos_dest[1]
                plt.annotate("", xy=(x, y), xytext=(his_x, his_y), arrowprops=dict(arrowstyle="->"))
        plt.show()


