#!/usr/bin/python3

"""Contains a function that prints the diagonal difference
    of a 3 * 3 matrix
"""


import math
import os
import random
import re
import sys
from typing import List


def get_diagonal_difference(matrix: List[List]) -> int:
    """
    A func that gets the diagonal difference of a 3*3 matrix
    :param matrix: A 3*3 matrix which is a list of lists
    :return: The diagonal difference
    """
    diagonal_sum = 0
    anti_diagonal_sum = 0
    diagonal_elements = [matrix[i][i] for i in range(len(matrix))]
    anti_diagonal_elements = [matrix[i][len(matrix) - i - 1] for i in range(len(matrix))]
    for i, j in zip(diagonal_elements, anti_diagonal_elements):
        diagonal_sum += i
        anti_diagonal_sum += j
    difference = diagonal_sum - anti_diagonal_sum
    return abs(difference)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = get_diagonal_difference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()