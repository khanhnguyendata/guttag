"""
Consider a list of positive (there is at least one positive) and negative numbers.
You are asked to find the maximum sum of a contiguous subsequence. For example,

in the list [3, 4, -1, 5, -4], the maximum sum is 3+4-1+5 = 11
in the list [3, 4, -8, 15, -1, 2], the maximum sum is 15-1+2 = 16
Write a function that meets the specification below.
"""


def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    max_sum_at_index = {}
    for index, num in enumerate(L):
        if index == 0:
            max_sum_at_index[index] = num
        else:
            max_sum_before = max_sum_at_index[index - 1]
            max_sum_now = max_sum_before + num
            # If max sum now > num, then num is included in max contiguous sum. Otherwise, contiguous sum breaks
            # and the new max contiguous sum will start at num
            max_sum_at_index[index] = max(num, max_sum_now)

    return max(max_sum_at_index.values())


l = [3, 4, -8, 15, -1, 2]
print(max_contig_sum(l))