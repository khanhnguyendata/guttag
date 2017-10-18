"""
Here is a different piece of code for working with lists:

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result
Suppose that you are given the following functions:

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1
"""


def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result


def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1


print(applyEachTo([inc, square, halve, abs], 3.0))