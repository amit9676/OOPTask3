from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


class DiGraph(GraphInterface):
    """This class represent directed weighted graph
    That possible different actions on the graph, node and edge
    Vertices - contains all the nodes in the graph using dictionary.
    neighborsOut - Dictionary that contains a dictionary of key (the key of the destination node) and a value that represents the weight of the edge by the key of the source node
    neighborsIn -Dictionary that contains a dictionary of key (the key of the source node) and a value that represents the weight of the edge by the key of the destination node
    MC- Represents the number of changes made to the graph (adding a vertex and more ..).
    edgeSize- Contains the number of edges in the graph"""

    def __init__(self):
        """
        A constructor that sets default values for a graph.
        """
        self.vertices: {int, NodeData} = dict()
        self.neighborsOut: {int, {int, float}} = dict()
        self.neighborsIn: {int, {int, float}} = dict()
        self.__MC = 0
        self.__edgeSize = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self.vertices)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.__edgeSize

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """
        return self.vertices

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        return self.neighborsIn.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        return self.neighborsOut.get(id1)

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.__MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if weight <= 0:
            return False
        if id1 == id2:
            return False

        if self.vertices.get(id1) is None or self.vertices.get(id2) is None:
            return False

        if id2 in self.neighborsOut.get(id1):
            return False

        self.neighborsOut[id1][id2] = weight
        self.neighborsIn[id2][id1] = weight
        self.__edgeSize += 1
        self.__MC += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """

        if self.vertices.get(node_id) is not None:
            return False

        self.vertices[node_id] = NodeData(key=node_id, location=pos)
        self.neighborsIn[node_id] = {}
        self.neighborsOut[node_id] = {}
        self.__MC += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        if node_id in self.vertices:
            edge_from_node = len(self.neighborsOut.get(node_id))
            edge_to_node = len(self.neighborsIn.get(node_id))
            self.__edgeSize -= edge_from_node + edge_to_node
            self.neighborsOut.pop(node_id)
            self.neighborsIn.pop(node_id)
            self.vertices.pop(node_id)
            self.__MC += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        if node_id1 in self.vertices and node_id2 in self.vertices:
            if self.neighborsOut.get(node_id1) is None or self.neighborsOut.get(node_id1).get(node_id2) is None:
                return False
            self.__edgeSize -= 1
            self.__MC += 1
            self.neighborsOut.get(node_id1).pop(node_id2)
            self.neighborsIn.get(node_id2).pop(node_id1)
            return True
        return False

    def get_node(self, id1: int) -> NodeData:
        return self.vertices.get(id1)

    def get_edge(self, src: int, index: int) -> dict:
        return {
            list(self.all_out_edges_of_node(src).keys())[index]: list(self.all_out_edges_of_node(src).values())[index]}
