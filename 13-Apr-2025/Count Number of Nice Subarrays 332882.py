# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = 0
        nice_count = 0
        freq = {0:1}
        for num in nums:
            odd_count += num%2
            nice_count += freq.get(odd_count - k, 0)
            freq[odd_count] = freq.get(odd_count, 0) + 1
        
        return nice_count