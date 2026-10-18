"""Experiment 5: BFS and DFS using an adjacency list.

Input file format (input.txt):
First line: number of vertices and number of edges
Next m lines: one undirected edge as: u v
Last line: starting vertex
Vertices are numbered 0 to V-1.
"""
from collections import deque
from pathlib import Path

INPUT_FILE = Path(__file__).with_name("input.txt")
OUTPUT_FILE = Path(__file__).with_name("output.txt")


def read_graph(path=INPUT_FILE):
    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines()
             if line.strip() and not line.lstrip().startswith("#")]
    if not lines:
        raise ValueError("input.txt is empty")
    first = lines[0].split()
    if len(first) != 2:
        raise ValueError("First line must contain: number_of_vertices number_of_edges")
    vertices, edges = map(int, first)
    if vertices <= 0 or edges < 0:
        raise ValueError("Number of vertices must be positive and edges cannot be negative")
    if len(lines) < edges + 2:
        raise ValueError(f"Expected {edges} edge lines and one starting-vertex line")

    graph = [[] for _ in range(vertices)]
    for i in range(1, edges + 1):
        pair = lines[i].split()
        if len(pair) != 2:
            raise ValueError(f"Edge line {i} must contain two vertex numbers")
        u, v = map(int, pair)
        if not (0 <= u < vertices and 0 <= v < vertices):
            raise ValueError(f"Edge ({u}, {v}) contains a vertex outside 0..{vertices - 1}")
        graph[u].append(v)
        graph[v].append(u)  # Remove this line for a directed graph.

    start = int(lines[edges + 1].split()[0])
    if not 0 <= start < vertices:
        raise ValueError(f"Starting vertex must be between 0 and {vertices - 1}")
    # Sorting neighbors makes the traversal output predictable.
    for neighbors in graph:
        neighbors.sort()
    return graph, start


def bfs(graph, start):
    visited = [False] * len(graph)
    order = []
    queue = deque([start])
    visited[start] = True
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return order


def dfs(graph, start):
    visited = [False] * len(graph)
    order = []

    def visit(vertex):
        visited[vertex] = True
        order.append(vertex)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visit(neighbor)

    visit(start)
    return order


def main():
    try:
        graph, start = read_graph()
        bfs_result = bfs(graph, start)
        dfs_result = dfs(graph, start)
        lines = [
            "Adjacency List:",
            *[f"{i}: {' '.join(map(str, neighbors)) if neighbors else '(no neighbors)'}"
              for i, neighbors in enumerate(graph)],
            f"Starting vertex: {start}",
            "BFS traversal: " + " ".join(map(str, bfs_result)),
            "DFS traversal: " + " ".join(map(str, dfs_result)),
        ]
        result = "\n".join(lines)
        print(result)
        OUTPUT_FILE.write_text(result + "\n", encoding="utf-8")
        print(f"\nResults saved to {OUTPUT_FILE.name}")
    except (OSError, ValueError) as error:
        print(f"Input error: {error}")
        print("Check input.txt format. See README.md for an example.")


if __name__ == "__main__":
    main()
