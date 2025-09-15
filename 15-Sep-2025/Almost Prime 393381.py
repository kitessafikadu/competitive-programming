# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input().strip())
factors = [0] * (n + 1)
for p in range(2, n + 1):
    if factors[p] == 0:
        for multiple in range(p, n + 1, p):
            factors[multiple] += 1
ans = sum(1 for i in range(2, n + 1) if factors[i] == 2)
print(ans)