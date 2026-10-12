class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r]):
                    return False
                else:
                    rows[r].add(board[r][c])
                if (board[r][c] in cols[c]):
                    return False
                else:
                    cols[c].add(board[r][c])

                if (board[r][c] in squares[(r//3, c//3)]):
                    return False
                else:
                    squares[(r//3, c//3)].add(board[r][c])

        return True