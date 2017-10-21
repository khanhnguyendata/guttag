def merge_lists(list1, list2):
    """
    Merge two sorted lists into a new sorted list
    :param list1: first sorted list
    :param list2: second sorted list
    :return: new sorted list containing all elements of two input lists
    """
    result = []
    while list1 and list2:  # Continue loop until one of the lists become empty
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    result.extend(list1 or list2)  # Extend the result with the remaining non-empty list

    return result


def merge_sort(unsorted_list):
    """
    Merge sort list
    :param unsorted_list: unsorted list containing integers
    :return: sorted list using merge sort
    """
    if len(unsorted_list) < 2:
        return unsorted_list
    else:
        mid = len(unsorted_list) // 2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        return merge_lists(sorted_left, sorted_right)


print(merge_sort([2, 1, 4, 5, 3]))


