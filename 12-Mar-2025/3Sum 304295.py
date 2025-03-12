# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  

        for i in range(len(nums)):
            if nums[i] > 0:
                break            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])                    
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1                   
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif three_sum < 0:
                    left += 1  
                else:
                    right -= 1  

        return res