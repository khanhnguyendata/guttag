class Item:
    """Represent item taken in the knapsack"""
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight
        self.density = self.value / self.weight

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def get_density(self):
        return self.density

    def __str__(self):
        return f'\t{self.name} - v: {self.value}, w: {self.weight}, d: {round(self.density, 1)}'


def build_items(names, values, weights):
    """
    Build list of item objects with lists of their names, values, and weights
    :param names: list of names of items
    :param values: list of item values
    :param weights: list of item weights
    :return: list of item objects
    """
    items = []
    for name, value, weight in zip(names, values, weights):
        items.append(Item(name, value, weight))

    return items


def take_items(items, available, priority_by):
    """
    Take objects from list of items (based on certain priority criteria) to put in knapsack
    :param items: list of item objects
    :param available: available space in knapsack
    :param priority_by: function as key parameter to sort and prioritize items to take from the list
    :return: list of knapsack items, total value of items in knapsack, remaining space after taking
    """
    knapsack = []
    knapsack_value = 0
    sorted_items = sorted(items, key=priority_by, reverse=True)
    for item in sorted_items:
        if available >= item.get_weight():
            knapsack.append(item)
            knapsack_value += item.get_value()
            available -= item.get_weight()
        else:
            break

    return knapsack, knapsack_value, available


def display_knapsack(items, available, criteria, priority_by):
    """
    Display final result after taking items into knapsack based on certain criteria
    :param items: list of item objects
    :param available: available space in knapsack
    :param criteria: str indicating criteria to prioritize item taking
    :param priority_by: func indicating the priority that the take_items function will use
    :return: None, print out knapsack content, value, and space after taking
    """
    knapsack, knapsack_value, available = take_items(items, available, priority_by)
    print('--------------------------------')
    print(f'Knapsack ({available}) contains (prioritized by {criteria} - total value of {knapsack_value}):')
    for item in knapsack:
        print(item)
    print(f'Available space: {available}')


def main():
    names = ['a', 'b', 'c', 'd']
    values = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    # Build list of item objects from list of names, values, and weights
    items = build_items(names, values, weights)

    # Set up different criterias for items to be taken
    criterias = ['highest value', 'lowest weight', 'highest value density']
    priorities_by = [Item.get_value, lambda obj: 1/obj.get_weight(), Item.get_density]
    available = 10

    # Take items based on each criteria and display results
    for criteria, priority_by in zip(criterias, priorities_by):
        display_knapsack(items, available, criteria, priority_by)

if __name__ == '__main__':
    main()
