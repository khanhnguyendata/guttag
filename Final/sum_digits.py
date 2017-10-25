'''
Implement a function that meets the specifications below.

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
For example, sum_digits("a;35d4") returns 12.

Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
'''


def sum_digits(s):
    """
    Find all digits in a string a sum them up
    :param s: string containing digits
    :return: sum of digits in string (raise ValueError if no digits found)
    """
    digits = [str(num) for num in range(10)]
    digits_in_s = [int(char) for char in s if char in digits]
    if not digits_in_s:
        raise ValueError('No digit found in string.')
    else:
        return sum(digits_in_s)


print(sum_digits(''))