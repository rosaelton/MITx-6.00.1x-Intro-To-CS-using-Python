#!/usr/bin/env python3

def lowest_payment(balance, annual_interest_rate):

    def _lowest(b, i, lower, upper, month):
        payment = (lower + upper)/2
        if month > 12 and b > 0.2:
            new_lower = payment + 0.01
            return _lowest(balance, i, new_lower, upper, 1)
        elif month > 12 and b < 0:
            new_upper = payment 
            return _lowest(balance, i, lower, new_upper, 1)
        elif month > 12:
            return round(payment, 2)

        b = b - payment
        b = round(b * (1 + i / 12), 2)
        return _lowest(b, i, lower, upper, month + 1)
    
    lower_guess = balance / 12
    upper_guess = (balance * (1 + annual_interest_rate) ** 12) / 12.0
    return _lowest(balance, annual_interest_rate, lower_guess, upper_guess, 1)


balance = 143915
annualInterestRate = 0.21

print("Lowest Payment:", lowest_payment(balance, annualInterestRate))
