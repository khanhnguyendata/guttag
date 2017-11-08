"""
How would you randomly generate an even number x, 0 <= x < 100? Fill out the definition for the function genEven().
Please generate a uniform distribution over the even numbers between 0 and 100 (not including 100).
"""
import random


def genEven():
    """
    Generate a random even number between 0 and 100 (excluding 100). All even numbers have the same probability
    of being selected
    :return: random even number between 0 and 100 (excluding 100)
    """
    return random.choice(range(0, 100, 2))


print(genEven())



