"""Karger's randomized contraction algorithm for min-cut on undirected graphs.

Repeatedly pick a random edge (u, v) and contract it — merge v into u and
drop self-loops — until only two super-nodes remain. The number of parallel
edges between them is a candidate min-cut. A single run has low success
probability, so we run many trials and take the smallest result.

Graphs are represented as adjacency lists: {vertex: [neighbors]}.
"""

import copy
import random


def karger_min_cut(graph):
    working = copy.deepcopy(graph)

    while len(working) > 2:
        u = random.choice(list(working.keys()))
        if not working[u]:
            continue
        v = random.choice(working[u])

        for neighbor in working[v]:
            if neighbor != u:
                working[neighbor] = [u if x == v else x for x in working[neighbor]]
                working[u].append(neighbor)

        working[u] = [x for x in working[u] if x != v]
        del working[v]

        for key in working:
            working[key] = [x for x in working[key] if x != key]

    remaining = list(working.keys())
    return len(working[remaining[0]])


def run_trials(graph, trials):
    return min(karger_min_cut(graph) for _ in range(trials))


if __name__ == "__main__":
    # Two triangles {1,2,3} and {4,5,6} joined by edges 1-6 and 3-4.
    # The min cut is 2 (cut those two bridge edges to separate the triangles).
    example_graph = {
        1: [2, 3, 6],
        2: [1, 3],
        3: [1, 2, 4],
        4: [3, 5, 6],
        5: [4, 6],
        6: [1, 4, 5],
    }

    min_cut = run_trials(example_graph, 200)
    print(f"Min cut found: {min_cut}")
