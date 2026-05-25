class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left+(right-left)//2

            x,y= mid // cols, mid % cols

            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False