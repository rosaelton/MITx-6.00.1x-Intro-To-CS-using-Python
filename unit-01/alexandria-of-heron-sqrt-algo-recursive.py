#!/usr/bin/env python3

def _recursive_sqrt(n: float, guess: float) -> float:
    epsilon = 0.000000001
    if abs(n - guess * guess) < epsilon:
        return guess
    return _recursive_sqrt(n, (guess + n/guess) / 2)


def sqrt(n: float) -> float:
    return _recursive_sqrt(n, 1)

if __name__ == "__main__":
    print(sqrt(1))
