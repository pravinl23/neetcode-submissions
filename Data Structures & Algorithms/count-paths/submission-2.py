class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m): #y
            dp.append([])
            for _ in range(n): #x
                dp[i].append(0)
        dp[0][0] = 1
        for y in range(m):
            for x in range(n):
                if x == y == 0:
                    continue
                dp[y][x] = dp[max(y-1, 0)][x] + dp[y][max(x-1, 0)]
                
        return dp[m - 1][n - 1]
        