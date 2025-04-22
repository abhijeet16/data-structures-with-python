import pytest
from src.data_structures.linked_list import LinkedList


def test_append():
    """
    Tests appending elements to the linked list.
    """
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.display() == [1, 2, 3], "Append operation failed."


def test_delete():
    """
    Tests deleting elements from the linked list.
    """
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.delete(2)
    assert ll.display() == [
        1,
        3,
    ], "Delete operation failed for middle element."
    ll.delete(1)
    assert ll.display() == [3], "Delete operation failed for head element."
    ll.delete(3)
    assert ll.display() == [], "Delete operation failed for last element."


def test_delete_nonexistent():
    """
    Tests deleting a non-existent element from the linked list.
    """
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    with pytest.raises(
        ValueError, match="Key 3 not found in the linked list."
    ):
        ll.delete(3)


def test_display():
    """
    Tests displaying elements of the linked list.
    """
    ll = LinkedList()
    assert ll.display() == [], "Display operation failed for an empty list."
    ll.append(1)
    ll.append(2)
    assert ll.display() == [
        1,
        2,
    ], "Display operation failed for a non-empty list."


def test_is_empty():
    """
    Tests the is_empty method of the linked list.
    """
    ll = LinkedList()
    assert (
        ll.is_empty() is True
    ), "is_empty should return True for an empty list."
    ll.append(1)
    assert (
        ll.is_empty() is False
    ), "is_empty should return False for a non-empty list."


def test_find():
    """
    Tests finding elements in the linked list.
    """
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.find(2) is True, "Find operation failed for an existing element."
    assert (
        ll.find(4) is False
    ), "Find operation failed for a non-existent element."


def test_length():
    """
    Tests the length of the linked list.
    """
    ll = LinkedList()
    assert ll.length() == 0, "Length should be 0 for an empty list."
    ll.append(1)
    ll.append(2)
    assert ll.length() == 2, "Length calculation is incorrect."
    ll.delete(1)
    assert ll.length() == 1, "Length calculation after deletion is incorrect."
