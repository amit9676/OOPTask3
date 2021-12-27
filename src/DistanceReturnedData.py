
class DistanceReturnedData:
    def __init__(self, distance: float):
        self.__distance = distance
        self.__path = []

    def getDistance(self) -> float:
        return self.__distance

    def addNodeToList(self, index, node):
        self.__path.insert(index,node)

    def getPath(self):
        if(self.__path == None):
            return None
        return self.__path.copy()
    def nullify(self):
        self.__path = None
