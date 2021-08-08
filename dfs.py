from __future__ import annotations

from common import Node, nodes


def dfs(node: Node, visited: list[bool]):
    if visited[node.index]:
        return

    print(node.data)
    visited[node.index] = True

    for connection in node.connections:
        dfs(connection, visited)


visited = [False] * len(nodes)

dfs(nodes[0], visited)
