class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        def dfs(r, c):
            if r < 0 or r == numRows or c < 0 or c == numCols:
                return
            
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        counter = 0
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == "1":
                    counter += 1
                    dfs(r, c)
        
        return counter



