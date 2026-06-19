#!/usr/bin/env python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an NxN chessboard.
Write a program that solves the N queens problem.
"""

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N", file=sys.stderr)
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number", file=sys.stderr)
    sys.exit(1)

if n < 4:
    print("N must be at least 4", file=sys.stderr)
    sys.exit(1)


def queens(n, a=None, b=None, c=None):
    """Search for possible positions."""
    if a is None:
        a = []
    if b is None:
        b = []
    if c is None:
        c = []
    if len(a) == n:
        yield a
    else:
        idx = len(a)
        for j in range(n):
            if j not in a and idx + j not in b and idx - j not in c:
                yield from queens(n, a + [j], b + [idx + j], c + [idx - j])


def solve(n):
    """Queens solution."""
    for solution in queens(n):
        print([[i, solution[i]] for i in range(n)])


if __name__ == "__main__":
    solve(n)
