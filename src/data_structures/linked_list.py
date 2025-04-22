from typing import Optional, List, Any


class Node:
    """
    Represents a single node in the linked list.

    Attributes:
        data (Any): The data stored in the node.
        next (Optional[Node]): Reference to the next node in the list.
    """

    def __init__(self, data: Any):
        """
        Initializes a new node with the given data.

        Args:
            data (Any): The data to store in the node.
        """
        self.data: Any = data
        self.next: Optional[Node] = None


class LinkedList:
    """
    Represents a singly linked list with basic operations.

    Attributes:
        head (Optional[Node]): The head node of the linked list.
    """

    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head: Optional[Node] = None

    def append(self, data: Any) -> None:
        """
        Appends a new node with the given data to the end of the linked list.

        Args:
            data (Any): The data to append to the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete(self, key: Any) -> None:
        """
        Deletes the first node with the specified key from the linked list.

        Args:
            key (Any): The value of the node to delete.

        Raises:
            ValueError: If the key is not found in the linked list.
        """
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            raise ValueError(f"Key {key} not found in the linked list.")
        prev_node.next = current_node.next
        current_node = None

    def display(self) -> List[Any]:
        """
        Returns a list of all elements in the linked list.

        Returns:
            List[Any]: A list of all elements in the linked list.
        """
        current_node = self.head
        elements: List[Any] = []
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.

        Returns:
            bool: True if the linked list is empty, False otherwise.
        """
        return self.head is None

    def find(self, key: Any) -> bool:
        """
        Searches for a node with the specified key in the linked list.

        Args:
            key (Any): The value to search for.

        Returns:
            bool: True if the key is found, False otherwise.
        """
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False

    def length(self) -> int:
        """
        Calculates the length of the linked list.

        Returns:
            int: The number of nodes in the linked list.
        """
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
