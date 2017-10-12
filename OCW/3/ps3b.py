"""
Write the function subStringMatchExact.This function takes two arguments: a target string, and a key string.
It should return a tuple of the starting points of matches of the key string in the target string,
when indexing starts at 0.

Complete the definition for
def subStringMatchExact(target,key):
For example,
subStringMatchExact("atgacatgcacaagtatgcat","atgc")
would return the tuple (5, 15).
"""


def subStringMatchExact(target,key):
    """
    Input: target string to be looked up and key string for the look up
    Output: list of indices where key string was found to start within target string
    """
    indices = []
    full_length = len(target)
    while target.find(key) != -1:
        match_index = target.find(key)
        starting_index = full_length - len(target)
        indices.append(starting_index + match_index)

        target = target[match_index + len(key):]
    return indices


print(subStringMatchExact("atgacatgcacaagtatgcat","atgcat"))