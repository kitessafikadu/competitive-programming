# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        count = float('inf')
        cur_window_sum = 0

        for right in range(0, len(nums)):
            cur_window_sum += nums[right]

            while cur_window_sum >= target:
                count = min(count, right - left + 1)
                cur_window_sum -= nums[left]
                left += 1
        return count if count != float('inf') else 0

        