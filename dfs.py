from __future__ import annotations

from common import Node, graph


def dfs(node: Node, visited: list[bool]):
    # visit current node
    # visit children in order, recursively
    if visited[node.index]:
        return

    print(node.data)
    visited[node.index] = True

    for connection in node.connections:
        dfs(connection, visited)


visited = [False] * len(graph)

dfs(graph[0], visited)
