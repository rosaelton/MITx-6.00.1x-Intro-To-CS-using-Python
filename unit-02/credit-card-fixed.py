#!/usr/bin/env python3

def lowest_payment(balance, annual_interest_rate):

    def _lowest(b, i, value, month):
        if month > 12 and b > 0:
            return _lowest(balance, i, value + 10, 1)

        if month > 12 and b <= 0:
            return value
    
        b = b - value
        b = round(b * (1 + i / 12), 2)
        return _lowest(b, i, value, month + 1)

    return _lowest(balance, annual_interest_rate, 10, 1)

print(lowest_payment(3926, 0.2))
