# Problem: Process Restricted Friend Requests - https://leetcode.com/problems/process-restricted-friend-requests/

class Solution:
    def friendRequests(self, n: int, restrictions: list[list[int]], requests: list[list[int]]) -> list[bool]:
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            parent[find(x)] = find(y)

        res = []
        for u, v in requests:
            pu, pv = find(u), find(v)
            if pu == pv:
                res.append(True)
                continue

            # check if merging violates restrictions
            valid = True
            for x, y in restrictions:
                px, py = find(x), find(y)
                if (px == pu and py == pv) or (px == pv and py == pu):
                    valid = False
                    break

            if valid:
                union(pu, pv)
                res.append(True)
            else:
                res.append(False)

        return res
