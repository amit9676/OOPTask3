class DistanceReturnedData:
    def __init__(self, distance: float):
        self.__distance = distance
        self.__path = []

    def get_distance(self) -> float:
        return self.__distance

    def add_node_to_list(self, index, node):
        self.__path.insert(index, node)

    def get_path(self):
        if self.__path is None:
            return None
        return self.__path.copy()

    def nullify(self):
        self.__path = None
