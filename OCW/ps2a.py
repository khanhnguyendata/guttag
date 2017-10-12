import pprint


def is_diophantine(x):
    """
    Input: a non-negative integer
    Output: list containing combination of 6, 9, and 20-multiples that add up wholly to the input integer
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


diophantine_dict = {}
for n in range(0, 70):
    diophantine_dict[n] = is_diophantine(n)
pprint.pprint(diophantine_dict)