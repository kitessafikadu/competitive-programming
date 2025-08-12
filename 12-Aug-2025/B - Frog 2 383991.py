# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

N, K = map(int, input().split())
h = list(map(int, input().split()))
dp =[float('inf')] * N
dp[0] = 0
for i in range(1, N):
    for j in range(max(0, i - K), i):
        dp[i]= min(dp[i], dp[j] + abs(h[i] - h[j]))
print(dp[-1])
