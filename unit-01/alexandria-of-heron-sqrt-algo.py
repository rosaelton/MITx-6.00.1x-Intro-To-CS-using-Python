#!/usr/bin/env python3

def sqrt(n: float) -> float:
    epsilon = 0.000000001
    guess = 1

    while abs(n - guess * guess) > epsilon:
        print(guess)
        guess = (guess + n/guess) / 2.0

    return guess

if __name__ == "__main__":
    print(sqrt(1_000_001))
