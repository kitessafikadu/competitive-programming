# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        prefix = [0] * (n + 1)

        for start, end, d in shifts:
            shift_value = 1 if d == 1 else -1
            prefix[start] += shift_value
            prefix[end + 1] -= shift_value

        shift = 0
        res = []
        for i in range(n):
            shift += prefix[i] 
            new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            res.append(new_char)

        return "".join(res)
        