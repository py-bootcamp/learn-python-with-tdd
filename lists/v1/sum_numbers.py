def sum_numbers(numbers):
    "Calculate the total from a list of numbers."
    total = 0

    for index, number in enumerate(numbers):
        total += numbers[index]

    return total
