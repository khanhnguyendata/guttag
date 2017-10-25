def merge_lists(list1, list2, compare_f):
    """
    Merge two sorted lists into a new sorted list
    :param compare_f: lambda function:
    x > y: descending list from 2 descending lists,
    x < y: ascending list from 2 ascending lists
    :param list1: first sorted list
    :param list2: second sorted list
    :return: new sorted list containing all elements of two input lists
    """
    result = []
    while list1 and list2:  # Continue loop until one of the lists become empty
        if compare_f(list1[0], list2[0]):
            result.append(list1.pop(0))

        else:
            result.append(list2.pop(0))

    result.extend(list1 or list2)  # Extend the result with the remaining non-empty list

    return result


def merge_sort(unsorted_list, compare_f=lambda x, y: x < y):
    """
    Merge sort list
    :param compare_f: comparison function: 2-argument lambda function
    to choose between ascending sort (x < y) or descending (x > y)
    :param unsorted_list: unsorted list containing integers
    :return: sorted list using merge sort
    """
    if len(unsorted_list) < 2:
        return unsorted_list
    else:
        mid = len(unsorted_list) // 2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]
        sorted_left = merge_sort(left, compare_f)
        sorted_right = merge_sort(right, compare_f)
        return merge_lists(sorted_left, sorted_right, compare_f)


print(merge_sort([2, 1, 4, 5, 3], lambda x, y: x > y))


