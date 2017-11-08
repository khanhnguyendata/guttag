"""
Write a generator that returns every arrangement of items such that each is in one or none of two different bags.
Each combination should be given as a tuple of two lists, the first being the items in bag1,
and the second being the items in bag2.
"""


def convert_to_base(num, base):
    """
    Convert a decimal number into a number of a different base
    :param num: decimal number
    :param base: base to be converted to
    :return: decimal number expressed in that base
    """
    converted = ''
    while num // base:
        converted += str(num % base)
        num = num // base
    converted += str(num)

    return converted[::-1]


def yieldAllCombos(items):
    """
    Generate all permutations where a list of items could exist in two bags
    Constraint: an item could only exist in bag 1, or bag 2, or none of these bags
    :param items: list of items
    :return: iterator that will generate each time a tuple containing 2 lists, one for each list of items in each bag
    """
    permutations = 3**len(items)
    for permutation in range(permutations):
        bag1 = []
        bag2 = []
        locations = convert_to_base(permutation, 3)
        shift = len(items) - len(locations)
        for index, location in enumerate(locations):
            if location == '1':
                bag1.append(items[index + shift])
            elif location == '2':
                bag2.append(items[index + shift])
        yield (bag1, bag2)



for combo in yieldAllCombos([4, 5]):
    print(combo)