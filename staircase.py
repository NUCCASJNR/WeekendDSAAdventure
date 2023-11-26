#!/usr/bin/python3

"""This module contains a function to print a staircase pattern."""

import math
import os
import random
import re
import sys


def staircase(n: int) -> None:
    """
    Print a staircase pattern of a given size.

    Parameters:
    - n (int): The size of the staircase.

    Returns:
    - None
    """
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        hashes = '#' * i
        print(f'{spaces}{hashes}')


if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)
