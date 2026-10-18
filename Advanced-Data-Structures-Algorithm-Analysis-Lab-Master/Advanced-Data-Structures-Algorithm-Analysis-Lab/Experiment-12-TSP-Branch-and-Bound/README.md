# Experiment 12: Travelling Salesperson Problem Using Branch and Bound

## Aim
To find a minimum-cost tour that visits every city exactly once and returns to the starting city, using the Branch and Bound technique.

## Language
Python 3 (standard library only)

## Files
- `tsp_branch_bound.py` — implementation of Branch and Bound
- `input.txt` — sample number of cities and cost matrix
- `sample_output.txt` — example result
- `output.txt` — generated result after running the program

## Input Format
The first value is the number of cities `n`, followed by `n × n` integer costs. Use `0` off the diagonal to indicate that no direct edge exists. The program starts at city `0` and uses zero-based city indices.

## How to Run
1. Install Python 3.
2. Keep `tsp_branch_bound.py` and `input.txt` in the same folder.
3. Run:
   ```bash
   python tsp_branch_bound.py
   ```
4. The result is printed on screen and saved to `output.txt`.

## Algorithm
1. Start from city 0.
2. Expand possible next cities, exploring lower-cost edges first.
3. Calculate a lower bound for each partial route.
4. Prune a route when its lower bound cannot improve the best complete tour.
5. When every city has been visited, return to city 0 and update the best tour.

## Complexity
The worst-case time complexity remains factorial, approximately `O(n!)`, as the TSP is an NP-hard problem. Branch and Bound can reduce the search by pruning unpromising partial routes.

## Result
The minimum-cost Hamiltonian tour is found using Branch and Bound and saved to `output.txt`.
