# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
            
        res = []
        for i in range(m):
            row = original[i * n : (i + 1) * n]
            res.append(row)

        return res
        