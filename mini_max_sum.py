#!/usr/bin/python3

"""This module contains a function that finds the minimum and
maximum values that can be calculated by summing
exactly four of the five integers"""

from typing import List, Tuple


def mini_max_sum(array: List[int]) -> None:
    """
    Calculate and print the minimum and maximum sums by summing exactly four
    out of the five integers in the given array.

    Parameters:
    - array (List[int]): A list of five positive integers.

    Returns:
    - None
    """
    s_f_elements: int = 0
    s_all_elements = 0
    sorted_arr = sorted(array)

    # Calculate the sum of the first four elements
    for i in sorted_arr[0:4]:
        s_f_elements += i

    # Calculate the sum of all elements except the smallest one
    for i in sorted_arr[1:]:
        s_all_elements += i

    # Print the minimum and maximum sums
    print(f'{s_f_elements} {s_all_elements}')


if __name__ == '__main__':
    # Input: Get five positive integers from the user
    arr = list(map(int, input().rstrip().split()))
    mini_max_sum(arr)
