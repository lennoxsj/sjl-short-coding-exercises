# sjl-short-coding-exercises

A collection of very short Python code samples — classic algorithms and small data-analysis scripts. Each file is self-contained and runs on its own with `python3 <file>.py`.

## Contents

dijkstra.py
Dijkstra's algorithm finds the shortest path from start to all other nodes in a graph with non-negative edge weights

bellman_ford.py
single-source shortest paths; handles negative edges and detects negative cycles

johnsons.py
All-pairs shortest paths; combines Bellman-Ford and Dijkstra to handle negative edges in O(V·E log V).

quicksort.py
Quicksort with median-of-three pivot, returns the sorted array and a comparison count

merge_sort_inversions.py
Merge sort that also counts inversions in O(n log n)

karatsuba.py
Karatsuba's divide-and-conquer integer multiplication

karger_min_cut.py
Karger's randomized contraction algorithm for finding minimum cuts in undirected graphs

wdi_correlations.py
Compares World Development Indicators (life expectancy, electricity access, compulsory education, aquaculture) between the US and the UN's aggregate of Least Developed Countries. Uses the two CSV files in this repo
