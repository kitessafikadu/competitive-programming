# Problem: Kefa and Company - https://codeforces.com/problemset/problem/580/B

n, d = map(int, input().split())
friends = [tuple(map(int, input().split())) for _ in range(n)]

friends.sort()

max_friendship = 0
current_friendship = 0
left = 0  

for right in range(n):
    current_friendship += friends[right][1]  
    
    while friends[right][0] - friends[left][0] >= d:
        current_friendship -= friends[left][1]  
        left += 1  
    
    max_friendship = max(max_friendship, current_friendship)  

print(max_friendship)
