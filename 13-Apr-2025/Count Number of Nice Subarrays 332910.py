# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            left, right = 0, 0
            cur_sum = 0
            count = 0
            while right < len(nums):
                cur_sum += nums[right] % 2
                while cur_sum > k:
                    cur_sum -= nums[left] % 2
                    left += 1
                count += (right - left + 1)
                right += 1
            return count
        return atMost(k) - atMost(k - 1)
