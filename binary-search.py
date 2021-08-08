from __future__ import annotations

import random

from common import BinaryNode, bst_root


def binary_search_tree(node: BinaryNode, target: int):
    if node == None:
        print("Didn't find: {}".format(target))
        return -1

    print("Looking at {}".format(node.data))

    if target == node.data:
        print("Found it: {}".format(node.data))
        return node.data
    elif target > node.data:
        return binary_search_tree(node.right, target)
    else:
        return binary_search_tree(node.left, target)


def binary_search_arr(arr, min, max, target):
    if(min > max):
        print("Didn't find: {}".format(target))
        return -1

    middle = int((min + max)/2)

    print("min: {}, max: {}".format(min, max))
    if target == arr[middle]:
        print("Found it: {}".format(arr[middle]))
        return arr[middle]
    elif target < arr[middle]:
        binary_search_arr(arr, min, middle-1, target)
    else:
        binary_search_arr(arr, middle+1, max, target)


# binary_search_tree(bst_root, 12)

arr = [random.randint(0, 100) for _ in range(20)]
arr.sort()
binary_search_arr(arr, 0, len(arr)-1, arr[1])
