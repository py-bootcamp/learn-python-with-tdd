from typing import List


def sum_numbers(numbers: List[float]) -> float:
    "Calculate the total from a list of numbers."
    total = 0.0

    for number in numbers:
        total += number

    return total
