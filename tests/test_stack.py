import pytest
from src.data_structures.stack import Stack


def test_stack_push():
    """
    Tests pushing elements onto the stack.
    """
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert (
        stack.peek() == 3
    ), "Push operation failed to set the correct top element."
    assert stack.size() == 3, "Stack size is incorrect after pushes."


def test_stack_pop():
    """
    Tests popping elements from the stack.
    """
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert (
        stack.pop() == 3
    ), "Pop operation failed to return the correct top element."
    assert (
        stack.pop() == 2
    ), "Pop operation failed to return the correct second element."
    assert (
        stack.pop() == 1
    ), "Pop operation failed to return the correct last element."
    assert (
        stack.is_empty() is True
    ), "Stack should be empty after popping all elements."


def test_stack_pop_empty():
    """
    Tests popping from an empty stack.
    """
    stack = Stack()
    with pytest.raises(IndexError, match="pop from empty stack"):
        stack.pop()


def test_stack_peek():
    """
    Tests peeking at the top element of the stack.
    """
    stack = Stack()
    stack.push(1)
    assert (
        stack.peek() == 1
    ), "Peek operation failed to return the correct top element."
    stack.push(2)
    assert (
        stack.peek() == 2
    ), "Peek operation failed after pushing a new element."
    stack.pop()
    assert (
        stack.peek() == 1
    ), "Peek operation failed after popping the top element."


def test_stack_peek_empty():
    """
    Tests peeking at an empty stack.
    """
    stack = Stack()
    with pytest.raises(IndexError, match="peek from empty stack"):
        stack.peek()


def test_stack_is_empty():
    """
    Tests the is_empty method of the stack.
    """
    stack = Stack()
    assert stack.is_empty() is True, "Stack should be empty initially."
    stack.push(1)
    assert (
        stack.is_empty() is False
    ), "Stack should not be empty after pushing an element."
    stack.pop()
    assert (
        stack.is_empty() is True
    ), "Stack should be empty after popping all elements."


def test_stack_size():
    """
    Tests the size method of the stack.
    """
    stack = Stack()
    assert stack.size() == 0, "Size should be 0 for an empty stack."
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2, "Size calculation is incorrect after pushes."
    stack.pop()
    assert stack.size() == 1, "Size calculation is incorrect after a pop."


def test_stack_clear():
    """
    Tests clearing all elements from the stack.
    """
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.clear()
    assert stack.is_empty() is True, "Stack should be empty after clearing."
    assert stack.size() == 0, "Stack size should be 0 after clearing."
