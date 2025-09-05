# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        n = len(s)
        graph = defaultdict(list)
        for a, b in pairs:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        s = list(s)  

        def dfs(i, comp):
            visited[i] = True
            comp.append(i)
            for nei in graph[i]:
                if not visited[nei]:
                    dfs(nei, comp)

        for i in range(n):
            if not visited[i]:
                comp = []
                dfs(i, comp)

                chars = sorted(s[j] for j in comp)
                for j, ch in zip(sorted(comp), chars):
                    s[j] = ch

        return "".join(s)
