# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2 :
            return False
        s1_count = Counter(s1)
        window_count = Counter(s2[:n1])
        if s1_count == window_count:
            return True
        for i in range(n1,n2):
            window_count[s2[i]] += 1
            window_count[s2[i-n1]] -= 1
            if window_count[s2[i-n1]] == 0:
                window_count.pop(s2[i-n1])
            if s1_count == window_count:
                return True
        return False
