"""
Write a function, called which takes three arguments: a tuple representing starting points for the first substring,
a tuple representing starting points for the second substring, and the length of the first substring.
The function should return a tuple of all members (call it n) of the first tuple for which there is an element in the
second tuple (call it k) such that n+m+1 = k, where m is the length of the first substring.

Complete the definition
def constrainedMatchPair(firstMatch,secondMatch,length)
"""


def constrainedMatchPair(firstMatch, secondMatch, length):
    """
    Input: 2 tuples of indices, and length of the string whose the 1st indices belong to
    Output: Filter the indices of the first tuple in which 1st index + length + 1 = 2nd index
    """
    matched_indices = []
    for index in firstMatch:
        if index + length + 1 in secondMatch:
            matched_indices.append(index)

    return matched_indices


def substrings(key):
    """
    Input: Key string
    Output: Complementary combinations (in tuples) of substrings of key, which are separated by one letter
    """
    substrings_list = []
    for i in range(1, len(key) - 1):
        substrings_list.append((key[0:i], key[i+1:]))

    return substrings_list


def subStringMatchExact(target, key):
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
    return tuple(indices)


def subStringMatchOneSub(target, key):
    """
    Input: target string to be looked up and key string for the look up
    Output: Complementary combinations (in tuples) of substrings of key, which are separated by one letter"""

    # Generate list of substring pair tuples
    key_substrings = substrings(key)

    # For each substring in each pair, get the matching indices and
    # filter it to match the indices from the other substring.
    # If there are matched indices, store it (list-form) as a dict value whose key is the concatenated wildcard string
    matched_indices_dict = {}
    for sub1, sub2 in key_substrings:
        from ps3b import subStringMatchExact
        indices1 = subStringMatchExact(target, sub1)
        indices2 = subStringMatchExact(target, sub2)

        indices_matched = constrainedMatchPair(indices1, indices2, len(sub1))
        if indices_matched:
            matched_indices_dict[sub1 + "*" + sub2] = indices_matched

    return matched_indices_dict


def subStringMatchExactlyOneSub(target, key):
    """
    Input: target string to be looked up and key string for the look up
    Output: tuple of starting indices where exactly one character of key is incorrectly matched to target"""

    # Convert tuple of exact match indices to set
    exact_indices = set(subStringMatchExact(target, key))

    # Unpack dict of onesub wildcard match indices to set of indices
    onesub_indices = set()
    for value_list in subStringMatchOneSub(target, key).values():
        for value in value_list:
            if value not in onesub_indices:
                onesub_indices.add(value)

    # Indices of exact onesub wildcard match indices is the difference of general one sub match indices aside from
    # the exact match indices
    exact_onesub_indices = onesub_indices - exact_indices

    return tuple(exact_onesub_indices)


key = "atgcat"
target = "atgtatgdataagtatgcat"
print(subStringMatchExactlyOneSub(target, key))

