class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = m + n - 2
        one = m - 1
        two = n - 1
        def factorial(num):
            res = 1
            for i in range(1, num + 1):
                res *= i
                print(res)
            return res

        return int(factorial(total)/(factorial(one) * factorial(two)))
            