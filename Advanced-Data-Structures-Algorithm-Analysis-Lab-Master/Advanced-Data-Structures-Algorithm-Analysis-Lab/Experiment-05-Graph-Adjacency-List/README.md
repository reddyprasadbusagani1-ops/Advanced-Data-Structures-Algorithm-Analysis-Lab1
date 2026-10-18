# Experiment 5: BFS and DFS Using an Adjacency List

## Aim
To represent a graph using an adjacency list and perform Breadth-First Search (BFS) and Depth-First Search (DFS) from a given starting vertex.

## Language
Python 3 (standard library only)

## Files
- `graph_traversal.py` — complete program for adjacency-list representation, BFS, and DFS
- `input.txt` — sample graph and starting vertex
- `sample_output.txt` — expected sample output
- `output.txt` — generated when the program runs

## Input format
The first line contains `V E` (number of vertices and edges). The next `E` lines each contain an edge `u v`. The final line contains the starting vertex. Vertices are numbered from `0` to `V-1`. This program treats the graph as undirected.

## Run
1. Install Python 3.
2. Keep `graph_traversal.py` and `input.txt` in the same folder.
3. Run `python graph_traversal.py`.
4. The program prints the adjacency list, BFS, and DFS traversals, then saves them to `output.txt`.

## Algorithms
- **BFS:** Uses a queue and visits reachable vertices level by level.
- **DFS:** Uses recursion to explore each reachable path before backtracking.

## Result
BFS and DFS traversals were implemented using an adjacency-list graph representation.
