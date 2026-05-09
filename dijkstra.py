"""Dijkstra's algorithm: Given a weighted graph and starting node, 
finds the shortest path from starting node to every other node.

Output: Distance from start node to all other nodes is stored as a dict.

Edges must be non-negative. See Johnson's algorithm or Bellman-Ford algorithm 
for problems with negative edges.
"""

import heapq

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph} # Current best known distance from start to each node
    distances[start] = 0
    predecessors = {node: None for node in graph} # Stored for use by show_shortest_path
    visited = set()
    heap = [(0, start)] # pqueue of tentative distance, node pairs

    while heap:
       dist, node = heapq.heappop(heap) # pop the smallest distance, node pair
       if node in visited:
           continue
       visited.add(node)

       for neighbor, weight in graph[node].items():
           new_dist = dist + weight
           if new_dist < distances[neighbor]:
               distances[neighbor] = new_dist
               predecessors[neighbor] = node
               heapq.heappush(heap, (new_dist, neighbor))
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
        "C": {"B": 1, "D": 4, "E": 5},
        "D": {"E": 1},
        "E": {},
    }

    distances, predecessors = dijkstra(graph, "A")

    for node in graph:
        path = show_shortest_path(predecessors, node)
        print(f"A -> {node}: distance {distances[node]}, path {' -> '.join(path)}")