"""
Problem: Find the Middle Element of a Linked List
Description:
    Write a function to find the middle element of a linked list.
    If the list has an even number of elements, return the first middle element.

Expected Output:
    Input: [1, 2, 3, 4, 5]
    Output: 3
"""

import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures.linked_list import LinkedList

def find_middle(linked_list):
    slow = linked_list.head
    fast = linked_list.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data if slow else None

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    print("Linked List:", ll.display())
    print("Middle Element:", find_middle(ll))