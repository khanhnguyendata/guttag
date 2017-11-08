balance = 320000
annualInterestRate = 0.2


def annual_remaining_balance(balance, annual_interest_rate, monthly_payment):
    """
    Input: initial balance, annual interest rate, monthly payment
    Output: remaining balance after one year
    """
    monthly_interest_rate = annual_interest_rate / 12

    for month in range(1, 13):
        balance = balance - monthly_payment
        monthly_interest = balance * monthly_interest_rate
        balance = balance + monthly_interest
    return balance


# Make starting balance a constant for repeated use of remaining balance function
starting_balance = balance

# Set low & high guess interval (high value takes into account very high interest rate that could cause
# monthly payment > starting balance. /12 at the end of high value since monthly interest rate is always less than
# (1/12) of compounded balance
low = 0
high = (starting_balance * (1 + annualInterestRate/12)**12)/12

# Starting guess
monthlyPayment = (low + high)/2
balance = annual_remaining_balance(starting_balance, annualInterestRate, monthlyPayment)

# Tolerance limit
epsilon = 0.01

# Bisection search begins
while abs(balance) >= epsilon:
    if balance > 0:
        low = monthlyPayment
    else:
        high = monthlyPayment
    monthlyPayment = (low + high)/2
    balance = annual_remaining_balance(starting_balance, annualInterestRate, monthlyPayment)

print("Lowest payment:", round(monthlyPayment,2), "balance")