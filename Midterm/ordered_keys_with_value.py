"""
Write a Python function that returns a list of keys in aDict with the value target.
The list of keys you return should be sorted in increasing order.
The keys and values in aDict are both integers.
(If aDict does not contain the value target, you should return an empty list.)

This function takes in a dictionary and an integer and returns a list.

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here
"""


def keysWithValue(aDict, target):
    """
    Return a list of keys (in increasing order) whose value matches value of a given target
    :param aDict: a dictionary
    :param target: target integer to be compared to
    :return: list of keys, sorted in increasing order, whose value matches target integer
    """
    matched_keys = [key for key in aDict if aDict[key] == target]
    matched_keys.sort()
    return matched_keys


if __name__ == '__main__':
    d1 = {1: 3, 2: 4, 5: 3, 4: 2}
    print(keysWithValue(d1, 9))
