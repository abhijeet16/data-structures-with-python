import pytest
from src.data_structures.binary_tree import BinaryTree


def test_insert():
    """
    Tests the insertion of elements into the binary tree.
    """
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    assert tree.inorder_traversal() == [5, 10, 15], "Inorder traversal after insertions is incorrect."


def test_search():
    """
    Tests the search functionality of the binary tree.
    """
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    assert tree.search(10) is True, "Search for existing element 10 failed."
    assert tree.search(5) is True, "Search for existing element 5 failed."
    assert tree.search(15) is True, "Search for existing element 15 failed."
    assert tree.search(20) is False, "Search for non-existing element 20 failed."


def test_inorder_traversal():
    """
    Tests the inorder traversal of the binary tree.
    """
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(7)
    assert tree.inorder_traversal() == [2, 5, 7, 10, 15], "Inorder traversal is incorrect."


def test_find_min():
    """
    Tests finding the minimum value in the binary tree.
    """
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(7)
    assert tree.find_min() == 2, "Minimum value in the tree is incorrect."


def test_find_max():
    """
    Tests finding the maximum value in the binary tree.
    """
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(7)
    assert tree.find_max() == 15, "Maximum value in the tree is incorrect."


def test_is_empty():
    """
    Tests the is_empty method of the binary tree.
    """
    tree = BinaryTree()
    assert tree.is_empty() is True, "Tree should be empty initially."
    tree.insert(10)
    assert tree.is_empty() is False, "Tree should not be empty after insertion."


def test_empty_tree_operations():
    """
    Tests operations on an empty binary tree.
    """
    tree = BinaryTree()
    assert tree.inorder_traversal() == [], "Inorder traversal of an empty tree should be an empty list."
    assert tree.search(10) is False, "Search in an empty tree should return False."
    assert tree.find_min() is None, "Minimum value in an empty tree should be None."
    assert tree.find_max() is None, "Maximum value in an empty tree should be None."