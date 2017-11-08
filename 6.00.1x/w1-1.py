# Assume s is a string of lower case characters.
#
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5


def count_vowel(string):
    vowel_count = 0
    for char in string:
        if char in ["a", "e", "i", "o", "u"]:
            vowel_count += 1
    return vowel_count


s = 'azcbobobegghakl'
print("Number of vowels:", count_vowel(s))
