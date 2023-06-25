def remaining_balance(balance, annual_interest_rate, monthly_payment_rate):
    def _month_bal(b, i, pr, m):
        if m > 12:
            print("Remaining balance:", b)
            return
        p = b * pr
        b = b - p
        b = round(b * (1 + i/12), 2)
        # print("Month", m, "Remaining balance:", b)
        return _month_bal(b, i, pr, m + 1)
    
    return _month_bal(balance, annual_interest_rate, monthly_payment_rate, 1)

balance = 42 
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
remaining_balance(balance, annualInterestRate, monthlyPaymentRate)
