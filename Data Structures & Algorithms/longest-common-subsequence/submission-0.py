class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []
        for row in range(len(text1)):
            dp.append([])
            for col in range(len(text2)):
                dp[row].append(0)
        m = 0
        for row in range(len(text1)):
            for col in range(len(text2)):
                top_left, left, top = 0,0,0
                if row-1 >= 0 and col-1 >= 0:
                    top_left = dp[row-1][col-1]
                if row-1 >= 0:
                    top = dp[row-1][col]
                if col-1 >= 0:
                    left = dp[row][col-1]
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + top_left
                else:
                    dp[row][col] = max(left, top)
                m = max(m, dp[row][col])
        return m
        