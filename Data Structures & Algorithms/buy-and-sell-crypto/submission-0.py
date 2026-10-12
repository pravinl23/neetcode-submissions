class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        globalMax = 0
        while r < len(prices):
            newPrice = prices[r] - prices[l]
            globalMax = max(newPrice, globalMax)

            if prices[l] < prices[r]:
                r += 1
            else:
                l = r
                r += 1

        return globalMax