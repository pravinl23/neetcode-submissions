class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix) * len(matrix[0])) - 1

        while left <= right:
            mid = (left + right) // 2
            #now split to coord
            #print(mid)
            #width is # of cols len(matrix[0])
            row = mid // (len(matrix[0]))
            col = mid % (len(matrix[0]))
            curr = matrix[row][col]
            if curr == target:
                return True
            if target < curr:
                right = mid - 1
            if target > curr:
                left = mid + 1

        return False