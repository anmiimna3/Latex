from math import gcd

for i in range(2, 40):
    ans = 0
    for j in range(1, i):
        if (gcd(i, j) == 1):
            ans += j
    print(i, ": ", ans)