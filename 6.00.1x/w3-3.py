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


def return_longest_substrings(string):
    substring = ""
    substring_list = []

    for index in range(len(string) - 1):  # Stop loop at second to last character to avoid index error
        char_current = string[index]
        char_next = string[index + 1]
        # If the next character is alphabetically greater or equal to current character:
        # Add both current character and next character if the longest substring is currently empty
        # Otherwise, if there's already a current substrate, just add next character to substring
        if char_current <= char_next:
            if substring == "":
                substring += char_current
                substring += char_next
            else:
                substring += char_next
        # When the next character is alphabetically smaller than current character:
        # Reset substring if it's already built up
        # Otherwise, if substring is empty (start of string or a break was found earlier), add the current
        # character to the substring list (to account for cases like "cba" -> ['c', 'b', 'a']
        else:
            if substring:
                substring_list.append(substring)
                substring = ""
            else:
                substring_list.append(char_current)

    # If there's still a substring when loop ends (at second to last character),
    # save this substring to the list as it wasn't saved during the looping
    # due to lack of exit condition (an alphabetically smaller next character)
    if substring:
        substring_list.append(substring)
    # If substring is empty when loop ends (at second to last character),
    # for example, string of one character, break character at end of string,
    # save the last lone character to substring list
    else:
        substring_list.append(string[-1])

    return substring_list


def longest_string(substring_list):
    highest_length = 0
    longest_substring = ""
    # If current indexed string is longer than the stored longest string,
    # replace longest string and highest length with the current string and length
    for index in range(len(substring_list)):
        current_substring = substring_list[index]
        current_length = len(current_substring)

        if current_length > highest_length:
            longest_substring = current_substring
            highest_length = current_length

    return longest_substring


def main():
    s = "aasdgadhsabcdefsadg"
    substring_list = return_longest_substrings(s)
    longest_substring = longest_string(substring_list)
    print("Longest substring in alphabetical order is: " + longest_substring)


main()


