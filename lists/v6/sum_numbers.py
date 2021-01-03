from typing import List


def sum_numbers(numbers: List[float]) -> float:
    "Calculate the total from a list of numbers."
    total = 0.0

    for number in numbers:
        total += number

    return total


def sum_all(*numbers_to_sum):
    "Calculate the respective sums of every list passed in."
    sums = []

    for numbers in numbers_to_sum:
        result = sum_numbers(numbers)
        sums.append(result)

    return sums
