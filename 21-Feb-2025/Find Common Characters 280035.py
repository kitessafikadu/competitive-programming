# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_freq = Counter(words[0])
        
        for word in words[1:]:
            common_freq &= Counter(word)
        
        return list(common_freq.elements())