#!/usr/bin/env python3

def to_binary(n: int) -> str:
    if n == 0:
        return '0'

    isNegative = False
    if n < 0:
        isNegative = True

    n = abs(n)

    result = ''
    while n > 0:
        result = str(n % 2) + result    
        n = n // 2

    if isNegative:
        result = "-" + result

    return result

if __name__ == "__main__":
    print(to_binary(19))

