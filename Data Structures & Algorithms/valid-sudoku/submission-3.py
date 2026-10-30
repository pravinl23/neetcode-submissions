class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        grid = {}
        for i in range(9):
            rows[i] = []
            cols[i] = []
            grid[i] = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r]:
                    return False
                rows[r].append(board[r][c])

                if board[r][c] in cols[c]:
                    return False
                cols[c].append(board[r][c])

                if board[r][c] in grid[((r//3) * 3) + (c//3)]:
                    return False
                grid[((r//3) * 3) + (c//3)].append(board[r][c])

        return True
        
        
        

