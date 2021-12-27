# Ex3:
fourth assignment of OOP course. Contributers: Yehonatan Amosi, Amit Goffer

# Project theme:
In this project we are assigned to implement a Directed Weighted Graph, and run basic algorithms on it. We also were asked to build a GUI were you could load and save graphs using a JSON file.
the main difference between this project and the last, is this time the project was made with Python.

# Algorithems:

# isConnected:
- This function check if a graph is strongly connected (if there is a path from each node to each node).<br>
  The algorithm checks the first BFS to mark if all the nodes were visited, then reverse all the edges of the nodes and set visited<br>
  tag of them to nonvisited and proceed a final BFS. If at the end all the nodes are visited then the graph is connected.

# shortest_path:

- The function uses Dijkstra Algorithm method to calculate the distance.
like its java equivalent - shortest_path uses a aid calculating methods: 'distanceInit' and 'ShortestDistAid' which make the calculations and returns an
object which contains all the data, including both distance and path, which are returned as pair.

- how it works: both shortest_path calls to 'distanceInit' which works similiary to java. its puprpose is to initialize all the data
that required for the Dijkstra calculation with 'src' and 'dest' parameters - which are keys of nodes.
in addition 'distanceInit' creates an array for every nodes, which its index is the nodes keys that is called 'allDists'.
the content of every array cell is the current lowest distance from the source to every node.
At the initilization - every cell in the array except the source cell is set to sys.maxsize - meaning infinity, meaning
that at the moment of the initilization, we have yet to discover any route from source to any other node.
the cell of the source index in the distance array is set to 0, as the distance from every node to itself is 0.
'distanceInit' also creates indexesArray - which purpose is to store at every sell, the key of the node which came before it
at the shortest possible path. at the initialization every cell in the array is set to the index itself.
finally, 'distanceInit' sets all tags to 1 - means every node is not yet visited.
the 'distanceInit' sets the data, and then call to 'ShortestDistAid'.

- 'ShortestDistAid' functions begins with the given source key node, its first actions are: a. create min-heap which stores the nodes based on the<br>
distance that required to get to that node - the shorter the distance - the matching target node will be extracted earlier.
b. set the node's tag to '2' - means we visited it.

-the main difference between Pyhton's 'ShortestDistAid' and its Java equivalent - is this time python had no built-in priority queue which could sort the input data
according to external parameter (inserting the destinations's id according to the current distance it takes to get to them).<br>
so we built one - we build existing min-heap template, and modified it to accept dictionary, the key is the destination's id, and the value is the distance.<br>
that way we could effectively access the minimum value, inserting and removing data.

- The function then proceed to check every node that the source node is directly can get into - meaning there is an edge from
source node to every target node.<br>.
for every target node visited - its cell at 'allDists' is updated to the distance from the source to target, its cell at 'indexesArray' is updated<br>
to source node's key.<br>
the target's keys are inserted to the priority queue based on the distances to those target nodes.

- when all edges were visitted from source node - we extract the first element from the min-heap, which is a dictionary in which the key of the node with the lowest distance stored,<br>
and the value is the distance itself - that node becomes the new source node to be checked.

- the function then begins doing the same action on the second source key node - the node's tag is set to 2 (visited) and iterates the edges coming out<br>
from that node. then it checked all nodes whose tags is set to 1 (and ignores the nodes whose tags are
set to 2), and if it finds new, shorter distance to the unvisited nodes - it updates, or re-updates them, and accordingly inserting
the values at the min-heap.

- at some points, after enough iterations - one of the 2 conditions is assured: a: we ran out of unvisited nodes while the destination node reamines unreached,<br>
meaning its impossible to get to it. in this case the returned distance valued is -1, and the returned path is empty list, as there are no distance and path.<br>
b: the destination node becomes the source node - it means that when get to it - according to the Dijkstra algorithm the path and
the distance that were found to get to the destination - is indeed the most optimal.<br>
at this point the function checks the indexesArray of the sell of the destination's index - and takes the value - the node that
sent the edge that reached the destination node. then it does the same action in a loop until it reaches back to the source node.<br>
that way we can create the route that were used to get from the source node to the destination node.
at the end of the function - relevant data is returned and the function finishes running.

- Returned data: the calculating functions return an object of the class 'DistanceReturnedData' - which is a designated class whose purpose is to store<br>
both the found distance as double, and the formed List of the path that was found.<br>
these data members are the values that returned to 'shortest_path'.<br>
- The complexity of the 'shortest_path' using Dijkstra Algorithm is O(|E|) - as the algorithm in the worst case checks every possible edge in the graph.

# center:
- in the function center, we are looking for node whose maximum distance to any other node - is the lowest of all the nodes. for that the general idea is to check every node, take from each one the highest distance to all other nodes (the minimum distance to each node), and from all maximum distances found - we take the lowest distance. the node with that lowest distance - is the center of the graph.

- how it works: first, we initialize variable that called "currentMaxDistance" whose purpose is to store the maximum distance obtained from every node.
then, we take at the first possible node, and we use the 'shortest_path' that the checked node is given as source input.<br>
however, this time there is no destination input (the destinatation input is -1), the reason for that is that we are not looking for the distance<br>
to a specific node, but generally find the maximal possible distance, to any node.<br>
a third parameter is also sent called 'key', at the first node checked the key value is 0. its purpose is to store the minimal highest
distance found to that point. at the first node check the key parameter is not yet used.
as the first node recieve the returned distance data from the 'ShortestDistAid' distance calculation, the returned value will be set as 'key',<br>
that value will be used for the second node distance check.<br>
at the second node run of 'ShortestDistAid' - it is possible that the maximum distance will be greater than 'key' - the maximum distance possible<br>
found at the first node's run. and it is possible that the greater distance can be found before the 'ShortestDistAid' function is finished,<br>
if that the case - we know for sure that the second node is definetly not the center, and we immediately stop the 'ShortestDistAid' calculation,<br>
and proceed to check the next node. that methods result is saving time for the calculation.<br>
if after we check another node, and the returned result is lower than 'key', then key will be the new returned result for next nodes calculations.<br>
- the function ends when all nodes were checked, the the returned result is the node which gave us the 'key' - the lowest of the maximums of distances.<br>
the running time is the amount of nodes * the run time of each Dijkstra calculation = O(|V| * |E|).<br>
the "key method" however can decrease some of the total running time.

# tsp:
- The tsp - traveling salesman's problem purpose is to find the shortest route which goes trough every city a least once. in the graph - we need to<br>
find a path that goes trough every node that was included on input, and if needed - we can use other no cities node to find the graph.<br>
Before discussing the function itself, it's important to note that the "brute force" method - checking every possible premutation of the input<br>
is not viable for large number of cities, that is because the running time of such methos is O(n!).<br>
Dynamic programming is also not viable in this situation, that is because we can use nodes multiple times,<br>
which makes the table creating of "subproblem" route - too costly as there are too many subproblems.<br>
thus - we are resorted to use the greedy algorithm method - which its result is not necessary the lowest of result, however: <br>
a: it will guarantee lower than average route's distance of all possible combinations.<br>
b. it will run in plausible running time for large inputs.<br>
therefore - we used greedy algorithm for tsp.<br>
How the algorithm works: Lets assume the input is: "A,B,C,D,E" (every letter represents a node).<br>
first - we will take 'A' and puts it in a new list. then we will take B, and we will check A->B, and B->A. and we take the option which gives us the<br>
lower distance. lets assume B->A was selected. before checking 'C' node - we check the path of B-> with 'shortestPath'.<br>
if, for example - the shortest path is B->D->A, it means that from 'B' to 'A' we pass through another city in the input,<br>
so we can eliminate 'D' from the input list, and add it at the result list between 'A' and 'B' and for now the output list will be "B, D, A".<br>
next - we check the next un-used city in the input list - 'C'. we check all possible combinations: C->B->D->A, B->C->D->A, B->D->C->A, B->D->A->C.<br>
lets assume B->C->D->A path was found to be the shortest, we will check all B->C, C->D, D->A paths to see if the remaining city 'E' is located in any of the paths.<br>
if so - we insert it at the right place, like the way we inserted 'C', then it means we found the path. else - we do the same calculation with E city.<br>
If with any of the calculations - 'shortestPath' will return null for every premutation of given city, it means there is no possible path that goes through<br>
every city and the function will return null.<br>
This calculation will assure relatively low distance result for path, if exists.

# Graph Design
- in Java, the graph is implemented with 3 HashMaps.
- in Python, the hashmaps were replaces with dictionaries
- the first - Node dictionary, which with given Integer key - will retrieve the matching node.
- secondly - neighborsOut: which with given Integer key - will retrieve dictionary of dictionaries, in which each internal dictionary key is the destination<br>
node, and the value is the weight.
- the third dictionary is neighborsIn, which works similiary to neighborsOut - however in neighborsIn, the key of every internal dictionary<br>
is the source node id, which get to the extrernal dictionary key - the node's id.
        
# GUI
TBA

# Folders:
api:
        - GeoLocation
        - NodeData
        - EdgeData
        - DirectedWeightedGraph
        - DirectedWeightedGraphAlgorithms
# GUI:
        - frameGUI
        - GUImenu
        - panelGUI
        
# Main Classes:
        - DiGraph
        - NodeData
        - GraphAlgo
        - DistanceReturnedData
        - minHeap_Aid
        
# Test:
        - geolocationTest
        - VertexTest
        - EdgedataTest
        - directeweightedgraphTest
        - DWGATest
# UML
TBA

# Results Run Time using unittest
        - Note: the run time of the algorithms may change between computers and even between to runs of the same json file</b></br>
        Build and load the graph:
        G1.json (17 Nodes): java: 62 ms, python: </br>
        G2.json (31 Nodes): 72 ms</br>
        G3.json (48 Nodes): 83 ms</br>
        1,000 Nodes: 320 ms</br>
        10,000 Nodes: 1 sec 124 ms</br>
        100,000 Nodes: 12 sec 31 sec</br>
        
        isConnected:
        G1.json (17 Nodes):62 ms</br>
        G2.json (31 Nodes):85 ms</br>
        G3.json (48 Nodes):86 ms</br>
        1,000 Nodes:552 ms</br>
        10,000 Nodes:2 sec 373 ms</br>
        100,000 Nodes:3 min 1 sec</br>

        center:
        G1.json (17 Nodes):69 ms</br>
        G2.json (31 Nodes):83 ms</br>
        G3.json (48 Nodes):98 ms</br>
        1,000 Nodes:3 sec 380 ms</br>
        10,000 Nodes:6 min 48 sec</br>
        100,000 Nodes:</br>

        tsp:
        G1.json (17 Nodes):110ms</br>
        G2.json (31 Nodes):327ms</br>
        G3.json (48 Nodes):498ms</br>
        1,000 Nodes (30 cities): 4 sec, 794ms</br>
        10,000 Nodes (30 cities): 1 min, 22 sec</br>
        10,000 Nodes (50 cities): 5 min, 33 sec</br>
        100,000 Nodes (10 cities) 5 min 4 sec:</br>
# Instructions for using the GUI
        - File Menu By clicking <b>Load</b> you can load a graph from a json file existing in your computer.
        - By clicking <b>Save</b> the graph will be saved and replace the existing file with his name.
        - By clicking "Save as" the graph will be saved in the directory as your choose with the name that you gave.

# Instructions for running the program
        - Download the following zip file- https://github.com/yehonatan169/Ex2_SS/releases/download/v.1/Ex2_jar.zip
        - Extract the files to your computer.
        - Open CMD.
        - Cd the directory that you saved the files in.
        - Write the next command: java -jar "enter the full path of the Ex2.jar" "enter the full path of the json file"
