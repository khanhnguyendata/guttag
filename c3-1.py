while True:
    x = input("Input an integer (type 'q' to quit): ")

    # Handle exit
    root_pwr_pairs = {}
    if x.lower() == 'q':
        break
    else:
        # Handle exceptions
        try:
            x = int(x)
        except ValueError:
            print("Invalid input")
            continue

        # Handle unique cases
        if x == 0:
            root_pwr_pairs[0] = "any power"
        elif x == 1:
            root_pwr_pairs[1] = "any power"
        else:

            # Handle normal cases
            for root in range(2, abs(x)+1):
                pwr = 1
                while root**pwr < abs(x):
                    pwr += 1
                if root**pwr == abs(x):
                    # Handle multiple roots for positive integers, and negative roots
                    # for negative integers
                    if x > 1:
                        root_pwr_pairs[root] = pwr
                        root_pwr_pairs[-root] = pwr
                    elif x < 0:
                        root_pwr_pairs[-root] = pwr
        print(root_pwr_pairs)
