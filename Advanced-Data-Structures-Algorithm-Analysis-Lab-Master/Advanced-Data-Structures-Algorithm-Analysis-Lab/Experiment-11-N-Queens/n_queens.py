"""Experiment 11: N-Queens using backtracking.
Reads N from input.txt (or prompts if the file is unavailable), prints all solutions,
and saves them to output.txt.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input.txt"
OUTPUT_FILE = BASE_DIR / "output.txt"


def solve_n_queens(n):
    """Return all valid solutions, each represented as a list of column indices."""
    solutions = []
    columns = set()
    diag1 = set()  # row - column
    diag2 = set()  # row + column
    placement = [-1] * n

    def backtrack(row):
        if row == n:
            solutions.append(placement.copy())
            return
        for col in range(n):
            if col in columns or row - col in diag1 or row + col in diag2:
                continue
            placement[row] = col
            columns.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            backtrack(row + 1)
            columns.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
            placement[row] = -1

    if n > 0:
        backtrack(0)
    return solutions


def format_solution(solution):
    n = len(solution)
    lines = []
    for queen_col in solution:
        lines.append(" ".join("Q" if col == queen_col else "." for col in range(n)))
    return "\n".join(lines)


def main():
    try:
        raw = INPUT_FILE.read_text(encoding="utf-8").strip()
        n = int(raw)
    except (OSError, ValueError):
        n = int(input("Enter the value of N: ").strip())

    if n < 1:
        message = "Please enter a positive integer for N."
        print(message)
        OUTPUT_FILE.write_text(message + "\n", encoding="utf-8")
        return

    solutions = solve_n_queens(n)
    output_lines = [f"N = {n}", f"Number of solutions: {len(solutions)}"]
    for index, solution in enumerate(solutions, start=1):
        output_lines.extend([f"\nSolution {index}:", format_solution(solution)])
    if not solutions:
        output_lines.append("No solutions exist for this value of N.")

    result = "\n".join(output_lines)
    print(result)
    OUTPUT_FILE.write_text(result + "\n", encoding="utf-8")
    print(f"\nResults saved to {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
