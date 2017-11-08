"""
You are given a dictionary aDict that maps integer keys to integer values.
Write a Python function that returns a list of keys in aDict that map to dictionary values that
appear exactly once in aDict.

This function takes in a dictionary and returns a list.
Return the list of keys in increasing order.
If aDict does not contain any values appearing exactly once, return an empty list.
If aDict is empty, return an empty list.
For example:
If aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0} then your function should return [1, 3, 8]
If aDict = {1: 1, 2: 1, 3: 1} then your function should return []

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here

Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
"""

def uniqueValues(aDict):
    """
    Find dict keys whose value appear only once in the value space
    :param aDict: dict with integer keys and values
    :return: list of keys whose value in dict appear only once in the value space
    """
    values = list(aDict.values())
    counted_keys = []
    for key, value in aDict.items():
        if values.count(value) == 1:
            counted_keys.append(key)

    return sorted(counted_keys)


print(uniqueValues({6: 0, 7: 0, 10: 0}))