# Experiment 8: Single-Source Shortest Path Using Dijkstra's Algorithm

## Aim
Implement the greedy Dijkstra algorithm to find shortest-path distances from a source vertex and compare adjacency-matrix and adjacency-list representations.

## Language
Python 3 (standard library only)

## Files
- `shortest_path.py` — implementation of Dijkstra's algorithm for both graph representations
- `input.txt` — sample weighted undirected graph and source vertex
- `sample_output.txt` — sample results (execution timings vary)
- `output.txt` — generated when the program runs

## Input format
The first line contains `V E` (number of vertices and edges). The next `E` lines contain `u v weight`. The last line contains the source vertex. Vertices are numbered from `0` to `V-1`. Edge weights must be non-negative.

## How to run
1. Install Python 3.
2. Keep `shortest_path.py` and `input.txt` in the same folder.
3. Run:
   ```bash
   python shortest_path.py
   ```
4. The program prints shortest distances for both representations and writes the results to `output.txt`.

## Algorithm
Dijkstra's greedy algorithm repeatedly chooses the unvisited vertex with the smallest tentative distance, then relaxes its outgoing edges. The adjacency-list version uses a min-priority queue.

## Time complexity
- Adjacency matrix implementation: `O(V^2)`
- Adjacency list with binary heap: `O((V + E) log V)`

## Result
Shortest distances from the chosen source are calculated using both representations and the results are compared.
