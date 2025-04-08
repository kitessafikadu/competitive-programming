# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        count = 0

        for i in range(n):
            vowels = set()
            for j in range(i, n):
                if word[j] in 'aeiou':
                    vowels.add(word[j])
                    if len(vowels) == 5:
                        count += 1
                else:
                    break  # not a vowel anymore, stop this substring

        return count