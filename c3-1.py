x = 32
root_pwr_pairs = {}

for root in range(1, abs(x)+1):
    for pwr in range(1, 7):
        powered = root**pwr
        if powered == abs(x):
            if x > 0:
                root_pwr_pairs[root] = pwr
                root_pwr_pairs[-root] = pwr
            elif x < 0:
                root_pwr_pairs[-root] = pwr
            break
        elif powered > abs(x):
            break
print(root_pwr_pairs)