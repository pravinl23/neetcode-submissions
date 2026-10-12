class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[1] = 1
        dp[2] = 2

        for i in range(1,n + 1):
            if i in dp:
                continue
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]
        