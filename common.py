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


nodes = []
nodes.append(Node(0, "n0"))
nodes.append(Node(1, "n1"))
nodes.append(Node(2, "n2"))
nodes.append(Node(3, "n3"))
nodes.append(Node(4, "n4"))
nodes.append(Node(5, "n5"))
nodes.append(Node(6, "n6"))
nodes.append(Node(7, "n7"))
nodes.append(Node(8, "n8"))

nodes[0].connect(nodes[1], nodes[3], nodes[8])
nodes[1].connect(nodes[0], nodes[7])
nodes[2].connect(nodes[3], nodes[5], nodes[7])
nodes[3].connect(nodes[0], nodes[2], nodes[4])
nodes[4].connect(nodes[3], nodes[8])
nodes[5].connect(nodes[2], nodes[6])
nodes[6].connect(nodes[5])
nodes[7].connect(nodes[1], nodes[2])
nodes[8].connect(nodes[0], nodes[4])


bst_root = BinaryNode(10)

b0 = BinaryNode(2)
b1 = BinaryNode(4)
b2 = BinaryNode(5)
b3 = BinaryNode(12)
b4 = BinaryNode(15)
b5 = BinaryNode(17)

bst_root.left = b1
bst_root.right = b4

b1.left = b0
b1.right = b2

b4.left = b3
b4.right = b5
