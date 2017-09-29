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
        if x == 0 or x == 1:
            root_pwr_pairs[x] = "any power"
        elif x == -1:
            root_pwr_pairs[x] = "any odd power"
        else:

            # Handle normal cases
            print(x)
            root = 2
            pwr = 0

            while root**pwr < abs(x):
                pwr = 1
                while root**pwr < abs(x):
                    pwr += 1

                # Store root and power
                if root**pwr == abs(x):
                    if x > 1:  # Store both positive and negative roots for positive integers
                        root_pwr_pairs[root] = pwr
                        root_pwr_pairs[-root] = pwr
                    elif x < 0 and pwr%2 != 0:  # Store negative root for negative integer and odd powers
                        root_pwr_pairs[-root] = pwr
            root += 1
        print(root_pwr_pairs)
