class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        DIR = (0,1)
        row_l, row_r = 0, len(matrix) - 1
        col_l, col_r = 0, len(matrix[0]) - 1
        r, c = 0, 0
        res = []
        for i in range((row_r + 1) * (col_r + 1)):
            if DIR == (0,1) and c == col_r:
                row_l += 1
                DIR = (1,0)
            elif DIR == (1,0) and r == row_r:
                col_r -= 1
                DIR = (0,-1)
            elif DIR == (0,-1) and c == col_l:
                row_r -= 1
                DIR = (-1,0)
            elif DIR == (-1,0) and r == row_l:
                col_l += 1
                DIR = (0,1)
            

            res.append(matrix[r][c])
            r += DIR[0]
            c += DIR[1]

        return res
            
            

            

            

            
            
