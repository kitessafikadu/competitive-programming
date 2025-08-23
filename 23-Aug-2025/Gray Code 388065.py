# Problem: Gray Code - https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]