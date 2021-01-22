#!/usr/bin/python3
"""returns a list of lists of integers\
 representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    You are not allowed to import any module
    """
    lis = []
    if n <= 0:
        return lis
    for i in range(0, n):
        tmp = []
        tmp.append(1)
        j = 0
        while j < (i - 1):
            tmp.append(lis[i - 1][j] + lis[i - 1][j + 1])
            j += 1
        if i != 0:
            tmp.append(1)
        lis.append(tmp)
    return lis
