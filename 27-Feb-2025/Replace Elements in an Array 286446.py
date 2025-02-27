# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_map = {num: i for i, num in enumerate(nums)} 

        for old, new in operations:
            index_ = index_map[old]  
            nums[index_] = new  
            index_map[new] = index_  
            del index_map[old]

        return nums