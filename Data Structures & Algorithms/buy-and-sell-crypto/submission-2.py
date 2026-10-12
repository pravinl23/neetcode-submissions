class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        m = 0
        for r in range(1, len(prices)):
            delta = prices[r] - prices[l]
            if delta > 0:
                m = max(m, delta)
            else:
                l = r

        return m