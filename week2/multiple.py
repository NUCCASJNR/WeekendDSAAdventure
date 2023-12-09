#!/usr/bin/env python3

"""
Contains a function that calculates multiples of a number
"""

import math
import os
import random
import re
import sys


def multiples(n: int) -> int:
    """
    Args:
        n (int): The number to calculate multiples for
    Returns:
        int: The sum of all multiples of 3 and 5 below n
    """
    # Initialize the sum
    sum = 0
    # Loop through all numbers below n
    for i in range(n):
        # If the number is a multiple of 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            # Add it to the sum
            sum += i
    # Return the sum
    return sum


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(multiples(n))
        