# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state: buying or selling
        # buy->=i+1
        # sell->i+2
        dp={}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i,buying)]
            cooldown=dfs(i+1, buying)
            if buying:
                buy=dfs(i+1, not buying)-prices[i]
                dp[(i,buying)]=max(buy, cooldown)
            else:
                sell=dfs(i+2, not buying)+prices[i]
                dp[(i,buying)]=max(sell, cooldown)               
            return dp[(i, buying)]
        return dfs(0, True)