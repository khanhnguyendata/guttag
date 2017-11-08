def is_diophantine(x, a, b, c):
    """
    Input: a non-negative integer
    Output: boolean on whether the integer is a diophantine
    """
    diophantine_flag = False
    for k in range(x//c + 1):
        for j in range((x - k*c)//b + 1):
            remaining = x - k*c - j*b
            if remaining % a == 0:
                return True
            else:
                diophantine_flag = False

    return diophantine_flag


def diophantine_combination(x, a, b, c):
    """
    Input: a non-negative integer (x), and package sizes (a, b, c)
    Output: list containing combination of a, b, and c packages that add up wholly to the input integer
    """
    combinations = []
    for k in range(x//c + 1):
        for j in range((x - k*c)//b + 1):
            remaining = x - k*c - j*b
            if remaining % a == 0:
                i = remaining//6
                combinations.append([i, j, k])

    return combinations


while True:
    diophantine_count = 0

    # Input package size
    packages = input("Enter package size from large to small ('q' to quit): ")
    if packages.lower() == 'q':
        break
    a, b, c = (int(x) for x in packages.split(','))
    if a > b or b > c:
        print("You did not enter package sizes in the right order (smallest to largest)")
        continue

    # Input nugget count
    max_nuggets = input("Enter max numbers of McNuggets you want to buy ('q' to quit): ")
    if max_nuggets.lower() == 'q':
        break
    max_nuggets = int(max_nuggets)

    # Count diophantine numbers between range, exit loop when there are 6 diophantine numbers in a row or when all
    # nugget sizes are counted
    for num in range(0, max_nuggets + 1):
        if is_diophantine(num, a, b, c):
            diophantine_count += 1
        else:
            diophantine_count = 0
        # Optional since all the diophantine numbers will be subtracted at the end,
        # but this provides a quick way to end loop
        if diophantine_count == a:
            break

    print("Largest number of McNuggets (between 0 and", str(max_nuggets) +
          ") that cannot be bought in exact quantity:", num - diophantine_count)
