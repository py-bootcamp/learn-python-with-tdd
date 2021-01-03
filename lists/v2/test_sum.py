from sum_numbers import sum_numbers


def test_sum():
    numbers = [1, 2, 3, 4, 5]

    got = sum_numbers(numbers)
    want = 15

    assert got == want
