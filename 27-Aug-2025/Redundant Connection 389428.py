# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False  # cycle
            parent[rootX] = rootY
            return True
        for u, v in edges:
            if not union(u, v):
                return [u, v]