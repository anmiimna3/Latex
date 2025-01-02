from math import gcd

n = 144

for i in range(1, n):
    x = i**5 + i - 6
    if (x % 144 == 0):
        print(i)
    