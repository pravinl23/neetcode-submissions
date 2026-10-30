class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])
        l, h = 0, numRows * numCols - 1

        while l <= h:
            m = (l + h) // 2
            r = (m // numCols)
            c = m - numCols * r
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                l = m + 1
            else:
                h = m - 1
        return False
