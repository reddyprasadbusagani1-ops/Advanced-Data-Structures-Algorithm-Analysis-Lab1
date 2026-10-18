"""Experiment 8: Single-source shortest paths using Dijkstra's greedy algorithm.
Compares adjacency-matrix and adjacency-list representations.
Input format: first line: V E; next E lines: u v weight (undirected); final line: source.
Vertices are numbered 0 to V-1. Edge weights must be non-negative.
"""
import heapq
import time
from math import inf
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input.txt"
OUTPUT_FILE = BASE_DIR / "output.txt"


def read_graph(path):
    tokens = path.read_text(encoding="utf-8").split()
    if len(tokens) < 3:
        raise ValueError("Input must contain V E, edge lines, and a source vertex.")
    it = iter(tokens)
    vertices, edges = int(next(it)), int(next(it))
    if vertices <= 0 or edges < 0:
        raise ValueError("V must be positive and E must be non-negative.")
    edge_list = []
    for _ in range(edges):
        try:
            u, v, w = int(next(it)), int(next(it)), float(next(it))
        except StopIteration as exc:
            raise ValueError("Not enough values for the declared edges.") from exc
        if not (0 <= u < vertices and 0 <= v < vertices):
            raise ValueError(f"Vertex must be in range 0..{vertices - 1}.")
        if w < 0:
            raise ValueError("Dijkstra's algorithm requires non-negative weights.")
        edge_list.append((u, v, w))
    try:
        source = int(next(it))
    except StopIteration as exc:
        raise ValueError("Please include the source vertex after the edges.") from exc
    if not 0 <= source < vertices:
        raise ValueError(f"Source must be in range 0..{vertices - 1}.")
    return vertices, edge_list, source


def make_matrix(vertices, edges):
    matrix = [[inf] * vertices for _ in range(vertices)]
    for i in range(vertices):
        matrix[i][i] = 0
    for u, v, w in edges:
        matrix[u][v] = min(matrix[u][v], w)
        matrix[v][u] = min(matrix[v][u], w)
    return matrix


def dijkstra_matrix(matrix, source):
    n = len(matrix)
    distances = [inf] * n
    visited = [False] * n
    distances[source] = 0
    for _ in range(n):
        u = -1
        best = inf
        for vertex in range(n):
            if not visited[vertex] and distances[vertex] < best:
                best, u = distances[vertex], vertex
        if u == -1:
            break
        visited[u] = True
        for v, weight in enumerate(matrix[u]):
            if weight != inf and not visited[v] and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    return distances


def make_adjacency_list(vertices, edges):
    graph = [[] for _ in range(vertices)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph


def dijkstra_list(graph, source):
    distances = [inf] * len(graph)
    distances[source] = 0
    heap = [(0, source)]
    while heap:
        current_distance, u = heapq.heappop(heap)
        if current_distance != distances[u]:
            continue
        for v, weight in graph[u]:
            candidate = current_distance + weight
            if candidate < distances[v]:
                distances[v] = candidate
                heapq.heappush(heap, (candidate, v))
    return distances


def show_distance(value):
    if value == inf:
        return "INF"
    return str(int(value)) if value.is_integer() else str(value)


def main():
    try:
        vertices, edges, source = read_graph(INPUT_FILE)
        matrix = make_matrix(vertices, edges)
        graph = make_adjacency_list(vertices, edges)

        start = time.perf_counter()
        matrix_distances = dijkstra_matrix(matrix, source)
        matrix_time = time.perf_counter() - start

        start = time.perf_counter()
        list_distances = dijkstra_list(graph, source)
        list_time = time.perf_counter() - start

        lines = [
            "Experiment 8: Single-Source Shortest Path (Dijkstra's Algorithm)",
            f"Number of vertices: {vertices}",
            f"Source vertex: {source}",
            "",
            "Shortest distances using adjacency matrix:",
        ]
        lines += [f"Vertex {v}: {show_distance(d)}" for v, d in enumerate(matrix_distances)]
        lines += ["", "Shortest distances using adjacency list:"]
        lines += [f"Vertex {v}: {show_distance(d)}" for v, d in enumerate(list_distances)]
        lines += [
            "",
            f"Results match: {'Yes' if matrix_distances == list_distances else 'No'}",
            f"Adjacency-matrix execution time: {matrix_time:.8f} seconds",
            f"Adjacency-list execution time: {list_time:.8f} seconds",
            "Note: Execution times vary by computer and run.",
        ]
        result = "\n".join(lines)
        print(result)
        OUTPUT_FILE.write_text(result + "\n", encoding="utf-8")
        print(f"\nResults saved to {OUTPUT_FILE.name}")
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}")
        print("Check input.txt format and try again.")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
