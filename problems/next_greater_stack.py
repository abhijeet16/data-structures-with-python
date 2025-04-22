"""
Problem: Next Greater Element
Description:
    Write a function to find the next greater element for each element in an array using a stack.

Expected Output:
    Input: [4, 5, 2, 10]
    Output: [5, 10, 10, -1]
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_structures.stack import Stack

def next_greater_element(arr):
    stack = Stack()
    result = [-1] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        while not stack.is_empty() and stack.peek() <= arr[i]:
            stack.pop()
        if not stack.is_empty():
            result[i] = stack.peek()
        stack.push(arr[i])
    return result

if __name__ == "__main__":
    arr = [4, 5, 2, 10]
    print("Input Array:", arr)
    print("Next Greater Elements:", next_greater_element(arr))