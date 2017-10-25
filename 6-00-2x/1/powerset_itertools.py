from itertools import chain, combinations


def powerset(items):
    """
    Generate subsets (of all lengths) of a list of items
    :param items: input list of items
    :return: iterator that will generate subsets (in list-form) of all lengths
    """

    def fixed_length_combo(items, length):
        """
        Generate subsets (of fixed length) of a list of items
        :param items: input lists of items
        :param length: length of generated subset
        :return: iterator that generates each fixed-length subset in list-form
        """
        for combo in combinations(items, length):
            yield list(combo)

    # Combine all fixed-length combos into iterator that will generate each set of combo each time
    variable_length_combos = (fixed_length_combo(items, i) for i in range(len(items)+1))

    # Chain all fixed-length combos so each subset could be queried for each fixed-length combos
    all_combos = chain.from_iterable(variable_length_combos)
    return all_combos


items = ['a', 'b', 'c', 'd', 'e']
combos = powerset(items)
print('There are {0} subsets of [{1}]:'.format(2**len(items), ', '.join(items)))
numbering = 1
for subset in combos:
    print('{0}. {1}'.format(numbering, subset))
    numbering += 1