# Problem: Last Stone Weight II - https://leetcode.com/problems/last-stone-weight-ii/description/

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        S = sum(stones)
        target = S // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for w in stones:
            for s in range(target, w - 1, -1):
                if dp[s - w]:
                    dp[s] = True
        for t in range(target, -1, -1):
            if dp[t]:
                return S - 2 * t
        return 0