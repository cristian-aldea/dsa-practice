from __future__ import annotations

from common import Node, graph


def bfs(nodes: list[Node]):
    # visit current node
    # add children to queue
    # repeat
    queue: list[Node] = []
    visited = [False] * len(nodes)

    queue.append(nodes[0])
    visited[nodes[0].index] = True

    while queue:
        el = queue.pop(0)
        print(el)

        for connection in el.connections:
            if not visited[connection.index]:
                queue.append(connection)
                visited[connection.index] = True
    pass


if __name__ == "__main__":
    bfs(graph)
