import math
import numpy as np


def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L:
        lengths = [len(word) for word in L]
        mean = sum(lengths)/len(lengths)
        variance = sum((length - mean)**2 for length in lengths) / len(lengths)
        stdev = math.sqrt(variance)
        return stdev
    else:
        return float('NaN')


L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L))