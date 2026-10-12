class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        res = high
        while low <= high:
            k = (low + high) // 2
            totalHours = 0
            for p in piles:
                totalHours += math.ceil(p/k)

            if totalHours <= h:
                res = min(res, k)
                high = k - 1
            else:
                low = k + 1

        return res
            
