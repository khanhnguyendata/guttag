"""
Consider the following sequence of expressions:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
We want to write some simple procedures that work on dictionaries to return information.

First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.
For example:
print(how_many(animals))
6
"""


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    """
    Return total value items in a dictionary
    :param aDict: Dictionary where each key value is a list
    :return: Total items in value lists in that dictionary
    """
    values = aDict.values()
    total_values = sum(len(value) for value in values)
    return total_values


print(how_many(animals))
