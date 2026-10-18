# Advanced Data Structures & Algorithm Analysis Lab

Python 3 implementations of the 12 lab experiments. Each experiment folder contains the source program, sample input, sample output, and an experiment-specific README. Some experiments also include a generated `output.txt` file.

## Experiments

| No. | Experiment | Folder |
|---:|---|---|
| 1 | AVL Tree: insertion, deletion, and inorder traversal | `Experiment-01-AVL-Tree` |
| 2 | B-Tree of order 5 | `Experiment-02-B-Tree` |
| 3 | Min Heap and Max Heap operations | `Experiment-03-Heaps` |
| 4 | BFS and DFS using an adjacency matrix | `Experiment-04-Graph-Traversal` |
| 5 | BFS and DFS using an adjacency list | `Experiment-05-Graph-Adjacency-List` |
| 6 | Biconnected components | `Experiment-06-Biconnected-Components` |
| 7 | Quick Sort and Merge Sort with execution-time comparison | `Experiment-07-Quick-Merge-Sort` |
| 8 | Single-source shortest path using a greedy algorithm | `Experiment-08-Single-Source-Shortest-Path` |
| 9 | Job sequencing with deadlines | `Experiment-09-Job-Sequencing` |
| 10 | 0/1 Knapsack using dynamic programming | `Experiment-10-Knapsack-DP` |
| 11 | N-Queens using backtracking | `Experiment-11-N-Queens` |
| 12 | Travelling Salesperson Problem using Branch and Bound | `Experiment-12-TSP-Branch-and-Bound` |

## Requirements

- Python 3.9 or later recommended
- No third-party packages are expected for the supplied programs

## How to run an experiment

1. Open the folder for the experiment you want to run.
2. Read its `README.md` for the input format and instructions.
3. Run the listed Python file from that folder, for example:

   ```bash
   python avl_tree.py
   ```

   Replace `avl_tree.py` with the source filename for the experiment you selected.
4. If the program reads `input.txt`, keep that file in the same folder when running it.

## Repository structure

Each experiment is kept in its own folder so it can be uploaded to GitHub as one repository or run independently. The `sample_output.txt` files are examples; execution times and prompts can vary by environment.
