# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_sets = [set(w) for w in words]
        res = 0
        for i in range(len(words)):
            for j in range(i):
                if not (word_sets[i] & word_sets[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res