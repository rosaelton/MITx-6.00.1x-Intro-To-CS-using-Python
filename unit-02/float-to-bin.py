#!/usr/bin/env python3

def to_binary(n: int) -> str:
    if n == 0:
        return '0'

    result = ''
    while n > 0:
        result = str(n % 2) + result
        n = n >> 1
    return result

if __name__ == "__main__":
    x = float(input("Insert a number between 0 and 1: "))

    p = 0
    while (x * 2 ** p)%1 != 0:
        p += 1

    result = str(to_binary(int(x * 2 ** p)))

    for i in range(p - len(result)):
        result = "0" + result 

    result = result[:-p] + "." + result[-p:]
    print(result)

