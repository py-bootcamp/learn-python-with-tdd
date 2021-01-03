from typing import List


def sum_numbers(numbers: List[float]) -> float:
    "Calculate the total from a list of numbers."
    total = 0.0

    for number in numbers:
        total += number

    return total


def sum_all_tails(*numbers_to_sum: List[float]) -> List[float]:
    """
    Calculate the sums of all but the first number
    given a collection of lists.
    """
    return [sum_numbers(numbers[1:]) for numbers in numbers_to_sum]
