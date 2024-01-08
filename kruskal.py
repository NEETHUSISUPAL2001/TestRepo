class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal_mst(graph):
    if not graph:
        return []

    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((weight, vertex, neighbor))

    edges.sort()  # Sort edges by weight
    vertices = set(vertex for vertex in graph)
    mst = []
    uf = UnionFind(vertices)

    for edge in edges:
        weight, v1, v2 = edge
        if uf.find(v1) != uf.find(v2):
            uf.union(v1, v2)
            mst.append((v1, v2, weight))

    return mst


# Example graph
example_graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 1), ('C', 2)]
}

minimum_spanning_tree = kruskal_mst(example_graph)
print("Minimum Spanning Tree Edges:")
for edge in minimum_spanning_tree:
    print(edge)
