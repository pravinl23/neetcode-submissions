class Solution:
    def rob(self, nums: List[int]) -> int:
        def robHelper(lon: List[int]) -> int:
            n = len(lon)
            if n <= 2:
                return max(lon)

            dp = [0 for _ in range(n)]
            dp[n - 1] = lon[n - 1]
            dp[n - 2] = max(lon[n - 2], dp[n - 1])
            for i in range(n - 3, -1, -1):
                dp[i] = max(lon[i] + dp[i + 2], dp[i + 1])

            return dp[0]
        if len(nums) <= 2:
                return max(nums)
        return max(robHelper(nums[:len(nums) - 1]), robHelper(nums[1:]))