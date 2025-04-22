import pytest
from src.data_structures.queue import Queue


def test_enqueue():
    """
    Tests enqueuing elements into the queue.
    """
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.display() == [1, 2, 3], "Enqueue operation failed."


def test_dequeue():
    """
    Tests dequeuing elements from the queue.
    """
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert (
        queue.dequeue() == 1
    ), "Dequeue operation failed for the first element."
    assert queue.display() == [2, 3], "Queue state after dequeue is incorrect."
    assert (
        queue.dequeue() == 2
    ), "Dequeue operation failed for the second element."
    assert queue.display() == [
        3
    ], "Queue state after second dequeue is incorrect."


def test_dequeue_empty():
    """
    Tests dequeuing from an empty queue.
    """
    queue = Queue()
    with pytest.raises(IndexError, match="dequeue from an empty queue"):
        queue.dequeue()


def test_front():
    """
    Tests retrieving the front element of the queue.
    """
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.front() == 1, "Front operation failed for the first element."
    queue.dequeue()
    assert (
        queue.front() == 2
    ), "Front operation failed after dequeuing an element."


def test_front_empty():
    """
    Tests retrieving the front element from an empty queue.
    """
    queue = Queue()
    with pytest.raises(IndexError, match="front from an empty queue"):
        queue.front()


def test_is_empty():
    """
    Tests the is_empty method of the queue.
    """
    queue = Queue()
    assert queue.is_empty() is True, "Queue should be empty initially."
    queue.enqueue(1)
    assert (
        queue.is_empty() is False
    ), "Queue should not be empty after enqueue."
    queue.dequeue()
    assert (
        queue.is_empty() is True
    ), "Queue should be empty after dequeuing all elements."


def test_size():
    """
    Tests the size method of the queue.
    """
    queue = Queue()
    assert queue.size() == 0, "Size should be 0 for an empty queue."
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.size() == 2, "Size calculation is incorrect after enqueues."
    queue.dequeue()
    assert queue.size() == 1, "Size calculation is incorrect after dequeue."


def test_clear():
    """
    Tests clearing all elements from the queue.
    """
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.clear()
    assert queue.is_empty() is True, "Queue should be empty after clearing."
    assert (
        queue.display() == []
    ), "Queue display should be empty after clearing."
