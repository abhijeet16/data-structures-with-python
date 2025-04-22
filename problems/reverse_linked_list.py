"""
Problem: Reverse a Linked List
Description:
    Write a function to reverse a linked list using the LinkedList class.
    The function should return the reversed linked list.

Expected Output:
    Input: [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]
"""

import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.data_structures.linked_list import LinkedList

def reverse_linked_list(linked_list):
    reversed_list = LinkedList()
    current = linked_list.head
    stack = []
    while current:
        stack.append(current.data)
        current = current.next
    while stack:
        reversed_list.append(stack.pop())
    return reversed_list

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    print("Original List:", ll.display())
    reversed_ll = reverse_linked_list(ll)
    print("Reversed List:", reversed_ll.display())