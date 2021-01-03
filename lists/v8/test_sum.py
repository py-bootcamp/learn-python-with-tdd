import pytest
from sum_numbers import sum_all_tails, sum_numbers


@pytest.mark.parametrize(
    "numbers,want",
    [([1, 2, 3, 4.0, 5.0], 15), ([], 0)],
)
def test_sum_numbers(numbers, want):
    got = sum_numbers(numbers)
    assert got == want


@pytest.mark.parametrize(
    "numbers_1,numbers_2,want",
    [([1, 2], [0, 9], [2, 9]), ([], [], [0, 0])],
)
def test_sum_all_tails(numbers_1, numbers_2, want):
    got = sum_all_tails(numbers_1, numbers_2)
    assert got == want
