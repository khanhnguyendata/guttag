def find_smallest(list):
    """
    Return the smallest value of a list, and remove that value in place from the list
    :param list: a list of integer
    :return: smallest item of the list
    """
    smallest_index = 0
    smallest_number = list[0]
    for index, number in enumerate(list):
        if number < smallest_number:
            smallest_index = index
            smallest_number = number
    del list[smallest_index]
    return smallest_number


def build_sorted(list):
    """
    Return a sorted list (from smallest to largest) from a given list
    :param list: a list of integer
    :return: sorted list of input list (from smallest to largest)
    """
    sorted_list = []
    for i in range(len(list)):
        smallest = find_smallest(list)
        sorted_list.append(smallest)

    return sorted_list


print(build_sorted([3, 8, 2, 8, 2, 5, 7, 9, 2, 0, -3]))