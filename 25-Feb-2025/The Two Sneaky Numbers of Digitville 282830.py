# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq_map = Counter(nums)
        result = []

        for key, value in freq_map.items():
            if freq_map[key] > 1:
                result.append(key)

        return result
        