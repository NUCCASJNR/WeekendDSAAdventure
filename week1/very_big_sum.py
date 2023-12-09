#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List


def aVeryBigSum(array: List[int]) -> int:
    result: int = 0
    for number in array:
        result += number
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
