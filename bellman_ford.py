"""Bellman-Ford algorithm: Given a weighted graph and starting node,
finds the shortest path from the starting node to every other node.

Unlike Dijkstra's, supports negative edge weights. Detects negative
cycles (a cycle whose edge weights sum to a negative number) and raises
an error if one is reachable from the source.

Time complexity: O(V * E). Slower than Dijkstra's O((V+E) log V), but
necessary when negative edges are present.

Output: dict mapping each node to its shortest distance from source.
"""


def bellman_ford(graph, start):
    distances = {node: float("inf") for node in graph} # Current best known distance from start to each node
    distances[start] = 0
    predecessors = {node: None for node in graph} # Stored for use by show_shortest_path

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u
    
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative cycle")

    return distances, predecessors

def show_shortest_path(predecessors, end_point):
    path = []
    node = end_point
    while node is not None:
        path.append(node)
        node = predecessors[node]
    return list(reversed(path))
    

if __name__ == "__main__":
    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"C": 3, "D": 2, "E": 3},
        "C": {"B": -1, "D": 4, "E": 5},
        "D": {"E": 1},
        "E": {},
    }

    distances, predecessors = bellman_ford(graph, "A")
    for node, dist in distances.items():
        print(f"A -> {node}: {dist}")

        bad_graph = {
        "A": {"B": 1},
        "B": {"C": -3},
        "C": {"A": 1},
    }
    print("\nTrying graph with negative cycle...")
    try:
        bellman_ford(bad_graph, "A")
    except ValueError as e:
        print(f"Caught: {e}")