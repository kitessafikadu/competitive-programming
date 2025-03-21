# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left,longest,count_repet = 0,0,0

        for right in range(0, len(s)):
            if right > 0 and s[right] == s[right-1]:
                count_repet += 1
            while count_repet > 1:
                left += 1
                count_repet -= s[left] == s[left-1]
            longest = max(longest, right-left+1)
        return longest
        