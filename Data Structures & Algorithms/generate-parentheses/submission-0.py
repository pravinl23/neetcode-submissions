class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtracking(path, openedCounter):
            if len(path) == 2 * n:
                if openedCounter == 0:
                    res.append("".join(path))
                return

            # case 1 open:
            if openedCounter < n:
                path.append("(")
                backtracking(path, openedCounter + 1)
                path.pop()
            
            # case 2 closed
            if openedCounter > 0:
                path.append(")")
                backtracking(path, openedCounter - 1)
                path.pop()

        backtracking([], 0)

        return res