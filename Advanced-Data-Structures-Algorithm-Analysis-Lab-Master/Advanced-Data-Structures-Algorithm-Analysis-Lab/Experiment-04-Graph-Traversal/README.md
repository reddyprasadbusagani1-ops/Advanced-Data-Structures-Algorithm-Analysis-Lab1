# Experiment 4: BFS and DFS Using an Adjacency Matrix

## Aim
To implement Breadth-First Search (BFS) and Depth-First Search (DFS) graph traversal algorithms using an adjacency matrix in Python.

## Language
Python 3 (no external packages required)

## Files
- `graph_traversal.py` — complete Python source code
- `input.txt` — sample graph and starting vertex
- `sample_output.txt` — sample execution output
- `output.txt` — generated when the program runs

## Input Format
1. Number of vertices `n`.
2. `n` rows containing the `n × n` adjacency matrix (use `1` for an edge and `0` otherwise).
3. Starting vertex, numbered from `0` to `n-1`.

## How to Run
Keep `graph_traversal.py` and `input.txt` in the same folder, then run:

```bash
python graph_traversal.py
```

The program prints the BFS and DFS traversal orders and saves the same results in `output.txt`.

## Algorithms
- **BFS:** Uses a queue and visits adjacent vertices level by level.
- **DFS:** Uses recursion to explore each reachable path before backtracking.

## Result
BFS and DFS traversals using an adjacency matrix were implemented successfully.
