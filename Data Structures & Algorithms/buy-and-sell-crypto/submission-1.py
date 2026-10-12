class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        running_sum = prices[0]
        l, r = 0, 1
        while r < len(prices):
            running_sum = prices[r] - prices[l]
            if running_sum <= 0:
                l = r
                r = l + 1
            elif running_sum > 0:
                m = max(m, running_sum)
                r += 1 
        return m
