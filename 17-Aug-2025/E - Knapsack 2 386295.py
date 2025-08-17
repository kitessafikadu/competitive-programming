# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
MAX_VALUE = sum(v for _, v in items)
INF = 10**18
dp = [INF] * (MAX_VALUE + 1)
dp[0] = 0
for w, v in items:
    for val in range(MAX_VALUE, v - 1, -1):
        dp[val] = min(dp[val], dp[val - v] + w)
ans = 0
for val in range(MAX_VALUE + 1):
    if dp[val] <= W:
        ans = val
print(ans)