from math import pow
from copy import copy

primes = []


for i in range(2, 101):
    for j in primes:
        if i % j == 0:
            break
    else:
        primes.append(i)

print(primes)

numbers = list(range(2, 101))

factor = [[] for _ in range(101)]

for i in range(2, 101):
    if i in primes:
        factor[i].append(i)
        continue
    for j in primes:
        if i % j == 0:
            factor[i] = copy(factor[i // j])
            factor[i].append(j)
# print(factor)

for j in primes:
    numbers.remove(j)
for i in range(len(primes)):
    for j in range(i, len(primes)):
        x = primes[i] * primes[j]
        if (x <= 100):
            numbers.remove(x)

for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        x = primes[i] * primes[j] * primes[i]
        if (x <= 100):
            numbers.remove(x)
        x = primes[i] * primes[j] * primes[j]
        if (x <= 100):
            numbers.remove(x)

for i in primes:
    for j in range(3, 7):
        x = pow(i, j)
        if (x in numbers):
            numbers.remove(x)

for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        for k in range(j + 1, len(primes)):
            x = primes[i] * primes[j] * primes[k]
            if x in numbers:
                numbers.remove(x)

numbers.remove(60)
numbers.remove(24)
numbers.remove(48)
numbers.remove(96)
numbers.remove(40)
numbers.remove(80)
numbers.remove(36)
numbers.remove(54)
numbers.remove(56)
numbers.remove(72)
numbers.remove(84)
numbers.remove(88)

# print(numbers)
for i in numbers:
    print(i, factor[i])
