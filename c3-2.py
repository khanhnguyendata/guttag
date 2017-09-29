# Built-in split method
# s = '1.23,2.4,3.123'
# l = s.split(',')
# sum_l = sum([float(num) for num in l])
# print(sum_l)


num = ""
l = []
string = "1.23,2.4,3.123"
for char in string:
    # Add digits to number string,
    if char != ",":
        num += char
    # until encountering comma, then add gathered number to list,
    # and reset number string to zero to collect the next number
    else:
        l.append(float(num))
        num = ""
# Add the last number that wasn't added to list due to no comma at end of string
l.append(float(num))

print(sum(l))