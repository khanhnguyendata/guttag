import math


def coefficient_of_variation(numbers):
    """
    Calculate standard deviation from list of numbers
    :param numbers: list of numbers
    :return: standard deviation of numbers in list
    """
    mean = sum(numbers)/len(numbers)
    variance = sum((num - mean)**2 for num in numbers) / len(numbers)
    stdev = math.sqrt(variance)

    return stdev/mean


l = [10, 4, 12, 15, 20, 5]
print(coefficient_of_variation(l))