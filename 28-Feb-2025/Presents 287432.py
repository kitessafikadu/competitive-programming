# Problem: Presents - https://codeforces.com/problemset/problem/136/A

n = int(input())  
ans = [0] * n  

for i in range(1, n + 1):  
    p = int(input())  
    ans[p - 1] = i

print(*ans)