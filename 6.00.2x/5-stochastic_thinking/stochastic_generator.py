"""
Write a uniformly distributed stochastic program, stochasticNumber, that returns an even number between 9 and 21.
"""
import random


def stochasticNumber():
    """
    Return a random even number between 9 and 21
    :return: random even number between 9 and 21
    """
    return random.choice(range(10, 22, 2))
