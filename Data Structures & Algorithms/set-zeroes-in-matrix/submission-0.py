class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    for new_r in range(len(matrix)):
                        if matrix[new_r][c] != 0 and matrix[new_r][c] != 'a':
                            matrix[new_r][c] = 'a'
                    for new_c in range(len(matrix[0])):
                        if matrix[r][new_c] != 0 and matrix[r][new_c] != 'a':
                            matrix[r][new_c] = 'a'

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 'a':
                    matrix[r][c] = 0
                        
                        
                        
        