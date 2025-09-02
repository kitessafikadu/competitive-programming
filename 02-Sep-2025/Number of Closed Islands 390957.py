# Problem: Number of Closed Islands - https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS):
                return 0  # False (touches border)

            if grid[r][c] == 1 or (r, c) in visit:
                return 1  # True (valid land cell)

            visit.add((r, c))

            return min(
                dfs(r + 1, c),
                dfs(r - 1, c),
                dfs(r, c + 1),
                dfs(r, c - 1)
            )

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 and (r, c) not in visit:
                    count += dfs(r, c)
        return count
