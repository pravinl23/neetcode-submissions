class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        dp = [[0 for _ in range(2*s + 1)] for _ in range(n + 1)]

        if s + target > 2 * s:
            return 0
        dp[n][s + target] = 1
        
        
        for num in range(n - 1, -1, -1):
            for amt in range(2*s, -1, -1):
                if amt + nums[num] < 2*s + 1:
                    dp[num][amt] += dp[num + 1][amt + nums[num]]
                if amt - nums[num] >= 0:
                    dp[num][amt] += dp[num + 1][amt - nums[num]]

        return dp[0][s]
