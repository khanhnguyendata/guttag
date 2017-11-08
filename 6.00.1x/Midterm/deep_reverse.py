'''
Implement a function that meets the specifications below.

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    # Your code here
For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]

Paste your entire function, including the definition, in the box below.
Do not leave any debugging print statements.
'''


def deep_reverse(L):
    """
    Reverse list of lists, both in sublist order, and item order in each sublist
    :param L: list of lists, in which each sublist contains only integers
    :return: new list of lists, where sublist order and item order in sublist are reversed from the original list
    """
    L.reverse()
    for l in L:
        l.reverse()
    return L


L = [[1, 2], [3, 4], [5, 6, 7]]
print(deep_reverse(L))

