"""Multiple tests to check our output of series functions from series.py."""
import pytest


fibonacci_series = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8),
                    (7, 13)]
lucas_series = [(0, 2), (1, 1), (2, 3), (3, 4), (4, 7), (5, 11), (6, 18),
                (7, 29)]


sum_series_values = [(0, 5, 6, 5), (1, 5, 6, 6), (2, 5, 6, 11), (3, 5, 6, 17),
                     (4, 5, 6, 28), (5, 5, 6, 45), (6, 5, 6, 73), (0, 4, 2, 4),
                     (1, 4, 2, 2), (2, 4, 2, 6), (3, 4, 2, 8), (4, 4, 2, 14),
                     (5, 4, 2, 22), (6, 4, 2, 36), ]


@pytest.mark.parametrize('n, result', fibonacci_series)
def test_fibonacci(n, result):
    """A test to see if the fibonacci function works as expected."""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', lucas_series)
def test_lucas(n, result):
    """A test to see if the lucas function works as expected."""
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n, first, second, result', sum_series_values)
def test_sum_series(n, first, second, result):
    """Testing function for sum_series using optional params."""
    from series import sum_series
    assert sum_series(n, first, second) == result


@pytest.mark.parametrize('n, result', fibonacci_series)
def test_sum_series_fibonacci(n, result):
    """Testing function for sum_series without using optional params."""
    from series import sum_series
    assert sum_series(n) == result
