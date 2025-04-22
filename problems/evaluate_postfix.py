"""
Problem: Evaluate Postfix Expression
Description:
    Write a function to evaluate a postfix expression using a stack.

Expected Output:
    Input: "231*+9-"
    Output: -4
"""

import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures.stack import Stack

def evaluate_postfix(expression):
    stack = Stack()
    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.push(a + b)
            elif char == '-':
                stack.push(a - b)
            elif char == '*':
                stack.push(a * b)
            elif char == '/':
                stack.push(a // b)
    return stack.pop()

if __name__ == "__main__":
    postfix_expression = "231*+9-"
    print(f"Postfix Expression: {postfix_expression}")
    print(f"Result: {evaluate_postfix(postfix_expression)}")