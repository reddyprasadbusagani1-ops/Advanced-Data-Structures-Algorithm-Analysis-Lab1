"""0/1 Knapsack using Dynamic Programming (Experiment 10)."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input.txt"
OUTPUT_FILE = BASE_DIR / "output.txt"


def knapsack(weights, values, capacity):
    n = len(weights)
    # dp[i][w] is the maximum value using the first i items and capacity w.
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]
        for current_capacity in range(capacity + 1):
            dp[i][current_capacity] = dp[i - 1][current_capacity]
            if weight <= current_capacity:
                dp[i][current_capacity] = max(
                    dp[i][current_capacity],
                    value + dp[i - 1][current_capacity - weight],
                )

    chosen = []
    current_capacity = capacity
    for i in range(n, 0, -1):
        if dp[i][current_capacity] != dp[i - 1][current_capacity]:
            chosen.append(i)  # item numbers are 1-based
            current_capacity -= weights[i - 1]
    chosen.reverse()
    return dp[n][capacity], chosen


def read_input(path):
    """Input format: n, then n weights, then n values, then capacity."""
    tokens = path.read_text(encoding="utf-8").split()
    if not tokens:
        raise ValueError("input.txt is empty")
    numbers = list(map(int, tokens))
    n = numbers[0]
    expected = 1 + n + n + 1
    if n < 0 or len(numbers) != expected:
        raise ValueError(
            "Invalid input format. Expected: n, n weights, n values, capacity."
        )
    weights = numbers[1 : 1 + n]
    values = numbers[1 + n : 1 + 2 * n]
    capacity = numbers[-1]
    if capacity < 0 or any(weight < 0 for weight in weights):
        raise ValueError("Weights and capacity must be non-negative.")
    return weights, values, capacity


def main():
    try:
        weights, values, capacity = read_input(INPUT_FILE)
        maximum_value, chosen = knapsack(weights, values, capacity)
        total_weight = sum(weights[i - 1] for i in chosen)

        lines = [
            "0/1 Knapsack using Dynamic Programming",
            f"Capacity: {capacity}",
            f"Weights: {weights}",
            f"Values: {values}",
            f"Selected items (1-based): {chosen if chosen else 'None'}",
            f"Total weight: {total_weight}",
            f"Maximum value: {maximum_value}",
        ]
        result = "\n".join(lines) + "\n"
        print(result, end="")
        OUTPUT_FILE.write_text(result, encoding="utf-8")
        print(f"Results saved to {OUTPUT_FILE.name}")
    except (OSError, ValueError) as error:
        print(f"Error: {error}")
        print("Check input.txt and the format described in README.md.")


if __name__ == "__main__":
    main()
