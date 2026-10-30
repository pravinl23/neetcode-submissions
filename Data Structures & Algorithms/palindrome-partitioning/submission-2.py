class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = 1

        def backtrack(path, i):
            if i == n:
                res.append(path[:])
                return

            for j in range(i, n):
                if dp[i][j]:
                    path.append(s[i : j + 1])
                    backtrack(path, j + 1)
                    path.pop()

        backtrack([], 0)
        return res