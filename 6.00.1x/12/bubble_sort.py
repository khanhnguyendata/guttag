import random


def bubble_largest(nums, fragment_length):
    """
    Bubble the largest number of a list fragment in place
    :param nums: list of integers
    :param fragment_length: fragment size (from start) on which the largest number will be bubbled (to the end of fragment)
    :return: list with bubbled fragment
    """
    for i in range(fragment_length-1):  # Avoid index errors when indexing one more item at end of fragment
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]


def bubble_sort(nums):
    """
    Bubble sort a list of integer
    :param list: unsorted list of integer
    :return: sorted list of integer
    """
    # Bubble increasingly smaller fragment until list is sorted
    for fragment_length in range(len(nums), 0, -1):
        bubble_largest(nums, fragment_length)


nums = random.sample(range(1, 100), 10)
print(nums)
bubble_sort(nums)
print(nums)
