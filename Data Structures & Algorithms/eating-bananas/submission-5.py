import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(speed):
            t = 0
            for p in piles:
                t += math.ceil(p / speed)
            return t

        lo, hi = 1, max(piles)
        res = hi
        while lo <= hi:
            m = (lo + hi) // 2
            time = eat(m)
            if time <= h:
                res = min(res, m)
                hi = m - 1
            elif time >= h:
                lo = m + 1
        return res

        
