# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = 0
        left = 0
        seen = set()
        cur_sum = 0 # total sum upto right element

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                cur_sum -= nums[left]
                left += 1
            seen.add(nums[right])
            cur_sum += nums[right]
            max_score = max(max_score, cur_sum)
        return max_score


        

        


        