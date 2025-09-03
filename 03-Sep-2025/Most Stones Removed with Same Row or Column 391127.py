# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        visited = set()
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if j not in visited:
                    # same row or same column
                    if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                        dfs(j)
        
        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        return n - components
