def problem1():
    def annual_remaining_balance(balance, annual_interest_rate, monthly_payment_rate):
        monthly_interest_rate = annual_interest_rate / 12

        for month in range(1, 13):
            balance = balance * (1 - monthly_payment_rate)
            monthly_interest = balance * monthly_interest_rate
            balance = balance + monthly_interest

        return balance

    def main():
        balance = 484
        annualInterestRate = 0.2
        monthlyPaymentRate = 0.04
        print("Remaining balance:", round(annual_remaining_balance(balance, annualInterestRate, monthlyPaymentRate), 2))

    main()


def problem2():
    def annual_remaining_balance(balance, annual_interest_rate, monthly_payment, months):
        monthly_interest_rate = annual_interest_rate / months

        for month in range(1, months + 1):
            balance = balance - monthly_payment
            monthly_interest = balance * monthly_interest_rate
            balance = balance + monthly_interest
        return balance

    def main():
        starting_balance = 3329
        annualInterestRate = 0.2

        months = 12
        balance = starting_balance
        monthlyPayment = 250

        while balance > 0:
            balance = annual_remaining_balance(starting_balance, annualInterestRate, monthlyPayment, months)
            lowest_payment = monthlyPayment
            monthlyPayment += 10
            # print(monthlyPayment, balance)

        print("Lowest payment:", lowest_payment)

    main()


problem2()