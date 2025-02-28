# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_map = Counter(nums)
        result = []

        for key in freq_map.keys():
            if freq_map[key] > len(nums)/3:
                result.append(key)

        return result