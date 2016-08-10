# GraphTheory-Python3
## Rafael Cartenet
I implemented an easy approach of the so-called graphs and the weighed graphs, in python 3

## Graphs
I represented a graph as a python dictionnary, where the keys are the different nodes of the graph, and where the corresponding value of the key is a list containing all the nodes linked to this node. This is though a oriented graph.  
Furthermore, I implemented typical graph theory functions like :
- DFS (Depth First Search), finds an element in the graph traveling through the graph in depth first.  
- BFS (Breadth First Search), finds an element in the graph traveling through the graph in breadth first.  

## Weighed graphs
I represented a weighed graph as a dictionnary of dictionnaries, where to each node (a key) corresponds a dictionnary. In this dictionnary each key is a node and the corresponding value is the weigh from the key to the sub key.  
I developped some interesting functions regarding the weighed graphs :  
- Kruskal, using Union Find, returns the nodes and edges of the minimum spanning tree of a given weighed graph.
- Prim, using a BruteForce method, returns the nodes and edges of the minimum spanning tree of a given weighed graph.
- Dijkstra, returns the shortest path from a node to another one, given the graph and the two nodes.

