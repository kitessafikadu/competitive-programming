# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for bitIndex in range(32):  # check each of 32 bits
            count = 0
            for num in nums:
                if (num >> bitIndex) & 1:
                    count += 1
            if count % 3:  # if not divisible by 3, this bit belongs it
                ans |= (1 << bitIndex)
            if ans >= (1 << 31):
                ans -= (1 << 32)

        return ans