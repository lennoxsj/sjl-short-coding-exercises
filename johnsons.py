"""Johnson's algorithm: all-pairs shortest paths, supports negative
edges (but not negative cycles).

Combines Bellman-Ford (to compute reweighting potentials from a virtual
source) and Dijkstra (run V times on the reweighted graph) to get
all-pairs shortest distances in O(V*E log V) on sparse graphs.

Output: nested dict {source: {target: distance}}.
"""

from dijkstra import dijkstra
from bellman_ford import bellman_ford

def johnsons(graph):
    augmented = {node: dict(neighbors) for node, neighbors in graph.items()}
    augmented["__virtual__"] = {node: 0 for node in graph}

    try:
        distances_from_virtual, _ = bellman_ford(augmented, "__virtual__")
    except ValueError:
        raise ValueError("Graph contains a negative cycle")
    
    h = distances_from_virtual
    
    reweighted = {
        u: {v: w + h[u] - h[v] for v, w in neighbors.items()}
        for u, neighbors in graph.items()
    }

    all_distances = {}
    for source in graph:
        distances, _ = dijkstra(reweighted, source)
        all_distances[source] = distances

    return {
        u: {v: dist + h[v] - h[u] for v, dist in targets.items()}
        for u, targets in all_distances.items()
    }


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

    all_distances = johnsons(graph)

    print(f"{'':>4}", end="")
    for target in graph:
        print(f"{target:>5}", end="")
    print()

    for source in graph:
        print(f"{source:>4}", end="")
        for target in graph:
            d = all_distances[source][target]
            print(f"{d:>5}", end="")
        print()