"""
1) Show that it is possible to buy exactly 50, 51, 52, 53, 54, and 55 McNuggets, by finding
solutions to the Diophantine equation. You can solve this in your head, using paper and pencil,
or writing a program. However you chose to solve this problem, list the combinations of 6, 9
and 20 packs of McNuggets you need to buy in order to get each of the exact amounts.

2) Given that it is possible to buy sets of 50, 51, 52, 53, 54 or 55 McNuggets by combinations of 6,
9 and 20 packs, show that it is possible to buy 56, 57,…, 65 McNuggets. In other words, show
how, given solutions for 50-55, one can derive solutions for 56-65.
"""

import pprint


def diophantine_combination(x):
    """
    Input: a non-negative integer
    Output: list containing combination of 6, 9, and 20-multiples that add up wholly to the input integer
    """
    combinations = []
    for a in range(x//20 + 1):
        for b in range((x - a*20)//9 + 1):
            remaining = x - a*20 - b*9
            if remaining % 6 == 0:
                c = remaining//6
                combinations.append([a, b, c])
    return combinations


diophantine_dict = {}
for n in range(0, 70):
    diophantine_dict[n] = diophantine_combination(n)
pprint.pprint(diophantine_dict)

# 56 = 50 + 6 (both are diophantine number)
# Similarly, 57-61 are all diophantine numbers: 57 = 51 + 6, ..., 61 = 55 + 6
# Next, 62 = 56 + 6 (both are diophantine numbers), as are 63 (57 + 6), 64 (58 + 6), and 65 (59 + 6)
