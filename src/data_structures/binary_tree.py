from typing import Optional, List


class Node:
    """
    Represents a single node in the binary tree.

    Attributes:
        value (int): The value stored in the node.
        left (Optional[Node]): Reference to the left child node.
        right (Optional[Node]): Reference to the right child node.
    """

    def __init__(self, key: int):
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.value: int = key


class BinaryTree:
    """
    Represents a binary search tree (BST) with basic operations.

    Attributes:
        root (Optional[Node]): The root node of the binary tree.
    """

    def __init__(self):
        """
        Initializes an empty binary tree.
        """
        self.root: Optional[Node] = None

    def insert(self, key: int) -> None:
        """
        Inserts a new key into the binary tree.

        Args:
            key (int): The value to insert into the tree.

        Raises:
            ValueError: If the key is not an integer.
        """
        if not isinstance(key, int):
            raise ValueError(
                "Only integer keys are allowed in the binary tree."
            )
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, current_node: Node, key: int) -> None:
        """
        Helper method to recursively insert a key into the tree.

        Args:
            current_node (Node): The current node being traversed.
            key (int): The value to insert.
        """
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursively(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursively(current_node.right, key)

    def search(self, key: int) -> bool:
        """
        Searches for a key in the binary tree.

        Args:
            key (int): The value to search for.

        Returns:
            bool: True if the key is found, False otherwise.
        """
        return self._search_recursively(self.root, key)

    def _search_recursively(
        self, current_node: Optional[Node], key: int
    ) -> bool:
        """
        Helper method to recursively search for a key in the tree.

        Args:
            current_node (Optional[Node]): The current node being traversed.
            key (int): The value to search for.

        Returns:
            bool: True if the key is found, False otherwise.
        """
        if current_node is None:
            return False
        if current_node.value == key:
            return True
        if key < current_node.value:
            return self._search_recursively(current_node.left, key)
        return self._search_recursively(current_node.right, key)

    def inorder_traversal(self) -> List[int]:
        """
        Performs an in-order traversal of the binary tree.

        Returns:
            List[int]: A list of values in ascending order.
        """
        return self._inorder_recursively(self.root)

    def _inorder_recursively(self, current_node: Optional[Node]) -> List[int]:
        """
        Helper method to recursively perform an in-order traversal.

        Args:
            current_node (Optional[Node]): The current node being traversed.

        Returns:
            List[int]: A list of values in ascending order.
        """
        elements: List[int] = []
        if current_node:
            elements += self._inorder_recursively(current_node.left)
            elements.append(current_node.value)
            elements += self._inorder_recursively(current_node.right)
        return elements

    def is_empty(self) -> bool:
        """
        Checks if the binary tree is empty.

        Returns:
            bool: True if the tree is empty, False otherwise.
        """
        return self.root is None

    def find_min(self) -> Optional[int]:
        """
        Finds the minimum value in the binary tree.

        Returns:
            Optional[int]: The minimum value, or None if the tree is empty.
        """
        if self.root is None:
            return None
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node.value

    def find_max(self) -> Optional[int]:
        """
        Finds the maximum value in the binary tree.

        Returns:
            Optional[int]: The maximum value, or None if the tree is empty.
        """
        if self.root is None:
            return None
        current_node = self.root
        while current_node.right:
            current_node = current_node.right
        return current_node.value
