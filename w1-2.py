# Assume s is a string of lower case characters.
#
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print


s = 'shobooucnbobbgbobob'
bob_count = 0
for index in range(len(s)-2):
    # Conditional still works even though s[index + 1/2] might be out of bounds,
    # since conditionals are evaluated left to right: later clauses might not be evaluated
    # if the earlier clauses are False
    if s[index] == "b" and s[index + 1] == "o" and s[index + 2] == "b":
        bob_count += 1
print(bob_count)