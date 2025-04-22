"""
Problem: Generate Binary Numbers
Description:
    Write a function to generate binary numbers from 1 to N using a queue.

Expected Output:
    Input: 5
    Output: ['1', '10', '11', '100', '101']
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_structures.queue import Queue

def generate_binary_numbers(n):
    queue = Queue()
    result = []
    queue.enqueue("1")
    for _ in range(n):
        current = queue.dequeue()
        result.append(current)
        queue.enqueue(current + "0")
        queue.enqueue(current + "1")
    return result

if __name__ == "__main__":
    n = 7
    print("Total numbers to generate:", n)
    print("Binary Numbers:", generate_binary_numbers(n))