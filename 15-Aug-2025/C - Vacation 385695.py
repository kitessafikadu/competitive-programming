# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

n = int(input())
a = []
b = []
c = []
for _ in range(n):
    x, y, z = map(int, input().split())
    a.append(x)
    b.append(y)
    c.append(z)
# dp[i][0] = max happiness if choosing A on day i
dp = [[0] * 3 for _ in range(n)]
dp[0][0] = a[0]
dp[0][1] = b[0]
dp[0][2] = c[0]
for i in range(1, n):
    dp[i][0] = a[i] + max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = b[i] + max(dp[i-1][0], dp[i-1][2])
    dp[i][2] = c[i] + max(dp[i-1][0], dp[i-1][1])
print(max(dp[n-1]))
