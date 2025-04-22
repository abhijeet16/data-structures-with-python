"""
Problem: Sort a Stack
Description:
    Write a function to sort a stack in ascending order using only one additional stack.

Expected Output:
    Input: [3, 1, 4, 2]
    Output: [1, 2, 3, 4]
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_structures.stack import Stack

def sort_stack(stack):
    temp_stack = Stack()
    while not stack.is_empty():
        temp = stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            stack.push(temp_stack.pop())
        temp_stack.push(temp)
    return temp_stack

if __name__ == "__main__":
    stack = Stack()
    stack.push(3)
    stack.push(1)
    stack.push(4)
    stack.push(2)
    print("Original Stack:", stack.display())
    sorted_stack = sort_stack(stack)
    print("Sorted Stack:", sorted_stack.display())