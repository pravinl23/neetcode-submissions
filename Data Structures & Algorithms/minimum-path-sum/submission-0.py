class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        numCols = len(grid[0])
        numRows = len(grid)
        dp = [[0 for _ in range(numCols + 1)] for _ in range(numRows + 1)]
        for r in range(numRows + 1):
            dp[r][numCols] = 201
        for c in range(numCols + 1):
            dp[numRows][c] = 201
        dp[numRows - 1][numCols] = 0
        dp[numRows][numCols - 1] = 0
        
        
        
        for r in range(numRows - 1, -1, -1):
            for c in range(numCols - 1, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])

        return dp[0][0]
