"""
Write a Python function that takes in two lists and calculates whether they are permutations of each other.
The lists can contain both integers and strings. We define a permutation as follows:

1) the lists have the same number of elements
2) list elements appear the same number of times in both lists
3) If the lists are not permutations of each other, the function returns False.

If they are permutations of each other, the function returns a tuple consisting of the following elements:
1) the element occuring the most times
2) how many times that element occurs
3) the type of the element that occurs the most times
If both lists are empty return the tuple (None, None, None).
If more than one element occurs the most number of times, you can return any of them.

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    # Your code here
For example,

if L1 = ['a', 'a', 'b'] and L2 = ['a', 'b'] then is_list_permutation returns False
if L1 = [1, 'b', 1, 'c', 'c', 1] and L2 = ['c', 1, 'b', 1, 1, 'c'] then is_list_permutation returns
(1, 3, <class 'int'>) because the integer 1 occurs the most, 3 times, and the type of 1 is an integer
(note that the third element in the tuple is not a string).
Paste your entire function, including the definition, in the box below.
Do not leave any debugging print statements.
"""

from operator import itemgetter


def build_dict(items):
    """
    Build dict of items and occurrences of that item in a list
    :param items: given list of mixed-type items
    :return: dict containing unique items in the list and their corresponding occurrences in that list
    """
    item_dict = {}
    for item in items:
        item_dict[item] = item_dict.get(item, 0) + 1

    return item_dict


def is_list_permutation(L1, L2):
    """
    Check if 2 lists are permutations of each other. If they are, return the most common item, its occurrence & type
    :param L1: first mixed-type list
    :param L2: second mixed-type list
    :return: False if 2 lists are not permutations. If they are, return the most common item, its occurrence & type
    """
    if build_dict(L1) == build_dict(L2):
        if not L1:
            return (None, None, None)
        most_common, occurrence = max(build_dict(L1).items(), key=itemgetter(1))
        item_type = type(most_common)
        return (most_common, occurrence, item_type)
    else:
        return False


print(is_list_permutation([], []))