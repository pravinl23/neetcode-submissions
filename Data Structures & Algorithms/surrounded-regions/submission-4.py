class Solution:
    def solve(self, board: List[List[str]]) -> None:
        numRows = len(board)
        numCols = len(board[0])
        DIRS = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r, c):
            if not (0 <= r < numRows) or not (0 <= c < numCols):
                return
            if board[r][c] != "O":
                return
            
            board[r][c] = "NOT"
            for dr, dc in DIRS:
                dfs(r + dr, c + dc)
        
        for r in range(numRows):
            dfs(r, 0)
            dfs(r, numCols - 1)
        for c in range(numCols):
            dfs(0, c)
            dfs(numRows - 1, c)

        for r in range(numRows):
            for c in range(numCols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "NOT":
                    board[r][c] = "O"
                
        
