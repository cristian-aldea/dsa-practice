from __future__ import annotations


class Node:
    def __init__(self, index: int, data):
        self.index = index
        self.data = data
        self.connections: list[Node] = []

    def connect(self, *others):
        for other in others:
            self.connections.append(other)

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return self.__str__()


class BinaryNode:
    def __init__(self, data):
        self.right: BinaryNode = None
        self.left: BinaryNode = None
        self.data: int = data

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return self.__str__()


graph = []
graph.append(Node(0, "n0"))
graph.append(Node(1, "n1"))
graph.append(Node(2, "n2"))
graph.append(Node(3, "n3"))
graph.append(Node(4, "n4"))
graph.append(Node(5, "n5"))
graph.append(Node(6, "n6"))
graph.append(Node(7, "n7"))
graph.append(Node(8, "n8"))

graph[0].connect(graph[1], graph[3], graph[8])
graph[1].connect(graph[0], graph[7])
graph[2].connect(graph[3], graph[5], graph[7])
graph[3].connect(graph[0], graph[2], graph[4])
graph[4].connect(graph[3], graph[8])
graph[5].connect(graph[2], graph[6])
graph[6].connect(graph[5])
graph[7].connect(graph[1], graph[2])
graph[8].connect(graph[0], graph[4])


bst = BinaryNode(10)

b0 = BinaryNode(2)
b1 = BinaryNode(4)
b2 = BinaryNode(5)
b3 = BinaryNode(12)
b4 = BinaryNode(15)
b5 = BinaryNode(17)

bst.left = b1
bst.right = b4

b1.left = b0
b1.right = b2

b4.left = b3
b4.right = b5
