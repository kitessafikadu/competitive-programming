# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            odd = center(i, i)
            if len(odd) > len(longest):
                longest = odd

            even = center(i, i + 1)
            if len(even) > len(longest):
                longest = even

        return longest
