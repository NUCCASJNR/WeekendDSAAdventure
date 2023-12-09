#!/usr/bin/python3

import math
import os
import random
import re
import sys
from typing import List

"""
You are in charge of the cake for a child's birthday. You have decided the
cake will have one candle for each year of their total age.
They will only be able to blow out the tallest
of the candles. Count how many candles are tallest."""

def birthday_cake_candles(candles: List[int]) -> int:
    """
    Args:
        candles (List[int]): List of integers representing the height of each
        candle.
    Returns:
        int: The number of candles that are tallest.
    """
    # Get the max value in the list
    max_value = max(candles)
    # Get the number of times the max value appears in the list
    max_value_count = candles.count(max_value)
    return max_value_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthday_cake_candles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
