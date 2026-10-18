# Experiment 6: Biconnected Components Using Python

## Aim
To find the biconnected components of an undirected graph using depth-first search and Tarjan's algorithm.

## Language
Python 3 (no external libraries required).

## Files
- `biconnected_components.py` — source code
- `input.txt` — sample graph input
- `sample_output.txt` — expected sample output
- `output.txt` — generated results after execution

## Input format
The first line contains `V E`, where `V` is the number of vertices and `E` is the number of edges. Each following line contains one undirected edge `u v`. Vertices are numbered from `0` to `V-1`.

## How to run
1. Keep `biconnected_components.py` and `input.txt` in the same folder.
2. Run `python biconnected_components.py`.
3. The results are displayed and saved to `output.txt`.

## Algorithm
Depth-first search records discovery times and low-link values. A child subtree forms a separate biconnected component when its low-link value is at least the discovery time of its parent. Edges are kept on a stack until a component is identified.

## Result
Biconnected components of the given undirected graph are identified successfully.
