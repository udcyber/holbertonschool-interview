#!/usr/bin/python3
"""
Determine if all the boxes can be opened
n is a number of locked boxes
each box is numbered sequentially from 0 to n -1
A key with the same number as a box opens that box
all keys will be positive integers
There can be keys that do not have boxes
Return: True if yes, False otherwise
"""


def canUnlockAll(boxes):
    """Determine if all the boxes can be opened."""
    n = len(boxes)
    checked_b = set([0])
    unchecked_b = set(boxes[0]).difference(set([0]))
    while len(unchecked_b) > 0:
        id_b = unchecked_b.pop()
        if not id_b or id_b >= n or id_b < 0:
            continue
        if id_b not in checked_b:
            unchecked_b = unchecked_b.union(boxes[id_b])
            checked_b.add(id_b)
    return n == len(checked_b)
