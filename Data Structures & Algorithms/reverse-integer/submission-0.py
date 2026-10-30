class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        MIN = -2 ** 31
        MAX = (2 ** 31) - 1
        neg = 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        digits = math.floor(math.log10(x) + 1)

        for i in range(digits):
            d = (x // 10 ** i) % 10
            if res > MAX // 10 or (res >= MAX // 10 and d > MAX % 10):
                return 0
            res = res * 10 + d

        
        return res * sign            
