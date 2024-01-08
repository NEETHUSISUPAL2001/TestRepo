import heapq

def prims_mst(graph):
    if not graph:
        return []

    mst = []
    visited = set()
    start_vertex = list(graph.keys())[0]  # Choosing the first vertex arbitrarily
    visited.add(start_vertex)
    edges = [(cost, start_vertex, neighbor) for neighbor, cost in graph[start_vertex]]

    heapq.heapify(edges)

    while edges:
        cost, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, cost))

            for neighbor, edge_cost in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (edge_cost, v, neighbor))

    return mst

# Example graph
example_graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 1), ('C', 2)]
}

minimum_spanning_tree = prims_mst(example_graph)
print("Minimum Spanning Tree Edges:")
for edge in minimum_spanning_tree:
    print(edge)
