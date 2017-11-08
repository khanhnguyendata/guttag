# Function y = x**2 - 25
# Finding root of this function is the same thing as finding square root of 25

epsilon = 0.01
count = 0
k = 25
guess = k/2

while abs(guess**2 - k) >= epsilon:
    guess = guess - (guess**2 - k)/(2*guess)
    count += 1

print("Square root of", k, "(Newton-Ralphson) is", guess)
print("Number of iterations (Newton-Ralphson) is", count)

# Contrast with bisection method
epsilon = 0.01
count = 0
low = 0.0
high = max(1.0, k)
guess = (low + high)/2

while abs(guess**2 - k) >= epsilon:
    if guess**2 > k:
        high = guess
    else:
        low = guess
    guess = (low + high)/2
    count += 1

print("Square root of", k, "(Bisection) is", guess)
print("Number of iterations (Bisection) is", count)
