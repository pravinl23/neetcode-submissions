class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        numRows = len(board)
        numCols = len(board[0])
        DIRS = [(1,0),(0,1),(-1,0),(0,-1)]

        trie = {}
        root = trie
        for w in words:
            root = trie
            for c in w:
                if c not in root:
                    root[c] = {}
                root = root[c]
            root["."] = True
        
        def backtrack(r, c, root):
            if "." in root:
                root["inBoard"] = True

            if r < 0 or r == numRows or c < 0 or c == numCols:
                return False
            if board[r][c] not in root:
                return False
            if board[r][c] is True:
                return False
                
            next_root = root[board[r][c]]
            for d in DIRS:
                temp = board[r][c] 
                board[r][c] = True
                backtrack(r + d[0], c + d[1], next_root)
                board[r][c] = temp
            
        
        for rowIndex, row in enumerate(board):
            for colIndex, col in enumerate(row):
                if board[rowIndex][colIndex] in trie:
                    backtrack(rowIndex, colIndex, trie)

        res = []
        for w in words:
            root = trie
            for c in w:
                root = root[c]
            if "inBoard" in root:
                res.append(w)

        return res