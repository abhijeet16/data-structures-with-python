from typing import Any, List


class Queue:
    """
    Represents a queue data structure (FIFO - First In, First Out).

    Attributes:
        items (List[Any]): The list used to store elements in the queue.
    """

    def __init__(self):
        """
        Initializes an empty queue.
        """
        self.items: List[Any] = []

    def enqueue(self, item: Any) -> None:
        """
        Adds an item to the end of the queue.

        Args:
            item (Any): The item to add to the queue.
        """
        self.items.append(item)

    def dequeue(self) -> Any:
        """
        Removes and returns the item at the front of the queue.

        Returns:
            Any: The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from an empty queue")

    def front(self) -> Any:
        """
        Returns the item at the front of the queue without removing it.

        Returns:
            Any: The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if not self.is_empty():
            return self.items[0]
        raise IndexError("front from an empty queue")

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self) -> int:
        """
        Returns the number of items in the queue.

        Returns:
            int: The number of items in the queue.
        """
        return len(self.items)

    def clear(self) -> None:
        """
        Removes all items from the queue.
        """
        self.items.clear()

    def display(self) -> List[Any]:
        """
        Returns a list of all items in the queue.

        Returns:
            List[Any]: A list of all items in the queue.
        """
        return self.items[:]
