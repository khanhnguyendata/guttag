from knapsack_greedy import build_items
from random import sample, randint


def max_value(items, available_weight, call):
    """
    Find the combination with the highest value to take from list of items
    :param items: list of items available to be taken
    :param available_weight: remaining weight in knapsack to accommodate items
    :return: tuple with the combination of items that return the highest value (within the weight limit) and its value
    """
    if items == [] or available_weight == 0:
        return (), 0
    else:
        first_item = items[0]
        remaining_items = items[1:]
        # If taking the first item of the list makes the knapsack overweight,
        # then do not take first item, and available weight remains the same
        # This is the same as taking the right branch automatically (without comparing it to left branch)
        if first_item.get_weight() > available_weight:
            call.add_max_call()
            return max_value(remaining_items, available_weight, call)
        # If there are still space for the first item, then compare the values of left and right branches
        elif first_item.get_weight() <= available_weight:
            call.add_max_call(2)
            # Left branch: optimal combo & value of remaining items (with less space allowed) + first item
            left_max_combo, left_max = max_value(remaining_items, available_weight - first_item.get_weight(), call)
            left_max_combo += (first_item,)
            left_max += first_item.get_value()

            # Right branch: optimal combo & value of remaining items (with the same space)
            # Right branch can paradoxically be more valuable than left branch (the one with the first item).
            # This is because there are more space for the remaining items in the right branch, which means
            # valuable items from the remaining items could be taken (instead of thrown out due to lack of space)
            # and increase the value of the knapsack
            right_max_combo, right_max = max_value(remaining_items, available_weight, call)

            # Return the combo and knapsack value of the more valuable branch
            if left_max > right_max:
                return left_max_combo, left_max
            else:
                return right_max_combo, right_max


def max_value_memoized(items, available_weight, call, memo={}):
    """
    Find the combination with the highest value to take from list of items
    :param items: list of items available to be taken
    :param available_weight: remaining weight in knapsack to accommodate items
    :return: tuple with the combination of items that return the highest value (within the weight limit) and its value
    """
    if (len(items), available_weight) in memo:
        call.add_memo_call()
        return memo[(len(items), available_weight)]
    elif items == [] or available_weight == 0:
        return (), 0
    else:
        first_item = items[0]
        remaining_items = items[1:]
        # If taking the first item of the list makes the knapsack overweight,
        # then do not take first item, and available weight remains the same
        # This is the same as taking the right branch automatically (without comparing it to left branch)
        if first_item.get_weight() > available_weight:
            call.add_max_call()
            result = max_value_memoized(remaining_items, available_weight, call, memo)

        # If there are still space for the first item, then compare the values of left and right branches
        elif first_item.get_weight() <= available_weight:
            call.add_max_call(2)
            # Left branch: optimal combo & value of remaining items (with less space allowed) + first item
            left_max_combo, left_max = max_value_memoized(remaining_items, available_weight - first_item.get_weight(), call, memo)
            left_max_combo += (first_item,)
            left_max += first_item.get_value()

            # Right branch: optimal combo & value of remaining items (with the same space)
            # Right branch can paradoxically be more valuable than left branch (the one with the first item).
            # This is because there are more space for the remaining items in the right branch, which means
            # valuable items from the remaining items could be taken (instead of thrown out due to lack of space)
            # and increase the value of the knapsack
            right_max_combo, right_max = max_value_memoized(remaining_items, available_weight, call, memo)

            # Return the combo and knapsack value of the more valuable branch
            if left_max > right_max:
                result = left_max_combo, left_max
            else:
                result = right_max_combo, right_max
        memo[(len(items), available_weight)] = result
        return result


def display_names(items):
    """
    Display the names of items within a list
    :param items: list of Item objects
    :return: str with names of Item objects, separated by commas and enclosed by []
    """
    items_str = ', '.join(item.get_name() for item in items)
    return f'[{items_str}]'


class Counter:
    """Create counter to keep track of max value calls and memo query calls"""
    def __init__(self, max_call=0, memo_call=0):
        self.max_call = max_call
        self.memo_call = memo_call

    def add_max_call(self, n=1):
        self.max_call += n

    def add_memo_call(self, n=1):
        self.memo_call += n

    def __str__(self):
        call_log = f'Max value calls: {self.max_call}\n'
        if self.memo_call:
            call_log += f'Memo calls: {self.memo_call}'
        return call_log


def main():
    names = range(16)
    values = [randint(1, 10) for item in names]
    weights = [randint(1, 10) for item in names]
    items = build_items(names, values, weights)

    weight_limit = 16
    memoizations = ['non-memoized', 'memoized']
    funcs = [max_value, max_value_memoized]
    for memoization, func in zip(memoizations, funcs):
        counters = Counter(0)
        knapsack_items, knapsack_value = func(items, weight_limit, counters)
        print('--------------------------------')
        print(f'Using binary tree search ({memoization}), knapsack ({weight_limit}) '
              f'contains (total value of {knapsack_value}):')
        for item in knapsack_items:
            print(item)
        print('--------------------------------')
        print(counters)


main()
