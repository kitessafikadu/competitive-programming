# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n,m = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

left,right = 0,0
res = []
while left < n and right < m:
  if A[left] < B[right]:
    res.append(A[left])
    left += 1
  else:
    res.append(B[right])
    right += 1

res.extend(A[left:])
res.extend(B[right:])

print(*res)

