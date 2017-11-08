from knapsack_greedy import build_items
from powerset_itertools import powerset
from random import sample


def main():
    names = range(10)
    values = sample(range(1, 100), 10)
    weights = sample(range(1, 100), 10)
    items = build_items(names, values, weights)

    available = 100
    max_value = 0
    max_combo = []

    # Generate different item combinations in knapsack
    for combo in powerset(items):
        combo_value = sum(item.get_value() for item in combo)
        combo_weight = sum(item.get_weight() for item in combo)
        # Only combinations that are lighter than max value, and has value higher than current max value are recorded
        if combo_weight <= available and combo_value > max_value:
                max_value = combo_value
                max_combo = combo

    # Display most optimal knapsack by exhaustive enumeration
    print('--------------------------------')
    print(f'Knapsack ({available}) contains (total value of {max_value}):')
    for item in max_combo:
        print(item)


if __name__ == '__main__':
    main()