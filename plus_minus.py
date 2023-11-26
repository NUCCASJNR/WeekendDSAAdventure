#!/usr/bin/python3

"""Contains a function that calculate the ratios
 of its elements that are positive, negative, and zero.
"""

import math
import os
import random
import re
import sys
from typing import List


def plus_or_minus(arr: List[int]) -> str:
    """
    calculate the ratios
    of its elements that are positive, negative, and zero.
    :param arr: List of int
    :return:
    """
    p_count = 0
    n_count = 0
    z_count = 0
    len_arr = len(arr)
    for i in arr:
        if i > 0:
            p_count += 1 / len_arr
        if i < 0:
            n_count += 1 / len_arr
        if i == 0:
            z_count += 1 / len_arr
    print(f"{p_count:.6f}\n{n_count:.6f}\n{z_count:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    (plus_or_minus(arr))

