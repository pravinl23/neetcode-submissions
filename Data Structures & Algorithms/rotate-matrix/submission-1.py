class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # transpose
        for i in range(n):
            for j in range(i + 1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        # flip
        for r in matrix:
            r.reverse()