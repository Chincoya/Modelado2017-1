# Kruskal Algorithm
# Find the minimum spanning tree of a connected undirect graph.
# Complexity ?

import heapq

def kruskal(graph):
    edges = []
    for node in graph:
        init_node(node)
    remaining_edges = [(edge[2], edge[0:2]) for edge in get_edges(graph)]
    heapq.heapify(remaining_edges)
    while remaining_edges:
        edge = heapq.heappop(remaining_edges)
        node1, node2 = edge[1]
        if find_root(node1) != find_root(node2):
            union(node1, node2)
            edges.append(edge)
    return edges


def init_node(node):
    parent[node] = node
    rank[node] = 0


def find_root(node):
    if parent[node] != node:
        parent[node] = find_root(parent[node])
    return parent[node]


def union(node1, node2):
    root1, root2 = find_root(node1), find_root(node2)
    if root1 != root2:
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            if rank[root1] == rank[root2]:
                rank[root1] += 1


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


E = [['A', 'B', 3],
     ['A', 'C', 5],
     ['B', 'C', 6],
     ['B', 'D', 7],
     ['C', 'D', 1],
     ['D', 'C', 2],
     ['E', 'F', 3],
     ['F', 'C', 5]]

parent = {}
rank = {}
H = edges_to_graph(E)
print(to_string(H))
print(kruskal(H))
