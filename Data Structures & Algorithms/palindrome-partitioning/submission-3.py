class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        def isPalindrome(s):
            return s[::-1] == s

        def backtrack(path, i):
            if i == n:
                res.append(path[:])
                return

            for j in range(i, n):
                a = s[i:j + 1]
                if isPalindrome(a):
                    path.append(a)
                    backtrack(path, j + 1)
                    path.pop()
            
        backtrack([], 0)
        return res