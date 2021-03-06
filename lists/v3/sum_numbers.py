from typing import List


def sum_numbers(numbers: List[int]) -> int:
    "Calculate the total from a list of numbers."
    total = 0

    for number in numbers:
        total += number

    return total
