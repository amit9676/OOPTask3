import json
import math
import sys
from src.DistanceReturnedData import DistanceReturnedData
from src.GraphAlgoInterface import GraphAlgoInterface
from typing import List
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from src.Show_graph import Show_graph
from src.minHeap_Aid import minHeap_Aid


class GraphAlgo(GraphAlgoInterface):
    """This class represents a Directed (positive) Weighted Graph Theory Algorithms including:
    0. __init__()
    1. get_graph(self)
    2. load_from_json(self, file_name: str)
    3. save_to_json(self, file_name: str)
    4. shortest_path(self, id1: int, id2: int)
    5. TSP(self, node_lst: List[int])
    6. centerPoint(self)
    7. plot_graph(self)
    graph-Is an abstract representation of a set of nodes and edge,
    each edge has a weight, it is possible to have a route from node to another node."""

    def __init__(self, graph: DiGraph = None):
        """
        Graph builder
        :param graph: graph
        """
        self.__graph = graph

    def get_graph(self) -> GraphInterface:
        return self.__graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        p = ""
        for i in range(-5, 0, 1):
            p += file_name[i]
        if p != ".json":
            file_name += ".json"

        self.__graph = DiGraph()
        try:
            with open(file_name, "r") as f:
                graph_dic = json.load(f)
                for vec in graph_dic["Nodes"]:
                    if "pos" in vec:
                        pos = []
                        for loc in vec['pos'].split(','):
                            pos.append(float(loc))
                        pos_t = (pos[0], pos[1], pos[2])
                        self.__graph.add_node(vec['id'], pos_t)
                    else:
                        self.__graph.add_node(vec['id'])

                for edge in graph_dic["Edges"]:
                    self.__graph.add_edge(edge['src'], edge['dest'], edge['w'])
            return True
        except IOError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        try:
            data = {"Edges": [], "Nodes": []}
            for nodes in self.__graph.get_all_v():
                p = list(self.__graph.get_all_v().values())[nodes]
                q = p.get_location()
                if q is not None:
                    dict1_to_save = {"pos": str(q[0]) + "," + str(q[1]) + "," + str(q[2]), "id": nodes}
                    data["Nodes"].append(dict1_to_save)
                else:
                    dict1_to_save = {"id": nodes}
                    data["Nodes"].append(dict1_to_save)

                for edgesPerNode in self.__graph.all_out_edges_of_node(nodes):
                    dict2_to_save = {"src": nodes, "w": self.__graph.all_out_edges_of_node(nodes)[edgesPerNode],
                                     "dest": edgesPerNode}
                    data["Edges"].append(dict2_to_save)
            with open(file_name, "w") as file:
                file.write(json.dumps(data))
                return True
        except IOError:
            return False

    def is_connected(self) -> bool:
        if self.__graph.v_size() == 0:
            return False
        original = self.__graph.get_all_v()
        if self.__BFS(original, self.__graph):
            g2 = DiGraph()
            for item in self.__graph.get_all_v():
                g2.add_node(item)
            for item in self.__graph.get_all_v():
                for item2 in self.__graph.all_in_edges_of_node(item):
                    g2.add_edge(item, item2, 1)
            if self.__BFS(original, g2):
                return True
        return False

    def __BFS(self, o, g: DiGraph) -> bool:
        qn = []
        if g.v_size() == 0:
            return False
        self.__set_to_zero_all(g.get_all_v(), g)
        v = g.get_all_v()
        start_node = None
        for item in v:
            start_node = g.get_node(item)
            break
        qn.append(start_node.get_key())
        while len(qn) > 0:

            out = qn.pop(0)
            neighbors = g.all_out_edges_of_node(out)
            if neighbors is None or len(neighbors) == 0:
                return False

            for item in neighbors:

                if g.get_node(item).get_tag() == 0:
                    qn.append(item)
                    g.get_node(item).set_tag(1)
        return self.__check_visited(v, g)

    def __set_to_zero_all(self, input, g: DiGraph):
        for item in input:
            g.get_node(item).set_tag(0)

    def __check_visited(self, input, g: DiGraph) -> bool:
        for item in input:
            if g.get_node(item).get_tag() == 0:
                return False
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        data = self.__distance_init(id1, id2, -1)
        if data.getDistance() == -1:
            return math.inf, []
        return data.getDistance(), data.getPath()

    def __distance_init(self, src: int, dest: int, key: float):
        all_dists = {}
        indexes_array = {}
        v = self.__graph.get_all_v()
        for key1 in v:
            node = v[key1]
            node.set_tag(1)
            dict_a_to_add = {key1: sys.maxsize}
            all_dists.update(dict_a_to_add)

            dict_b_to_add = {key1: -1}
            indexes_array.update(dict_b_to_add)
        indexes_array.update({src: src})
        all_dists.update({src: 0})
        data = self.__shortest_dis_aid(src, src, dest, 0, all_dists, indexes_array, key)
        return data

    def __shortest_dis_aid(self, initial: int, src: int, dest: int, dist3: float, all_dists, indexes_array, key: float):
        q = minHeap_Aid(self.__graph.e_size() + self.__graph.v_size())
        temp_max = -1
        non_inf = self.__graph.v_size()

        while src != dest:
            non_inf -= 1
            self.__graph.get_node(src).set_tag(2)

            u = self.__graph.all_out_edges_of_node(src)
            edges_counter = 0
            while edges_counter < len(u):
                current = self.__graph.get_edge(src, edges_counter)
                edges_counter += 1
                instant_dist = list(current.values())[0]
                temp_dest = list(current.keys())[0]
                if 0 < key <= all_dists[src]:
                    return DistanceReturnedData(key)
                elif key >= 0 and all_dists[src] > temp_max and src != initial:
                    temp_max = all_dists[src]

                if instant_dist + dist3 < all_dists[temp_dest] and self.__graph.get_node(temp_dest).get_tag() == 1:
                    all_dists[temp_dest] = instant_dist + dist3
                    q.insert({temp_dest: all_dists[temp_dest]})
                    indexes_array[temp_dest] = src

            k = -1
            if q.size > 0 and all_dists[int(list(q.peek().keys())[0])] != sys.maxsize:
                while q.size > 0 and self.__graph.get_node(int(list(q.peek().keys())[0])).get_tag() == 2:
                    q.remove()
                if q.size > 0:
                    k = list(q.remove().keys())[0]
                    dist3 = all_dists[k]

            if k == -1:
                if key >= 0:
                    if temp_max == -1 or non_inf > 0:
                        temp_max = sys.maxsize
                    return DistanceReturnedData(temp_max)
                data = DistanceReturnedData(-1)
                data.nullify()
                return data
            src = k

        t = src
        data = DistanceReturnedData(dist3)
        data.addNodeToList(0, t)
        while t != initial:
            data.addNodeToList(0, indexes_array[t])
            t = indexes_array[t]

        return data

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
        cities = self.__remove_duplicates(node_lst)
        city_chain = [cities.pop(0)]

        while len(cities) > 0:

            minimum = 0
            k = 0
            for j in range(len(city_chain) + 1):
                temp_distance = 0
                city_chain.insert(j, cities[0])
                if j == 0:
                    for l in range(len(city_chain) - 1):
                        d, q = self.shortest_path(city_chain[l], city_chain[l + 1])
                        if d == math.inf:
                            minimum = sys.maxsize
                            break
                        minimum += d
                else:
                    for l in range(len(city_chain) - 1):
                        d, q = self.shortest_path(city_chain[l], city_chain[l + 1])
                        if d == math.inf:
                            temp_distance = sys.maxsize
                            break
                        temp_distance += d
                    if temp_distance < minimum:
                        minimum = temp_distance
                        k = j
                city_chain.pop(j)
            if minimum == sys.maxsize:
                return None
            city_chain.insert(k, cities[0])
            dist_chain_a = None
            if k > 0:
                da, dist_chain_a = self.shortest_path(city_chain[k - 1], city_chain[k])

            dist_chain_b = None
            if k < len(city_chain) - 1:
                db, dist_chain_b = self.shortest_path(city_chain[k], city_chain[k + 1])

            if dist_chain_a is not None:
                for item in dist_chain_a:
                    f = 1
                    for n in range(1, len(cities)):
                        if item == cities[f]:
                            city_chain.insert(k, cities[f])
                            k += 1
                            cities.pop(f)
                            f -= 1
                        f += 1

            if dist_chain_b is not None:
                for item in dist_chain_b:
                    f = 1
                    for n in range(1, len(cities)):
                        if item == cities[f]:
                            city_chain.insert(k + 1, cities[f])
                            k += 1
                            cities.pop(f)
                            n -= 1
                            f -= 1
                        f += 1

            cities.pop(0)

        end_result = []
        end_distance = 0
        for i in range(len(city_chain) - 1):
            q, t = self.shortest_path(city_chain[i], city_chain[i + 1])
            end_distance += q
            if len(t) == 0:
                return math.inf, []
            for j in range(len(t)):
                if i == 0 or j > 0:
                    end_result.append(t[j])

        return end_result, end_distance

    def __remove_duplicates(self, cities: List[int]) -> List[int]:
        new_list = [cities[0]]
        cities.pop(0)
        while len(cities) > 0:
            cond = 1
            for i in range(len(new_list)):
                if cities[0] == new_list[i]:
                    cond = 0
                    cities.pop(0)
                    break
            if cond == 1:
                new_list.append(cities[0])
                cities.pop(0)
        return new_list

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """
        k = 0
        chosen_ind = 0
        n = self.__graph.get_all_v()
        for item in n:
            current_data = self.__distance_init(item, -1, k)
            current_max_distance = current_data.getDistance()
            if item == 0:
                k = current_max_distance
            elif item > 0 and current_max_distance < k:
                k = current_max_distance
                chosen_ind = item
        if k == sys.maxsize:
            return None, float("inf")
        return chosen_ind, k

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        plot = Show_graph(self.__graph)
        plot.have_pos()
        plot.paint()
