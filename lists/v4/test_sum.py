from sum_numbers import sum_numbers


def test_sum():
    numbers = [1, 2, 3, 4, 5]

    got = sum_numbers(numbers)
    want = 15

    assert got == want


def test_sum_empty_list():
    numbers = []

    got = sum_numbers(numbers)
    want = 0

    assert got == want


def test_sum_with_floats():
    numbers = [1.5, 2.0, 3.5]

    got = sum_numbers(numbers)
    want = 7.0

    assert got == want
