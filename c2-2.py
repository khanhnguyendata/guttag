# Finger exercise: Write a program that asks the user to input 10 integers,
# and then prints the largest odd number that was entered.
# If no odd number was entered, it should print a message to that effect.


def input_10_integer():
    num = 10
    num_list = []
    while num > 0:
        num_input = input("Input an integer (" + str(num) + " integers to go): ")
        try:
            num_int = int(num_input)
        except ValueError:
            print("That is not an integer! Please try again.")
            continue
        num_list.append(num_int)
        num = num - 1
    return num_list


num_list = input_10_integer()
odd_list = [x for x in num_list if x%2 != 0]
if odd_list:
    sorted_odd_list = sorted(odd_list)
    largest_odd = sorted_odd_list[-1]
    print("Largest odd number of the list is: " + str(largest_odd))
else:
    print("No odd number was entered")