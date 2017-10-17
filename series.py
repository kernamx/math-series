"""This module defines functions that implement mathematical series."""


def fibonacci(n):
    """Return nth value in the fibonacci series."""
    first_num = 0
    second_num = 1
    temp = 0

    if n == 0:
        return 0
    if n == 1:
        return 1

    for i in range(1, n):
        temp = first_num + second_num
        first_num = second_num
        second_num = temp

    return second_num


def lucas(n):
    """Return nth value in the lucas series."""
    first_num = 2
    second_num = 1
    temp = 0

    if n == 0:
        return 2
    if n == 1:
        return 1

    for i in range(1, n):
        temp = first_num + second_num
        first_num = second_num
        second_num = temp

    return second_num
