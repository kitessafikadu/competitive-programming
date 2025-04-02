# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        total_pairs = 0
        left = 0
        good_subarrays = 0

        for right in range(len(nums)):
            total_pairs += freq[nums[right]]  
            freq[nums[right]] += 1

            # If we have at least k pairs, count valid subarrays
            while total_pairs >= k:
                good_subarrays += len(nums) - right  
                total_pairs -= (freq[nums[left]] - 1)  
                freq[nums[left]] -= 1
                left += 1
        
        return good_subarrays