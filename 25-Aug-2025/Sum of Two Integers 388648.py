# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # return sum([a,b])
        mask = 0xFFFFFFFF
        while (mask & b)>0:
            a,b=a^b, (a&b)<<1
        return (mask&a) if b>0 else a