"""Travelling Salesperson Problem using Branch and Bound.

Input format (input.txt):
    n
    n lines containing n integer costs each

Use 0 (off the diagonal) for no direct edge. The graph is directed unless
its cost matrix is symmetric. City indices are 0-based.
"""
from math import inf
from pathlib import Path

INPUT_FILE = Path(__file__).with_name("input.txt")
OUTPUT_FILE = Path(__file__).with_name("output.txt")


def read_graph(path=INPUT_FILE):
    tokens = path.read_text(encoding="utf-8").split()
    if not tokens:
        raise ValueError("input.txt is empty")
    n = int(tokens[0])
    if n < 2:
        raise ValueError("The number of cities must be at least 2")
    values = list(map(int, tokens[1:]))
    if len(values) != n * n:
        raise ValueError(f"Expected {n*n} matrix values, found {len(values)}")
    matrix = [values[i*n:(i+1)*n] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == 0:
                matrix[i][j] = inf
    return matrix


def tsp_branch_and_bound(cost):
    n = len(cost)
    best_cost = inf
    best_path = []
    path = [0]
    visited = {0}

    # Minimum possible outgoing edge from each city; used for an admissible
    # lower bound on the cost of completing a partial route.
    min_out = []
    for i in range(n):
        candidates = [cost[i][j] for j in range(n) if i != j and cost[i][j] != inf]
        min_out.append(min(candidates) if candidates else inf)

    def lower_bound(current, current_cost):
        # Every unvisited city must leave once, and the current city must leave
        # once. The destination of these edges is relaxed, so this cannot
        # overestimate the cost of a valid completion.
        required = [current] + [city for city in range(n) if city not in visited]
        extra = sum(min_out[city] for city in required)
        return current_cost + extra

    def search(current, current_cost):
        nonlocal best_cost, best_path
        if len(visited) == n:
            back = cost[current][0]
            total = current_cost + back
            if back != inf and total < best_cost:
                best_cost = total
                best_path = path[:] + [0]
            return

        if lower_bound(current, current_cost) >= best_cost:
            return

        # Explore lower-cost edges first to find a good upper bound quickly.
        candidates = [city for city in range(n) if city not in visited and cost[current][city] != inf]
        candidates.sort(key=lambda city: cost[current][city])
        for city in candidates:
            next_cost = current_cost + cost[current][city]
            if next_cost >= best_cost:
                continue
            visited.add(city)
            path.append(city)
            search(city, next_cost)
            path.pop()
            visited.remove(city)

    search(0, 0)
    return best_path, best_cost


def main():
    try:
        graph = read_graph()
        route, total_cost = tsp_branch_and_bound(graph)
        if not route:
            lines = ["No Hamiltonian tour exists for the given graph."]
        else:
            lines = [
                "Travelling Salesperson Problem - Branch and Bound",
                "Optimal tour: " + " -> ".join(map(str, route)),
                f"Minimum tour cost: {int(total_cost)}",
            ]
        result = "\n".join(lines)
        print(result)
        OUTPUT_FILE.write_text(result + "\n", encoding="utf-8")
        print(f"Results saved to {OUTPUT_FILE.name}")
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}")
        print("Make sure input.txt contains n followed by an n x n cost matrix.")


if __name__ == "__main__":
    main()
