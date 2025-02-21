# Problem: Maximum Sum of an Hourglass - LeetCode - https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_sum = float("-inf")

        for i in range(rows-2):
            for j in range(cols-2):
                hourglass_sum = (
                    grid[i][j] + grid[i][j+1] + grid[i][j+2] +
                                grid[i+1][j+1] +
                    grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]            
                )

                max_sum = max(max_sum, hourglass_sum)

        return max_sum