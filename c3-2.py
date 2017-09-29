# Built-in split method
# s = '1.23,2.4,3.123'
# l = s.split(',')
# sum_l = sum([float(num) for num in l])
# print(sum_l)


num = ""
l = []
string = "1.23, 2.4, 3.123"
for char in string:
    # Add digits to number string,
    if char not in [",", " "]:
        num += char
    # until encountering comma, then add gathered number to list,
    # and reset number string to zero to collect the next number
    else:
        if num != "":
            l.append(num)
            num = ""
# Add the last number that wasn't added to list due to no comma at end of string
l.append(num)

# Convert number strings to floats
l = [float(num_str) for num_str in l]

# Sum list of floats
print(sum(l))