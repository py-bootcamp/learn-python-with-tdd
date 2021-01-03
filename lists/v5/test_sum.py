import pytest
from sum_numbers import sum_numbers


@pytest.mark.parametrize(
    "numbers,want",
    [([1, 2, 3, 4.0, 5.0], 15), ([], 0)],
)
def test_sum_numbers(numbers, want):
    got = sum_numbers(numbers)
    assert got == want
