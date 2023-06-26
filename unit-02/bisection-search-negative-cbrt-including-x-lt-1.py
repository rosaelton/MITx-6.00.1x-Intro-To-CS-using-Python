#!/usr/bin/env python3

def _bissection_cbrt(min: float, max:float, n:float, epsilon: float) -> float:
    guess = (min + max) / 2.0

    print(f"Min: {min}; Max: {max}; Guess: {guess}")
    
    if abs(guess ** 3 - n) <= epsilon:
        return guess
    if guess ** 3 > n:
        return _bissection_cbrt(min, guess, n, epsilon)
    return _bissection_cbrt(guess, max, n, epsilon)

def bissection_cbrt(n: float, epsilon: float) -> float:
    if n < 0:
        min = n
        max = -n
    elif n < 1:
        min = 0
        max = 1
    else:
        min = 1
        max = n
    return _bissection_cbrt(min, max, n, epsilon)

if __name__ == "__main__":
    print(bissection_cbrt(0.09, 0.0000001))
