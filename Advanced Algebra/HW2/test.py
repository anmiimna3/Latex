
def mulllll(a, b):
    # print(a)
    ans = [0, 0, 0, 0]
    ans[0] = (a[0] * b[0] + a[1] * b[2]) % 5
    ans[1] = (a[0] * b[1] + a[1] * b[3]) % 5
    ans[2] = (a[2] * b[0] + a[3] * b[2]) % 5
    ans[3] = (a[2] * b[1] + a[3] * b[3]) % 5
    return ans

for i in range(5):
    for j in range(5):
        for k in range(5):
            for t in range(5):
                ans = [i, j,k, t]
                b = mulllll(mulllll(ans, ans), ans)
                if b[0] == 1 and b[1] == 0 and b[2] == 0 and b[3] == 1:
                    print(ans)
                    # print(mulllll(ans, ans))
                    # print(b)
