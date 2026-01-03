
# def factorial(n):
#     if (n == 0):
#         return 1
#     return n * factorial(n - 1)

# def choose(i, n):
#     a = factorial(n)
#     b = factorial(i) * factorial(n - i)
#     return a // b

# sum = 0

# for i in range(13):
#     for j in range(i + 1, 14):
#         sum += choose(i, 12) * choose(j, 13)

# print(sum / pow(2, 25))
i = 15627
for j in range(2, i):
    if i % j == 0:
        print(j)