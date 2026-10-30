class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(r, c):
            for prevr, prevc in cells:
                if prevr == r or prevc == c:
                    return False
                if abs((prevr - r)/(prevc - c)) == 1:
                    return False

            return True
                
        cells = []
        res = []
        def backtrack(path, r):
            if r == n:
                output = []
                for p in path:
                    output.append("".join(p))
                res.append(output)
                return

            for c in range(n):
                if isSafe(r, c):
                    cells.append([r,c])
                    path[r][c] = "Q"
                    backtrack(path, r + 1)
                    path[r][c] = "."
                    cells.pop()

        p = [["."] * n for _ in range(n)]
        backtrack(p, 0)
        return res