# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        longest = 0
        left = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            longest = max(longest, right - left + 1)
        return longest