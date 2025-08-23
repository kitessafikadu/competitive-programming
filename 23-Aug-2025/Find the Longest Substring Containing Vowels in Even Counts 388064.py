# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        mask = 0
        first_occurrence = {0: -1}
        max_len = 0
        for i, ch in enumerate(s):
            if ch in vowel_to_bit:
                mask ^= (1 << vowel_to_bit[ch])
            if mask in first_occurrence:
                max_len = max(max_len, i - first_occurrence[mask])
            else:
                first_occurrence[mask] = i
        return max_len