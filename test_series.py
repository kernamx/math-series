"""testing for series.py."""
import pytest


def test_foo():
    """It is a test."""
    assert 1 == 1


fibonacci_series = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8),
                    (7, 13)]
lucas_series = [(0, 2), (1, 1), (2, 3), (3, 4), (4, 7), (5, 11), (6, 18),
                (7, 29)]


@pytest.mark.parametrize('n, result', fibonacci_series)
def test_fibonacci(n, result):
    """Testing fibonacci function."""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', lucas_series)
def test_lucas(n, result):
    """Testing Lucas series."""
    from series import lucas
    assert lucas(n) == result
