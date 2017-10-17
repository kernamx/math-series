"""testing for series.py."""
import pytest


def test_foo():
    """It is a test."""
    assert 1 == 1


fibonacci_series = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8),
                    (7, 13)]


@pytest.mark.parametrize('n, result', fibonacci_series)
def test_fibonacci(n, result):
    """Testing fibonacci function."""
    from series import fibonacci
    assert fibonacci(n) == result
