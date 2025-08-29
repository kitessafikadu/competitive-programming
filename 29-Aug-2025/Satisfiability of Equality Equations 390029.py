# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        def find(x):
            if x not in parent:
                parent[x] = x
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        for eq in equations:
            if eq[1:3] == "==":
                union(eq[0], eq[3])
        for eq in equations:
            if eq[1:3] == "!=":
                if find(eq[0]) == find(eq[3]):
                    return False
        return True