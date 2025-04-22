"""
Problem: Implement a Circular Queue
Description:
    Demonstrate the behavior of a circular queue using the Queue class.

Expected Output:
    Enqueue: [1, 2, 3]
    Dequeue: [2, 3]
"""

import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures.queue import Queue

def demonstrate_circular_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue after enqueues:", queue.display())
    queue.dequeue()
    print("Queue after dequeue:", queue.display())

if __name__ == "__main__":
    demonstrate_circular_queue()