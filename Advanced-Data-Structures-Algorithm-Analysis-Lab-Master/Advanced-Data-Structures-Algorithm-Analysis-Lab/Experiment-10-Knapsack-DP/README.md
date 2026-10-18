# Experiment 10: 0/1 Knapsack Using Dynamic Programming

## Aim
To solve the 0/1 Knapsack problem using dynamic programming and find the maximum value that can fit within a given capacity.

## Language
Python 3 (standard library only)

## Files
- `knapsack_dp.py` — complete Python implementation
- `input.txt` — sample input
- `sample_output.txt` — expected console output
- `output.txt` — sample saved result

## Input Format
The input file contains whitespace-separated integers in this order:
1. Number of items `n`
2. `n` item weights
3. `n` item values/profits
4. Knapsack capacity

Example:
```text
3
10 20 30
60 100 120
50
```

## How to Run
1. Install Python 3.
2. Keep `knapsack_dp.py` and `input.txt` in the same folder.
3. Run:
   ```bash
   python knapsack_dp.py
   ```
4. The maximum value and selected 1-based item numbers are printed and saved to `output.txt`.

## Algorithm
For each item and each capacity, compare:
- Excluding the item: `dp[i-1][w]`
- Including the item, if it fits: `value[i-1] + dp[i-1][w-weight[i-1]]`

Choose the larger value and trace the DP table backwards to identify selected items.

## Complexity
- Time: `O(n × capacity)`
- Space: `O(n × capacity)`

## Sample Result
For weights `[10, 20, 30]`, values `[60, 100, 120]`, and capacity `50`, the selected items are 2 and 3, with total weight `50` and maximum value `220`.

## Result
The 0/1 Knapsack problem is solved using dynamic programming.
