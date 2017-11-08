"""
Suppose we rewrite the FancyDivide function to use a helper function.

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
   return item / denom


This code raises a ZeroDivisionError exception for the following call: fancy_divide([0, 2, 4], 0)

Your task is to change the definition of simple_divide so that the call does not raise an exception.
When dividing by 0, fancy_divide should return a list with all 0 elements.
Any other error cases should still raise exceptions. You should only handle the ZeroDivisionError.
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    """
    Divide a number with another number
    :param item: number (nominator)
    :param denom: another number (denominator)
    :return: division of nominator by denominator. If denominator is zero, return division result as 0.
    """
    try:
        return item / denom
    except ZeroDivisionError:
        return 0

