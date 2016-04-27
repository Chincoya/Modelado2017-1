def dijkstra(graph, current, target, start="", visited=set(), dist=dict(), prev=dict()):
    if not visited:
        start = current
        dist[current] = 0
    if current == target:
        return dist[target], get_path_dijkstra(prev, start, target, [])
    for next in get_neighbours(graph, current):
        if next not in visited:
            dist_next = dist.get(next, float('inf'))
            candidate_dist = dist[current] + graph[current][next]
            if candidate_dist < dist_next:
                dist[next] = candidate_dist
                prev[next] = current
    visited.add(current)
    nexts = dict((node, dist.get(node, float('inf'))) for node in graph if node not in visited)
    next = min(nexts, key=nexts.get)
    if dist.get(next, float('inf')) == float('inf'):
        return -1
    return dijkstra(graph, next, target, start, visited, dist, prev)


def get_path_dijkstra(paths, start, current, path):
    if current == start:
        return [start] + path
    return get_path_dijkstra(paths, start, paths[current], [current] + path)


def add_node(graph, node):
    if node not in graph:
        graph[node] = {}


def get_neighbours(graph, node):
    nodes = []
    if node in graph:
        for neighbour in graph[node]:
            if neighbour not in nodes:
                nodes.append(neighbour)
    return nodes


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

H = edges_to_graph(E)
print(to_string(H))
print(dijkstra(H, 'A', 'D'))
