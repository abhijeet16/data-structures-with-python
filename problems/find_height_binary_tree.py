"""
Problem: Find the Height of a Binary Tree
Description:
    Write a function to find the height of a binary tree.

Expected Output:
    Input: [5, 3, 7, 2, 4]
    Output: 3
"""

import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures.binary_tree import BinaryTree

def find_height(node):
    if node is None:
        return 0
    left_height = find_height(node.left)
    right_height = find_height(node.right)
    return max(left_height, right_height) + 1

if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    print("Inorder Traversal:", tree.inorder_traversal())
    print("Height of Tree:", find_height(tree.root))