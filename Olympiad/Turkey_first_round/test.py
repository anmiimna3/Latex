a = [0, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]




M = [[0 for _ in range(13)] for _ in range(13)]

M[0][10] = 2
M[0][11] = 2
M[0][12] = 2
M[12][0] = 0
M[11][0] = 0
M[10][0] = 0
print(*M, sep='\n')
print('-' * 50)

for i in range(13):
    # print(i, a[i])
    j = i
    while a[i] > 0:
        if j == i:
            M[i][j] = 0
        elif a[i] > 1:
            M[i][j] = 2
            M[j][i] = 0
            a[i] -= 2
        elif a[i] == 1:
            a[i] -= 1
            a[j] -= 1
            M[i][j] = 1
            M[j][i] = 1
        j += 1
        if (i == 0 and j == 10) or j == 13:
            break
    for k in range(j, 13):
        if (i == 0 and k == 10):
            break
        if (k > i):
            M[i][k] = 0
            M[k][i] = 2
            a[k] -= 2
    print(M[i], sum(M[i]))

