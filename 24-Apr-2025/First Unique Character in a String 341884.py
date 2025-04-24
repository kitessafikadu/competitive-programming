# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq=Counter(s)
        
        for i,char in enumerate(s):
            if freq[char] == 1:
                return i
        return -1