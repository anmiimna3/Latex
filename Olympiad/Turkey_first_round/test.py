def choose(n):
    return (n * (n - 1)) // 2


sum = 0
for i in range(2, 12):
    sum += choose(i) * (12 - i)
print(sum)