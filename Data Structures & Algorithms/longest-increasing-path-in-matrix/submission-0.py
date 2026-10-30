class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        DIRS = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(r, c, d):
            if dp[r][c] != 0:
                return dp[r][c]
            m = 0
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                    if matrix[nr][nc] > matrix[r][c]:
                        dfs(nr, nc, d + 1)
                        m = max(m, dp[nr][nc])

            dp[r][c] = 1 + m
            return dp[r][c]
        res = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res = max(res, dfs(r, c, 1))

        return res

            