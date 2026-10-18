"""Experiment 4: BFS and DFS graph traversal using an adjacency matrix."""
from collections import deque
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input.txt"
OUTPUT_FILE = BASE_DIR / "output.txt"


def read_graph(path):
    tokens = path.read_text(encoding="utf-8").split()
    if not tokens:
        raise ValueError("input.txt is empty")

    pos = 0
    n = int(tokens[pos])
    pos += 1
    if n <= 0:
        raise ValueError("Number of vertices must be positive")

    expected = n * n + 1
    if len(tokens) < pos + expected:
        raise ValueError("Not enough values for the adjacency matrix and start vertex")

    matrix = []
    for _ in range(n):
        row = [int(x) for x in tokens[pos:pos + n]]
        pos += n
        if any(value not in (0, 1) for value in row):
            raise ValueError("Adjacency matrix values must be 0 or 1")
        matrix.append(row)

    start = int(tokens[pos])
    if not 0 <= start < n:
        raise ValueError(f"Start vertex must be between 0 and {n - 1}")
    return matrix, start


def bfs(matrix, start):
    visited = [False] * len(matrix)
    order = []
    queue = deque([start])
    visited[start] = True

    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor, connected in enumerate(matrix[vertex]):
            if connected and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return order


def dfs(matrix, start):
    visited = [False] * len(matrix)
    order = []

    def visit(vertex):
        visited[vertex] = True
        order.append(vertex)
        for neighbor, connected in enumerate(matrix[vertex]):
            if connected and not visited[neighbor]:
                visit(neighbor)

    visit(start)
    return order


def main():
    try:
        matrix, start = read_graph(INPUT_FILE)
        bfs_order = bfs(matrix, start)
        dfs_order = dfs(matrix, start)
        result = (
            "Graph Traversal Using Adjacency Matrix\n"
            f"Starting vertex: {start}\n"
            f"BFS traversal: {' '.join(map(str, bfs_order))}\n"
            f"DFS traversal: {' '.join(map(str, dfs_order))}\n"
        )
        print(result, end="")
        OUTPUT_FILE.write_text(result, encoding="utf-8")
        print(f"Results saved to {OUTPUT_FILE.name}")
    except (ValueError, OSError) as error:
        print(f"Error: {error}")
        print("Check input.txt format and try again.")


if __name__ == "__main__":
    main()
