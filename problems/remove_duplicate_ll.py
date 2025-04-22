"""
Problem: Remove Duplicates from a Linked List
Description:
    Write a function to remove duplicate elements from an unsorted linked list.

Expected Output:
    Input: [1, 2, 2, 3, 4, 4, 5]
    Output: [1, 2, 3, 4, 5]
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_structures.linked_list import LinkedList

def remove_duplicates(linked_list):
    current = linked_list.head
    seen = set()
    prev = None
    while current:
        if current.data in seen:
            prev.next = current.next
        else:
            seen.add(current.data)
            prev = current
        current = current.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(4)
    ll.append(5)
    print("Original List:", ll.display())
    remove_duplicates(ll)
    print("List after removing duplicates:", ll.display())