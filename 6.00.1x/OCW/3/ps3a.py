"""
Write two functions, calledcountSubStringMatch and countSubStringMatchRecursive that take two arguments,
a key string and a target string. These functions iteratively and
recursively count the number of instances of the key in the target string.
You should complete definitions for

def countSubStringMatch(target,key):
and
def countSubStringMatchRecursive (target, key):
Place your answer in a file named ps3a.py
"""


def countSubStringMatch(target, key):
    """
    Input: target string to be looked up on, and key string for the look up
    Output: number of key strings found in target string
    """
    match_count = 0
    while target.find(key) != -1:
        index = target.find(key)
        match_count += 1
        target = target[index + len(key):]
    return match_count


def countSubStringMatchRecursive (target, key):
    """
    Input: target string to be looked up on, and key string for the look up
    Output: number of key strings found in target string (with recursion)
    """
    if target.find(key) == -1:
        match_count = 0
    else:
        index = target.find(key)
        match_count = 1 + countSubStringMatchRecursive(target[index + len(key):], key)

    return match_count


str1 = "atgacatgcatgcacaagtatgcat"
str2 = "atgc"
print("str1:", str1, "\nstr2:", str2)
print("Match count (iterative):", countSubStringMatch(str1, str2))
print("Match count (recursive):", countSubStringMatchRecursive(str1, str2))
