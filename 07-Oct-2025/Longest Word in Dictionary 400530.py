# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        valid=set([""])
        longest=""

        for word in words:
            if word[:-1] in valid:
                valid.add(word)
                if len(word) > len(longest):
                    longest=word

        return longest
