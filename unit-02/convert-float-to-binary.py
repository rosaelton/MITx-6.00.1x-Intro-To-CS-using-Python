#!/usr/bin/env python3

def to_binary(n: int) -> str:
    if n == 0:
        return '0'

    n = abs(n)

    result = ''
    while n > 0:
        result = str(n % 2) + result    
        n = n // 2

    return result

if __name__ == "__main__":
    x = float(input("Insert a number between 0 and 1: "))

    p = 0
    while (x * 2 ** p)%1 != 0:
        print("Remainder: " + str((x * 2 ** p) - int(x * 2 ** p)))
        p += 1

    num = int(x * 2 ** p)

    result = to_binary(num)

    for i in range(p - len(result)):
        result = '0' + result

    result = result[0:-p] + "." + result[-p:]

    print(result)

