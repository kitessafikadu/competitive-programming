# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                diff.append((s1[i], s2[i]))

        return count == 0 or (count == 2 and diff[0] == diff[1][::-1])