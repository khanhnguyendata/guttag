print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = (low + high)/2

while True:
    print("Is your secret number " + str(guess) + "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. "
                "Enter 'c' to indicate I guessed correctly. ")
    if ans not in ['h', 'l', 'c']:
        print("Sorry, I did not understand your input.")
        continue

    if ans == 'h':
        high = guess
        guess = int((low + high)/2)
    elif ans == 'l':
        low = guess
        guess = int((low + high)/2)
    elif ans == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
