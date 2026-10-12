class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {}
        def solve(i):
            if i < n and s[i] == "0":
                return 0
            if i >= n - 1:
                return 1
            if i in dp:
                return dp[i]
            num = int(s[i]) * 10 + int(s[i + 1])
            if 10 <= num <= 26:
                dp[i] = solve(i + 1) + solve(i + 2)
            else:
                dp[i] = solve(i + 1)

            return dp[i]

        dp[0] = solve(0)
        return dp[0]

        
