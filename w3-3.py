# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
#
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example,
# if s = 'abcbcd', then your program should print
#
# Longest substring in alphabetical order is: abc

import string

s = 'xoarnmkkutouublskxjoudze'
abc = list(string.ascii_lowercase)

substring = ""
substring_list = []
str_index = 0
for str_index in range(len(s) - 1):
    char = s[str_index]
    char_next = s[str_index + 1]
    char_abcindex = abc.index(char)
    char_next_abcindex = abc.index(char_next)
    # print(char, char_abcindex, char_next, char_next_abcindex, substring)
    if char_abcindex <= char_next_abcindex:
        if substring:
            substring += char_next
        else:
            substring += char
            substring += char_next
    else:
        if substring != "":
            substring_list.append(substring)
            substring = ""
    # print(substring, "\n")

    str_index += 1

if substring != "":
    substring_list.append(substring)

highest_length = 0
longest_substring = ""
index = 0
for index in range(len(substring_list)):
    current_substring = substring_list[index]
    current_length = len(current_substring)
    # print(current_substring, current_length, longest_substring, highest_length)
    if current_length > highest_length:
        longest_substring = current_substring
        highest_length = current_length
print("Longest substring in alphabetical order is: " + longest_substring)
