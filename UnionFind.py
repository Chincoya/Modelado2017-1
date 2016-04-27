parent = {}
rank = {}

def init_node(node):
    parent[node] = node
    rank[node] = 0

def find_root(node):
    if parent[node] != node:
        parent[node] = find_root(parent[node])
    return parent[node]

def union(node1, node2):
    root1 = find_root(node1)
    root2 = find_root(node2)
    if root1 != root2:
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            if rank[root1] == rank[root2]:
                rank[root1] += 1


G = {'a': {'b': 4, 'c': 2},
     'b': {'a': 4, 'c': 1},
     'c': {'a': 2},
     'd': {}}

for node in G:
    init_node(node)

print(parent)

union('a','b')

print(parent)

union('b', 'c')

print(parent)