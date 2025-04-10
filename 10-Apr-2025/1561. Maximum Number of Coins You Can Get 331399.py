# Problem: 1561. Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_coin = 0
        n = len(piles)
        for i in range(n//3, n, 2):
            max_coin += piles[i]

        return max_coin 
