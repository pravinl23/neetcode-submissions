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
                if isPalindrome(s[i:j + 1]):
                    path.append(s[i:j + 1])
                    backtrack(path, j + 1)
                    path.pop()
            
        backtrack([], 0)
        return res