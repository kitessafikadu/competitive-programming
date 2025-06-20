# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p=0 #perimeter
        rows,cols=len(grid),len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    p+=4
                    if r>0 and grid[r-1][c]==1:
                        p-=2
                    if c>0 and grid[r][c-1]==1:
                        p-=2
        return p