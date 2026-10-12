class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        numRows = len(board)
        numCols = len(board[0])
        n = len(word)
        DIRS = [(1,0),(0,1),(-1,0),(0,-1)]
        def backtrack(r, c, i):
            if i == n:
                return True
            if r < 0 or r == numRows or c < 0 or c == numCols:
                return False
            if word[i] != board[r][c]:
                return False
            if board[r][c] is True:
                return False
            
            t = False
            for d in DIRS:
                temp = board[r][c] 
                board[r][c] = True
                t = t or backtrack(r + d[0], c + d[1], i + 1)
                board[r][c] = temp
            
            return t

        
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True
        return False
