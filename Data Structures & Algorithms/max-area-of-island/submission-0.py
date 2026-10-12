class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        def dfs(r,c):
            if r < 0 or r == num_rows or c < 0 or c == num_cols:
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

        m = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1:
                    m = max(m, dfs(r,c))
        

        return m