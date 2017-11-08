"""
Write a recursive Python function, given a non-negative integer N, to count and return the number of occurrences
of the digit 7 in N.

For example:
count7(717) -> 2
count7(1237123) -> 1
count7(8989) -> 0
Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6),
while doing integer division by 10 removes the rightmost digit (126 / 10 is 12).

This function has to be recursive; you may not use loops!
This function takes in one integer and returns one integer.

"""


def count7(N):
    """
    Return number of 7's in a non-negative integer
    :param N: Non-negative integer
    :return: Number of 7's in that integer
    """
    if N < 10:
        count = int(N == 7)
    else:
        last_digit = N % 10
        count = int(last_digit == 7) + count7(N // 10)

    return count

print(count7(7))