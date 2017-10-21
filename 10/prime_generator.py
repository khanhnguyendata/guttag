"""
ESTIMATED TIME TO COMPLETE: 10 minutes

Write a generator, genPrimes, that returns the sequence of prime numbers
on successive calls to its next() method: 2, 3, 5, 7, 11, ...
"""


def isPrime(num, list):
    """
    Check if a number is prime
    :param num: given number
    :param list: list containing prime numbers lesser than the given number
    :return: True if number is prime, False otherwise
    """
    for item in list:
        if num % item == 0:
            return False
    return True


def genPrimes():
    """
    Generate prime numbers starting from 2
    :return: Iterator containing prime numbers starting from 2
    """
    list = [2]
    num = 2
    yield 2

    while True:
        if isPrime(num, list):
            list.append(num)
            yield num
        num += 1


prime = genPrimes()

