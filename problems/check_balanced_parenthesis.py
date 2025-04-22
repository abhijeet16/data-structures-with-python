"""
Problem: Check for Balanced Parentheses
Description:
    Write a function to check if a string has balanced parentheses using a stack.

Expected Output:
    Input: "((()))"
    Output: True
    Input: "(()"
    Output: False
"""

import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures.stack import Stack

def is_balanced_parentheses(string):
    stack = Stack()
    for char in string:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

if __name__ == "__main__":
    test_string = "((()))"
    print(f"Input: {test_string}")
    print(f"Is Balanced: {is_balanced_parentheses(test_string)}")