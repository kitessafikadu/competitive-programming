# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_count = 0  
        res = 0
        count = {}  

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1  
            res = max(res, right - left + 1)
        return res