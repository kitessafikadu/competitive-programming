# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(k):
            freq = defaultdict(int)
            left = 0
            count = 0

            for right in range(len(nums)):
                if freq[nums[right]] == 0:
                    k -= 1
                freq[nums[right]] += 1
                while k < 0:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        k += 1
                    left += 1
                count += right - left + 1
            return count
        return atMostK(k) - atMostK(k - 1)