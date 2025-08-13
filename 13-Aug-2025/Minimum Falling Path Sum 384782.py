# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                # Get the possible top values
                top_left = matrix[i-1][j-1] if j > 0 else float('inf')
                top = matrix[i-1][j]
                top_right = matrix[i-1][j+1] if j < n-1 else float('inf')
                matrix[i][j] += min(top_left, top, top_right)
        return min(matrix[-1])