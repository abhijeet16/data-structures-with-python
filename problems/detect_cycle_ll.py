"""
Problem: Detect a Cycle in a Linked List
Description:
    Write a function to detect if a linked list contains a cycle.

Expected Output:
    Input: [1, 2, 3, 4, 5] (with a cycle)
    Output: True
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_structures.linked_list import LinkedList

def detect_cycle(linked_list):
    slow = linked_list.head
    fast = linked_list.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    # Create a cycle for testing
    ll.head.next.next.next.next.next = ll.head.next
    print("Cycle Detected:", detect_cycle(ll))