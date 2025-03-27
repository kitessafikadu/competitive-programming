# Problem: Maximum Sum of Distinct Subarrays With Length K - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        num_set = set()
        window_sum = 0
        max_sum = 0
        left = 0

        for right in range(len(nums)):
            while nums[right] in num_set:
                num_set.remove(nums[left])
                window_sum -= nums[left]
                left += 1

            num_set.add(nums[right])
            window_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(max_sum, window_sum)
                num_set.remove(nums[left])
                window_sum -= nums[left]
                left += 1  # Slide window forward

        return max_sum