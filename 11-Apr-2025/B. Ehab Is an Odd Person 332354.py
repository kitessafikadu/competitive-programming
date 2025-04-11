# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n=int(input())

nums=list(map(int,input().split()))

odd=any(x%2==0 for x in nums)

even=any(x%2==1 for x in nums)


if odd and even:
    nums.sort()
print(*nums)