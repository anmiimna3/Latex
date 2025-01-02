n = int(input())


for i in range(1, n):
    for j in range(1, n):
        if j * j % n == i:
            print(i, "yes", j)
            break
    else:
        print(i, "no")