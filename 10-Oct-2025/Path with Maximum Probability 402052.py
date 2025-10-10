# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0
        heap = [(-1.0, start_node)]  # use negative for max heap

        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob

            if node == end_node:
                return prob

            for nei, p in graph[node]:
                new_prob = prob * p
                if new_prob > max_prob[nei]:
                    max_prob[nei] = new_prob
                    heapq.heappush(heap, (-new_prob, nei))

        return 0.0
