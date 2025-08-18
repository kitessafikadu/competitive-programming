# Problem: Reducing Dishes - https://leetcode.com/problems/reducing-dishes/

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        res = 0
        prefixSum =0
        for x in reversed(satisfaction):
            prefixSum += x
            if prefixSum > 0:
                res += prefixSum
            else:
                break
        return res