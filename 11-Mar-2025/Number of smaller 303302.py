# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n,m = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

res = []
ptr = 0

for b in B:
  while ptr < n and A[ptr] < b:
      ptr += 1
  res.append(ptr)

print(*res)
