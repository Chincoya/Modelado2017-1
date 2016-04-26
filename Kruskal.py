# Kruskal Algorithm
# Find the minimum spanning tree of a connected undirect graph.
# Complexity ?

import heapq

def kruskal(graph):
    visited = set()
    edges = []
    remaining_edges = [(edge[2], edge[0:2]) for edge in get_edges(graph)]
    heapq.heapify(remaining_edges)
    print(remaining_edges)
    while remaining_edges:
        print(visited)
        edge = heapq.heappop(remaining_edges)
        print(edge)

        nodes = set(edge[1])
        print(nodes <= visited)
        print()
        if not (nodes <= visited):
            edges.append(edge)
            visited.add(nodes.pop())
            visited.add(nodes.pop())
    return edges

def add_edge(graph, edge, weight):
    edge = set(edge)
    node1 = edge.pop()
    if edge:
        node2 = edge.pop()
    else:
        node2 = node1
    graph[node1][node2] = weight


def add_node(graph, node):
    if node not in graph:
        graph[node] = {}


def get_edges(graph):
    edges = []
    for node1 in graph:
        for node2 in graph[node1]:
            edges.append([node1, node2, graph[node1][node2]])
    return edges


def get_neighbours(graph, node):
    nodes = []
    if node in graph:
        for neighbour in graph[node]:
            if neighbour not in nodes:
                nodes.append(neighbour)
    return nodes


def get_neighbours_edges(graph, node):
    edges = dict()
    if node in graph:
        edges = graph[node]
    return edges


def edges_to_graph(edges):
    graph = dict()
    for edge in edges:
        weight = edge.pop()
        node1 = edge.pop()
        if node1 not in graph:
            add_node(graph, node1)
        if edge:
            node2 = edge.pop()
            if node2 not in graph:
                add_node(graph, node2)
        else:
            node2 = node1
        graph[node2][node1] = weight
    return graph


def to_string(graph):
    res = "Graph :\n"
    for k in graph:
        res += str(k) + " : " + str(graph[k]) + "\n"
    return res


G = {'a': {'b': 4, 'c': 2},
     'b': {'a': 4, 'c': 1},
     'c': {'a': 2}}

E = [['A', 'B', 3],
     ['A', 'C', 5],
     ['B', 'C', 6],
     ['B', 'D', 7],
     ['C', 'D', 1],
     ['D', 'C', 2],
     ['E', 'F', 3],
     ['F', 'C', 5]]

print(len(G))

add_edge(G, ['c', 'b'], 10)
add_edge(G, ['a', 'a'], 5)

print(get_neighbours(G, 'c'))
add_node(G, 'z')
print(to_string(G))

H = edges_to_graph(E)
print(to_string(H))



E = get_edges(H)
print(*E, sep='\n')

print(kruskal(H))