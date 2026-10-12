class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0

        coins.sort(reverse = True)
        for i in range(1, amount + 1):
            ways = amount + 1
            for c in coins:
                if i - c >= 0 and dp[i - c] >= 0:
                    ways = min(dp[i - c] + 1, ways)
            if ways != amount + 1:
                dp[i] = ways
        print(dp)
        return dp[amount]