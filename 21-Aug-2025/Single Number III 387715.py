# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for num in nums:
            xor_all ^= num
        mask = xor_all & -xor_all
        a = b = 0
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a, b]