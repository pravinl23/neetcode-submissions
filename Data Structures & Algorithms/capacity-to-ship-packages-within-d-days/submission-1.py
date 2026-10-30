class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canComplete(k):
            i = 0
            for _ in range(days):
                w = 0
                while i < len(weights) and w + weights[i] <= k:
                    w += weights[i]
                    i += 1
            return i == len(weights)

        lo, hi = 0, sum(weights)
        res = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if canComplete(mid):
                res = min(res, mid)
                hi = mid - 1
            else:
                lo = mid + 1

        return res
        