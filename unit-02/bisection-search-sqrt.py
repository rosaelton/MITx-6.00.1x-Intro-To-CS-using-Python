#!/usr/bin/env python3

def bissection_sqrt(min: float, max:float, n:float, epsilon: float) -> float:
    guess = (min + max) / 2.0

    print(f"Min: {min}; Max: {max}; Guess: {guess}")
    
    if abs(guess ** 2 - n) <= epsilon:
        return guess
    if guess ** 2 > n:
        return bissection_sqrt(min, guess, n, epsilon)
    return bissection_sqrt(guess, max, n, epsilon)

if __name__ == "__main__":
    print(bissection_sqrt(1, 27, 27, 0.0001))
