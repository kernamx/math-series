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


def sum_series(n, first=0, second=1):
    """Evaluate a series at a given n value, can set starting values."""
    first_num = first
    second_num = second
    temp = 0

    if n == 0:
        return first
    if n == 1:
        return second

    for i in range(1, n):
        temp = first_num + second_num
        first_num = second_num
        second_num = temp

    return second_num


if __name__ == '__main__':

    print("""This module defines functions that implement mathematical series

fibonacci(n):
returns the nth value in the fibonacci series
calling finbonacci with a value of 3, expect an output of 2
output is """ + str(fibonacci(3)) + """

lucas(n):
returns the nth value in the lucas series.
calling lucas with a value of 3, expect an output of 4
output is """ + str(lucas(3)) + """

sum_series(n, first=0, second=1)
Evaluate a series at a given n value, can set starting values.
calling sum_series with a value of n = 3, first_num = 4, scond_num = 2,
expect an output of 8, output is """ + str(sum_series(3, 4, 2)))
