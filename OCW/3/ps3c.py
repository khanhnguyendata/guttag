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


key = "atgcat"
target = "atgtatgdataagtatgcat"

key_substrings = substrings(key)
matched_indices_dict = {}

# For each pair of complimentary substring, find the matched indices for that pair and display them as value for the
# substring-pair key (separated by wildcard *)
for sub1, sub2 in key_substrings:
    from ps3b import subStringMatchExact
    indices1 = subStringMatchExact(target, sub1)
    indices2 = subStringMatchExact(target, sub2)

    indices_matched = constrainedMatchPair(indices1, indices2, len(sub1))
    if indices_matched:
        matched_indices_dict[sub1 + "*" + sub2] = indices_matched

print(matched_indices_dict)


