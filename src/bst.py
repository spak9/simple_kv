"""
A simple implementation of a binary search tree just to get up to speed.
"""


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def insert(root: Node, value: int):
    """
    Recursively inserts a node w.r.t `root`

    :param root: root Node
    :param value: int value to insert, if it doesn't exist
    :return:
    """
    # Base Case: reached the bottom most level; create new Node
    if root == None:
        return Node(value)

    # Recurse left
    if value < root.value:
        root.left = insert(root.left, value)

    # Recurse right
    elif value > root.value:
        root.right = insert(root.right, value)

    # Return the root node to have the recursive calls link
    return root


def find(root: Node, key: int):
    """
    Recursively find node w.r.t to `root`.

    :param root: root Node
    :param key:
    :return: bool
    """
    # Base case 1: root is None, value cannot be found
    if root is None:
        return False

    # Base case 2: key is found
    if root.value == key:
        return True

    # Recurse - key < root.value
    if key < root.value:
        return find(root.left, key)

    # Recurse - key > root.value
    else:
        return find(root.right, key)


if __name__ == '__main__':

    root = Node(15)
    keys = [10, 20, 8, 25, 3, 22]

    # Inserts
    for key in keys:
        insert(root, key)

    # Finds - all true
    for key in keys:
        print(find(root, key))
    print('\n' * 2)

    # Finds - all false
    non_keys = [1, 2, 4, 5, 6, 7, 9, 11, 12]
    for non_key in non_keys:
        print(find(root, non_key))
