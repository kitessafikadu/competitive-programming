# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            graph[u].append((v, w))

        min_heap = [(0, k)]
        dist = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in dist:
                continue
            dist[node] = time
            for nei, w in graph[node]:
                if nei not in dist:
                    heapq.heappush(min_heap, (time + w, nei))

        return max(dist.values()) if len(dist) == n else -1