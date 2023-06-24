s = 'azcbobobegghaklbob'
bob = 0
for i, c in enumerate(s[:-2]):
    if c == 'b' and s[i + 1] == 'o' and s[i + 2] == 'b':
        bob += 1
print("Number of time bob occurs is:", bob)
