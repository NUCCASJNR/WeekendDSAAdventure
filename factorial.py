#!/usr/bin/python3

"""
This script defines a function 'extraLongFactorials' to calculate the factorial
of a given non-negative integer. The result can be very large, as Python
supports arbitrary-precision integers.

To use this script, run it and enter a non-negative integer when prompted.
"""

import math
import os
import random
import re
import sys


def extraLongFactorials(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
    - n (int): The non-negative integer for which the factorial is calculated.

    Returns:
    - int: The factorial of the given integer.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == '__main__':
    n = int(input().strip())

    # Call the function and print the result
    print(extraLongFactorials(n))
