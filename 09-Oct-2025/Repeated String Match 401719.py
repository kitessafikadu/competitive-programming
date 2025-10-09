# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeated = a
        count = 1
        while len(repeated) < len(b):
            repeated += a
            count += 1
        if b in repeated:
            return count
        if b in repeated + a:
            return count + 1
        return -1