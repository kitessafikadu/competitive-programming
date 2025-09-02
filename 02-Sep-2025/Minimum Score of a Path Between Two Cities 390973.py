# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)  # node -> list of (neighbor, dist)

        for src, dst, dist in roads:
            adj[src].append((dst, dist))
            adj[dst].append((src, dist))

        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            nonlocal res
            for nei, dist in adj[i]:
                res = min(res, dist)
                dfs(nei)

        res = float("inf")
        visit = set()
        dfs(1)
        return res
