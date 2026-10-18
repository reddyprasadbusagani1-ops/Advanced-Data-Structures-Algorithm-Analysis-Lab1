# Experiment 9: Job Sequencing with Deadlines Using Greedy Algorithm

## Aim
To implement the job sequencing with deadlines problem using a greedy strategy and maximize the total profit.

## Language
Python 3

## Files
- `job_sequencing.py` — program implementation
- `input.txt` — sample input
- `sample_output.txt` — sample execution output
- `output.txt` — generated results after running the program

## Input Format
The first line contains the number of jobs. Each following line contains:
`job_id deadline profit`

Example:
```text
5
J1 2 100
J2 1 19
J3 2 27
J4 1 25
J5 3 15
```

## How to Run
1. Install Python 3.
2. Keep `job_sequencing.py` and `input.txt` in the same folder.
3. Run:
   ```bash
   python job_sequencing.py
   ```
4. The schedule and total profit are printed and saved to `output.txt`.

## Algorithm
1. Sort jobs by decreasing profit.
2. For each job, find the latest free time slot on or before its deadline.
3. Schedule the job if a free slot exists.
4. Add the selected jobs' profits to calculate total profit.

## Time Complexity
The straightforward slot-search implementation takes `O(n log n + nD)` time, where `n` is the number of jobs and `D` is the maximum deadline. Sorting takes `O(n log n)` time.

## Result
Job sequencing with deadlines was implemented using a greedy algorithm to maximize profit.
