class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path, openCount, closeCount):
            if closeCount > openCount or openCount > n:
                return
            if closeCount == n and openCount == closeCount:
                res.append(path)
                return
            
            
            backtrack(path + ")", openCount, closeCount + 1)
            backtrack(path + "(", openCount + 1, closeCount)
            

        backtrack("(", 1, 0)
        return res