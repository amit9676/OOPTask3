class NodeData:
    """this class represents the set of operations applicable on a node (vertex) in a (directional) weighted graph.
    The node in the graph consists of five things:
    key - Unique ID of the node in graph
    info- Contains some characteristic of the node such as color and more .. In this project it stores the parent node.
    tag-Temporal data which can be used be algorithms.
    location- location of this node.
    weight- Weight of the node."""

    def __init__(self, key: int = 0, info: str = "", tag: int = 0, location: tuple = None, weight: float = 0):
        """
        Constructor of a node in graph
        :param key:
        :param info:
        :param tag:
        :param location:
        :param weight:
        """
        self.__key = key
        self.__info = info
        self.__tag = tag
        self.__location = location
        self.__weight = weight

    def set_key(self, k: int):
        """
        Defines a unique ID for node
        :param k:
        """
        self.__key = k

    def get_key(self) -> int:
        """
        Return a unique ID of node
        :return: ID of node
        """
        return self.__key

    def set_info(self, i: str):
        """
        Defines an attribute for node
        :param i:
        """
        self.__info = i

    def get_info(self) -> str:
        """
        Return an attribute of node
        :return:  attribute of node
        """
        return self.__info

    def set_tag(self, t: int):
        """
        Defines temporary data for node
        :param t:
        """
        self.__tag = t

    def get_tag(self) -> int:
        """
        Return temporary data of node
        :return: temporary data of node
        """
        return self.__tag

    def set_location(self, t: tuple = (0, 0, 0)):
        """
        Defines the location of a node
        :param t:
        :return: location of a node
        """
        self.__location = t

    def get_location(self) -> tuple:
        """
        Return the location of a node
        :return: location of a node
        """
        return self.__location

    def set_weight(self, w: float):
        """
        Defines weight for node
        :param w:
        """
        self.__weight = w

    def get_weight(self) -> float:
        """
        Return weight for node
        :return:weight for node
        """
        return self.__weight

    def __repr__(self):
        """
        Returns the node data in the graph
        :return: ode data in the graph
        """
        if self.__location is None:
            self.__location = (0, 0, 0)
        return "{" + f"\"pos\":\"{self.__location[0]},{self.__location[1]},{self.__location[2]}\",\"id\":{self.__key}" + "}"
