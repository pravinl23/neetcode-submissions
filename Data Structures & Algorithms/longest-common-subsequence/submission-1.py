class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1) + 1
        cols = len(text2) + 1
        dp = [[0] * cols for _ in range(rows)]
        m = 0
        for row in range(1, rows):
            for col in range(1, cols):
                if text1[row-1] == text2[col-1]:
                    dp[row][col] = 1 + dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
                
        return dp[len(text1)][len(text2)]
        