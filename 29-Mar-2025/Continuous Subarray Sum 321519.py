# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0:-1}
        sum_ = 0 
        for i,num in enumerate(nums):
            sum_ += num
            remainder = sum_%k
            if remainder not in remainder_map:
                remainder_map[remainder] = i
            elif i - remainder_map[remainder] >= 2:
                return True
            
        return False