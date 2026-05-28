#!/usr/bin/python3
"""
The test editor can only execute [Copy All] and [Paste]
Given a number n
Write a method that calculates the fewest number of operations needed
to result in exactly n H character in the file
"""


def minOperations(n):
    """
    Calculate the fewest operations needed to get n H characters.
        Args:
            n: number of operations
        Return:
            An integer.
            0 if n is impossible to achieve.
    """
    lastcopy = "H"
    totalH = "H"
    operations = 0
    while (len(totalH) < n):
        if n % len(totalH) == 0:
            operations += 2
            lastcopy = totalH
            totalH += totalH
        else:
            operations += 1
            totalH += lastcopy
    if len(totalH) != n:
        return 0
    return operations
