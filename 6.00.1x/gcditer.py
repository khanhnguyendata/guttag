"""
https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017_2/courseware/0de4fecc5a9a4749923133fcf4de181f/38007cdb67c44b46b124cdbce33510b5/?activate_block_id=block-v1%3AMITx%2B6.00.1x%2B2T2017_2%2Btype%40sequential%2Bblock%4038007cdb67c44b46b124cdbce33510b5
The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder.
For example,
gcd(2, 12) = 2
gcd(6, 12) = 6
gcd(9, 12) = 3
gcd(17, 12) = 1

---Iterative---
Write an iterative function, gcdIter(a, b), that implements this idea.
One easy way to do this is to begin with a test value equal to the smaller of the two input arguments,
and iteratively reduce this test value by 1 until you either reach a case where
the test divides both a and b without remainder, or you reach 1.

---Recursive---
A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors.
Suppose that a and b are two positive integers:
If b = 0, then the answer is a
Otherwise, gcd(a, b) is the same as gcd(b, a % b)"""


def valid_integer_input(n):
    """Input: number that indicate whether the user is entering first or second integer
    Prompt user to input the order-specified integer, check whether an integer was entered, and re-prompted if not.
    If input was an integer, return that integer"""
    while True:
        try:
            if n == 1:
                num = int(input("Input your first integer: "))
            elif n == 2:
                num = int(input("Input your second integer: "))
        except ValueError:
            print("You did not enter an integer")
        else:
            break
    return num


def gcdIter(a, b):
    """Input: two positive integers
    Find the lowest common divisor of the two integers using iteration"""
    lower = min(a, b)
    while a%lower != 0 or b%lower != 0:
        lower -= 1
    return lower


def gcdRecur(a, b):
    """Input: two positive integers
    Find the lowest common divisor of the two integers using recursion"""
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


def main():
    while True:
        num1 = valid_integer_input(1)
        num2 = valid_integer_input(2)
        print(gcdRecur(num1, num2))
        rerun = input("Would you like to do it again (y/n)? ")
        while rerun.lower() not in ['y', 'n']:
            rerun = input("Invalid input. Would you like to do it again (y/n)? ")
        if rerun.lower() == 'n':
            print("Thank you for using the program!")
            break


main()