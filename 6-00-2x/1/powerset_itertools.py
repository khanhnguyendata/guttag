from itertools import chain, combinations
from timeit import timeit
from matplotlib import pyplot as plt

# My implementation of powerset using combinations and chain from itertools
def powerset(items):
    """
    Generate subsets (of all lengths) of a list of items
    :param items: input list of items
    :return: iterator that generates subset (in list-form) of all lengths
    """

    def fixed_length_combo(items, length):
        """
        Generate subsets (of fixed length) of a list of items
        :param items: input list of items
        :param length: length of generated subset
        :return: iterator that generates each fixed-length subset in list-form
        """
        for combo in combinations(items, length):
            yield list(combo)

    # Combine all fixed-length combos into an iterator that will generate each set of combo each time
    variable_length_combos = (fixed_length_combo(items, i) for i in range(len(items)+1))

    # Chain all fixed-length combos so each subset could be queried for each fixed-length combos
    all_combos = chain.from_iterable(variable_length_combos)
    return all_combos


# EdX's powerset using binary positions
def powerSetEdX(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


def query_items(f, items):
    """
    Query items from iterators without any further processing (for timing purposes only)
    :param f: function that operates on item and returns an iterator containing processed elements
    :param items: list passed to f
    :return: nothing, for loop runs and queries items from iterator f(items)
    """
    for combo in f(items):
        pass


def wrapper(func, *args):
    """
    :param func: function to be timed
    :param args: arguments to the timed function
    :return: wrapper function containing timed function (to pass to timeit)
    """
    def wrapped():
        return func(*args)
    return wrapped


# Time both itertools powerset and EdX's powerset
powerset_times = []
powersetEdX_times = []
lengths = []
for items_length in range(21):
    items = range(items_length)
    powerset_time = timeit(wrapper(query_items, powerset, items),number=1)
    powersetEdX_time = timeit(wrapper(query_items, powerSetEdX, items),number=1)

    lengths.append(items_length)
    powerset_times.append(powerset_time)
    powersetEdX_times.append(powersetEdX_time)


# Plot times for both powersets vs. number of items, powerset using itertools combinations and chain
# perform much faster than powerset using binary positions, especially at higher number of items
powerset_line, = plt.plot(lengths, powerset_times)
powersetEdX_line, = plt.plot(lengths, powersetEdX_times)
plt.title('itertools powerset (powerset) vs binary powerset (powersetEdX)')
plt.xlabel('Number of items in list')
plt.ylabel('Timing')
plt.legend([powerset_line, powersetEdX_line], ['powerset', 'powersetEdX'])
plt.savefig('powerset vs powersetEdX.png')

