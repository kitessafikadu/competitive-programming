# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        subarray_after_op = sum(nums) - x
        if subarray_after_op < 0:
            return -1  

        max_subarray_len = -1
        current_sum = 0
        left = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum > subarray_after_op and left <= right:
                current_sum -= nums[left]
                left += 1
            if current_sum == subarray_after_op:
                max_subarray_len = max(max_subarray_len, right - left + 1)
        return len(nums) - max_subarray_len if max_subarray_len != -1 else -1
