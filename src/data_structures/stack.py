from typing import Any, List


class Stack:
    """
    Represents a stack data structure (LIFO - Last In, First Out).

    Attributes:
        items (List[Any]): The list used to store elements in the stack.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.items: List[Any] = []

    def push(self, item: Any) -> None:
        """
        Adds an item to the top of the stack.

        Args:
            item (Any): The item to add to the stack.
        """
        self.items.append(item)

    def pop(self) -> Any:
        """
        Removes and returns the item at the top of the stack.

        Returns:
            Any: The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self) -> Any:
        """
        Returns the item at the top of the stack without removing it.

        Returns:
            Any: The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self) -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return len(self.items)

    def clear(self) -> None:
        """
        Removes all items from the stack.
        """
        self.items.clear()

    def display(self) -> List[Any]:
        """
        Returns a list of all items in the stack.

        Returns:
            List[Any]: A list of all items in the stack.
        """
        return self.items[:]
