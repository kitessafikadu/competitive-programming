# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = min(dist[u][v], w)
            dist[v][u] = min(dist[v][u], w)
        for k in range(n):
            for i in range(n):
                if dist[i][k] > distanceThreshold:
                    continue
                for j in range(n):
                    if dist[k][j] > distanceThreshold:
                        continue
                    new_dist = dist[i][k] + dist[k][j]
                    if new_dist < dist[i][j]:
                        dist[i][j] = new_dist
        ans = -1
        min_count = float('inf')
        for i in range(n):
            count = sum(dist[i][j] <= distanceThreshold for j in range(n) if i != j)
            if count < min_count or (count == min_count and i > ans):
                min_count = count
                ans = i
        return ans