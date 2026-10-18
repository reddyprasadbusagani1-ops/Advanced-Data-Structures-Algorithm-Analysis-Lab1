# Experiment 11: N-Queens Problem Using Backtracking

## Aim
To solve the N-Queens problem using the backtracking technique and display all valid arrangements of N queens on an N × N chessboard so that no two queens attack each other.

## Language
Python 3

## Files
- `n_queens.py` — implementation using backtracking
- `input.txt` — sample value of N
- `sample_output.txt` — sample execution output for N = 4
- `output.txt` — results generated when the program runs

## Algorithm
1. Start from the first row.
2. Try placing a queen in each column of the current row.
3. Check that the column and both diagonals are not occupied.
4. If the position is safe, place the queen and recursively process the next row.
5. If no placement works, backtrack and try another column.
6. When all rows are filled, record the solution.

## How to Run
1. Install Python 3.
2. Keep `n_queens.py` and `input.txt` in the same folder.
3. Run:
   ```bash
   python n_queens.py
   ```
4. The program reads N from `input.txt`, prints every solution, and saves the results to `output.txt`.

## Sample Result
For `N = 4`, the program finds **2 solutions**.

## Result
The N-Queens problem is solved using backtracking.
