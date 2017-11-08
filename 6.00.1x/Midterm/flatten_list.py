"""
Write a function to flatten a list. The list contains other lists, strings, or ints.
For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]
(order matters).
"""


def flatten(aList):
    """
    Flatten nested list of multiple levels
    :param aList: nested list
    :return: flat list containing all elements of nested list
    """
    flattened_list = []
    for item in aList:
        if isinstance(item, list):
            flattened_item = flatten(item)
            flattened_list.extend(flattened_item)
        else:
            flattened_list.append(item)
    return flattened_list


l1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(l1))