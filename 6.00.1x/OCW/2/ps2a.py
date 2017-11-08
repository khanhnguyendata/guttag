def is_diophantine(x):
    """
    Input: a non-negative integer
    Output: boolean on whether the integer is a diophantine
    """
    diophantine_flag = False
    for a in range(x//20 + 1):
        for b in range((x - a*20)//9 + 1):
            remaining = x - a*20 - b*9
            if remaining % 6 == 0:
                return True
            else:
                diophantine_flag = False

    return diophantine_flag


diophantine_count = 0
for num in range(0, 70):
    if is_diophantine(num):
        diophantine_count += 1
        print(num, diophantine_count)
    else:
        diophantine_count = 0
        print(num, diophantine_count)

    # if diophantine_count == 6:
    #     break

print("Largest number of McNuggets that cannot be bought in exact quantity:", num - 6)

