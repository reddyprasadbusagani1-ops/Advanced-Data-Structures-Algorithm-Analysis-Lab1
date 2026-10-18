"""Find biconnected components of an undirected graph using Tarjan's algorithm."""
from collections import defaultdict


def find_biconnected_components(vertex_count, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    discovery = [-1] * vertex_count
    low = [-1] * vertex_count
    parent = [-1] * vertex_count
    edge_stack = []
    components = []
    timer = 0

    def dfs(u):
        nonlocal timer
        discovery[u] = low[u] = timer
        timer += 1
        children = 0

        for v in graph[u]:
            if discovery[v] == -1:
                parent[v] = u
                children += 1
                edge_stack.append((u, v))
                dfs(v)
                low[u] = min(low[u], low[v])

                # u separates a biconnected component from its child subtree.
                if (parent[u] == -1 and children > 1) or (
                    parent[u] != -1 and low[v] >= discovery[u]
                ):
                    component = []
                    while edge_stack:
                        edge = edge_stack.pop()
                        component.append(edge)
                        if edge == (u, v):
                            break
                    if component:
                        components.append(component)
            elif v != parent[u] and discovery[v] < discovery[u]:
                low[u] = min(low[u], discovery[v])
                edge_stack.append((u, v))

    for vertex in range(vertex_count):
        if discovery[vertex] == -1:
            dfs(vertex)
            if edge_stack:
                components.append(edge_stack[:])
                edge_stack.clear()

    return components


def main():
    try:
        with open("input.txt", "r", encoding="utf-8") as file:
            values = [line.strip() for line in file if line.strip() and not line.lstrip().startswith("#")]
    except FileNotFoundError:
        print("input.txt not found. Please create it in the same folder.")
        return

    try:
        vertex_count, edge_count = map(int, values[0].split())
        edges = [tuple(map(int, line.split())) for line in values[1:1 + edge_count]]
        if len(edges) != edge_count or any(len(edge) != 2 for edge in edges):
            raise ValueError("The number of edges does not match the input header.")
        if any(u < 0 or u >= vertex_count or v < 0 or v >= vertex_count for u, v in edges):
            raise ValueError("Vertex labels must be between 0 and V-1.")
    except (ValueError, IndexError) as error:
        print(f"Invalid input: {error}")
        return

    components = find_biconnected_components(vertex_count, edges)
    lines = [f"Number of biconnected components: {len(components)}"]
    for index, component in enumerate(components, start=1):
        vertices = sorted({vertex for edge in component for vertex in edge})
        lines.append(f"Component {index}: edges {sorted(tuple(sorted(edge)) for edge in component)}")
        lines.append(f"           vertices {vertices}")

    if not components:
        lines.append("No edges found; the graph has no edge-based biconnected components.")

    result = "\n".join(lines)
    print(result)
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(result + "\n")
    print("Results saved to output.txt")


if __name__ == "__main__":
    main()
