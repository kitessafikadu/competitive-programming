# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq_map = Counter(nums)
        result = []
        for key in freq_map.keys():
            if freq_map[key] > 1:
                result.append(key)

        return result