"""
Problem: Find the Lowest Common Ancestor
Description:
    Write a function to find the lowest common ancestor of two nodes.
    The function takes root of binary tree and two node values as input.

Expected Output:
    Input: Nodes 2 and 4
    Output: 3
"""

from src.data_structures.binary_tree import BinaryTree
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def find_lca(root, n1, n2):
    if root is None:
        return None
    if root.value == n1 or root.value == n2:
        return root
    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca else right_lca


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(3)
    tree.insert(2)
    tree.insert(4)
    tree.insert(1)
    tree.insert(5)
    print("Inorder Traversal:", tree.inorder_traversal())
    lca = find_lca(tree.root, 2, 4)
    print("Lowest Common Ancestor of 2 and 4:", lca.value if lca else None)
