# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        dic = {}
        res = []

        for i in range(len(nums)):
            if sortedNums[i] not in dic:
                dic[sortedNums[i]] = i

        for num in nums:
            res.append(dic[num])
        
        return res