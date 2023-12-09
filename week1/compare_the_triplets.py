#!/usr/bin/python3

import math
import os
import random
import re
import sys
from typing import List, Tuple


def compareTriplets(a: List[int], b: List[int]) -> tuple[int, int]:
    point_a = 0
    point_b = 0
    for i, j in zip(a, b):
        if i > j:
            point_a += 1
        if j > i:
            point_b += 1
    return point_a, point_b


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
