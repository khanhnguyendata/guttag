"""
https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017_2/courseware/0de4fecc5a9a4749923133fcf4de181f/38007cdb67c44b46b124cdbce33510b5/?activate_block_id=block-v1%3AMITx%2B6.00.1x%2B2T2017_2%2Btype%40sequential%2Bblock%4038007cdb67c44b46b124cdbce33510b5
We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in
alphabetical order.
First, test the middle character of a string against the character you're looking for (the "test character").

If they are the same, we are done - we've found the character we're looking for!
If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only
consider the lower half of the string; otherwise, we only consider the upper half of the string.
(Note that you can compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr.
char will be a single character and aStr will be a string that is in alphabetical order. The function should return
a boolean value.

As you design the function, think very carefully about what the base cases should be.
"""
import string


def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    """
    if len(aStr) == 0 or len(aStr) == 1 and char != aStr:
        return False

    sorted_str = "".join(sorted(aStr))
    middle = len(aStr) // 2
    # print(char, aStr, sorted_str, len(aStr), middle, sorted_str[middle])

    if char == sorted_str[middle]:
        return True
    elif char < sorted_str[middle]:
        return isIn(char, sorted_str[:middle])
    else:
        return isIn(char, sorted_str[middle + 1:])


def main():
    while True:
        char = input("Enter your character: ")
        s = input("Enter your string: ")
        print(isIn(char, s))
        rerun = input("Would you like to do it again (y/n)? ")
        while rerun.lower() not in ['y', 'n']:
            rerun = input("Invalid input. Would you like to do it again (y/n)? ")
        if rerun.lower() == 'n':
            print("Thank you for using the program!")
            break


main()
