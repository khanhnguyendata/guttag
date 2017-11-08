"""
Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output,
where every other element of the input tuple is copied, starting with the first one.
So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input
would return the tuple ('I', 'a', 'tuple').
"""


def oddTuples(aTup):
    """
    Return odd elements of a tuple in a smaller tuple
    :param aTup: Input tuple
    :return: Tuple containing odd elements (starting from the first item) of the input tuple
    """
    odd_tuple = aTup[::2]
    return odd_tuple


test_tuple = ('I', 'am', 'a', 'test', 'tuple')
odd_test_tuple = oddTuples(test_tuple)
print(odd_test_tuple)

