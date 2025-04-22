# main.py

from data_structures.linked_list import LinkedList
from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.binary_tree import BinaryTree


def demonstrate_linked_list():
    """
    Demonstrates basic operations on a LinkedList.
    """
    print("Linked List Operations:")
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    print("Initial List:", linked_list.display())
    linked_list.delete(2)
    print("After Deleting 2:", linked_list.display())
    print("Is the list empty?", linked_list.is_empty())
    print()


def demonstrate_stack():
    """
    Demonstrates basic operations on a Stack.
    """
    print("Stack Operations:")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack after pushes:", stack.display())
    print("Top element:", stack.peek())
    stack.pop()
    print("Stack after pop:", stack.display())
    print("Is the stack empty?", stack.is_empty())
    print()


def demonstrate_queue():
    """
    Demonstrates basic operations on a Queue.
    """
    print("Queue Operations:")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue after enqueues:", queue.display())
    print("Front element:", queue.front())
    queue.dequeue()
    print("Queue after dequeue:", queue.display())
    print("Is the queue empty?", queue.is_empty())
    print()


def demonstrate_binary_tree():
    """
    Demonstrates basic operations on a BinaryTree.
    """
    print("Binary Tree Operations:")
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(7)
    binary_tree.insert(2)
    binary_tree.insert(4)
    print("Inorder Traversal:", binary_tree.inorder_traversal())
    print("Search for 3:", binary_tree.search(3))
    print("Search for 10:", binary_tree.search(10))
    print("Minimum value:", binary_tree.find_min())
    print("Maximum value:", binary_tree.find_max())
    print("Is the tree empty?", binary_tree.is_empty())
    print()


def main():
    """
    Main function to demonstrate operations on various data structures.
    """
    print("=== Data Structures Demonstration ===\n")
    demonstrate_linked_list()
    demonstrate_stack()
    demonstrate_queue()
    demonstrate_binary_tree()


if __name__ == "__main__":
    main()
