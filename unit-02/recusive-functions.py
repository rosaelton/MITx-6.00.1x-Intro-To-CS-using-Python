def mult(a, b):
    if b == 1:
        return a
    return a + mult(a, b - 1)

def fac(n: int) -> int:
    if n <= 1:
        return 1
    return n * fac(n - 1)

print(mult(3, 100))
print(fac(3))
