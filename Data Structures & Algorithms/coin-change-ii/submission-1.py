class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # coin_i, amount
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        for c in range(n + 1):
            dp[c][amount] = 1


        for c in range(c - 1, -1, -1):
            for amt in range(amount - 1, -1, -1):
                dp[c][amt] = dp[c + 1][amt]
                if amt + coins[c] <= amount:
                    dp[c][amt] = max(dp[c][amt] + dp[c][amt + coins[c]], dp[c][amt])

        return dp[0][0]
