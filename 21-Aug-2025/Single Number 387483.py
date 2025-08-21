# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_map = Counter(nums)
        for num in freq_map:
            if freq_map[num] == 1:
                return num